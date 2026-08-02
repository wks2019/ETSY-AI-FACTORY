"""
layout_renderer.py
ETSY-AI-FACTORY / _ENGINE
Version: 2.1

Converts a product specification into an HTML document and a size-specific
stylesheet.

This module makes no design decisions and holds no product knowledge. Colour
arrives as resolved tokens, type sizes come from the token scale below, and
page content comes from the spec. What lives here is layout mechanics only.

Adding a page type means adding one function and one registry entry. Nothing
else in the engine changes.
"""

from __future__ import annotations

import html
from dataclasses import dataclass, field

from assets import PageSize, font_face_css
from tokens import Theme

# 8-point spacing system. systems/BRAND_SYSTEM.md 14.
SPACE = 8

# Type tokens. systems/TYPOGRAPHY_SYSTEM.md 7. Sizes in pt at reference scale.
TYPE = {
    "display":    {"size": 44,   "height": 1.05, "track": "-0.01em", "weight": 300, "family": "display"},
    "headline":   {"size": 26,   "height": 1.10, "track": "0",       "weight": 500, "family": "display"},
    "title":      {"size": 18,   "height": 1.15, "track": "0",       "weight": 500, "family": "display"},
    "subtitle":   {"size": 8,    "height": 1.30, "track": "0.14em",  "weight": 500, "family": "body"},
    "section":    {"size": 9,    "height": 1.30, "track": "0.10em",  "weight": 500, "family": "body"},
    "body-large": {"size": 11.5, "height": 1.50, "track": "0",       "weight": 400, "family": "body"},
    "body":       {"size": 10.5, "height": 1.45, "track": "0",       "weight": 400, "family": "body"},
    "body-small": {"size": 9,    "height": 1.40, "track": "0",       "weight": 400, "family": "body"},
    "caption":    {"size": 7.5,  "height": 1.35, "track": "0",       "weight": 400, "family": "body"},
    "label":      {"size": 6.6,  "height": 1.25, "track": "0.12em",  "weight": 500, "family": "body"},
    "table":      {"size": 8.5,  "height": 1.35, "track": "0",       "weight": 400, "family": "body"},
    "table-head": {"size": 6.8,  "height": 1.25, "track": "0.12em",  "weight": 500, "family": "body"},
    "button":     {"size": 6.8,  "height": 1.20, "track": "0.10em",  "weight": 500, "family": "body"},
    "footnote":   {"size": 6.5,  "height": 1.30, "track": "0",       "weight": 400, "family": "body"},
    "metadata":   {"size": 6.5,  "height": 1.30, "track": "0.04em",  "weight": 400, "family": "body"},
}

# Writing-line spacing. systems/TYPOGRAPHY_SYSTEM.md 14.1 — binding constraint.
WRITING_LINE_PT = 19


class SpecError(ValueError):
    pass


# ----------------------------------------------------------------------
# PAGE MODEL
# ----------------------------------------------------------------------

@dataclass
class Page:
    """One expanded page after repeat labels are resolved."""
    id: str
    type: str
    layout: str
    title: str = ""
    subtitle: str = ""
    theme: str | None = None
    elements: dict = field(default_factory=dict)
    links: list = field(default_factory=list)
    metadata: dict = field(default_factory=dict)
    validation: dict = field(default_factory=dict)

    def el(self, key, default=None):
        return self.elements.get(key, default)


# Legacy top-level keys promoted into `elements` for specs predating schema 1.1.
LEGACY_ELEMENT_KEYS = (
    "panels", "items", "columns", "rows", "lines", "chips",
    "weekday_labels", "day_labels", "hour_start", "hour_end",
    "include_types", "column_break", "blocks", "months",
    "totals", "periods", "notice", "action_columns", "eyebrow",
)


def _page_from_entry(entry: dict, page_id: str, title: str) -> Page:
    elements = dict(entry.get("elements") or {})
    for key in LEGACY_ELEMENT_KEYS:
        if key in entry and key not in elements:
            elements[key] = entry[key]

    return Page(
        id=page_id,
        type=entry["type"],
        layout=entry.get("layout", entry["type"]),
        title=title,
        subtitle=entry.get("subtitle", ""),
        theme=entry.get("theme"),
        elements=elements,
        links=list(entry.get("links") or []),
        metadata=dict(entry.get("metadata") or {}),
        validation=dict(entry.get("validation") or {}),
    )


def expand_pages(spec: dict) -> list[Page]:
    """Resolve repeat labels into individual pages."""
    raw = spec.get("pages")
    if not raw:
        raise SpecError("spec.pages is empty")

    pages: list[Page] = []
    for entry in raw:
        for key in ("id", "type"):
            if key not in entry:
                raise SpecError(f"page entry missing '{key}': {entry}")

        labels = entry.get("repeat_labels")
        if labels:
            for index, label in enumerate(labels, start=1):
                pages.append(_page_from_entry(entry, f"{entry['id']}-{index:02d}", label))
        else:
            pages.append(_page_from_entry(entry, entry["id"], entry.get("title", "")))

    seen: set[str] = set()
    for page in pages:
        if page.id in seen:
            raise SpecError(f"duplicate page id: {page.id}")
        seen.add(page.id)
        if page.layout not in RENDERERS:
            raise SpecError(
                f"page '{page.id}' requests unknown layout '{page.layout}'. "
                f"Available: {', '.join(sorted(RENDERERS))}"
            )

    return pages


def index_by_type(pages: list[Page]) -> dict[str, list[Page]]:
    out: dict[str, list[Page]] = {}
    for page in pages:
        out.setdefault(page.type, []).append(page)
    return out


# ----------------------------------------------------------------------
# STYLESHEET
# ----------------------------------------------------------------------

def _type_rule(selector: str, token: str, scale: float, extra: str = "") -> str:
    t = TYPE[token]
    family = "var(--font-display)" if t["family"] == "display" else "var(--font-body)"
    return (
        f"{selector} {{\n"
        f"  font-family: {family};\n"
        f"  font-weight: {t['weight']};\n"
        f"  font-size: {round(t['size'] * scale, 2)}pt;\n"
        f"  line-height: {t['height']};\n"
        f"  letter-spacing: {t['track']};\n"
        f"{extra}}}"
    )


def build_css(spec: dict, size: PageSize, theme: Theme, font_paths) -> str:
    fonts = spec.get("design", {}).get("fonts", {})
    display = fonts.get("display", "Cormorant Garamond")
    body = fonts.get("body", "Inter")

    s = size.scale
    margin_mm = round(14 * s, 2)
    line_pt = round(WRITING_LINE_PT * s, 1)

    def sp(multiple: float = 1) -> float:
        """8-point spacing, scaled with the page.

        Fixed px spacing does not shrink at A5 and Half Letter, which silently
        clipped content that still fitted inside the page count. Caught by the
        link-parity gate during the Product 001 build.
        """
        return round(SPACE * multiple * s, 1)

    parts = [
        font_face_css(font_paths),
        theme.css_variables(),
        f":root {{ --font-display: '{display}', serif; --font-body: '{body}', sans-serif; }}",
        f"""
@page {{ size: {size.css}; margin: {margin_mm}mm; background: var(--background); }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; }}
.page {{ page-break-after: always; height: 100%; display: flex; flex-direction: column;
         color: var(--text-primary); }}
.page:last-child {{ page-break-after: auto; }}
a {{ color: inherit; text-decoration: none; }}
.head {{ margin-bottom: {sp(2)}px; }}
.body {{ flex: 1; }}
table {{ width: 100%; border-collapse: collapse; }}
.split {{ display: flex; gap: {sp(2)}px; }}
.col {{ flex: 1; }}
""",
        _type_rule("html", "body", s, "  color: var(--text-primary);\n"),
        _type_rule("h1", "headline", s,
                   "  margin: 0 0 4px 0;\n  bookmark-level: 1;\n  bookmark-state: closed;\n"),
        # Subtitles are not navigation targets. Without bookmark-level:none the
        # outline gains a second level and bookmark count exceeds page count.
        _type_rule("h2", "subtitle", s,
                   "  text-transform: uppercase;\n  color: var(--text-muted);\n"
                   f"  margin: 0 0 {sp(1.5)}px 0;\n  bookmark-level: none;\n"),
        _type_rule("h3", "section", s,
                   "  text-transform: uppercase;\n  color: var(--text-muted);\n"
                   f"  margin: {sp(2)}px 0 {sp()}px 0;\n  bookmark-level: none;\n"),
        _type_rule(".tab", "button", s,
                   "  text-transform: uppercase;\n  color: var(--text-muted);\n"
                   f"  padding: {sp(0.4)}px {sp(0.9)}px;\n"
                   "  border: 0.5pt solid var(--border);\n  border-radius: 2pt;\n"),
        _type_rule(".chip", "button", s,
                   "  color: var(--text-primary);\n"
                   f"  padding: {sp(0.5)}px {sp(0.9)}px;\n"
                   "  border: 0.5pt solid var(--border);\n  border-radius: 2pt;\n"
                   f"  min-width: {round(52 * s, 1)}pt;\n  text-align: center;\n"),
        _type_rule(".label", "label", s,
                   "  text-transform: uppercase;\n  color: var(--text-muted);\n"
                   f"  margin-bottom: {sp(0.8)}px;\n"),
        _type_rule(".foot", "footnote", s, "  color: var(--text-muted);\n"),
        _type_rule(".prose p", "body-large", s, f"  margin: 0 0 {sp()}px 0;\n"),
        _type_rule(".prose li", "body-large", s, "  margin: 0 0 4px 0;\n"),
        _type_rule("td", "table", s, "  color: var(--text-secondary);\n"),
        _type_rule("th", "table-head", s,
                   "  text-transform: uppercase;\n  color: var(--text-muted);\n"
                   "  font-weight: 500;\n  text-align: left;\n"),
        f"""
/* Active tab uses primary-strong. Inverse text on `primary` measures 2.83:1
   and fails the 4.5:1 floor in systems/COLOR_SYSTEM.md 15. */
.tab.current {{ color: var(--text-inverse); background: var(--primary-strong);
                border-color: var(--primary-strong); }}

.tabs {{ display: flex; gap: {sp(0.5)}px; margin-bottom: {sp(2)}px;
         padding-bottom: {sp()}px; border-bottom: 0.5pt solid var(--divider); }}
.chips {{ display: flex; flex-wrap: wrap; gap: {sp(0.5)}px; margin-top: {sp(1.5)}px; }}
.foot {{ margin-top: {sp(2)}px; padding-top: {sp()}px;
         border-top: 0.5pt solid var(--divider); display: flex; justify-content: space-between; }}

.cover {{ justify-content: center; align-items: center; text-align: center; }}
.cover .rule {{ width: {round(60 * s, 1)}pt; height: 0.75pt; background: var(--secondary);
                margin: {sp(3)}px auto; }}
.cover .sub {{ font-family: var(--font-body); font-weight: 500; font-size: {round(9 * s, 2)}pt;
               letter-spacing: 0.28em; text-transform: uppercase; color: var(--text-muted); }}

.lines .line {{ border-bottom: 0.5pt solid var(--border); height: {line_pt}pt; }}
.panel {{ border: 0.5pt solid var(--border); border-radius: 2pt;
          padding: {sp(1.2)}px; margin-bottom: {sp(1.2)}px; }}

.cal th {{ padding-bottom: {sp(0.6)}px; border-bottom: 0.5pt solid var(--border); }}
.cal td {{ height: {round(52 * s, 1)}pt; border: 0.5pt solid var(--border);
           vertical-align: top; padding: {sp(0.4)}px; color: var(--text-muted); }}

.track th {{ padding-bottom: {sp(0.5)}px; border-bottom: 0.5pt solid var(--border);
             text-align: center; }}
.track td {{ border-bottom: 0.5pt solid var(--border); height: {round(17 * s, 1)}pt; }}
.track td.name {{ text-align: left; width: 34%; }}
.track td.cell {{ border-left: 0.5pt solid var(--border); }}

.hours td {{ border-bottom: 0.5pt solid var(--border); height: {round(21 * s, 1)}pt; }}
.hours td.h {{ width: {round(38 * s, 1)}pt; color: var(--text-muted); }}

.toc td {{ border-bottom: 0.5pt solid var(--divider); padding: {sp(0.7)}px 0; }}
.toc td.num {{ text-align: right; color: var(--text-muted); width: 18%; }}

.grid th {{ background: var(--surface); padding: {sp(0.5)}px {sp(0.4)}px;
            border-bottom: 0.5pt solid var(--border); }}
.grid td {{ border-bottom: 0.5pt solid var(--border); border-left: 0.5pt solid var(--border);
            height: {line_pt}pt; padding: 0 {sp(0.4)}px; }}
.grid td:first-child, .grid th:first-child {{ border-left: none; }}
.grid td.num, .grid th.num {{ text-align: right; font-variant-numeric: tabular-nums; }}
.grid tr.total td {{ background: var(--surface); font-weight: 500; color: var(--text-primary); }}

.timeline th {{ text-align: center; border-bottom: 0.5pt solid var(--border);
                padding-bottom: {sp(0.5)}px; }}
.timeline td {{ border-bottom: 0.5pt solid var(--border); height: {round(20 * s, 1)}pt; }}
.timeline td.name {{ width: 30%; text-align: left; }}
.timeline td.slot {{ border-left: 0.5pt solid var(--border); }}

.quarter .month {{ flex: 1; }}
.quarter .month .label {{ text-align: center; }}

.prose {{ max-width: 75ch; }}
.prose ol, .prose ul {{ margin: 0 0 {sp()}px 0; padding-left: {sp(2)}px; }}
.notice {{ border: 0.5pt solid var(--border); border-left: 2pt solid var(--danger);
           padding: {sp()}px; margin-top: {sp(1.5)}px; color: var(--text-secondary); }}
""",
    ]
    return "\n".join(parts)


# ----------------------------------------------------------------------
# HELPERS
# ----------------------------------------------------------------------

def _esc(value) -> str:
    return html.escape(str(value), quote=True)


def _lines(count) -> str:
    return '<div class="lines">' + '<div class="line"></div>' * int(count) + "</div>"


def _panels(page: Page) -> str:
    out = ""
    for panel in page.el("panels", []) or []:
        out += (
            f'<div class="panel"><div class="label">{_esc(panel.get("label", ""))}</div>'
            f'{_lines(panel.get("lines", 4))}</div>'
        )
    return out


def _grid(columns: list, rows: int, totals: bool = False) -> str:
    """Shared table for ledger, record and agenda actions.

    A column may be a string or {"label": str, "numeric": bool}. Numeric
    columns right-align with tabular figures so digits stack.
    """
    def parts(column):
        if isinstance(column, dict):
            return column.get("label", ""), bool(column.get("numeric"))
        return column, False

    head = "".join(
        f'<th class="{"num" if numeric else ""}">{_esc(label)}</th>'
        for label, numeric in (parts(c) for c in columns)
    )
    empty = "".join(
        f'<td class="{"num" if numeric else ""}"></td>'
        for _, numeric in (parts(c) for c in columns)
    )
    body = f"<tr>{empty}</tr>" * int(rows)

    if totals:
        cells = ""
        for index, column in enumerate(columns):
            _, numeric = parts(column)
            cells += "<td>Total</td>" if index == 0 else f'<td class="{"num" if numeric else ""}"></td>'
        body += f'<tr class="total">{cells}</tr>'

    return f'<table class="grid"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


# ----------------------------------------------------------------------
# RENDERERS
# ----------------------------------------------------------------------

def r_cover(page: Page, ctx: dict) -> str:
    product = ctx["spec"].get("product", {})
    return (
        f'<div class="sub">{_esc(page.el("eyebrow") or product.get("collection", ""))}</div>'
        f'<div class="rule"></div>'
        f'<h1>{_esc(page.title or product.get("name", ""))}</h1>'
        f'<div class="rule"></div>'
        f'<div class="sub">{_esc(page.subtitle or product.get("subtitle", ""))}</div>'
    )


def r_prose(page: Page, ctx: dict) -> str:
    """Licence, Read Me, and any page that is read rather than written on."""
    out = '<div class="prose">'
    for block in page.el("blocks", []) or []:
        if block.get("heading"):
            out += f'<h3>{_esc(block["heading"])}</h3>'
        for paragraph in block.get("paragraphs", []) or []:
            out += f"<p>{_esc(paragraph)}</p>"
        items = block.get("items") or []
        if items:
            tag = "ol" if block.get("ordered") else "ul"
            out += f"<{tag}>" + "".join(f"<li>{_esc(i)}</li>" for i in items) + f"</{tag}>"
    out += "</div>"
    if page.el("notice"):
        out += f'<div class="notice">{_esc(page.el("notice"))}</div>'
    return out


def r_index(page: Page, ctx: dict) -> str:
    include = page.el("include_types", []) or []
    entries = [p for p in ctx["pages"]
               if p.id != page.id and (not include or p.type in include)]

    def row(target: Page) -> str:
        return (
            f'<tr><td><a href="#{_esc(target.id)}">{_esc(target.title)}</a></td>'
            f'<td class="num"><a href="#{_esc(target.id)}">{_esc(target.type)}</a></td></tr>'
        )

    def table(items) -> str:
        return f'<table class="toc"><tbody>{"".join(row(i) for i in items)}</tbody></table>'

    limit = int(page.el("column_break", 20))
    if len(entries) <= limit:
        return table(entries)
    half = (len(entries) + 1) // 2
    return (f'<div class="split"><div class="col">{table(entries[:half])}</div>'
            f'<div class="col">{table(entries[half:])}</div></div>')


def r_calendar(page: Page, ctx: dict) -> str:
    days = page.el("weekday_labels") or ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    rows = int(page.el("rows", 6))
    head = "".join(f"<th>{_esc(d)}</th>" for d in days)
    body = ("<tr>" + "<td></td>" * len(days) + "</tr>") * rows
    return f'<table class="cal"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def r_quarter(page: Page, ctx: dict) -> str:
    """Three month columns plus objective panels. The plane most small
    businesses actually operate on."""
    months = page.el("months") or ["Month One", "Month Two", "Month Three"]
    lines = int(page.el("lines", 9))
    columns = "".join(
        f'<div class="col month"><div class="label">{_esc(m)}</div>{_lines(lines)}</div>'
        for m in months
    )
    return f'<div class="split quarter">{columns}</div>{_panels(page)}'


def r_week(page: Page, ctx: dict) -> str:
    cols = page.el("day_labels") or ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    lines = int(page.el("lines", 4))
    half = (len(cols) + 1) // 2

    def block(label: str) -> str:
        return f'<div class="panel"><div class="label">{_esc(label)}</div>{_lines(lines)}</div>'

    left = "".join(block(c) for c in cols[:half])
    right = "".join(block(c) for c in cols[half:])
    return f'<div class="split"><div class="col">{left}</div><div class="col">{right}</div></div>'


def r_day(page: Page, ctx: dict) -> str:
    start, end = int(page.el("hour_start", 6)), int(page.el("hour_end", 21))
    rows = "".join(f'<tr><td class="h">{h:02d}:00</td><td></td></tr>'
                   for h in range(start, end + 1))
    hours = f'<table class="hours"><tbody>{rows}</tbody></table>'
    return (f'<div class="split"><div class="col">{hours}</div>'
            f'<div class="col">{_panels(page) or _lines(18)}</div></div>')


def r_agenda(page: Page, ctx: dict) -> str:
    """Meeting Notes. Panels above an action table carrying owner and due
    columns — the action table is the reason the page exists."""
    columns = page.el("action_columns") or ["Action", "Owner", "Due"]
    return (f"{_panels(page)}"
            f'<div class="label">Notes</div>{_lines(page.el("lines", 8))}'
            f'<h3>Actions</h3>{_grid(columns, int(page.el("rows", 6)))}')


def r_ledger(page: Page, ctx: dict) -> str:
    """Expense Tracker. Numeric columns right-align with tabular figures.
    No currency symbol — systems/TYPOGRAPHY_SYSTEM.md 16."""
    columns = page.el("columns") or [
        "Date", "Description", "Category", {"label": "Amount", "numeric": True}]
    return _grid(columns, int(page.el("rows", 20)), totals=bool(page.el("totals", True)))


def r_record(page: Page, ctx: dict) -> str:
    """Contacts, Resources, and any record-card list."""
    columns = page.el("columns") or ["Name", "Company", "Contact", "Notes"]
    out = _grid(columns, int(page.el("rows", 18)), totals=bool(page.el("totals", False)))
    if page.el("notice"):
        out += f'<div class="notice">{_esc(page.el("notice"))}</div>'
    return out


def r_timeline(page: Page, ctx: dict) -> str:
    """Gantt-style strip. Cells stay empty for the customer to shade — a
    pre-filled bar would be decoration, not a planning tool."""
    items = page.el("items") or []
    periods = page.el("periods") or [f"W{i}" for i in range(1, 13)]
    head = '<th class="name"></th>' + "".join(f"<th>{_esc(p)}</th>" for p in periods)
    body = "".join(
        f'<tr><td class="name">{_esc(item)}</td>'
        + '<td class="slot"></td>' * len(periods) + "</tr>"
        for item in items
    )
    grid = f'<table class="timeline"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
    return f"{grid}{_panels(page)}"


def r_tracker(page: Page, ctx: dict) -> str:
    items = page.el("items") or []
    columns = int(page.el("columns", 31))
    head = '<th class="name"></th>' + "".join(f"<th>{i}</th>" for i in range(1, columns + 1))
    body = "".join(
        f'<tr><td class="name">{_esc(item)}</td>' + '<td class="cell"></td>' * columns + "</tr>"
        for item in items
    )
    return f'<table class="track"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def r_panels(page: Page, ctx: dict) -> str:
    return _panels(page)


def r_notes(page: Page, ctx: dict) -> str:
    return _lines(page.el("lines", 22))


RENDERERS = {
    "cover": r_cover,
    "prose": r_prose,
    "index": r_index,
    "year": r_calendar,
    "month": r_calendar,
    "quarter": r_quarter,
    "week": r_week,
    "day": r_day,
    "agenda": r_agenda,
    "ledger": r_ledger,
    "record": r_record,
    "timeline": r_timeline,
    "tracker": r_tracker,
    "panels": r_panels,
    "notes": r_notes,
}


# ----------------------------------------------------------------------
# ASSEMBLY
# ----------------------------------------------------------------------

def _tabs(spec: dict, page: Page, by_type: dict[str, list[Page]]) -> str:
    tabs = spec.get("navigation", {}).get("tabs", [])
    if not tabs:
        return ""
    out = []
    for tab in tabs:
        target = tab.get("target")
        href = by_type[target][0].id if by_type.get(target) else (target or "")
        current = " current" if page.type == target else ""
        out.append(f'<a class="tab{current}" href="#{_esc(href)}">{_esc(tab.get("label", ""))}</a>')
    return f'<nav class="tabs">{"".join(out)}</nav>'


def _chips(page: Page, by_type: dict[str, list[Page]]) -> str:
    targets: list[Page] = list(by_type.get(page.el("chips"), []) if page.el("chips") else [])
    if page.links:
        wanted = {link.get("target") if isinstance(link, dict) else link for link in page.links}
        for group in by_type.values():
            targets.extend(p for p in group if p.id in wanted)
    if not targets:
        return ""
    links = "".join(f'<a class="chip" href="#{_esc(t.id)}">{_esc(t.title)}</a>' for t in targets)
    return f'<div class="chips">{links}</div>'


def render_page(spec: dict, page: Page, pages: list[Page],
                by_type: dict[str, list[Page]]) -> str:
    ctx = {"spec": spec, "pages": pages, "by_type": by_type}
    body = RENDERERS[page.layout](page, ctx)

    if page.layout == "cover":
        return f'<section class="page cover" id="{_esc(page.id)}">{body}</section>'

    subtitle = f"<h2>{_esc(page.subtitle)}</h2>" if page.subtitle else ""
    return (
        f'<section class="page" id="{_esc(page.id)}">'
        f"{_tabs(spec, page, by_type)}"
        f'<header class="head"><h1>{_esc(page.title)}</h1>{subtitle}</header>'
        f'<div class="body">{body}{_chips(page, by_type)}</div>'
        f'<footer class="foot"><span>{_esc(spec.get("product", {}).get("name", ""))}</span>'
        f'<a href="#{_esc(pages[0].id)}">Contents</a></footer></section>'
    )


def render_document(spec: dict, size: PageSize, theme: Theme, font_paths) -> str:
    pages = expand_pages(spec)
    by_type = index_by_type(pages)
    product = spec.get("product", {})
    sections = "".join(render_page(spec, p, pages, by_type) for p in pages)
    css = build_css(spec, size, theme, font_paths)

    return f"""<!DOCTYPE html>
<html lang="{_esc(spec.get('language', 'en'))}">
<head>
<meta charset="utf-8">
<title>{_esc(product.get('name', 'Planner'))} — {_esc(size.label)}</title>
<style>{css}</style>
</head>
<body>{sections}</body>
</html>"""
