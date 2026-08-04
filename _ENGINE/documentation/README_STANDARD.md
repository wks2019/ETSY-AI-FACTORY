# Build, QA and Packaging Standard

Engine 2.1 · Shared documentation for every product in the collection.

This file exists because the same eight sections were repeated in every
product README, drifting slightly each time. Product READMEs now carry only
what is specific to that product and refer here for everything else.

---

## 1. Build

```bash
# From an existing spec.json — the original workflow, unchanged
python _ENGINE/planner_engine.py products/<n>-<slug>/spec.json

# Validate without rendering
python _ENGINE/planner_engine.py products/<n>-<slug>/spec.json --validate-only

# From a compact source — Engine 2.1
python _ENGINE/expand_spec.py expand products/<n>-<slug>/product.dsl \
    --out products/<n>-<slug>/spec.json
python _ENGINE/planner_engine.py products/<n>-<slug>/spec.json
```

Both paths produce byte-equivalent page content. The renderer receives the
same JSON either way and has no knowledge of the expansion layer.

---

## 2. Validation gates

`validate_spec` runs before any rendering and fails the build on:

- schema violations against `_SCHEMA/spec.schema.json`
- navigation tab targets matching no page **type** — the schema cannot catch
  this, and an unresolved target silently degrades to a dead anchor on every
  page
- literal colour values anywhere in the spec — colour belongs to the theme
- duplicate page ids
- unknown layouts

---

## 3. Verification gates

Run after rendering, before anything shippable is written to disk:

| Gate | Fails when |
|---|---|
| Page parity | page counts differ across the four sizes |
| Link parity | link counts differ across sizes — catches content clipped at a smaller page |
| Bookmark parity | bookmark count ≠ page count |
| Contrast | any of nine token pairings falls below its WCAG floor |
| `must_link_to` | a declared link target does not exist |

**Link parity is the gate that earns its keep.** Page and bookmark counts stay
correct while a chip row is clipped off the bottom of a shorter page; only the
link count moves.

---

## 4. QA pipeline

Beyond the engine's own gates, every product is checked for:

- dead HTML anchors — every `href="#id"` resolves to a real page id
- unresolved PDF destinations across all four rendered files
- named destination count equal to page count
- archive extraction test — CRC, member parity, per-entry digest match
- visual spot-check at the worst-case size for any layout new to that product

---

## 5. Known layout ceilings

Recorded from real build failures. Respect these when authoring.

| Renderer | Ceiling | Evidence |
|---|---|---|
| `agenda` | Four panels plus a notes block plus an action table plus a chip row overflows at **US Letter** | Products 05 and 10 both failed link parity this way. `MEETING_STANDARD` is capped at two panels and no chips. |
| `tracker` | 33 columns renders correctly but is fiddly to tick by hand on printed Half Letter | Product 12, 66-day builder |
| `prose` | Roughly 40 body lines at A4 before a page break appears | — |

US Letter is 17.6mm shorter than A4 at the same type scale. It is the size
that fails first, not Half Letter, because Half Letter scales type down by
0.66 while US Letter does not.

---

## 6. Packaging

`packager.build_package` writes the customer deliverable:

```
package/
  <slug>-<size>.pdf     one per rendered size
  README.pdf            generated from the spec
  LICENSE.pdf           generated from the spec
  manifest.json         build record including archive metadata
  previews/             cover PNG and listing preview JPG
  <slug>.zip            everything above, minus itself
```

The package folder is cleared and rebuilt every time. The archive is verified
by extraction — CRC, member parity and a per-entry digest comparison — before
the manifest is finalised.

**PDFs are not byte-reproducible.** WeasyPrint writes a fresh document ID into
every render, so two builds of an unchanged spec produce different file
hashes. The SHA256 in a manifest identifies a specific build, proving a
customer's download matches what was uploaded. It does not prove the spec is
unchanged. To compare two builds for equivalence, compare extracted text per
page plus page, link and bookmark counts.

---

## 7. Repository standards

- **Directory number is build order. `collection_number` in `manifest.json` is
  catalogue position.** These diverged at product 08 and neither can be
  inferred from the other.
- Directory names use two digits: `products/08-focus-planner`.
- `dist/` is generated and gitignored. Never commit rendered output.
- Every product commits: `spec.json`, `README.md`, `LICENSE.md`,
  `manifest.json`, `metadata.json`, `preview_manifest.json`.
- `product.dsl` is optional and regenerable at any time:
  `python _ENGINE/expand_spec.py decompile <spec.json> --out product.dsl`

---

## 8. Rendering notes

- Four sizes: A4, A5, US Letter, Half Letter. A5 and Half Letter scale type
  and margins by 0.66 — a verified figure, not a derived one. 0.72 was tried
  and produced 46 pages at A5 against 42 at A4.
- Fonts are Cormorant Garamond and Inter, both OFL 1.1, embedded as subsets.
  The build fails rather than substituting a face.
- Text is never rasterised or converted to outlines.
- There is no tablet page size in engine v2.1. A5 and Half Letter are the
  tablet-appropriate sizes.

---

## 9. Engine notes

The renderer is stable and is not modified by product work. Adding a page type
means adding one function and one registry entry in `layout_renderer.py`;
nothing else in the engine changes.

Engine 2.1 added an authoring layer — `language.py`, `expand_spec.py`,
`templates/`, `components/`, `defaults/` — that sits entirely before the
renderer. None of `planner_engine.py`, `layout_renderer.py`,
`pdf_renderer.py`, `packager.py`, `assets.py` or `tokens.py` was changed to
support it.
