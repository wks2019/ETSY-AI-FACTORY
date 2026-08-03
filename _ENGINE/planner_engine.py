"""
planner_engine.py
ETSY-AI-FACTORY / _ENGINE

Version is defined once, in version.py. Do not restate it here.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import assets  # noqa: E402
import layout_renderer as layout  # noqa: E402
import packager  # noqa: E402
import pdf_renderer as renderer  # noqa: E402
import tokens  # noqa: E402
from version import ENGINE_STAMP  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILE = ROOT / "_SCHEMA" / "spec.schema.json"


class BuildError(RuntimeError):
    pass


def validate_spec(spec: dict) -> None:
    try:
        import jsonschema
    except ImportError:
        print("  warning : jsonschema not installed, structural validation skipped")
    else:
        if not SCHEMA_FILE.exists():
            raise BuildError(f"Schema not found: {SCHEMA_FILE}")
        schema = json.loads(SCHEMA_FILE.read_text(encoding="utf8"))
        try:
            jsonschema.validate(spec, schema)
        except jsonschema.ValidationError as exc:
            location = " / ".join(str(p) for p in exc.absolute_path) or "root"
            raise BuildError(f"Spec invalid at {location}: {exc.message}") from None

    # Tab targets resolve against page *type*, not id (layout_renderer.nav).
    # An unresolved target silently degrades to a dead '#target' anchor on
    # every page — the schema cannot catch it, and page and link parity both
    # still pass. Product 04 shipped with a dead 'review' tab this way.
    page_types = {page.get("type") for page in spec.get("pages", [])}
    dead = [
        tab.get("target")
        for tab in spec.get("navigation", {}).get("tabs", [])
        if tab.get("target") not in page_types
    ]
    if dead:
        raise BuildError(
            "navigation tab target(s) match no page type: "
            + ", ".join(sorted(str(t) for t in dead))
        )

    overrides = spec.get("design", {}).get("token_overrides", {})
    probe = json.loads(json.dumps(spec))
    probe.get("design", {}).pop("token_overrides", None)
    tokens.assert_no_literal_colours(probe)
    if overrides:
        print(f"  note    : {len(overrides)} token override(s) declared")


def load_spec(path: Path) -> dict:
    if not path.exists():
        raise BuildError(f"Spec not found: {path}")
    try:
        spec = json.loads(path.read_text(encoding="utf8"))
    except json.JSONDecodeError as exc:
        raise BuildError(f"Spec is not valid JSON: {exc}") from exc
    validate_spec(spec)
    return spec


def build(spec_path: Path, sizes=None, theme_name=None, previews=True,
          out_dir: Path | None = None) -> dict:
    spec = load_spec(spec_path)
    product = spec["product"]
    slug = product["slug"]

    design = spec.get("design", {})
    theme = tokens.load_theme(
        theme_name or design.get("theme", "neutral"),
        overrides=design.get("token_overrides"),
    )
    theme.enforce()

    size_keys = sizes or spec.get("sizes") or assets.DEFAULT_SIZES
    out_dir = out_dir or (spec_path.parent / "dist")
    out_dir.mkdir(parents=True, exist_ok=True)

    font_paths = assets.ensure_fonts()
    pages = layout.expand_pages(spec)

    print(f"  product : {product.get('name')} v{product.get('version')}")
    print(f"  theme   : {theme.name}")
    print(f"  pages   : {len(pages)}")
    print(f"  sizes   : {', '.join(size_keys)}")
    print(f"  layouts : {', '.join(sorted({p.layout for p in pages}))}")
    print()

    results = []
    for key in size_keys:
        size = assets.resolve_size(key)
        html_text = layout.render_document(spec, size, theme, font_paths)
        suffix = f"-{theme.name}" if theme.name != "neutral" else ""
        target = out_dir / f"{slug}{suffix}-{key}.pdf"
        result = renderer.render_pdf(html_text, size, target, metadata=product)
        results.append(result)
        print(f"  {size.label:<12} {result.pages:>3} pages  "
              f"{result.links:>5} links  {result.bookmarks:>3} bookmarks")

    # Verification runs before anything shippable is written. Previously it
    # ran last, so a failed build still left a complete, hash-stamped ZIP in
    # dist/package — the exact file someone would upload by mistake.
    verify(results, spec, pages, theme)

    cover = preview = None
    if previews:
        primary = results[0].path
        cover = renderer.export_cover_png(primary, out_dir / f"{slug}-cover.png")
        panels = min(12, results[0].pages)
        preview = renderer.export_preview_jpg(
            primary, out_dir / f"{slug}-listing-preview.jpg", panels=panels,
            background=theme["background"])
        print(f"\n  cover   : {cover.name}")
        print(f"  preview : {preview.name} ({panels} panels)")

    package = packager.build_package(out_dir / "package", spec, results, cover, preview,
                                     theme=theme)
    return {"results": results, "package": package, "out_dir": out_dir, "theme": theme}


def verify(results, spec: dict, pages, theme) -> None:
    problems: list[str] = []
    expected = len(pages)

    link_counts = {r.links for r in results}
    if len(link_counts) != 1:
        problems.append(
            f"link count differs across sizes: {sorted(link_counts)} — "
            "content is being clipped at the smaller size")

    counts = {r.pages for r in results}
    if len(counts) != 1:
        problems.append(f"page count differs across sizes: {sorted(counts)}")
    if expected not in counts:
        problems.append(f"expected {expected} pages, rendered {sorted(counts)}")

    for result in results:
        if result.bookmarks != expected:
            problems.append(
                f"{result.size_key}: {result.bookmarks} bookmarks, expected {expected}")
        if result.links == 0:
            problems.append(f"{result.size_key}: no internal links")

    audit = theme.verify()
    for row in audit:
        if not row["pass"]:
            problems.append(
                f"contrast {row['fg']} on {row['bg']} = {row['ratio']}:1 "
                f"(min {row['min']}:1)")

    ids = {p.id for p in pages}
    for page in pages:
        for target in page.validation.get("must_link_to", []):
            if target not in ids:
                problems.append(f"{page.id}: must_link_to '{target}' does not exist")

    if problems:
        print("\n  VERIFY FAILED")
        for problem in problems:
            print(f"    - {problem}")
        raise BuildError("Build did not pass verification")

    print(f"\n  contrast: {len(audit)} pairings checked, all pass")
    print("  verify  : passed")


def main() -> int:
    parser = argparse.ArgumentParser(description="ETSY-AI-FACTORY planner renderer")
    parser.add_argument("spec", type=Path, help="path to spec.json")
    parser.add_argument("--sizes", nargs="+", help="override sizes")
    parser.add_argument("--theme", help="override theme")
    parser.add_argument("--out", type=Path, help="output directory")
    parser.add_argument("--no-previews", action="store_true")
    parser.add_argument("--validate-only", action="store_true",
                        help="validate the spec and exit without rendering")
    args = parser.parse_args()

    print(f"ETSY-AI-FACTORY / {ENGINE_STAMP}\n")
    try:
        if args.validate_only:
            spec = load_spec(args.spec)
            pages = layout.expand_pages(spec)
            theme = tokens.load_theme(
                args.theme or spec.get("design", {}).get("theme", "neutral"),
                overrides=spec.get("design", {}).get("token_overrides"))
            theme.enforce()
            print(f"  spec    : valid ({len(pages)} pages)")
            print(f"  theme   : {theme.name} passes all contrast rules")
            return 0

        outcome = build(args.spec, sizes=args.sizes, theme_name=args.theme,
                        previews=not args.no_previews, out_dir=args.out)
    except (BuildError, layout.SpecError, assets.MissingFontError,
            tokens.TokenError, tokens.ContrastError) as exc:
        print(f"\nBUILD FAILED: {exc}", file=sys.stderr)
        return 1

    print(f"\n  output  : {outcome['out_dir']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
