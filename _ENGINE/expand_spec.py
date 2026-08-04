"""
expand_spec.py
ETSY-AI-FACTORY / _ENGINE
Engine 2.1 — Product Generation Optimization Layer

Turns `product.dsl` into the spec.json structure the renderer has always
consumed, resolving templates, components and shared default metadata on the
way.

The renderer is not aware this module exists. Nothing in planner_engine.py,
layout_renderer.py, pdf_renderer.py, packager.py, assets.py or tokens.py was
modified to support it. Expansion happens strictly before the renderer is
handed a spec.

Pipeline, per Engine 2.1 section 6:

    product.dsl
      -> language.parse
      -> load defaults          (_ENGINE/defaults/metadata.yaml)
      -> load templates         (_ENGINE/templates/*.yaml)
      -> load components        (_ENGINE/components/*.yaml)
      -> apply page commands    (USE / ADD / REMOVE / REPLACE)
      -> apply explicit overrides
      -> spec dict
      -> planner_engine.build

Three entry points:

    expand      product.dsl  -> spec.json
    decompile   spec.json    -> product.dsl        (lossless, used for regression)
    verify      product.dsl  -> compare against an existing spec.json

`decompile` exists so that every already-shipped product can be round-tripped
automatically. A regression suite that only tests hand-written samples proves
the samples work; round-tripping the real collection proves the language is
complete.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import yaml  # noqa: E402

import language  # noqa: E402
from language import format_column, parse_column, split_fields  # noqa: E402

ENGINE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = ENGINE_DIR / "templates"
COMPONENT_DIR = ENGINE_DIR / "components"
DEFAULTS_FILE = ENGINE_DIR / "defaults" / "metadata.yaml"


class ExpansionError(ValueError):
    pass


# ----------------------------------------------------------------------
# LIBRARY LOADING
# ----------------------------------------------------------------------

def _load_yaml_dir(directory: Path, kind: str) -> dict[str, dict]:
    library: dict[str, dict] = {}
    if not directory.exists():
        return library
    for path in sorted(directory.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf8")) or {}
        name = str(data.get("name", path.stem)).upper()
        if name in library:
            raise ExpansionError(f"duplicate {kind} name '{name}' in {path}")
        library[name] = data
    return library


def load_templates() -> dict[str, dict]:
    return _load_yaml_dir(TEMPLATE_DIR, "template")


def load_components() -> dict[str, dict]:
    return _load_yaml_dir(COMPONENT_DIR, "component")


def load_defaults() -> dict:
    if not DEFAULTS_FILE.exists():
        return {}
    return yaml.safe_load(DEFAULTS_FILE.read_text(encoding="utf8")) or {}


# ----------------------------------------------------------------------
# MERGING
# ----------------------------------------------------------------------

def _merge(base: dict, overlay: dict) -> dict:
    """Recursive dict merge. Overlay wins; lists replace rather than append.

    Lists replace because a template that supplied four panels and a product
    that supplies five means the product wants five, not nine.
    """
    out = dict(base)
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


def _apply_component(page: dict, component: dict) -> dict:
    """Fold a component's elements into a page, appending list elements.

    Components are additive by design — ADD HABIT_TRACKER should extend the
    page, not overwrite what is already on it.
    """
    elements = dict(page.get("elements") or {})
    for key, value in (component.get("elements") or {}).items():
        if isinstance(value, list) and isinstance(elements.get(key), list):
            elements[key] = elements[key] + value
        else:
            elements[key] = value
    page = dict(page)
    page["elements"] = elements
    for key, value in component.items():
        if key not in ("name", "elements", "description"):
            page.setdefault(key, value)
    return page


# ----------------------------------------------------------------------
# EXPANSION
# ----------------------------------------------------------------------

def _product_from_block(block, defaults: dict) -> dict:
    meta = defaults.get("product", {})
    product = {
        "name": block.value("NAME", meta.get("name", "")),
        "slug": block.value("SLUG", meta.get("slug", "")),
        "version": block.value("VERSION", meta.get("version", "1.0")),
    }
    optional = {
        "collection": "COLLECTION",
        "subtitle": "SUBTITLE",
        "edition": "EDITION",
        "author": "AUTHOR",
        "standard": "STANDARD",
    }
    for field_name, keyword in optional.items():
        value = block.value(keyword, meta.get(field_name))
        if value:
            product[field_name] = value

    keywords = block.value("KEYWORDS")
    if keywords:
        product["keywords"] = split_fields(keywords)
    elif meta.get("keywords"):
        product["keywords"] = list(meta["keywords"])

    # Preserve the field order the shipped specs use, so a decompile /
    # expand round trip is diff-clean as well as structurally equal.
    order = ["name", "slug", "collection", "subtitle", "edition", "version",
             "author", "standard", "keywords"]
    return {k: product[k] for k in order if k in product}


def _page_from_block(block, templates: dict, components: dict) -> dict:
    page: dict = {}

    use = block.value("USE")
    if use:
        key = use.strip().upper()
        if key not in templates:
            raise ExpansionError(
                f"page '{block.name}': unknown template '{key}'. "
                f"Available: {', '.join(sorted(templates)) or 'none'}"
            )
        template = templates[key]
        page = _merge(page, json.loads(json.dumps(template.get("page", {}))))
        for component_name in template.get("uses", []) or []:
            component_key = str(component_name).upper()
            if component_key not in components:
                raise ExpansionError(
                    f"template '{key}' requires unknown component "
                    f"'{component_key}'"
                )
            page = _apply_component(page, components[component_key])

    for component_name in block.values("ADD"):
        component_key = component_name.strip().upper()
        if component_key not in components:
            raise ExpansionError(
                f"page '{block.name}': unknown component '{component_key}'. "
                f"Available: {', '.join(sorted(components)) or 'none'}"
            )
        page = _apply_component(page, components[component_key])

    elements: dict = dict(page.get("elements") or {})
    panels: list = list(elements.get("panels") or [])
    blocks: list = list(elements.get("blocks") or [])
    replaced_panels = False

    page["id"] = block.name

    for keyword, value, number in block.lines:
        if keyword in ("USE", "ADD"):
            continue

        if keyword == "REMOVE":
            target = value.strip().upper()
            mapping = {"PANELS": "panels", "NOTES": "lines", "BLOCKS": "blocks",
                       "COLUMNS": "columns", "ITEMS": "items", "CHIPS": "chips",
                       "NOTICE": "notice"}
            key = mapping.get(target, target.lower())
            elements.pop(key, None)
            if key == "panels":
                panels = []
            if key == "blocks":
                blocks = []
            continue

        if keyword == "REPLACE":
            head, _, rest = value.partition(" ")
            target = head.strip().upper()
            if target in ("TITLE", "HEADER"):
                page["title"] = rest.strip()
            elif target == "SUBTITLE":
                page["subtitle"] = rest.strip()
            else:
                raise ExpansionError(
                    f"line {number}: REPLACE supports TITLE, HEADER or "
                    f"SUBTITLE, not '{target}'"
                )
            continue

        if keyword == "TYPE":
            page["type"] = value
        elif keyword == "LAYOUT":
            page["layout"] = value
        elif keyword == "TITLE":
            page["title"] = value
        elif keyword == "SUBTITLE":
            page["subtitle"] = value
        elif keyword == "REPEAT":
            page["repeat_labels"] = split_fields(value)
        elif keyword == "LINK":
            page["links"] = split_fields(value)
        elif keyword == "PANEL":
            if not replaced_panels:
                panels = []
                replaced_panels = True
            fields = split_fields(value)
            panel = {"label": fields[0]}
            if len(fields) > 1 and fields[1]:
                panel["lines"] = int(fields[1])
            panels.append(panel)
        elif keyword == "COLUMNS":
            elements["columns"] = (
                int(value) if value.strip().isdigit()
                else [parse_column(f) for f in split_fields(value)]
            )
        elif keyword == "ACTIONS":
            elements["action_columns"] = [parse_column(f) for f in split_fields(value)]
        elif keyword == "ROWS":
            elements["rows"] = int(value)
        elif keyword == "LINES":
            elements["lines"] = int(value)
        elif keyword == "BREAK":
            elements["column_break"] = int(value)
        elif keyword == "TOTALS":
            elements["totals"] = value.strip().lower() in ("true", "yes", "1")
        elif keyword == "NOTICE":
            elements["notice"] = value
        elif keyword == "CHIPS":
            elements["chips"] = value
        elif keyword == "EYEBROW":
            elements["eyebrow"] = value
        elif keyword == "ITEMS":
            elements["items"] = split_fields(value)
        elif keyword == "INCLUDE":
            elements["include_types"] = split_fields(value)
        elif keyword == "PERIODS":
            elements["periods"] = split_fields(value)
        elif keyword == "DAYS":
            elements["day_labels"] = split_fields(value)
        elif keyword == "WEEKDAYS":
            elements["weekday_labels"] = split_fields(value)
        elif keyword == "MONTHS":
            elements["months"] = split_fields(value)
        elif keyword == "HOURS":
            fields = split_fields(value)
            if len(fields) != 2:
                raise ExpansionError(f"line {number}: HOURS needs start | end")
            elements["hour_start"] = int(fields[0])
            elements["hour_end"] = int(fields[1])
        elif keyword == "BLOCK":
            blocks.append({"heading": value} if value else {})
        elif keyword == "TEXT":
            if not blocks:
                blocks.append({})
            blocks[-1].setdefault("paragraphs", []).append(value)
        elif keyword == "ITEM":
            if not blocks:
                blocks.append({})
            blocks[-1].setdefault("items", []).append(value)
        elif keyword == "ORDERED":
            if not blocks:
                blocks.append({})
            blocks[-1]["ordered"] = True

    if panels:
        elements["panels"] = panels
    if blocks:
        elements["blocks"] = blocks

    if "type" not in page:
        page["type"] = page["id"]
    if elements:
        page["elements"] = _order_elements(elements)

    order = ["id", "type", "layout", "title", "subtitle", "repeat_labels",
             "links", "elements"]
    return {k: page[k] for k in order if k in page}


ELEMENT_ORDER = [
    "eyebrow", "hour_start", "hour_end", "columns", "rows", "lines",
    "column_break", "totals", "chips", "include_types", "items", "periods",
    "day_labels", "weekday_labels", "months", "action_columns", "panels",
    "blocks", "notice",
]


def _order_elements(elements: dict) -> dict:
    known = {k: elements[k] for k in ELEMENT_ORDER if k in elements}
    extra = {k: v for k, v in elements.items() if k not in known}
    return {**known, **extra}


def expand(source: str) -> dict:
    """Expand DSL text into a spec dictionary."""
    blocks = language.parse(source)
    templates = load_templates()
    components = load_components()
    defaults = load_defaults()

    product_block = next(b for b in blocks if b.kind == "PRODUCT")

    spec: dict = {
        "schema": product_block.value("SCHEMA", defaults.get("schema", "1.1")),
        "language": product_block.value("LANGUAGE", defaults.get("language", "en")),
        "product": _product_from_block(product_block, defaults),
    }

    design = json.loads(json.dumps(defaults.get("design", {})))
    theme = product_block.value("THEME")
    if theme:
        design["theme"] = theme
    fonts = dict(design.get("fonts", {}))
    if product_block.value("DISPLAYFONT"):
        fonts["display"] = product_block.value("DISPLAYFONT")
    if product_block.value("BODYFONT"):
        fonts["body"] = product_block.value("BODYFONT")
    if fonts:
        design["fonts"] = fonts
    if design:
        spec["design"] = design

    sizes = product_block.value("SIZES")
    spec["sizes"] = split_fields(sizes) if sizes else list(
        defaults.get("sizes", ["a4", "a5", "us_letter", "half_letter"]))

    nav_block = next((b for b in blocks if b.kind == "NAV"), None)
    if nav_block:
        tabs = []
        for value in nav_block.values("TAB"):
            fields = split_fields(value)
            if len(fields) != 2:
                raise ExpansionError(f"TAB needs 'label | target', got '{value}'")
            tabs.append({"label": fields[0], "target": fields[1]})
        if tabs:
            spec["navigation"] = {"tabs": tabs}

    spec["pages"] = [
        _page_from_block(b, templates, components)
        for b in blocks if b.kind == "PAGE"
    ]

    if not spec["pages"]:
        raise ExpansionError("no PAGE sections found")

    return spec


# ----------------------------------------------------------------------
# DECOMPILATION
# ----------------------------------------------------------------------

def _emit(out: list, keyword: str, value) -> None:
    if value is None or value == "":
        return
    out.append(f"{keyword} {value}")


def decompile(spec: dict) -> str:
    """spec.json -> DSL text. Lossless: expand(decompile(s)) == s."""
    out: list[str] = []
    product = spec.get("product", {})

    out.append("PRODUCT")
    _emit(out, "NAME", product.get("name"))
    _emit(out, "SLUG", product.get("slug"))
    _emit(out, "COLLECTION", product.get("collection"))
    _emit(out, "SUBTITLE", product.get("subtitle"))
    _emit(out, "EDITION", product.get("edition"))
    _emit(out, "VERSION", product.get("version"))
    _emit(out, "AUTHOR", product.get("author"))
    _emit(out, "STANDARD", product.get("standard"))
    if product.get("keywords"):
        _emit(out, "KEYWORDS", " | ".join(product["keywords"]))

    design = spec.get("design", {})
    _emit(out, "THEME", design.get("theme"))
    fonts = design.get("fonts", {})
    _emit(out, "DISPLAYFONT", fonts.get("display"))
    _emit(out, "BODYFONT", fonts.get("body"))
    if spec.get("sizes"):
        _emit(out, "SIZES", " | ".join(spec["sizes"]))
    if spec.get("schema") and spec["schema"] != "1.1":
        _emit(out, "SCHEMA", spec["schema"])
    if spec.get("language") and spec["language"] != "en":
        _emit(out, "LANGUAGE", spec["language"])

    tabs = spec.get("navigation", {}).get("tabs") or []
    if tabs:
        out.append("")
        out.append("NAV")
        for tab in tabs:
            out.append(f"TAB {tab.get('label', '')} | {tab.get('target', '')}")

    for page in spec.get("pages", []):
        out.append("")
        out.append(f"PAGE {page['id']}")
        if page.get("type") != page["id"]:
            _emit(out, "TYPE", page.get("type"))
        _emit(out, "LAYOUT", page.get("layout"))
        _emit(out, "TITLE", page.get("title"))
        _emit(out, "SUBTITLE", page.get("subtitle"))
        if page.get("repeat_labels"):
            _emit(out, "REPEAT", " | ".join(page["repeat_labels"]))
        if page.get("links"):
            _emit(out, "LINK", " | ".join(str(l) for l in page["links"]))

        elements = page.get("elements") or {}
        if "hour_start" in elements:
            out.append(f"HOURS {elements['hour_start']} | {elements['hour_end']}")
        columns = elements.get("columns")
        if isinstance(columns, int):
            _emit(out, "COLUMNS", columns)
        elif columns:
            _emit(out, "COLUMNS", " | ".join(format_column(c) for c in columns))
        if elements.get("action_columns"):
            _emit(out, "ACTIONS",
                  " | ".join(format_column(c) for c in elements["action_columns"]))
        for keyword, key in (("ROWS", "rows"), ("LINES", "lines"),
                             ("BREAK", "column_break")):
            if key in elements:
                _emit(out, keyword, elements[key])
        if "totals" in elements:
            _emit(out, "TOTALS", "true" if elements["totals"] else "false")
        _emit(out, "CHIPS", elements.get("chips"))
        _emit(out, "EYEBROW", elements.get("eyebrow"))
        for keyword, key in (("ITEMS", "items"), ("INCLUDE", "include_types"),
                             ("PERIODS", "periods"), ("DAYS", "day_labels"),
                             ("WEEKDAYS", "weekday_labels"), ("MONTHS", "months")):
            if elements.get(key):
                _emit(out, keyword, " | ".join(elements[key]))
        for panel in elements.get("panels") or []:
            lines = panel.get("lines")
            out.append(f"PANEL {panel.get('label', '')}"
                       + (f" | {lines}" if lines is not None else ""))
        for block in elements.get("blocks") or []:
            out.append(f"BLOCK {block.get('heading', '')}".rstrip())
            if block.get("ordered"):
                out.append("ORDERED")
            for paragraph in block.get("paragraphs") or []:
                out.append(f"TEXT {paragraph}")
            for item in block.get("items") or []:
                out.append(f"ITEM {item}")
        _emit(out, "NOTICE", elements.get("notice"))

    return "\n".join(out) + "\n"


# ----------------------------------------------------------------------
# COMPARISON
# ----------------------------------------------------------------------

def differences(left: dict, right: dict, path: str = "spec") -> list[str]:
    """Structural diff. Empty list means the two specs are identical."""
    problems: list[str] = []
    if type(left) is not type(right):
        return [f"{path}: type {type(left).__name__} vs {type(right).__name__}"]
    if isinstance(left, dict):
        for key in sorted(set(left) | set(right)):
            if key not in left:
                problems.append(f"{path}.{key}: missing on left")
            elif key not in right:
                problems.append(f"{path}.{key}: missing on right")
            else:
                problems += differences(left[key], right[key], f"{path}.{key}")
    elif isinstance(left, list):
        if len(left) != len(right):
            problems.append(f"{path}: length {len(left)} vs {len(right)}")
        for index, (a, b) in enumerate(zip(left, right)):
            problems += differences(a, b, f"{path}[{index}]")
    elif left != right:
        problems.append(f"{path}: {left!r} vs {right!r}")
    return problems


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="AIDPF specification expansion layer (Engine 2.1)")
    parser.add_argument("command", choices=["expand", "decompile", "verify"])
    parser.add_argument("path", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--against", type=Path,
                        help="spec.json to compare against, for verify")
    args = parser.parse_args()

    try:
        if args.command == "expand":
            spec = expand(args.path.read_text(encoding="utf8"))
            text = json.dumps(spec, indent=2, ensure_ascii=False) + "\n"
            if args.out:
                args.out.write_text(text, encoding="utf8")
                print(f"  expanded: {args.path.name} -> {args.out}")
            else:
                sys.stdout.write(text)

        elif args.command == "decompile":
            spec = json.loads(args.path.read_text(encoding="utf8"))
            text = decompile(spec)
            if args.out:
                args.out.write_text(text, encoding="utf8")
                print(f"  decompiled: {args.path.name} -> {args.out}")
            else:
                sys.stdout.write(text)

        else:
            if not args.against:
                raise ExpansionError("verify requires --against spec.json")
            produced = expand(args.path.read_text(encoding="utf8"))
            expected = json.loads(args.against.read_text(encoding="utf8"))
            problems = differences(expected, produced)
            if problems:
                print(f"  MISMATCH: {len(problems)} difference(s)")
                for problem in problems[:20]:
                    print(f"    - {problem}")
                return 1
            print(f"  identical: {args.path.name} matches {args.against.name}")

    except (language.LanguageError, ExpansionError) as exc:
        print(f"\nEXPANSION FAILED: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
