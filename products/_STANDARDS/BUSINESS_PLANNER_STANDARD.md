# BUSINESS_PLANNER_STANDARD.md

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY
Applies to: every Business Planner product, all editions, all future versions

---

# 0. AUTHORITY

This standard sits at rank 7 (`systems/`) in the hierarchy defined by `PROJECT_RULES.md` §3. It extends the rules above it and never contradicts them.

Where this document and a higher-ranked file disagree, the higher-ranked file wins and the conflict is logged per `FACTORY_PROTOCOL.md`.

This is a blueprint, not a product. No planner is built from this document alone — each product supplies its own `spec.json` conforming to §11.

---

# 1. PRODUCT PURPOSE

A Business Planner is an undated, hyperlinked planning system for running a small business or a self-employed practice.

It exists to remove three specific frictions:

| Friction | Page response |
|---|---|
| Work scattered across apps, notebooks, and memory | One index, one navigation model |
| No record of what was decided or promised | Meeting Notes, Project Planner, Client-facing pages |
| Money tracked only at tax time | Expense Tracker, Review |

It is a tool, not stationery. Every page must earn its place by completing a task the customer already performs badly.

---

# 2. TARGET CUSTOMER

| Attribute | Definition |
|---|---|
| Primary | Solo founder, freelancer, consultant, or owner of a business with fewer than ten staff |
| Age | 25–55 |
| Market | English-speaking. US, UK, CA, AU primary |
| Device | iPad with GoodNotes or Notability, or printed and filed |
| Sophistication | Comfortable with digital tools. Has abandoned at least one previous planner |
| Buying trigger | A new quarter, a new financial year, or a period of feeling out of control |

**What this customer rejects:** decorative illustration, motivational quotes, cramped writing space, anything that looks like a school workbook.

**What this customer pays more for:** navigation that works, generous writing areas, and a product that prints correctly the first time.

---

# 3. PRODUCT GOALS

| # | Goal | Measure |
|---|---|---|
| 1 | Usable within sixty seconds of opening | Index is page 4; every page reaches every section in one tap |
| 2 | Prints correctly without instruction | 100% scale, safe margins, no bleed dependency |
| 3 | Editable by the customer in Canva | Live text, Canva-available fonts, no clipping masks |
| 4 | Recognisably part of the Business Collection | Shared palette, type pairing, component set |
| 5 | Competes with the top-rated listings in its niche | Quality score ≥ 95/100 |
| 6 | Produces its variants at near-zero cost | Theme and edition changes are spec-only |

---

# 4. SUPPORTED PAPER SIZES

All four are mandatory. A product missing one is incomplete.

| Key | Label | Dimensions | Notes |
|---|---|---|---|
| `a4` | A4 | 210 × 297 mm | Primary. Preview and cover render from this |
| `a5` | A5 | 148 × 210 mm | Two-up printable on A4 |
| `us_letter` | US Letter | 8.5 × 11 in | Primary for US market |
| `half_letter` | Half Letter | 5.5 × 8.5 in | Two-up printable on US Letter |

**Rules**

- All four render from one source. Never re-author a layout per size.
- Page count must be identical across all four. A differing count is a build failure, not a variation.
- Margins and type scale proportionally to the page. A5 is not A4 shrunk on a photocopier.
- Every size carries the full link and bookmark set.

---

# 5. THEME SYSTEM

A theme is a palette and nothing else. It changes no layout, no page count, no component.

| Theme | Character | Use |
|---|---|---|
| `neutral` | Ivory, charcoal, sage, gold | Default. The collection anchor |
| `dark` | Charcoal ground, warm off-white ink | Screen-first buyers. Warn on print cost in the listing |
| `mono` | Pure greyscale | Print economy. No colour ink required |
| `slate` | Cool grey with a single blue accent | Corporate/consulting positioning |

**Rules**

- A theme is a swap of the `design.palette` block. If a theme requires a layout change, it is not a theme.
- Every theme must pass contrast checks at body text size.
- A theme variant is a separate listing, not a separate product. It does not consume a slot in the collection.

---

# 6. TYPOGRAPHY RULES

Inherits `engines/DESIGN_ENGINE.md`.

| Constraint | Value |
|---|---|
| Font families | Maximum 2 |
| Weights | Maximum 3 |
| Sizes | Maximum 4 |
| Display face | Cormorant Garamond — page titles only |
| Body / UI face | Inter — everything else |
| Licence | SIL Open Font License 1.1 |
| Canva availability | Both faces must exist in Canva. Verify before substituting either |

**Rules**

- Text is never rasterised or converted to outlines. Fonts embed as subsets.
- Body text must remain legible at Half Letter scale. This is the binding constraint, not A4.
- Labels and tabs use uppercase Inter with letter-spacing. Never uppercase the display face.
- No decorative or script faces anywhere, including the cover.
- Never synthesise bold or italic. Use a real weight from the variable axis.

---

# 7. COLOUR PALETTE STRUCTURE

Every theme defines exactly these roles. No colour exists outside a role.

| Role | Purpose | Constraint |
|---|---|---|
| `ink` | Body text, titles | ≥ 7:1 against `paper` |
| `paper` | Page ground | Never pure white |
| `muted` | Labels, secondary text, tab text | ≥ 4.5:1 against `paper` |
| `rule` | Hairlines, table borders, panel edges | Visible in print at 0.5pt |
| `accent` | Current-state indicators, active tab | Used sparingly. Never as a fill behind body text |
| `gold` | Cover rule, single emphasis mark | Cover and dividers only |

**Rules**

- Six roles. Not five, not eight. A product needing a seventh is proposing a system change, not a colour.
- Colour never carries meaning alone. A state shown in colour must also be shown in position or label.
- Financial pages use no red/green profit-loss coding — it fails in greyscale print and for colour-blind users.

---

# 8. PAGE ORDER

The canonical sequence. Every Business Planner follows it. Pages may be omitted where marked optional; the surviving pages keep this relative order.

| # | Page | Repeats | Optional |
|---|---|---|---|
| 1 | Cover | — | No |
| 2 | License | — | No |
| 3 | Read Me | — | No |
| 4 | Index | — | No |
| 5 | Year Overview | — | No |
| 6 | Quarter Planner | × 4 | No |
| 7 | Monthly Planner | × 12 | No |
| 8 | Weekly Planner | × 5 | No |
| 9 | Daily Planner | × 7 | No |
| 10 | Meeting Notes | × 4 | No |
| 11 | Project Planner | × 4 | No |
| 12 | Goal Planner | × 2 | No |
| 13 | Habit Tracker | × 2 | No |
| 14 | Expense Tracker | × 3 | No |
| 15 | Notes | × 4 | No |
| 16 | Contacts | × 2 | No |
| 17 | Passwords | × 1 | **Yes — see §8.1** |
| 18 | Resources | × 1 | Yes |
| 19 | Review | × 2 | No |
| 20 | Back Cover | — | No |

**Reference page count:** 1+1+1+1+1+4+12+5+7+4+4+2+2+3+4+2+1+1+2+1 = **59 pages** with all optional pages included.

Repeat counts are the standard baseline. A product may change them in its spec; it may not change the order.

## 8.1 Passwords page — conditional

Include only when the listing states plainly that entries are stored unencrypted on paper or in an unprotected PDF.

A planner sold to business owners invites them to record client and banking credentials. If the file is synced, shared, or printed and left on a desk, those credentials are exposed — and the customer's exposure is not limited to themselves.

**Required if included:** the page must be titled for non-critical access hints, must carry a printed caution against recording full passwords or banking credentials, and must not be included in the `mono` print-economy edition, which is the one most likely to be printed and left loose.

Default: **omit**. Include only on deliberate decision.

---

# 9. PAGE DEFINITIONS

Each page defines Purpose, Layout Type, Required Components, Optional Components, Renderer Type, and JSON Fields.

**Renderer Type** names the function in `_ENGINE/layout_renderer.py`. Types marked **NEW** do not exist yet and must be built before that page can render.

---

### 1. Cover

| | |
|---|---|
| **Purpose** | Establish perceived value in under two seconds. Sets the price the customer accepts |
| **Layout Type** | Centred, full-bleed ground, no navigation |
| **Required** | Collection line, product title, gold rule, subtitle |
| **Optional** | Edition mark, year |
| **Renderer** | `cover` |
| **JSON** | `id`, `type`, `title`, `subtitle`, inherits `product.collection` |

### 2. License

| | |
|---|---|
| **Purpose** | State permitted and prohibited use. Reduces refund and dispute rate |
| **Layout Type** | Two-column prose |
| **Required** | Permitted use, prohibited use, font attribution |
| **Optional** | Commercial upgrade path |
| **Renderer** | `prose` **NEW** |
| **JSON** | `id`, `type`, `title`, `blocks[]` |

### 3. Read Me

| | |
|---|---|
| **Purpose** | Get the customer using the product in sixty seconds |
| **Layout Type** | Numbered instruction blocks |
| **Required** | Digital use, printing, Canva editing, navigation explanation |
| **Optional** | Support contact |
| **Renderer** | `prose` **NEW** |
| **JSON** | `id`, `type`, `title`, `blocks[]` |

### 4. Index

| | |
|---|---|
| **Purpose** | Single point of navigation to every page |
| **Layout Type** | Two-column linked table, auto-split |
| **Required** | Every non-cover page, linked; page type label |
| **Optional** | Section grouping headers |
| **Renderer** | `index` |
| **JSON** | `id`, `type`, `title`, `include_types[]`, `column_break` |

### 5. Year Overview

| | |
|---|---|
| **Purpose** | Whole-year view for planning launches, seasons, and quiet periods |
| **Layout Type** | Quarter grid |
| **Required** | Four quarter cells, month chip navigation |
| **Optional** | Annual objective strip |
| **Renderer** | `year` |
| **JSON** | `id`, `type`, `title`, `weekday_labels[]`, `rows`, `chips` |

### 6. Quarter Planner

| | |
|---|---|
| **Purpose** | Bridge between annual intent and monthly execution. The plane most small businesses actually operate on |
| **Layout Type** | Three month columns plus objective panel |
| **Required** | Three month blocks, quarter objective, key dates |
| **Optional** | Revenue target, review link |
| **Renderer** | `quarter` **NEW** |
| **JSON** | `id`, `type`, `repeat_labels[]`, `panels[]`, `chips` |

### 7. Monthly Planner

| | |
|---|---|
| **Purpose** | Month at a glance with commitments and deadlines |
| **Layout Type** | Six-row calendar grid |
| **Required** | Seven-day grid, month chip navigation, footer link |
| **Optional** | Focus panel, monthly target |
| **Renderer** | `month` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `rows`, `weekday_labels[]`, `chips` |

### 8. Weekly Planner

| | |
|---|---|
| **Purpose** | Distribute the month's commitments across working days |
| **Layout Type** | Two-column, seven day blocks |
| **Required** | Seven labelled day blocks with writing lines |
| **Optional** | Weekly priorities panel, carry-over block |
| **Renderer** | `week` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `day_labels[]`, `lines`, `chips` |

### 9. Daily Planner

| | |
|---|---|
| **Purpose** | Hour-level execution for the working day |
| **Layout Type** | Split — hourly schedule left, panels right |
| **Required** | Hourly rows, top-three priorities, task panel |
| **Optional** | Notes panel, energy or focus marker |
| **Renderer** | `day` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `hour_start`, `hour_end`, `panels[]`, `chips` |

### 10. Meeting Notes

| | |
|---|---|
| **Purpose** | Capture what was decided and who owes what. The page that prevents disputes |
| **Layout Type** | Header block, notes area, action-item table |
| **Required** | Attendees, agenda, notes, actions with owner and due column |
| **Optional** | Follow-up date, decision log |
| **Renderer** | `agenda` **NEW** |
| **JSON** | `id`, `type`, `repeat_labels[]`, `panels[]`, `action_columns[]` |

### 11. Project Planner

| | |
|---|---|
| **Purpose** | Take one project from outcome to sequenced steps |
| **Layout Type** | Definition panels plus step list |
| **Required** | Project name, outcome, steps, deadline |
| **Optional** | Timeline strip, dependency notes, budget |
| **Renderer** | `panels`, upgrade to `timeline` **NEW** for the strip |
| **JSON** | `id`, `type`, `repeat_labels[]`, `panels[]`, `chips` |

### 12. Goal Planner

| | |
|---|---|
| **Purpose** | Convert an intention into milestones and a first action |
| **Layout Type** | Stacked panels |
| **Required** | Goal, why it matters, milestones, first action |
| **Optional** | Obstacles, review date |
| **Renderer** | `panels` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `panels[]`, `chips` |

### 13. Habit Tracker

| | |
|---|---|
| **Purpose** | Sustain the behaviours that keep the business running |
| **Layout Type** | Row-per-habit grid, 31 columns |
| **Required** | Habit name column, day columns |
| **Optional** | Target count, streak column |
| **Renderer** | `tracker` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `items[]`, `columns`, `chips` |

### 14. Expense Tracker

| | |
|---|---|
| **Purpose** | Record outgoings as they occur rather than reconstructing them at tax time |
| **Layout Type** | Ledger table with totals row |
| **Required** | Date, description, category, amount, total |
| **Optional** | Payment method, receipt-held marker, VAT column |
| **Renderer** | `ledger` **NEW** |
| **JSON** | `id`, `type`, `repeat_labels[]`, `columns[]`, `rows`, `totals` |

### 15. Notes

| | |
|---|---|
| **Purpose** | Unstructured capture. The page that stops the customer reaching for a different app |
| **Layout Type** | Ruled lines, full page |
| **Required** | Writing lines |
| **Optional** | Dot or grid alternative |
| **Renderer** | `notes` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `lines`, `chips` |

### 16. Contacts

| | |
|---|---|
| **Purpose** | Client and supplier reference without opening a device |
| **Layout Type** | Record rows |
| **Required** | Name, company, contact, notes |
| **Optional** | Category, last-contacted column |
| **Renderer** | `record` **NEW** |
| **JSON** | `id`, `type`, `repeat_labels[]`, `columns[]`, `rows` |

### 17. Passwords — optional, see §8.1

| | |
|---|---|
| **Purpose** | Non-critical access hints only |
| **Layout Type** | Record rows |
| **Required** | Service, username, hint field, printed caution |
| **Optional** | Recovery-email column |
| **Renderer** | `record` **NEW** |
| **JSON** | `id`, `type`, `columns[]`, `rows`, `notice` |

The field is a **hint**, never a password field. The caution text is required, not optional.

### 18. Resources

| | |
|---|---|
| **Purpose** | Tools, subscriptions, and references in one place |
| **Layout Type** | Two-column list |
| **Required** | Item, purpose |
| **Optional** | Cost, renewal date |
| **Renderer** | `record` **NEW** |
| **JSON** | `id`, `type`, `columns[]`, `rows` |

### 19. Review

| | |
|---|---|
| **Purpose** | Close the loop. Look back before planning forward |
| **Layout Type** | Stacked panels |
| **Required** | What worked, what did not, what changes, one win |
| **Optional** | Numbers summary, next-period focus |
| **Renderer** | `panels` |
| **JSON** | `id`, `type`, `repeat_labels[]`, `panels[]`, `chips` |

### 20. Back Cover

| | |
|---|---|
| **Purpose** | Close the document. Reinforce the brand at the last impression |
| **Layout Type** | Centred mark, minimal |
| **Required** | Collection line, gold rule |
| **Optional** | Shop name, version mark |
| **Renderer** | `cover` |
| **JSON** | `id`, `type`, `title`, `subtitle` |

---

## 9.1 Renderer gap

Six page types in this standard do not exist in the engine.

| Renderer | Needed by | Status |
|---|---|---|
| `prose` | License, Read Me | **NEW** |
| `quarter` | Quarter Planner | **NEW** |
| `agenda` | Meeting Notes | **NEW** |
| `ledger` | Expense Tracker | **NEW** |
| `record` | Contacts, Passwords, Resources | **NEW** |
| `timeline` | Project Planner (optional strip) | **NEW** |

Existing and sufficient: `cover`, `index`, `year`, `month`, `week`, `day`, `tracker`, `panels`, `notes`.

This standard is therefore **not yet buildable in full**. It is buildable today at 14 of 20 page types. The six above are the engine work this standard authorises — each becomes permanently reusable across the whole Business Collection.

---

# 10. NAMING CONVENTION

| Item | Pattern | Example |
|---|---|---|
| Product directory | `NN-kebab-case` | `02-business-planner` |
| Product slug | kebab-case | `business-planner` |
| PDF | `{slug}-{size}.pdf` | `business-planner-a4.pdf` |
| Themed PDF | `{slug}-{theme}-{size}.pdf` | `business-planner-dark-a4.pdf` |
| Cover | `{slug}-cover.png` | `business-planner-cover.png` |
| Preview | `{slug}-listing-preview.jpg` | — |
| ZIP | `{slug}-v{version}.zip` | `business-planner-v1.0.zip` |
| Page id | kebab-case, repeats suffixed `-NN` | `monthly-03` |
| Commit | Conventional commits | `feat:`, `fix:`, `docs:` |

**Rules:** lower case throughout. No spaces. No dates in filenames — the product is undated and a dated filename ages the listing.

---

# 11. FOLDER STRUCTURE

```
products/
    NN-business-planner/
        spec.json           product specification — the only required file
        README.md           build notes, decisions, deviations
        LICENSE.md          customer licence source
        assets/             product-specific source assets
        fonts/              only if the product overrides collection fonts
        source/             working files, HTML dumps, drafts
        exports/            generated PDFs — gitignored
        previews/           generated PNG and JPG — gitignored
        mockups/            listing mockups — gitignored
```

**Rules**

- `exports/`, `previews/`, `mockups/` are build output. Never committed.
- `fonts/` stays empty unless the product deliberately breaks from the collection pairing, which requires a written reason in `README.md`.
- The directory name carries the number; the slug inside `spec.json` does not.

**Deviation note:** the requested example used `products/BusinessPlanner/`. This standard uses `products/NN-business-planner/` to stay consistent with `products/01-ultimate-digital-planner/`, which already exists, and to keep the catalogue ordered. The subfolder set is exactly as requested.

---

# 12. JSON SPECIFICATION RULES

## 12.1 Document shape

```
{
  "schema":     "1.0",
  "language":   "en",
  "product":    { ... },
  "design":     { "palette": {...}, "fonts": {...} },
  "sizes":      [ "a4", "a5", "us_letter", "half_letter" ],
  "navigation": { "tabs": [...] },
  "pages":      [ ... ]
}
```

## 12.2 Page object

Every page carries these keys.

| Field | Required | Purpose |
|---|---|---|
| `id` | Yes | Unique. Becomes the PDF anchor and link target |
| `title` | Yes | Rendered heading. Becomes the bookmark label |
| `type` | Yes | Semantic page kind. Drives index grouping and tab state |
| `layout` | Yes | Renderer function. Maps to `_ENGINE/layout_renderer.py` |
| `theme` | No | Per-page palette override. Omit to inherit `design.palette` |
| `elements` | Yes | Layout-specific content — panels, columns, items, rows |
| `links` | No | Explicit link targets beyond the automatic tab and chip sets |
| `metadata` | No | Non-rendered notes — author intent, source, revision reason |
| `validation` | No | Per-page assertions the build must satisfy |

## 12.3 Rules

- `id` is unique across the document. Duplicates fail the build.
- Repeats use `repeat_labels[]`; ids are auto-suffixed `-01`, `-02`.
- No colour value appears outside `design.palette` or a `theme` block.
- No font name appears outside `design.fonts`.
- `elements` never contains raw HTML. The renderer owns markup.
- `validation` may assert expected line counts, column counts, or link counts. A failed assertion fails the build.

**Engine gap:** the current engine reads `type`, `title`, `subtitle`, `panels`, `items`, `columns`, `lines`, `chips`, `repeat_labels`. It does not yet read `layout`, `theme`, `elements`, `links`, `metadata`, or `validation`. Adopting this schema requires a spec-loader update, which must ship before or with the first product built to this standard.

---

# 13. PACKAGING RULES

The deliverable the customer receives.

```
{slug}-v{version}/
    PDF/
        {slug}-a4.pdf
        {slug}-a5.pdf
        {slug}-us_letter.pdf
        {slug}-half_letter.pdf
    Previews/
        {slug}-cover.png
        {slug}-listing-preview.jpg
    Documentation/
        INSTRUCTIONS.md
        LICENCE.md
    manifest.json
```

**Rules**

- Nothing in the package is empty or placeholder. A file with nothing to say is omitted, not shipped blank.
- `manifest.json` records product, version, date, engine version, and per-size page/link/bookmark counts.
- The ZIP is named `{slug}-v{version}.zip` and contains one top-level folder, never loose files.
- Documentation is Markdown in the repo and PDF in the customer package where the platform renders poorly.

---

# 14. QUALITY CHECKLIST

Minimum release score: **95/100**. Below that, the product does not ship. `engines/QUALITY_ENGINE.md` holds the veto.

| # | Check | Pass condition |
|---|---|---|
| 1 | Margins | Consistent across all pages and all four sizes. Safe print area respected |
| 2 | Typography | ≤ 2 families, ≤ 3 weights, ≤ 4 sizes. No synthesised bold. No fallback substitution |
| 3 | Hyperlinks | Every internal link resolves to an existing anchor. Zero dead targets |
| 4 | Bookmarks | Outline count equals page count. One entry per page, correctly ordered |
| 5 | Spacing | 8-point system throughout. No ad-hoc offsets |
| 6 | Alignment | Grid-aligned. No overlapping or clipped elements |
| 7 | Page count | Identical across all four sizes and equal to the spec's expanded count |
| 8 | Export integrity | Vector PDF. Live selectable text. Fonts embedded as subsets. No rasterised type |
| 9 | Packaging | Structure per §13 complete. Manifest present and accurate |
| 10 | Naming | Every file matches §10 |

**Additional gates**

- Contrast passes at body size in every theme.
- Canva import verified manually — text editable, fonts resolved, layout unshifted.
- One page printed and physically checked before first release of a new page type.

A failure in any row returns the product to production. There is no partial pass.

---

# 15. EXPORT REQUIREMENTS

Every build produces, automatically:

| Output | Specification |
|---|---|
| PDF A4 | Vector, live text, embedded subsets, links, bookmarks, metadata |
| PDF A5 | As above |
| PDF US Letter | As above |
| PDF Half Letter | As above |
| Cover PNG | 300 DPI, rendered from page 1 of the A4 file |
| Preview JPG | 12 panels, 4 columns, rendered from the A4 file |
| ZIP package | Structure per §13 |
| Manifest | JSON, per §13 |

**Rules**

- Exports are generated, never hand-assembled.
- A partial export set is a failed build. There is no "PDFs now, previews later".
- Build output is gitignored. The spec is the committed artefact; the PDFs are reproducible from it.

---

# 16. ETSY DELIVERABLES

What the buyer downloads:

- Four printable, hyperlinked PDFs — A4, A5, US Letter, Half Letter
- Preview images
- Instructions
- Licence
- Read Me
- Manifest

What the listing requires, per `engines/AUTOMATION_ENGINE.md` Stage 16–17:

- SEO title, short title, long title
- Description with the hook in the first two lines
- Thirteen tags, all used
- Primary and secondary keywords
- FAQ
- Bundle and cross-sell suggestions
- Mockups — cover, flat lay, desk, tablet, lifestyle, thumbnail

No listing publishes with an incomplete SEO package.

---

# 17. VERSIONING

Semantic, applied to the product.

| Change | Increment | Example |
|---|---|---|
| Typo, spacing, colour correction | Patch | 1.0.0 → 1.0.1 |
| Pages added, layout improved, tracker extended | Minor | 1.0.1 → 1.1.0 |
| Page order changed, page removed, structure altered | Major | 1.1.0 → 2.0.0 |

**Rules**

- Version appears in `spec.json`, `manifest.json`, and the ZIP filename.
- Every release is recorded in `CHANGELOG.md`.
- Existing buyers receive minor and patch updates. A major version is a new listing, not a silent replacement — a buyer who bought a 20-page planner should not find its structure changed under them.
- The standard itself versions independently. A product records which standard version it was built to.

---

# 18. FUTURE COMPATIBILITY

Rules that keep this standard extensible without a rewrite.

| Rule | Reason |
|---|---|
| New page types extend §9. They never replace an existing definition | Shipped products must keep rendering |
| New renderer functions are additive. Existing signatures do not change | A spec built to v1.0 must build under v1.x |
| `schema` in every spec declares its version | The loader can migrate rather than fail |
| Themes never alter layout | A future theme cannot break an existing product |
| Page order is stable. Insertions go at the section boundary | Customer familiarity across the collection |
| Renderer gaps are declared, never silently unsupported | §9.1 exists so nobody discovers the gap mid-build |
| Standard changes require a real production reason | `PROJECT_RULES.md` §14 |

**Deprecation:** a page type is marked Deprecated for one minor version before removal. Products still using it build with a warning, not a failure.

---

# 19. STATUS

| Item | State |
|---|---|
| Standard | Complete, v1.0 |
| Buildable page types | 14 of 20 |
| Renderer work authorised | 6 new types — §9.1 |
| Spec-loader work required | Yes — §12.3 |
| Blocking prerequisites | `systems/BRAND_SYSTEM.md`, `COLOR_SYSTEM.md`, `TYPOGRAPHY_SYSTEM.md` |
| First product | `products/02-business-planner/` — not started |

No planner is generated from this document. It defines the blueprint every Business Planner follows.
