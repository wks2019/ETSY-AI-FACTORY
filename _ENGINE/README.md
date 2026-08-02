# _ENGINE

The canonical rendering engine. Version 2.0.

Spec in, four vector PDFs out, with a verification gate that fails the build
rather than shipping a defect.

## Modules

| File | Responsibility |
|---|---|
| `planner_engine.py` | CLI orchestration, spec validation, build verification |
| `tokens.py` | Semantic colour resolution and WCAG contrast enforcement |
| `layout_renderer.py` | Spec → HTML plus size-specific CSS. Fifteen page renderers |
| `pdf_renderer.py` | WeasyPrint render, PDF inspection, raster export |
| `packager.py` | Deliverable folder, manifest, instructions, licence |
| `assets.py` | Font resolution and page geometry |
| `tests/renderer_fixture.json` | Exercises every renderer across all four sizes |

## Usage

```bash
python _ENGINE/planner_engine.py products/01-name/spec.json
python _ENGINE/planner_engine.py spec.json --theme dark --sizes a4
python _ENGINE/planner_engine.py spec.json --validate-only
```

## Requirements

```bash
pip install weasyprint pypdf pillow jsonschema
apt install poppler-utils          # pdftoppm, for preview export
```

Fonts download once into `_ENGINE/fonts/` on first run. That directory is
gitignored — OFL permits embedding a font in a PDF, but shipping the font
file is redistribution.

## Available layouts

`cover` · `prose` · `index` · `year` · `month` · `quarter` · `week` · `day`
`agenda` · `ledger` · `record` · `timeline` · `tracker` · `panels` · `notes`

Adding a page type means one function and one registry entry in
`layout_renderer.py`. Nothing else changes.

## Design rule

The engine renders. It does not decide.

No palette, no type scale, no page list and no product knowledge belongs in
this code. Colour arrives as resolved tokens; everything else arrives in the
spec. If a change here needs a product name in it, the change belongs in the
spec instead.

## Verification gate

Every build checks, and fails on:

- Page count parity across all four sizes
- Page count matching the expanded spec
- Bookmark count equal to page count
- Presence of internal links
- Every contrast rule in `_SCHEMA/themes.json`
- Declared `must_link_to` targets existing

Three defects were caught by this gate during v1 development — page overflow,
margins not scaling at A5, and subtitles becoming stray bookmarks. None were
visible without it.

## Enforcement at load

1. JSON Schema validation against `_SCHEMA/spec.schema.json`
2. Literal colour rejection — any hex anywhere in a spec fails the build
3. Theme contrast enforcement before a single page renders
