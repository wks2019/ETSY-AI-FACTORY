"""
mockup_renderer.py
ETSY-AI-FACTORY / _ENGINE

Generates the ten Etsy listing images from a built product.

Input is the rendered PDFs in dist/. Nothing here re-renders the planner —
pages are rasterised from the PDF so the mockups can never drift from the
file the customer receives.

Seven slots need only code. Two need a photographic plate, supplied by the
shop owner (see PLATE LICENSING below). Missing plates are skipped and
reported; they never fail the run.

ETSY CONSTRAINTS encoded here, from help.etsy.com image requirements:
  - Listing photos: width and height of at least 2000px recommended.
  - First photo: at least 635x635 or the listing ranks lower.
  - First photo should be landscape or square; it dictates the shape of the
    rest, so all ten are rendered at one ratio.
  - Files over 1MB may fail to upload. Quality is stepped down until every
    image clears that.
  - Transparency is not supported — transparent regions render black on
    Etsy. Everything composites onto an opaque background and saves as JPEG.

PLATE LICENSING:
  Etsy's Listing Image Requirements policy requires sellers to use their own
  photos — taken by you, or by someone on your behalf. Stock photography is
  not compliant. The plates must be photographed, not downloaded.
"""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))

import assets  # noqa: E402
import tokens  # noqa: E402
from version import ENGINE_STAMP  # noqa: E402

ENGINE_DIR = Path(__file__).resolve().parent
ROOT = ENGINE_DIR.parent
PLATE_DIR = ROOT / "_ASSETS" / "plates"

# 4:3 landscape. Height clears Etsy's 2000px recommendation on the short side.
CANVAS = (2667, 2000)
SAFE_FRACTION = 0.70
MAX_BYTES = 1_000_000
QUALITY_LADDER = (92, 88, 84, 80, 76, 70, 64)

SLOTS = [
    "01-hero", "02-tablet", "03-desk", "04-pages", "05-sizes",
    "06-features", "07-spread", "08-included", "09-howto", "10-licence",
]


class MockupError(RuntimeError):
    pass


# ----------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------

def safe_box(canvas: tuple[int, int] = CANVAS) -> tuple[int, int, int, int]:
    """Central region that survives Etsy's 3:4, 4:3 and 1:1 crops."""
    w, h = canvas
    mw, mh = int(w * (1 - SAFE_FRACTION) / 2), int(h * (1 - SAFE_FRACTION) / 2)
    return mw, mh, w - mw, h - mh


def save_listing_jpeg(image: Image.Image, path: Path) -> dict:
    """Save as opaque JPEG under Etsy's 1MB upload ceiling."""
    if image.mode != "RGB":
        flat = Image.new("RGB", image.size, "#FFFFFF")
        flat.paste(image, mask=image.split()[-1] if image.mode == "RGBA" else None)
        image = flat

    path.parent.mkdir(parents=True, exist_ok=True)
    for quality in QUALITY_LADDER:
        image.save(path, "JPEG", quality=quality, optimize=True,
                   progressive=True, subsampling=0)
        if path.stat().st_size <= MAX_BYTES:
            return {"file": path.name, "bytes": path.stat().st_size,
                    "quality": quality, "size": list(image.size)}

    raise MockupError(
        f"{path.name} is {path.stat().st_size:,} bytes at the lowest quality "
        f"step; Etsy may reject uploads over {MAX_BYTES:,}."
    )


# ----------------------------------------------------------------------
# PAGE RASTERISATION
# ----------------------------------------------------------------------

def rasterise(pdf: Path, first: int, last: int, dpi: int, work: Path) -> list[Image.Image]:
    work.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["pdftoppm", "-png", "-r", str(dpi), "-f", str(first), "-l", str(last),
         str(pdf), str(work / "pg")],
        check=True, capture_output=True,
    )
    frames = sorted(work.glob("pg-*.png"))
    if not frames:
        raise MockupError(f"pdftoppm produced no output for {pdf.name}")
    return [Image.open(f).convert("RGB") for f in frames]


def shadowed(page: Image.Image, blur: int = 14, offset: int = 10,
             opacity: int = 70) -> Image.Image:
    """Page on a soft drop shadow, returned RGBA."""
    from PIL import ImageFilter

    pad = blur * 3
    canvas = Image.new("RGBA", (page.width + pad * 2, page.height + pad * 2), (0, 0, 0, 0))
    shadow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rectangle(
        [pad, pad + offset, pad + page.width, pad + page.height + offset],
        fill=(0, 0, 0, opacity))
    shadow = shadow.filter(ImageFilter.GaussianBlur(blur))
    canvas.alpha_composite(shadow)
    canvas.paste(page, (pad, pad))
    return canvas


# ----------------------------------------------------------------------
# PERSPECTIVE — no numpy dependency
# ----------------------------------------------------------------------

def _solve(matrix: list[list[float]], vector: list[float]) -> list[float]:
    n = len(vector)
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(matrix[r][col]))
        if abs(matrix[pivot][col]) < 1e-12:
            raise MockupError("Plate corners are degenerate; check the quad.")
        matrix[col], matrix[pivot] = matrix[pivot], matrix[col]
        vector[col], vector[pivot] = vector[pivot], vector[col]
        for row in range(n):
            if row == col:
                continue
            factor = matrix[row][col] / matrix[col][col]
            for k in range(col, n):
                matrix[row][k] -= factor * matrix[col][k]
            vector[row] -= factor * vector[col]
    return [vector[i] / matrix[i][i] for i in range(n)]


def perspective_coeffs(dst_quad, src_size) -> list[float]:
    """Coefficients mapping the full source image onto four target corners.

    PIL's PERSPECTIVE transform is an inverse map, so the system is built
    destination-to-source.
    """
    w, h = src_size
    src = [(0, 0), (w, 0), (w, h), (0, h)]
    rows, values = [], []
    for (dx, dy), (sx, sy) in zip(dst_quad, src):
        rows.append([dx, dy, 1, 0, 0, 0, -sx * dx, -sx * dy])
        rows.append([0, 0, 0, dx, dy, 1, -sy * dx, -sy * dy])
        values += [sx, sy]
    return _solve(rows, values)


def place_on_plate(plate: Image.Image, page: Image.Image, quad) -> Image.Image:
    coeffs = perspective_coeffs(quad, page.size)
    warped = page.convert("RGBA").transform(
        plate.size, Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    out = plate.convert("RGBA")
    out.alpha_composite(warped)
    return out.convert("RGB")


# ----------------------------------------------------------------------
# TYPE
# ----------------------------------------------------------------------

@dataclass
class Fonts:
    display: Path
    body: Path

    def d(self, size: int) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(str(self.display), size)

    def b(self, size: int) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(str(self.body), size)


def draw_centred(draw: ImageDraw.ImageDraw, y: int, text: str,
                 font: ImageFont.FreeTypeFont, fill: str,
                 width: int = CANVAS[0], tracking: int = 0) -> int:
    if not tracking:
        box = draw.textbbox((0, 0), text, font=font)
        draw.text(((width - (box[2] - box[0])) / 2 - box[0], y), text,
                  font=font, fill=fill)
        return y + (box[3] - box[1])

    widths = [draw.textbbox((0, 0), ch, font=font)[2] for ch in text]
    total = sum(widths) + tracking * (len(text) - 1)
    x = (width - total) / 2
    for ch, cw in zip(text, widths):
        draw.text((x, y), ch, font=font, fill=fill)
        x += cw + tracking
    box = draw.textbbox((0, 0), text, font=font)
    return y + (box[3] - box[1])


def wrap(draw, text: str, font, max_width: int) -> list[str]:
    words, lines, line = text.split(), [], ""
    for word in words:
        trial = f"{line} {word}".strip()
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            line = trial
        else:
            if line:
                lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def text_slot(theme, fonts: Fonts, heading: str, eyebrow: str,
              rows: list[tuple[str, str]], footer: str = "") -> Image.Image:
    """Shared layout for the informational slots: 06, 08, 09, 10."""
    bg, ink, muted = theme["background"], theme["text-primary"], theme["text-muted"]
    accent, line = theme["primary-strong"], theme["border"]

    image = Image.new("RGB", CANVAS, bg)
    draw = ImageDraw.Draw(image)
    left, right, _, _ = safe_box()
    inner = CANVAS[0] - left * 2

    y = int(CANVAS[1] * 0.11)
    y = draw_centred(draw, y, eyebrow.upper(), fonts.b(34), muted, tracking=13) + 34
    y = draw_centred(draw, y, heading, fonts.d(112), ink) + 30
    draw.line([(CANVAS[0] / 2 - 90, y), (CANVAS[0] / 2 + 90, y)], fill=accent, width=4)
    y += 80

    label_font, value_font = fonts.b(38), fonts.b(44)
    for label, value in rows:
        draw.text((left, y), label.upper(), font=label_font, fill=muted)
        for i, part in enumerate(wrap(draw, value, value_font, inner - 640)):
            draw.text((left + 640, y + i * 58), part, font=value_font, fill=ink)
        step = max(58 * len(wrap(draw, value, value_font, inner - 640)), 58) + 34
        y += step
        draw.line([(left, y - 17), (CANVAS[0] - left, y - 17)], fill=line, width=2)

    if footer:
        draw_centred(draw, CANVAS[1] - 150, footer, fonts.b(32), muted, tracking=6)
    return image


# ----------------------------------------------------------------------
# SLOTS
# ----------------------------------------------------------------------

def slot_hero(pages, theme, fonts, product) -> Image.Image:
    image = Image.new("RGB", CANVAS, theme["background"])
    draw = ImageDraw.Draw(image)

    cover = pages[0]
    target_h = int(CANVAS[1] * 0.62)
    cover = cover.resize((int(cover.width * target_h / cover.height), target_h),
                         Image.LANCZOS)
    card = shadowed(cover)
    image.paste(card, (int((CANVAS[0] - card.width) / 2),
                       int(CANVAS[1] * 0.10)), card)

    y = int(CANVAS[1] * 0.78)
    y = draw_centred(draw, y, product.get("name", ""), fonts.d(96),
                     theme["text-primary"]) + 42
    sizes = len(product.get("_sizes", [])) or 4
    strap = f"{product.get('_pages', '')} PAGES · {sizes} SIZES · HYPERLINKED · UNDATED"
    draw_centred(draw, y, strap, fonts.b(36), theme["text-muted"], tracking=9)
    return image


def slot_pages(pages, theme, fonts) -> Image.Image:
    image = Image.new("RGB", CANVAS, theme["background"])
    cols, rows, gutter = 6, 2, 34
    left, top, right, bottom = safe_box()
    cell_w = (right - left - gutter * (cols - 1)) / cols
    cell_h = (bottom - top - gutter * (rows - 1)) / rows

    for index, page in enumerate(pages[:cols * rows]):
        scale = min(cell_w / page.width, cell_h / page.height)
        thumb = page.resize((int(page.width * scale), int(page.height * scale)),
                            Image.LANCZOS)
        card = shadowed(thumb, blur=7, offset=5, opacity=55)
        x = left + (index % cols) * (cell_w + gutter) + (cell_w - card.width) / 2
        y = top + (index // cols) * (cell_h + gutter) + (cell_h - card.height) / 2
        image.paste(card, (int(x), int(y)), card)
    return image


def slot_sizes(pages, theme, fonts, size_keys) -> Image.Image:
    """Four sizes at true relative scale, not four identical thumbnails."""
    image = Image.new("RGB", CANVAS, theme["background"])
    draw = ImageDraw.Draw(image)
    draw_centred(draw, int(CANVAS[1] * 0.09), "FOUR SIZES INCLUDED",
                 fonts.b(40), theme["text-muted"], tracking=13)

    known = [assets.resolve_size(k) for k in size_keys if k in assets.PAGE_SIZES]
    tallest = max(s.height_mm for s in known)
    base_h = int(CANVAS[1] * 0.52)
    page = pages[min(4, len(pages) - 1)]

    cards, labels = [], []
    for size in known:
        h = int(base_h * size.height_mm / tallest)
        w = int(h * size.width_mm / size.height_mm)
        cards.append(shadowed(page.resize((w, h), Image.LANCZOS), blur=9, offset=6))
        labels.append(size.label)

    gutter = 70
    total = sum(c.width for c in cards) + gutter * (len(cards) - 1)
    x = (CANVAS[0] - total) / 2
    baseline = int(CANVAS[1] * 0.76)
    for card, label in zip(cards, labels):
        image.paste(card, (int(x), baseline - card.height), card)
        box = draw.textbbox((0, 0), label, font=fonts.b(40))
        draw.text((x + (card.width - box[2]) / 2, baseline + 34), label,
                  font=fonts.b(40), fill=theme["text-primary"])
        x += card.width + gutter
    return image


def slot_spread(pages, theme, fonts) -> Image.Image:
    """Close crop of an interior page, so the buyer can read the layout."""
    image = Image.new("RGB", CANVAS, theme["surface"])
    page = pages[min(6, len(pages) - 1)]
    crop = page.crop((0, 0, page.width, int(page.height * 0.62)))
    scale = (CANVAS[0] * 0.86) / crop.width
    crop = crop.resize((int(crop.width * scale), int(crop.height * scale)), Image.LANCZOS)
    card = shadowed(crop, blur=18, offset=12)
    image.paste(card, (int((CANVAS[0] - card.width) / 2),
                       int((CANVAS[1] - card.height) / 2)), card)
    return image


def slot_plate(name: str, page: Image.Image) -> Image.Image | None:
    """Composite a page onto a photographic plate, if one is present."""
    definition = PLATE_DIR / f"{name}.json"
    if not definition.exists():
        return None
    meta = json.loads(definition.read_text(encoding="utf8"))
    photo = PLATE_DIR / meta["image"]
    if not photo.exists():
        return None
    plate = Image.open(photo).convert("RGB")
    if plate.size != CANVAS:
        plate = plate.resize(CANVAS, Image.LANCZOS)
    quad = [tuple(point) for point in meta["quad"]]
    return place_on_plate(plate, page, quad)


# ----------------------------------------------------------------------
# BUILD
# ----------------------------------------------------------------------

def build_mockups(spec_path: Path, dist_dir: Path | None = None,
                  out_dir: Path | None = None, dpi: int = 200) -> dict:
    spec = json.loads(spec_path.read_text(encoding="utf8"))
    product = spec.get("product", {})
    slug = product.get("slug", "planner")

    dist_dir = dist_dir or (spec_path.parent / "dist")
    out_dir = out_dir or (dist_dir / "mockups")
    primary = dist_dir / f"{slug}-a4.pdf"
    if not primary.exists():
        candidates = sorted(dist_dir.glob(f"{slug}-*.pdf"))
        if not candidates:
            raise MockupError(
                f"No built PDF in {dist_dir}. Run planner_engine.py first.")
        primary = candidates[0]

    theme = tokens.load_theme(spec.get("design", {}).get("theme", "neutral"))
    font_paths = assets.ensure_fonts()
    fonts = Fonts(font_paths["CormorantGaramond"], font_paths["Inter"])

    size_keys = spec.get("sizes") or assets.DEFAULT_SIZES

    with tempfile.TemporaryDirectory() as tmp:
        pages = rasterise(primary, 1, 12, dpi, Path(tmp))
        from pypdf import PdfReader
        product = dict(product)
        product["_pages"] = len(PdfReader(str(primary)).pages)
        product["_sizes"] = size_keys

        written, skipped = [], []

        def emit(slot: str, image: Image.Image | None) -> None:
            if image is None:
                skipped.append(slot)
                return
            written.append(save_listing_jpeg(image, out_dir / f"{slug}-{slot}.jpg"))

        emit("01-hero", slot_hero(pages, theme, fonts, product))
        emit("02-tablet", slot_plate("tablet", pages[4]))
        emit("03-desk", slot_plate("desk", pages[5]))
        emit("04-pages", slot_pages(pages, theme, fonts))
        emit("05-sizes", slot_sizes(pages, theme, fonts, size_keys))

        emit("06-features", text_slot(
            theme, fonts, "What Makes It Different", "Features",
            [("Navigation", "Tap any tab to jump between sections. Every page is bookmarked."),
             ("Undated", "Start any month, any year. Buy once, reuse indefinitely."),
             ("Four sizes", "A4, A5, US Letter and Half Letter, identical page for page."),
             ("Print ready", "Vector text at any scale. No pixelation when printed."),
             ("Typography", "Cormorant Garamond and Inter, licensed for embedding.")],
            footer=product.get("name", "")))

        emit("07-spread", slot_spread(pages, theme, fonts))

        emit("08-included", text_slot(
            theme, fonts, "What You Receive", "Included",
            [("Files", f"{len(size_keys)} PDF files, one per size"),
             ("Pages", f"{product['_pages']} pages in every file"),
             ("Documents", "README and licence, included in the download"),
             ("Delivery", "Instant download. Nothing is posted."),
             ("Format", "PDF. Opens on any device, prints on any printer.")],
            footer=product.get("name", "")))

        emit("09-howto", text_slot(
            theme, fonts, "How To Use It", "Three Steps",
            [("One", "Download the ZIP and open the size that suits your device."),
             ("Two", "Import into GoodNotes, Notability, Xodo or any PDF app."),
             ("Three", "Switch to read mode to tap links, write mode to annotate."),
             ("Printing", "Print at 100% scale. Never select fit to page.")],
            footer="Full instructions are included in the download"))

        emit("10-licence", text_slot(
            theme, fonts, "Terms Of Use", "Licence",
            [("You may", "Use it personally or in one business. Print unlimited copies."),
             ("You may not", "Resell, share or redistribute the files."),
             ("Fonts", "Embedded under the SIL Open Font License 1.1."),
             ("Refunds", "Faulty or misdescribed files are replaced or refunded.")],
            footer="Digital download. No physical item is shipped."))

    report = {
        "product": product.get("name"),
        "slug": slug,
        "engine": ENGINE_STAMP,
        "canvas": list(CANVAS),
        "written": written,
        "skipped": skipped,
        "plates_required": ["tablet", "desk"],
        "out_dir": str(out_dir),
    }
    (out_dir / "mockups.json").write_text(json.dumps(report, indent=2), encoding="utf8")

    print(f"  mockups : {len(written)} written to {out_dir}")
    for entry in written:
        print(f"    {entry['file']:<44} {entry['bytes']:>8,} B  q{entry['quality']}")
    if skipped:
        print(f"  skipped : {', '.join(skipped)} — no plate in {PLATE_DIR}")
    return report


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Etsy listing mockup renderer")
    parser.add_argument("spec", type=Path)
    parser.add_argument("--dist", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--dpi", type=int, default=200)
    args = parser.parse_args()

    print(f"ETSY-AI-FACTORY / {ENGINE_STAMP} / mockups\n")
    try:
        build_mockups(args.spec, dist_dir=args.dist, out_dir=args.out, dpi=args.dpi)
    except (MockupError, tokens.TokenError, assets.MissingFontError) as exc:
        print(f"\nMOCKUPS FAILED: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
