"""
language.py
ETSY-AI-FACTORY / _ENGINE
Engine 2.1 — Product Generation Optimization Layer

Parser for the AIDPF product specification language.

This module is authoring-side only. The renderer never sees it. It converts
`product.dsl` text into a neutral block structure that `expand_spec.py` turns
into the same spec.json the renderer has always consumed.

Grammar, deliberately small:

    SECTION            PRODUCT | NAV | PAGE <id>
    KEYWORD <value>    one per line, uppercase keyword, rest is the value
    |                  field separator inside a value
    #                  prefix on a column name marks it numeric
    --                 comment to end of line

Whitespace and blank lines are insignificant. Indentation is permitted for
readability and ignored by the parser, because a language whose meaning
depends on invisible characters is a language that generates support tickets.
"""

from __future__ import annotations

from dataclasses import dataclass, field

SEPARATOR = "|"
COMMENT = "--"

SECTIONS = ("PRODUCT", "NAV", "PAGE")

# Keywords permitted inside each section. An unknown keyword is an error
# rather than a silent no-op — a typo that quietly drops a page of content is
# the worst possible failure mode for a generator.
PRODUCT_KEYWORDS = {
    "NAME", "SLUG", "COLLECTION", "SUBTITLE", "EDITION", "VERSION", "AUTHOR",
    "STANDARD", "KEYWORDS", "THEME", "SIZES", "LANGUAGE", "SCHEMA",
    "DISPLAYFONT", "BODYFONT",
}

NAV_KEYWORDS = {"TAB"}

PAGE_KEYWORDS = {
    "USE", "ADD", "REMOVE", "REPLACE",
    "TYPE", "LAYOUT", "TITLE", "SUBTITLE", "REPEAT", "LINK",
    "PANEL", "COLUMNS", "ROWS", "LINES", "ITEMS", "TOTALS", "NOTICE",
    "CHIPS", "INCLUDE", "BREAK", "EYEBROW", "HOURS", "PERIODS",
    "DAYS", "WEEKDAYS", "MONTHS", "ACTIONS",
    "BLOCK", "TEXT", "ITEM", "ORDERED",
}


class LanguageError(ValueError):
    """Raised on any malformed source. Never recovered from silently."""


@dataclass
class Block:
    """One SECTION and every keyword line beneath it."""
    kind: str                       # PRODUCT | NAV | PAGE
    name: str = ""                  # page id, for PAGE
    lines: list = field(default_factory=list)   # (keyword, value, line_number)

    def values(self, keyword: str) -> list[str]:
        return [v for k, v, _ in self.lines if k == keyword]

    def value(self, keyword: str, default: str | None = None) -> str | None:
        found = self.values(keyword)
        return found[0] if found else default

    def has(self, keyword: str) -> bool:
        return any(k == keyword for k, _, _ in self.lines)


def split_fields(value: str) -> list[str]:
    """Split a value on the field separator, trimming each field."""
    return [part.strip() for part in value.split(SEPARATOR)]


def parse_column(text: str) -> str | dict:
    """`#Minutes` becomes a numeric column, `Date` stays a plain string."""
    text = text.strip()
    if text.startswith("#"):
        return {"label": text[1:].strip(), "numeric": True}
    return text


def format_column(column) -> str:
    """Inverse of parse_column, used by the decompiler."""
    if isinstance(column, dict):
        prefix = "#" if column.get("numeric") else ""
        return f"{prefix}{column.get('label', '')}"
    return str(column)


def _strip_comment(line: str) -> str:
    index = line.find(COMMENT)
    return line if index == -1 else line[:index]


def parse(source: str) -> list[Block]:
    """Parse DSL text into an ordered list of blocks."""
    blocks: list[Block] = []
    current: Block | None = None

    for number, raw in enumerate(source.splitlines(), start=1):
        line = _strip_comment(raw).strip()
        if not line:
            continue

        head, _, rest = line.partition(" ")
        keyword = head.strip().upper()
        value = rest.strip()

        if keyword in SECTIONS:
            if keyword == "PAGE" and not value:
                raise LanguageError(f"line {number}: PAGE requires an id")
            current = Block(kind=keyword, name=value)
            blocks.append(current)
            continue

        if current is None:
            raise LanguageError(
                f"line {number}: '{keyword}' appears before any "
                f"PRODUCT, NAV or PAGE section"
            )

        permitted = {
            "PRODUCT": PRODUCT_KEYWORDS,
            "NAV": NAV_KEYWORDS,
            "PAGE": PAGE_KEYWORDS,
        }[current.kind]

        if keyword not in permitted:
            raise LanguageError(
                f"line {number}: '{keyword}' is not valid inside "
                f"{current.kind}. Valid: {', '.join(sorted(permitted))}"
            )

        current.lines.append((keyword, value, number))

    if not blocks:
        raise LanguageError("source contains no sections")

    kinds = [b.kind for b in blocks]
    if kinds[0] != "PRODUCT":
        raise LanguageError("the first section must be PRODUCT")
    if kinds.count("PRODUCT") > 1:
        raise LanguageError("only one PRODUCT section is permitted")
    if kinds.count("NAV") > 1:
        raise LanguageError("only one NAV section is permitted")

    ids = [b.name for b in blocks if b.kind == "PAGE"]
    duplicates = {i for i in ids if ids.count(i) > 1}
    if duplicates:
        raise LanguageError(f"duplicate PAGE ids: {', '.join(sorted(duplicates))}")

    return blocks
