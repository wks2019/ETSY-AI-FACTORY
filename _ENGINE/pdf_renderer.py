"""
pdf_renderer.py
ETSY-AI-FACTORY / _ENGINE

WeasyPrint rendering and raster preview export.

Produces vector PDFs with live text, embedded subset fonts, internal link
annotations and a bookmark outline. Text is never rasterised or converted to
outlines — systems/TYPOGRAPHY_SYSTEM.md 28.
"""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

from weasyprint import HTML

from assets import PageSize


@dataclass
class RenderResult:
    size_key: str
    path: Path
    pages: int
    links: int
    bookmarks: int


def render_pdf(html_text: str, size: PageSize, out_path: Path,
               metadata: dict | None = None) -> RenderResult:
    """Render one size to a vector PDF."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    document = HTML(string=html_text, base_url=str(out_path.parent)).render()
    document.write_pdf(target=str(out_path), pdf_variant=None)

    if metadata:
        _write_metadata(out_path, metadata, size)

    pages, links, bookmarks = inspect_pdf(out_path)
    return RenderResult(size.key, out_path, pages, links, bookmarks)


def _write_metadata(path: Path, metadata: dict, size: PageSize) -> None:
    """Attach document metadata. engines/QUALITY_ENGINE.md PDF QUALITY."""
    from pypdf import PdfReader, PdfWriter

    reader = PdfReader(str(path))
    writer = PdfWriter(clone_from=reader)
    writer.add_metadata(
        {
            "/Title": f"{metadata.get('name', '')} — {size.label}",
            "/Author": metadata.get("author", ""),
            "/Subject": metadata.get("subtitle", ""),
            "/Keywords": ", ".join(metadata.get("keywords", [])),
            "/Creator": "ETSY-AI-FACTORY planner_engine",
        }
    )
    tmp = path.with_suffix(".tmp.pdf")
    with open(tmp, "wb") as handle:
        writer.write(handle)
    tmp.replace(path)


def inspect_pdf(path: Path) -> tuple[int, int, int]:
    """Return (page count, internal link annotations, bookmark entries)."""
    from pypdf import PdfReader

    reader = PdfReader(str(path))
    pages = len(reader.pages)

    links = 0
    for page in reader.pages:
        for annot in page.get("/Annots", []) or []:
            try:
                obj = annot.get_object()
            except Exception:  # noqa: BLE001
                continue
            if obj.get("/Subtype") == "/Link":
                links += 1

    def count(nodes) -> int:
        """Count titled destinations only. Container lists are structure,
        not bookmarks, and counting them inflates the total."""
        total = 0
        for node in nodes:
            if isinstance(node, list):
                total += count(node)
            elif getattr(node, "title", None) is not None:
                total += 1
        return total

    try:
        bookmarks = count(reader.outline)
    except Exception:  # noqa: BLE001
        bookmarks = 0

    return pages, links, bookmarks


def export_cover_png(pdf_path: Path, out_path: Path, dpi: int = 300) -> Path:
    """300 DPI cover raster for the Etsy listing."""
    _require("pdftoppm")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    stem = out_path.with_suffix("")
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), "-f", "1", "-l", "1",
         "-singlefile", str(pdf_path), str(stem)],
        check=True, capture_output=True,
    )
    return out_path


def export_preview_jpg(pdf_path: Path, out_path: Path, panels: int = 12,
                       columns: int = 4, dpi: int = 110,
                       gutter: int = 18, background: str = "#FBF9F4") -> Path:
    """Multi-panel listing preview built from the first N pages.

    The sheet background takes the theme's `background` token so a dark
    edition does not get an ivory surround.
    """
    from PIL import Image

    _require("pdftoppm")
    work = out_path.parent / "_panels"
    work.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), "-f", "1", "-l", str(panels),
         str(pdf_path), str(work / "p")],
        check=True, capture_output=True,
    )

    frames = sorted(work.glob("p-*.png"))[:panels]
    if not frames:
        raise RuntimeError("No preview panels were rendered")

    tiles = [Image.open(f).convert("RGB") for f in frames]
    tile_w = max(t.width for t in tiles)
    tile_h = max(t.height for t in tiles)
    rows = (len(tiles) + columns - 1) // columns

    sheet = Image.new(
        "RGB",
        (columns * tile_w + gutter * (columns + 1),
         rows * tile_h + gutter * (rows + 1)),
        background,
    )
    for i, tile in enumerate(tiles):
        x = gutter + (i % columns) * (tile_w + gutter)
        y = gutter + (i // columns) * (tile_h + gutter)
        sheet.paste(tile, (x, y))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out_path, "JPEG", quality=90, optimize=True)

    shutil.rmtree(work, ignore_errors=True)
    return out_path


def _require(binary: str) -> None:
    if shutil.which(binary) is None:
        raise RuntimeError(
            f"'{binary}' not found. Install poppler-utils to export previews."
        )
