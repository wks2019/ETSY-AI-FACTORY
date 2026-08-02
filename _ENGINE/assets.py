"""
assets.py
ETSY-AI-FACTORY / _ENGINE

Resource resolution: fonts and page geometry.

Holds no design decisions. Palettes, type scales and page content come from
the product spec and the resolved theme. This module only resolves the
physical resources the renderer needs.
"""

from __future__ import annotations

import urllib.request
from dataclasses import dataclass
from pathlib import Path

ENGINE_DIR = Path(__file__).resolve().parent
FONT_DIR = ENGINE_DIR / "fonts"

# Canva-available, OFL-licensed. systems/TYPOGRAPHY_SYSTEM.md 5.
FONTS = {
    "CormorantGaramond": {
        "file": "CormorantGaramond.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/"
               "cormorantgaramond/CormorantGaramond%5Bwght%5D.ttf",
        "css_family": "Cormorant Garamond",
    },
    "Inter": {
        "file": "Inter.ttf",
        "url": "https://github.com/google/fonts/raw/main/ofl/"
               "inter/Inter%5Bopsz,wght%5D.ttf",
        "css_family": "Inter",
    },
}


@dataclass(frozen=True)
class PageSize:
    key: str
    label: str
    css: str          # CSS @page size value
    width_mm: float
    height_mm: float
    scale: float      # type and margin scale relative to A4


# Four mandatory sizes. systems/TYPOGRAPHY_SYSTEM.md 25.1.
#
# The 0.66 scale is verified, not derived. 0.72 was tried first and produced
# 46 pages at A5 against 42 at A4 — page parity is the test that catches it.
PAGE_SIZES = {
    "a4": PageSize("a4", "A4", "210mm 297mm", 210.0, 297.0, 1.00),
    "a5": PageSize("a5", "A5", "148mm 210mm", 148.0, 210.0, 0.66),
    "us_letter": PageSize("us_letter", "US Letter", "8.5in 11in", 215.9, 279.4, 1.00),
    "half_letter": PageSize("half_letter", "Half Letter", "5.5in 8.5in", 139.7, 215.9, 0.66),
}

DEFAULT_SIZES = ["a4", "a5", "us_letter", "half_letter"]


class MissingFontError(RuntimeError):
    pass


def ensure_fonts(download: bool = True) -> dict[str, Path]:
    """Resolve font files, downloading once into _ENGINE/fonts if absent.

    The build fails rather than substituting. A substituted face ships wrong
    metrics and broken pagination — systems/TYPOGRAPHY_SYSTEM.md 6.
    """
    FONT_DIR.mkdir(parents=True, exist_ok=True)
    resolved: dict[str, Path] = {}

    for name, meta in FONTS.items():
        path = FONT_DIR / meta["file"]
        if not path.exists():
            if not download:
                raise MissingFontError(f"Font missing and download disabled: {path}")
            try:
                urllib.request.urlretrieve(meta["url"], path)
            except Exception as exc:  # noqa: BLE001
                raise MissingFontError(
                    f"Could not fetch {name}. Place {meta['file']} in {FONT_DIR} manually."
                ) from exc
        if path.stat().st_size < 10_000:
            raise MissingFontError(f"Font file looks truncated: {path}")
        resolved[name] = path

    return resolved


def font_face_css(paths: dict[str, Path]) -> str:
    """@font-face rules pointing at local files.

    Variable fonts are declared across a weight range so WeasyPrint instances
    the axis rather than synthesising a fake bold.
    """
    blocks = []
    for name, path in paths.items():
        family = FONTS[name]["css_family"]
        blocks.append(
            f"@font-face {{\n"
            f"  font-family: '{family}';\n"
            f"  src: url('{path.as_uri()}') format('truetype');\n"
            f"  font-weight: 300 700;\n"
            f"  font-style: normal;\n"
            f"}}"
        )
    return "\n".join(blocks)


def resolve_size(key: str) -> PageSize:
    try:
        return PAGE_SIZES[key]
    except KeyError:
        raise ValueError(
            f"Unknown page size '{key}'. Valid: {', '.join(PAGE_SIZES)}"
        ) from None
