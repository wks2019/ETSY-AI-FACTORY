# ENGINE

Technical reference for the PDF generation pipeline.

---

## Stack

| Layer | Choice | Reason |
|---|---|---|
| Render | WeasyPrint | HTML/CSS → PDF with reliable link annotations and outlines |
| Layout | HTML + CSS Paged Media | `@page` rules give per-size control without re-authoring |
| Fonts | Cormorant Garamond + Inter | OFL — embeddable and commercially redistributable |
| Raster export | Cover PNG @ 300 DPI, listing preview JPG | Etsy listing assets |

---

## Location

```
_ENGINE/planner_engine.py
```

The engine is product-agnostic. It consumes a spec and emits a build. It contains no product-specific content.

---

## Contract

**Input:** `products/<id>/spec.json`

**Output:** `products/<id>/dist/` (gitignored)

```
dist/
  <product>-A4.pdf
  <product>-A5.pdf
  <product>-US-Letter.pdf
  <product>-Half-Letter.pdf
  cover-300dpi.png
  listing-preview.jpg
```

---

## Size matrix

| Size | Dimensions |
|---|---|
| A4 | 210 × 297 mm |
| A5 | 148 × 210 mm |
| US Letter | 8.5 × 11 in |
| Half Letter | 5.5 × 8.5 in |

All four are generated from one source. Layout is proportional — never re-author per size.

---

## Navigation

Two independent systems, both required:

1. **Internal link annotations** — tab bars, month jumps, day cells, back-links. Product 1 baseline: 943.
2. **PDF bookmarks** — outline tree matching the page list. Product 1 baseline: 42.

Bookmark count must equal page count unless the spec declares grouped sections.

---

## Design tokens

| Token | Value |
|---|---|
| Base | Ivory |
| Text | Charcoal |
| Accent 1 | Sage |
| Accent 2 | Gold |
| Display | Cormorant Garamond |
| Body / UI | Inter |

Tokens live in the spec, not the engine.

---

## Build

```bash
python _ENGINE/planner_engine.py products/<id>/spec.json
```

---

## Verification checklist

Run before any product is considered shipped:

- [ ] Page count matches spec
- [ ] All four sizes render without overflow
- [ ] Link annotation count matches expected total
- [ ] Every link resolves to an in-document target (no dead targets)
- [ ] Bookmark tree complete and correctly nested
- [ ] Fonts embedded (subset), no fallback substitution
- [ ] Cover PNG is 300 DPI
- [ ] Listing preview panel count matches spec

---

## Extension rule

New product types get a new engine file in `_ENGINE/`, not a branch inside `planner_engine.py`. Shared helpers may be factored out only once a second engine actually needs them.
