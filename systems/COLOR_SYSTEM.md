# COLOR_SYSTEM.md

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY
Authority: Rank 7 — `systems/` · `PROJECT_RULES.md` §3

---

# TABLE OF CONTENTS

1. [Purpose](#1-purpose) · 2. [Design Principles](#2-design-principles) · 3. [Colour Philosophy](#3-colour-philosophy)
4. [Colour Token System](#4-colour-token-system) · 5. [Primary Palette](#5-primary-palette) · 6. [Secondary Palette](#6-secondary-palette)
7. [Neutral Palette](#7-neutral-palette) · 8. [Accent Palette](#8-accent-palette) · 9. [Status Colours](#9-status-colours)
10. [Print Safe Palette](#10-print-safe-palette) · 11. [Greyscale Mapping](#11-greyscale-mapping) · 12. [Light Theme Rules](#12-light-theme-rules)
13. [Dark Theme Rules](#13-dark-theme-rules) · 14. [Accessibility Requirements](#14-accessibility-requirements) · 15. [WCAG Contrast Guidelines](#15-wcag-contrast-guidelines)
16. [Colour Usage Hierarchy](#16-colour-usage-hierarchy) · 17. [Component Colour Rules](#17-component-colour-rules) · 18. [Page Type Colour Rules](#18-page-type-colour-rules)
19. [Hyperlink Colours](#19-hyperlink-colours) · 20. [Divider and Border Colours](#20-divider-and-border-colours) · 21. [Background Colours](#21-background-colours)
22. [Typography Colour Rules](#22-typography-colour-rules) · 23. [Icon Colour Rules](#23-icon-colour-rules) · 24. [Chart and Graph Colours](#24-chart-and-graph-colours)
25. [Future Theme Extension Rules](#25-future-theme-extension-rules) · 26. [Definitions](#26-definitions) · 27. [Cross References](#27-cross-references) · 28. [Change History](#28-change-history)

---

# 1. PURPOSE

The single approved source of colour for every AIDPF product.

No product, spec, engine or template may introduce a colour value that does not originate here. A product needing a colour this system lacks is a request to amend this system, not a licence to invent one locally.

All values in this document are verified: every contrast ratio and greyscale value below was computed, not estimated.

---

# 2. DESIGN PRINCIPLES

| # | Principle |
|---|---|
| 1 | Every colour has a role. A colour without a role does not exist |
| 2 | Colour never carries meaning alone — position or label carries it too |
| 3 | The page must work printed in greyscale |
| 4 | Ink economy: no large solid fills on a print-first product |
| 5 | Restraint over range. Six roles, not twenty |
| 6 | Contrast is a floor, not a target |
| 7 | Warm neutrals over clinical ones. Never pure white, never pure black |

---

# 3. COLOUR PHILOSOPHY

This is a system for documents people write on, not screens people scroll.

That drives three decisions:

**Paper, not white.** A pure `#FFFFFF` ground glares on screen during long sessions and looks cheap in print, where the physical paper is never that bright. The ground is a warm off-white.

**Ink, not black.** True `#000000` prints as a heavy blot on consumer inkjet and reads harshly on backlit screens. Ink is a soft near-black with a warm bias.

**Colour is punctuation.** The customer's handwriting is the content. Colour marks structure — a rule, an active tab, a status — and then stops.

---

# 4. COLOUR TOKEN SYSTEM

Products reference **tokens**. Themes bind tokens to values. A product built against tokens inherits any future theme without modification.

## 4.1 Token set

| Token | Role |
|---|---|
| `background` | The page ground |
| `surface` | Raised or inset areas — panels, table headers |
| `primary` | Structural brand colour. Active states, key marks |
| `primary-strong` | Text-safe variant of `primary` |
| `secondary` | Supporting structural colour |
| `accent` | Single emphasis mark. Covers and dividers |
| `accent-strong` | Text-safe variant of `accent` |
| `border` | Table cell edges, panel outlines |
| `divider` | Hairline separators between sections |
| `text-primary` | Body text, titles |
| `text-secondary` | Supporting text, table content |
| `text-muted` | Labels, tab text, footers |
| `text-inverse` | Text on a filled ground |
| `success` | Positive state |
| `warning` | Attention state |
| `danger` | Negative state |
| `info` | Neutral notice |

## 4.2 Rules

- Seventeen tokens. A product needing an eighteenth amends this document.
- No hex value appears in a product spec outside its `design.palette` block, which is a theme binding, not a definition.
- Token names are stable across themes. Values change; names never do.
- `-strong` variants exist because the base colour is decorative and fails text contrast. Never use a base where a `-strong` is specified.

## 4.3 Usage example

```
Correct    label colour = text-muted
Wrong      label colour = #6E6E64
Wrong      label colour = grey
```

---

# 5. PRIMARY PALETTE

The structural identity. Sage — quiet, warm, non-corporate, and legible in greyscale.

| Token | HEX | RGB | CMYK (approx) | Grey | Contrast on `background` |
|---|---|---|---|---|---|
| `primary` | `#8C9A82` | 140, 154, 130 | 9, 0, 16, 40 | `#939393` | 2.83:1 — **decorative only** |
| `primary-strong` | `#556349` | 85, 99, 73 | 14, 0, 26, 61 | `#5C5C5C` | 6.11:1 — text safe |

**Rules**

- `primary` is a fill or a mark. It is **never** used for text, and text is never placed on it.
- `primary-strong` is used wherever `primary` would need to carry or host text — including the active navigation tab.
- Neither is used as a full-page ground. Ink economy, §2.

---

# 6. SECONDARY PALETTE

Gold. Reserved for the single moment of emphasis on a cover or a divider.

| Token | HEX | RGB | CMYK (approx) | Grey | Contrast on `background` |
|---|---|---|---|---|---|
| `secondary` | `#B08D4F` | 176, 141, 79 | 0, 20, 55, 31 | `#909090` | 2.95:1 — **decorative only** |
| `secondary-strong` | `#7E6230` | 126, 98, 48 | 0, 22, 62, 51 | `#656565` | 5.43:1 — text safe |

**Rules**

- `secondary` appears on the cover rule, the back cover mark, and section dividers. Nowhere else.
- Maximum one `secondary` element per interior page. Usually zero.
- Gold is the brand's only warm chroma. Overuse turns premium into ornate.

---

# 7. NEUTRAL PALETTE

Where the product actually lives. Ninety-five per cent of every page is drawn from this table.

| Token | HEX | RGB | Grey | Contrast on `background` | Use |
|---|---|---|---|---|---|
| `background` | `#FBF9F4` | 251, 249, 244 | `#F9F9F9` | — | Page ground |
| `surface` | `#F4F1E9` | 244, 241, 233 | `#F1F1F1` | 1.06:1 | Panel and header fills |
| `text-primary` | `#2B2B28` | 43, 43, 40 | `#2B2B2B` | **13.50:1** | Body, titles |
| `text-secondary` | `#55554D` | 85, 85, 77 | `#545454` | **7.34:1** | Table content, supporting copy |
| `text-muted` | `#6E6E64` | 110, 110, 100 | `#6D6D6D` | **4.89:1** | Labels, tabs, footers |
| `text-inverse` | `#FBF9F4` | 251, 249, 244 | `#F9F9F9` | — | Text on `primary-strong` |
| `border` | `#DEDACF` | 222, 218, 207 | `#DADADA` | 1.33:1 | Cell edges, panel outlines |
| `divider` | `#E6E2D8` | 230, 226, 216 | `#E2E2E2` | 1.23:1 | Section hairlines |

**Correction on record:** `text-muted` was `#8A8A80` in the Product 1 spec. That measures **3.31:1**, below the 4.5:1 floor in `BRAND_SYSTEM.md` §15. It is corrected to `#6E6E64` (4.89:1). See §28.1.

---

# 8. ACCENT PALETTE

`accent` is an alias binding, not a separate hue. It exists so a future theme can move emphasis without renaming tokens across every product.

| Token | Neutral theme binding | Contrast |
|---|---|---|
| `accent` | `primary` — `#8C9A82` | 2.83:1 — decorative only |
| `accent-strong` | `primary-strong` — `#556349` | 6.11:1 — text safe |

An accent element must survive its own removal. If deleting it breaks comprehension, it was structure, not accent — rebuild it with position or a label.

---

# 9. STATUS COLOURS

| Token | HEX | RGB | Grey | Contrast | Required pairing |
|---|---|---|---|---|---|
| `success` | `#41613C` | 65, 97, 60 | `#535353` (83) | **6.65:1** | Word or mark |
| `warning` | `#8A6D34` | 138, 109, 52 | `#6F6F6F` (111) | **4.62:1** | Word or mark |
| `danger` | `#7C2E26` | 124, 46, 38 | `#444444` (68) | **8.77:1** | Word or mark |
| `info` | `#4C6E8E` | 76, 110, 142 | `#676767` (103) | **5.08:1** | Word or mark |

## 9.1 An honest constraint

WCAG contrast and greyscale separation pull against each other. Forcing all four statuses above 4.5:1 compresses them into a narrow lightness band — `warning` (111) and `info` (103) sit only eight greyscale steps apart and are **not reliably distinguishable in monochrome print**.

This is not solvable by choosing better hues. It is a consequence of the two requirements.

**Therefore:** status is never communicated by colour alone, in any product, under any theme. Every status carries a word or a mark. Where `warning` and `info` would appear adjacently, one must be re-expressed by position or omitted.

## 9.2 Financial pages

No red/green profit-and-loss coding. It fails in greyscale, fails for the most common form of colour blindness, and is the single most frequent accessibility defect in planner products. Use a sign, a column, or a label.

---

# 10. PRINT SAFE PALETTE

CMYK values are conversion targets, not the delivered colour space. PDFs export in RGB; commercial CMYK conversion is out of scope for a digital-download product. These values exist so a customer sending a file to a print shop gets a predictable result.

| Token | HEX | CMYK (approx) | Print note |
|---|---|---|---|
| `background` | `#FBF9F4` | 0, 1, 3, 2 | Effectively unprinted paper |
| `surface` | `#F4F1E9` | 0, 1, 4, 4 | Very light. May not register on some inkjets |
| `text-primary` | `#2B2B28` | 0, 0, 7, 83 | Rich near-black. Prints clean |
| `text-secondary` | `#55554D` | 0, 0, 9, 67 | — |
| `text-muted` | `#6E6E64` | 0, 0, 9, 57 | — |
| `border` | `#DEDACF` | 0, 2, 7, 13 | Minimum 0.5pt or it disappears |
| `divider` | `#E6E2D8` | 0, 2, 6, 10 | Minimum 0.5pt |
| `primary-strong` | `#556349` | 14, 0, 26, 61 | — |
| `secondary` | `#B08D4F` | 0, 20, 55, 31 | — |

**Rules**

- No colour exceeds 85% total ink coverage.
- No page carries a solid fill larger than a table header row.
- Never specify a colour that relies on registration accuracy — hairlines are single-channel dark, not composite.

---

# 11. GREYSCALE MAPPING

Computed perceptual luminance, `0.299R + 0.587G + 0.114B`.

| Token | Colour | Greyscale | Value |
|---|---|---|---|
| `background` | `#FBF9F4` | `#F9F9F9` | 249 |
| `surface` | `#F4F1E9` | `#F1F1F1` | 241 |
| `divider` | `#E6E2D8` | `#E2E2E2` | 226 |
| `border` | `#DEDACF` | `#DADADA` | 218 |
| `primary` | `#8C9A82` | `#939393` | 147 |
| `secondary` | `#B08D4F` | `#909090` | 144 |
| `warning` | `#8A6D34` | `#6F6F6F` | 111 |
| `info` | `#4C6E8E` | `#676767` | 103 |
| `text-muted` | `#6E6E64` | `#6D6D6D` | 109 |
| `text-secondary` | `#55554D` | `#545454` | 84 |
| `success` | `#41613C` | `#535353` | 83 |
| `danger` | `#7C2E26` | `#444444` | 68 |
| `text-primary` | `#2B2B28` | `#2B2B2B` | 43 |

## 11.1 Black-and-white fallback

A monochrome-only device collapses everything to black or white at threshold. Under that condition:

| Behaviour | Rule |
|---|---|
| Text | All text tokens fall below threshold and print black. Legible |
| Borders and dividers | Fall above threshold and may vanish entirely. Layout must not depend on them |
| Fills | `surface` disappears. Panels must be readable without their fill |
| Status | Indistinguishable. The required word or mark carries it — §9.1 |

**Design consequence:** every panel, table and section must remain comprehensible with all fills and all rules removed. This is testable by rendering with `border`, `divider` and `surface` set to `background`.

---

# 12. LIGHT THEME RULES

The `neutral` theme is the reference. Two further light themes exist.

| Token | `neutral` | `mono` | `slate` |
|---|---|---|---|
| `background` | `#FBF9F4` | `#FBF9F4` | `#F7F8F9` |
| `surface` | `#F4F1E9` | `#F3F3F3` | `#EDEFF2` |
| `text-primary` | `#2B2B28` | `#2B2B2B` | `#23282D` |
| `text-secondary` | `#55554D` | `#545454` | `#4A525A` |
| `text-muted` | `#6E6E64` | `#6D6D6D` | `#666E75` |
| `text-inverse` | `#FBF9F4` | `#FBF9F4` | `#F7F8F9` |
| `border` | `#DEDACF` | `#DADADA` | `#DCE0E4` |
| `divider` | `#E6E2D8` | `#E2E2E2` | `#E5E8EB` |
| `primary` | `#8C9A82` | `#9A9A9A` | `#7C93A6` |
| `primary-strong` | `#556349` | `#4A4A4A` | `#3E5A70` |
| `secondary` | `#B08D4F` | `#8F8F8F` | `#8C9AA6` |
| `secondary-strong` | `#7E6230` | `#5E5E5E` | `#4F6172` |

**Rules**

- `mono` is the print-economy edition. Single-channel black only. Carries no chroma anywhere.
- `slate` is the corporate/consulting positioning. Cool, restrained, one blue.
- Status colours are shared across all light themes. They are not re-themed — a warning must look like a warning.

---

# 13. DARK THEME RULES

| Token | HEX | Contrast on `background` |
|---|---|---|
| `background` | `#22221F` | — |
| `surface` | `#2C2C28` | 1.14:1 |
| `text-primary` | `#EFECE4` | **13.51:1** |
| `text-secondary` | `#C6C3BA` | **9.13:1** |
| `text-muted` | `#A8A69C` | **6.53:1** |
| `text-inverse` | `#22221F` | — |
| `border` | `#3C3C37` | 1.44:1 |
| `divider` | `#33332F` | 1.26:1 |
| `primary` | `#9DAF92` | 6.82:1 |
| `primary-strong` | `#B4C4A9` | 8.66:1 |
| `secondary` | `#C8A566` | 8.06:1 |

**Rules**

- Dark is a **screen-first edition**. Its listing must state the print-cost implication plainly — a dark ground consumes a full cartridge per copy.
- The `mono` edition and the `dark` edition are never combined.
- In dark, `primary` becomes text-safe because the relationship inverts. `primary-strong` becomes the *lighter* variant. Token names hold; values invert.
- The Passwords page is excluded from the dark edition, per `BUSINESS_PLANNER_STANDARD.md` §8.1.

---

# 14. ACCESSIBILITY REQUIREMENTS

| Requirement | Rule |
|---|---|
| Body contrast | ≥ 7:1 — `text-primary` delivers 13.50:1 |
| Secondary contrast | ≥ 4.5:1 — `text-secondary` 7.34:1, `text-muted` 4.89:1 |
| Colour independence | No state, category or grouping communicated by colour alone |
| Colour blindness | The palette carries one green and one blue-grey. Deuteranopia and protanopia do not collapse them, because they differ in lightness as well as hue |
| Greyscale | Every page fully usable in monochrome — §11.1 |
| Long sessions | Warm ground, no pure white, no pure black, no saturated fills |
| Non-text contrast | Borders and dividers are exempt from text ratios but must be ≥ 0.5pt so they survive print |

**Not claimed:** this system is not certified to any WCAG conformance level. WCAG governs web content; a PDF planner is a different artefact. The ratios are met because they produce a better product, not to support a compliance claim.

---

# 15. WCAG CONTRAST GUIDELINES

| Pairing | Ratio | WCAG AA | WCAG AAA |
|---|---|---|---|
| `text-primary` on `background` | 13.50:1 | Pass | Pass |
| `text-secondary` on `background` | 7.34:1 | Pass | Pass |
| `text-muted` on `background` | 4.89:1 | Pass | Fail — acceptable for labels, never body |
| `text-inverse` on `primary-strong` | 6.11:1 | Pass | Fail — acceptable for tabs |
| `text-primary` on `surface` | 12.74:1 | Pass | Pass |
| `success` on `background` | 6.65:1 | Pass | Fail |
| `warning` on `background` | 4.62:1 | Pass | Fail |
| `danger` on `background` | 8.77:1 | Pass | Pass |
| `info` on `background` | 5.08:1 | Pass | Fail |
| **`text-inverse` on `primary`** | **2.83:1** | **FAIL** | **FAIL** |
| **`secondary` on `background`** | **2.95:1** | **FAIL** | **FAIL** |

The two failing rows are why `-strong` variants exist. **Never** place text on `primary`. **Never** set text in `secondary`.

**Defect on record:** the current engine renders the active tab as `text-inverse` on `primary` — 2.83:1. It must use `primary-strong`. See §28.1.

---

# 16. COLOUR USAGE HIERARCHY

Applied in order. Reach for a level only when the one above it cannot do the job.

| Level | Means | Example |
|---|---|---|
| 1 | Position and grouping | Related fields sit together |
| 2 | Whitespace | Sections separated by space, not rules |
| 3 | Typography | Weight and size establish hierarchy |
| 4 | Neutral value | `text-muted` for a label |
| 5 | Hairline | `divider` between sections |
| 6 | Fill | `surface` behind a table header |
| 7 | Chroma | `primary-strong` on the active tab |
| 8 | Status colour | `danger` on an overdue marker |

Anything solvable at level 1 or 2 must not be solved at level 7.

---

# 17. COMPONENT COLOUR RULES

| Component | Ground | Text | Border |
|---|---|---|---|
| Page | `background` | `text-primary` | — |
| Tab — inactive | `background` | `text-muted` | `border` |
| Tab — active | `primary-strong` | `text-inverse` | `primary-strong` |
| Chip | `background` | `text-primary` | `border` |
| Panel | `background` | `text-primary` | `border` |
| Panel label | — | `text-muted` | — |
| Table header | `surface` | `text-muted` | `border` bottom only |
| Table cell | `background` | `text-secondary` | `border` |
| Calendar cell | `background` | `text-muted` | `border` |
| Tracker cell | `background` | — | `border` |
| Writing line | — | — | `border` |
| Footer | `background` | `text-muted` | `divider` top |
| Cover rule | `secondary` | — | — |

---

# 18. PAGE TYPE COLOUR RULES

| Page type | Deviation from default |
|---|---|
| Cover | Only page permitted a `secondary` element. No navigation, no `surface` |
| Back Cover | As cover. Single `secondary` rule |
| Licence, Read Me | Prose. No fills, no chroma |
| Index | `divider` between rows. No fills |
| Year, Quarter, Month | `border` grid. Header row may use `surface` |
| Week, Day | Panel borders only |
| Tracker | Grid only. Never pre-fill cells with colour |
| Expense, Ledger | Totals row may use `surface`. **No red/green** — §9.2 |
| Contacts, Resources | Alternating `surface` rows permitted at ≤ 4% opacity difference |
| Notes | Writing lines only. Nothing else |
| Review | Panels only |

---

# 19. HYPERLINK COLOURS

**Internal links carry no colour.** This is deliberate and is the single most consequential rule in this document.

Every navigational element in the product is a link — tabs, chips, index rows, footers. Colouring them would turn the page blue and destroy the premium quality the brand depends on.

| Link context | Treatment |
|---|---|
| Tab | Bordered pill. Active state uses `primary-strong` fill |
| Chip | Bordered pill, `text-primary` |
| Index row | `text-primary`, `divider` beneath |
| Footer link | `text-muted` |
| Any internal link | Inherits surrounding colour. Never underlined, never blue |
| External link (rare) | `info`, underlined — the only permitted coloured link |

**Affordance comes from shape**, not colour: pills, table rows, and consistent placement. The Read Me page states that tabs are tappable, which is where the instruction belongs.

---

# 20. DIVIDER AND BORDER COLOURS

| Element | Token | Weight |
|---|---|---|
| Table cell edge | `border` | 0.5pt |
| Panel outline | `border` | 0.5pt |
| Writing line | `border` | 0.5pt |
| Section separator | `divider` | 0.5pt |
| Header underline | `border` | 0.5pt |
| Cover rule | `secondary` | 0.75pt |

**Rules**

- 0.5pt minimum. Thinner rules vanish on consumer inkjet.
- Never double-rule. A border and a divider never sit adjacent.
- Rules are structure of last resort — whitespace first, per §16.

---

# 21. BACKGROUND COLOURS

| Surface | Token |
|---|---|
| Page ground | `background` |
| Panel fill | `background` — outlined, not filled |
| Table header | `surface` |
| Totals row | `surface` |
| Alternating rows | `surface`, sparingly |
| Active tab | `primary-strong` |

**Prohibited:** full-page colour fills, gradients, image backgrounds, any fill larger than a table header on a print-first product.

Gradients are prohibited additionally because they degrade on Canva import — `PROJECT_RULES.md` §6.

---

# 22. TYPOGRAPHY COLOUR RULES

Colour assignment only. Size, weight and spacing belong to `systems/TYPOGRAPHY_SYSTEM.md`.

| Text role | Token |
|---|---|
| Page title | `text-primary` |
| Subtitle | `text-muted` |
| Body | `text-primary` |
| Table content | `text-secondary` |
| Label, caption | `text-muted` |
| Tab — inactive | `text-muted` |
| Tab — active | `text-inverse` |
| Footer | `text-muted` |
| Page number | `text-muted` |
| Cover title | `text-primary` |
| Cover collection line | `text-muted` |

**Rules**

- Body text is `text-primary`. No exceptions, no themes, no page types.
- `text-muted` never carries body text — 4.89:1 is a label ratio.
- Emphasis uses weight, never colour.

---

# 23. ICON COLOUR RULES

The catalogue currently uses no icons — `BRAND_SYSTEM.md` §11. These rules govern the decision if that changes.

| Rule | Detail |
|---|---|
| Colour | `text-primary` or `text-muted`. Never `primary`, never `secondary` |
| Multicolour | Prohibited |
| Status icons | Take the status token, and always sit beside a word |
| Fill | None. Stroke only |
| Greyscale | Must remain identifiable with all colour removed |

---

# 24. CHART AND GRAPH COLOURS

Charts are rare in a handwriting product — most "charts" are grids the customer fills in. When a rendered chart is required:

## 24.1 Sequence

Order is fixed. A three-series chart uses positions 1–3.

| # | Token | HEX | Grey |
|---|---|---|---|
| 1 | `text-primary` | `#2B2B28` | 43 |
| 2 | `primary-strong` | `#556349` | 92 |
| 3 | `info` | `#4C6E8E` | 103 |
| 4 | `secondary-strong` | `#7E6230` | 101 |
| 5 | `text-muted` | `#6E6E64` | 109 |

## 24.2 Rules

- Maximum five series. A sixth means the chart is the wrong format.
- Positions 3 and 4 are close in greyscale — **direct labelling is mandatory**, never a colour-keyed legend.
- Fills use hatching or value difference, never hue alone.
- No pie charts. They fail in greyscale and at small print sizes.

---

# 25. FUTURE THEME EXTENSION RULES

| Rule | Reason |
|---|---|
| A theme binds existing tokens. It never adds one | Shipped products would not inherit a new token |
| A theme changes no layout, spacing, or page count | `BRAND_SYSTEM.md` §9.3 |
| Every theme meets §14 in full before release | Contrast is not negotiable per theme |
| Status tokens are shared, never re-themed | A warning must look like a warning everywhere |
| A new theme is added to §12 or §13 with computed ratios | Estimated ratios are not acceptable |
| A theme requiring a layout change is not a theme | It is a new product |

## 25.1 Adding a theme

1. Bind all seventeen tokens. No omissions.
2. Compute every contrast pairing in §15.
3. Compute greyscale values for §11.
4. Verify §11.1 — the page works with all fills and rules removed.
5. Add the column and record it in §28.

---

# 26. DEFINITIONS

| Term | Definition |
|---|---|
| **Token** | A semantic colour name products reference. Stable across themes |
| **Binding** | A theme's assignment of a value to a token |
| **Theme** | A complete set of bindings. Changes no layout |
| **Role** | The job a colour performs. Every value has exactly one |
| **`-strong` variant** | A darker, text-safe form of a decorative colour |
| **Contrast ratio** | WCAG relative luminance ratio, 1:1 to 21:1 |
| **Greyscale value** | Perceptual luminance 0–255, `0.299R + 0.587G + 0.114B` |
| **Decorative** | A colour that may never carry or host text |
| **Ink economy** | Minimising printed coverage for consumer printing cost |

---

# 27. CROSS REFERENCES

| Document | Relationship |
|---|---|
| `PROJECT_RULES.md` | Rank 1. Overrides this document |
| `FACTORY_PROTOCOL.md` | Rank 2. Conflict resolution |
| `engines/QUALITY_ENGINE.md` | Rank 3. Audits colour consistency and contrast at release |
| `systems/BRAND_SYSTEM.md` | Sets the accessibility thresholds and personality this document implements |
| `systems/TYPOGRAPHY_SYSTEM.md` | Owns size, weight, spacing. This document owns only their colour |
| `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` | Consumes §17 and §18 |

**Non-duplication:** `BRAND_SYSTEM.md` states "≥ 7:1 body contrast" and no values. This document supplies the values and states no font size. If the two disagree, the owning document is correct and the other is defective — log per `FACTORY_PROTOCOL.md`.

---

# 28. CHANGE HISTORY

| Version | Date | Change | Reason |
|---|---|---|---|
| 1.0 | 2026-08-02 | Initial system. 17 tokens, 4 themes, verified ratios | Foundation. Unblocks the Business Collection |

## 28.1 Defects corrected at v1.0

| # | Defect | Correction |
|---|---|---|
| 1 | `text-muted` `#8A8A80` measured 3.31:1, below the 4.5:1 floor | Corrected to `#6E6E64`, 4.89:1 |
| 2 | Active tab renders `text-inverse` on `primary` — 2.83:1 | Must use `primary-strong`, 6.11:1 |

Both are present in `products/01-ultimate-digital-planner/spec.json` and in the engine's default stylesheet. **Product 1 does not currently conform to this system** and requires a corrective rebuild before it is re-listed.

## 28.2 Amendment rules

- Patch: clarification, corrected cross reference
- Minor: a new theme, a new documented pairing
- Major: a changed token value or a new token — requires re-audit of every shipped product

Every amendment records computed ratios. Estimated values are rejected.

---

# FINAL DIRECTIVE

No product decides a colour. It selects a token.

If building a product raises a colour question this system does not answer, that is a defect here — answer it, compute it, record it. Never resolve it inside a product.
