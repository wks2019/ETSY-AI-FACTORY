# MASTER INSTRUCTIONS

End-to-end production procedure for one product. Target lineup: 20.

---

## Phase 0 — Define

1. Assign product ID: `NN-kebab-case-name`
2. Create `products/NN-name/`
3. Author `spec.json`: page list, sizes, palette, typography, link map, bookmark tree
4. Confirm the product is differentiated from every shipped product — not a recolour

---

## Phase 1 — Build (PDF track)

1. Select or write the engine in `_ENGINE/`
2. Build: `python _ENGINE/<engine>.py products/NN-name/spec.json`
3. Run the ENGINE.md verification checklist
4. Iterate until all checks pass

Outputs land in `products/NN-name/dist/` — gitignored, never committed.

---

## Phase 2 — Build (Canva track)

Run in parallel, not sequentially. Independent deliverable.

1. `generate-design` — `design_type: document`, page-by-page prompt with hex values, typography, and grid structure
2. Review the four returned candidates
3. `create-design-from-candidate` on the selected one
4. **Manual correction pass — mandatory.** Calendar grids, tracker column counts, and hourly schedule rows are consistently wrong as generated
5. Verify all text is editable and all fonts are Canva-native

Never import the PDF into Canva. Import degrades quality and produces non-editable output.

---

## Phase 3 — Assets

| Asset | Spec |
|---|---|
| Cover | 300 DPI PNG |
| Listing preview | Multi-panel JPG (Product 1: 12 panels) |
| Mockups | Device + print context |
| Thumbnail | First listing image, readable at small size |

---

## Phase 4 — SEO

Write `_SEO/NN-name.md`:

- Title — front-load the primary keyword, 140 char limit
- Tags — all 13 used, multi-word, no duplicated single terms
- Description — hook in the first two lines (mobile truncates), then contents, then usage, then compatibility
- Attributes — fully completed

---

## Phase 5 — List

1. Upload to shop `wks2019`
2. Attach all size variants as a single digital download
3. Include a usage/compatibility PDF in the download bundle
4. Publish

---

## Phase 6 — Commit

Commit spec, assets source, SEO copy, and any engine changes. Never commit `dist/` binaries.

---

## Order of operations

Phases 1 and 2 run in parallel. Phase 3 depends on Phase 1. Phases 4–5 depend on 1 and 3. Do not start Phase 5 with an incomplete Phase 4.
