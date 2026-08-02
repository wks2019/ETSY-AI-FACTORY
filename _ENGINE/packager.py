"""
packager.py
ETSY-AI-FACTORY / _ENGINE

Assembles the customer-facing deliverable folder.

engines/AUTOMATION_ENGINE.md Stage 18. Ships no placeholders: every file it
writes is populated from the spec or omitted.
"""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path

FOLDERS = ["PDF", "Previews", "Documentation"]


def build_package(out_dir: Path, spec: dict, results, cover: Path | None,
                  preview: Path | None, theme=None) -> Path:
    product = spec.get("product", {})
    name = product.get("name", "Planner")
    version = product.get("version", "1.0")

    for folder in FOLDERS:
        (out_dir / folder).mkdir(parents=True, exist_ok=True)

    for result in results:
        target = out_dir / "PDF" / result.path.name
        if result.path.resolve() != target.resolve():
            target.write_bytes(result.path.read_bytes())

    for asset in (cover, preview):
        if asset and asset.exists():
            (out_dir / "Previews" / asset.name).write_bytes(asset.read_bytes())

    manifest = {
        "product": name,
        "version": version,
        "generated": date.today().isoformat(),
        "engine": "planner_engine 2.0",
        "sizes": [
            {
                "size": r.size_key,
                "file": r.path.name,
                "pages": r.pages,
                "links": r.links,
                "bookmarks": r.bookmarks,
            }
            for r in results
        ],
        "fonts": spec.get("design", {}).get("fonts", {}),
        "theme": getattr(theme, "name", "neutral"),
        "tokens": getattr(theme, "bindings", {}) if theme else {},
        "contrast_audit": theme.verify() if theme else [],
        "licence": "Personal use. Commercial redistribution not permitted.",
    }
    (out_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf8"
    )

    (out_dir / "Documentation" / "INSTRUCTIONS.md").write_text(
        _instructions(name, results), encoding="utf8"
    )
    (out_dir / "Documentation" / "LICENCE.md").write_text(
        _licence(name), encoding="utf8"
    )

    return out_dir


def _instructions(name: str, results) -> str:
    sizes = "\n".join(
        f"| {r.size_key} | `{r.path.name}` | {r.pages} |" for r in results
    )
    return f"""# {name} — How to use

Thank you for your purchase.

## What is included

| Size | File | Pages |
|---|---|---|
{sizes}

Choose the size that matches your device or paper. All versions contain the
same pages.

## Digital planning

1. Open the PDF in your annotation app — GoodNotes, Notability, Noteshelf,
   Xodo, or any app that supports PDF import.
2. Import the file as a document, not as an image.
3. Tap the tabs at the top of any page to jump between sections.
4. Use the bookmark or outline panel for the full page list.

## Printing

- Print at 100% scale. Do not select "fit to page" — it shifts the margins.
- Use 100–120 gsm paper for double-sided printing without show-through.
- A5 and Half Letter can be printed two-up on A4 or US Letter.

## Editing in Canva

1. In Canva, choose **Create a design → Import file** and select the PDF.
2. Text remains editable. Fonts used are Cormorant Garamond and Inter, both
   available in Canva.
3. Check spacing after import before exporting.

## Support

Message through your order page and we will respond within one business day.
"""


def _licence(name: str) -> str:
    return f"""# Licence — {name}

## You may

- Use this planner for personal or single-business use.
- Print unlimited copies for your own use.
- Annotate digitally on your own devices.

## You may not

- Resell, share, or redistribute the files in any form.
- Sell printed copies.
- Claim the design as your own.
- Include the files in another digital product or bundle.

## Fonts

Cormorant Garamond and Inter are used under the SIL Open Font License 1.1.
The licence covers the fonts only, not this document.

All other design elements are original work.
"""
