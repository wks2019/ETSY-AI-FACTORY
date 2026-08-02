"""
planner_engine.py
ETSY-AI-FACTORY / _ENGINE
Version: 2.1

Rendering orchestrator.

Reads a product specification and produces vector PDFs, preview images and
the deliverable package for one product.

This engine renders. It does not decide. Every design and commercial rule
lives in the repository Markdown files and reaches this code only through
the spec and the resolved theme. Do not add rules here.

Usage:
    python _ENGINE/planner_engine.py products/01-name/spec.json
    python _ENGINE/planner_engine.py spec.json --theme dark --sizes a4
    python _ENGINE/planner_engine.py spec.json --validate-only
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

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_FILE = ROOT / "_SCHEMA" / "spec.schema.json"


class BuildError(RuntimeError):
    pass


# ----------------------------------------------------------------------
# SPEC LOADING
# ----------------------------------------------------------------------

def validate_spec(spec: dict) -> None:
    """Validate against _SCHEMA/spec.schema.json, then against the rules the
    schema cannot express."""
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

    # A hex value in a spec has bypassed the token system. The schema cannot
    # catch this because it can appear under any key.
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


# ----------------------------------------------------------------------
# BUILD
# ----------------------------------------------------------------------

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
    verify(results, spec, pages, theme)
    return {"results": results, "package": package, "out_dir": out_dir, "theme": theme}


# ----------------------------------------------------------------------
# VERIFICATION
# ----------------------------------------------------------------------

def verify(results, spec: dict, pages, theme) -> None:
    """Fail loudly on defects the Quality Engine would reject anyway."""
    problems: list[str] = []
    expected = len(pages)

    # Equal page counts can still hide a defect. Content that overflows at a
    # smaller size is clipped rather than pushed onto a new page, and the only
    # visible symptom is a missing link. Product 001 lost one index row this
    # way before spacing was scaled with the page.
    link_counts = {r.links for r in results}
    if len(link_counts) != 1:
        problems.append(
            f"link count differs across sizes: {sorted(link_counts)} \u2014 "
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


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

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

    print("ETSY-AI-FACTORY / planner_engine 2.1\n")
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
