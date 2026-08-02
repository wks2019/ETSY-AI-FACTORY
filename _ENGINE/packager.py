"""
packager.py
ETSY-AI-FACTORY / _ENGINE

Assembles the customer-facing deliverable folder and the Etsy-ready archive.

engines/AUTOMATION_ENGINE.md Stage 18. Ships no placeholders: every file it
writes is populated from the spec or omitted.

Deliverable layout:

    package/
      <slug>-<size>.pdf     one per rendered size
      README.pdf            how to use, generated from the spec
      LICENSE.pdf           terms of use, generated from the spec
      manifest.json         build record, including archive metadata
      previews/             cover PNG and listing preview JPG
      <slug>.zip            everything above, minus itself

The archive hash cannot appear inside the archive it describes. The manifest
written to disk carries the `archive` block; the copy sealed inside the ZIP
carries `archive: null`. That asymmetry is deliberate and recorded in the
manifest itself via `archive_recorded_outside`.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import zipfile
from datetime import date, datetime, timezone
from pathlib import Path

from weasyprint import HTML

from version import ENGINE_STAMP, ENGINE_VERSION, PACKAGE_FORMAT

PREVIEW_DIR = "previews"
CHUNK = 1024 * 1024


class PackageError(RuntimeError):
    pass


# ----------------------------------------------------------------------
# HASHING
# ----------------------------------------------------------------------

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(CHUNK), b""):
            digest.update(block)
    return digest.hexdigest()


# ----------------------------------------------------------------------
# DOCUMENT PDFs
# ----------------------------------------------------------------------

def _doc_css(theme) -> str:
    """Minimal print stylesheet for the two documentation PDFs.

    Deliberately does not load the product faces. These pages are read, not
    branded, and binding them to the font pipeline would make a documentation
    change able to fail a build for a font reason.
    """
    b = getattr(theme, "bindings", {}) if theme else {}
    background = b.get("background", "#FBF9F4")
    text = b.get("text-primary", "#2B2B28")
    muted = b.get("text-muted", "#6E6E64")
    rule = b.get("divider", "#E6E2D8")
    surface = b.get("surface", "#F4F1E9")

    return f"""
@page {{ size: 210mm 297mm; margin: 20mm; background: {background}; }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 10.5pt; line-height: 1.5;
        color: {text}; margin: 0; }}
h1 {{ font-family: 'DejaVu Serif', serif; font-size: 24pt; font-weight: 400;
      margin: 0 0 4pt 0; }}
.sub {{ font-size: 8pt; letter-spacing: 0.14em; text-transform: uppercase;
        color: {muted}; margin-bottom: 18pt; }}
h2 {{ font-size: 9pt; letter-spacing: 0.10em; text-transform: uppercase;
      color: {muted}; margin: 18pt 0 6pt 0; }}
p {{ margin: 0 0 8pt 0; }}
ul, ol {{ margin: 0 0 8pt 0; padding-left: 16pt; }}
li {{ margin: 0 0 3pt 0; }}
table {{ width: 100%; border-collapse: collapse; margin: 0 0 8pt 0; }}
th {{ font-size: 7pt; letter-spacing: 0.10em; text-transform: uppercase;
      color: {muted}; text-align: left; background: {surface};
      padding: 5pt 6pt; border-bottom: 0.5pt solid {rule}; }}
td {{ padding: 5pt 6pt; border-bottom: 0.5pt solid {rule}; font-size: 9pt; }}
.foot {{ margin-top: 24pt; padding-top: 8pt; border-top: 0.5pt solid {rule};
         font-size: 7pt; color: {muted}; }}
"""


def _render_doc(title: str, subtitle: str, body: str, out_path: Path,
                theme=None, footer: str = "") -> Path:
    document = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{title}</title>
<style>{_doc_css(theme)}</style></head>
<body><h1>{title}</h1><div class="sub">{subtitle}</div>{body}
<div class="foot">{footer}</div></body></html>"""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    HTML(string=document).write_pdf(target=str(out_path))
    return out_path


def _readme_body(results) -> str:
    rows = "".join(
        f"<tr><td>{r.size_key}</td><td>{r.path.name}</td><td>{r.pages}</td></tr>"
        for r in results
    )
    return f"""
<h2>What is included</h2>
<table><thead><tr><th>Size</th><th>File</th><th>Pages</th></tr></thead>
<tbody>{rows}</tbody></table>
<p>Choose the size that matches your device or paper. All versions contain the
same pages.</p>

<h2>Digital planning</h2>
<ol>
<li>Open the PDF in your annotation app — GoodNotes, Notability, Noteshelf,
Xodo, or any app that supports PDF import.</li>
<li>Import the file as a document, not as an image.</li>
<li>Tap the tabs at the top of any page to jump between sections.</li>
<li>Use the bookmark or outline panel for the full page list.</li>
</ol>

<h2>Printing</h2>
<ul>
<li>Print at 100% scale. Do not select "fit to page" — it shifts the margins.</li>
<li>Use 100–120 gsm paper for double-sided printing without show-through.</li>
<li>A5 and Half Letter can be printed two-up on A4 or US Letter.</li>
</ul>

<h2>Editing in Canva</h2>
<ol>
<li>In Canva, choose Create a design, then Import file, and select the PDF.</li>
<li>Text remains editable. Fonts used are Cormorant Garamond and Inter, both
available in Canva.</li>
<li>Check spacing after import before exporting.</li>
</ol>

<h2>Support</h2>
<p>Message through your order page and we will respond within one business day.</p>
"""


def _licence_body() -> str:
    return """
<h2>You may</h2>
<ul>
<li>Use this planner for personal or single-business use.</li>
<li>Print unlimited copies for your own use.</li>
<li>Annotate digitally on your own devices.</li>
</ul>

<h2>You may not</h2>
<ul>
<li>Resell, share, or redistribute the files in any form.</li>
<li>Sell printed copies.</li>
<li>Include the files in another digital product or bundle.</li>
<li>Claim the design as your own.</li>
</ul>

<h2>Fonts</h2>
<p>Cormorant Garamond and Inter are used under the SIL Open Font License 1.1.
That licence covers the fonts only, not this document. All other design
elements are original work.</p>
"""


# ----------------------------------------------------------------------
# ARCHIVE
# ----------------------------------------------------------------------

def _archive_members(root: Path, exclude: Path) -> list[Path]:
    return sorted(
        p for p in root.rglob("*")
        if p.is_file() and p.resolve() != exclude.resolve()
    )


def write_archive(package_dir: Path, zip_path: Path) -> dict:
    """Deflate the package into a single ZIP and describe it.

    Member order and entry timestamps are fixed, which removes the ZIP layer
    as a source of variation. The archive is still not reproducible across
    builds: WeasyPrint writes a fresh document ID into every PDF, so two
    builds of an unchanged spec yield different hashes. The SHA256 therefore
    identifies a specific build — use it to prove a customer's download
    matches what was uploaded, not to detect whether the spec changed.
    """
    members = _archive_members(package_dir, zip_path)
    if not members:
        raise PackageError(f"Nothing to archive in {package_dir}")

    fixed = (1980, 1, 1, 0, 0, 0)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for member in members:
            info = zipfile.ZipInfo(str(member.relative_to(package_dir)), date_time=fixed)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            archive.writestr(info, member.read_bytes())

    return {
        "file": zip_path.name,
        "bytes": zip_path.stat().st_size,
        "sha256": sha256_file(zip_path),
        "entries": len(members),
        "compression": "deflate",
        "package_format": PACKAGE_FORMAT,
        "created": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def verify_archive(zip_path: Path, package_dir: Path) -> dict:
    """Extraction test. A ZIP that opens is not a ZIP that restores.

    Checks CRC integrity, member parity against the source folder, and a
    byte-for-byte digest match on every extracted entry.
    """
    problems: list[str] = []
    try:
        with zipfile.ZipFile(zip_path) as archive:
            corrupt = archive.testzip()
            if corrupt is not None:
                problems.append(f"CRC failure in member: {corrupt}")

            names = set(archive.namelist())
            expected = {
                str(p.relative_to(package_dir))
                for p in _archive_members(package_dir, zip_path)
            }
            for missing in sorted(expected - names):
                problems.append(f"missing from archive: {missing}")
            for extra in sorted(names - expected):
                problems.append(f"unexpected in archive: {extra}")

            for name in sorted(names & expected):
                if corrupt is not None:
                    break
                source = (package_dir / name).read_bytes()
                if hashlib.sha256(archive.read(name)).hexdigest() != \
                   hashlib.sha256(source).hexdigest():
                    problems.append(f"content mismatch on extract: {name}")
    except zipfile.BadZipFile as exc:
        raise PackageError(f"Archive is corrupt and cannot be read: {exc}") from None

    if problems:
        raise PackageError(
            "Archive failed extraction test:\n  " + "\n  ".join(problems)
        )

    return {"extraction_test": "passed", "entries_verified": len(expected)}


# ----------------------------------------------------------------------
# BUILD
# ----------------------------------------------------------------------

def build_package(out_dir: Path, spec: dict, results, cover: Path | None,
                  preview: Path | None, theme=None) -> Path:
    product = spec.get("product", {})
    name = product.get("name", "Planner")
    slug = product.get("slug", "planner")
    version = product.get("version", "1.0")

    # The package folder is generated output, never hand-edited. Rebuilding
    # in place left files from a previous layout behind, and they were swept
    # into the archive — a stale PDF/ tree shipped inside a customer ZIP
    # during testing. Clearing is the only safe rebuild.
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    previews_dir = out_dir / PREVIEW_DIR
    previews_dir.mkdir(parents=True, exist_ok=True)

    for result in results:
        target = out_dir / result.path.name
        if result.path.resolve() != target.resolve():
            target.write_bytes(result.path.read_bytes())

    for asset in (cover, preview):
        if asset and asset.exists():
            (previews_dir / asset.name).write_bytes(asset.read_bytes())

    footer = f"{name} v{version} · built with {ENGINE_STAMP}"
    _render_doc(name, "How to use this planner", _readme_body(results),
                out_dir / "README.pdf", theme=theme, footer=footer)
    _render_doc(f"Licence — {name}", "Terms of use", _licence_body(),
                out_dir / "LICENSE.pdf", theme=theme, footer=footer)

    manifest = {
        "product": name,
        "slug": slug,
        "version": version,
        "generated": date.today().isoformat(),
        "engine": ENGINE_STAMP,
        "engine_version": ENGINE_VERSION,
        "package_format": PACKAGE_FORMAT,
        "sizes": [
            {
                "size": r.size_key,
                "file": r.path.name,
                "pages": r.pages,
                "links": r.links,
                "bookmarks": r.bookmarks,
                "bytes": r.path.stat().st_size,
                "sha256": sha256_file(r.path),
            }
            for r in results
        ],
        "documents": ["README.pdf", "LICENSE.pdf"],
        "previews": sorted(p.name for p in previews_dir.iterdir() if p.is_file()),
        "fonts": spec.get("design", {}).get("fonts", {}),
        "theme": getattr(theme, "name", "neutral"),
        "tokens": getattr(theme, "bindings", {}) if theme else {},
        "contrast_audit": theme.verify() if theme else [],
        "licence": "Personal use. Commercial redistribution not permitted.",
        "archive": None,
        "archive_recorded_outside": True,
    }

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf8")

    zip_path = out_dir / f"{slug}.zip"
    if zip_path.exists():
        zip_path.unlink()

    archive = write_archive(out_dir, zip_path)
    archive.update(verify_archive(zip_path, out_dir))

    manifest["archive"] = archive
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf8")

    print(f"  archive : {zip_path.name}  {archive['bytes']:,} bytes  "
          f"{archive['entries']} entries")
    print(f"  sha256  : {archive['sha256']}")
    print(f"  extract : {archive['extraction_test']}")

    return out_dir
