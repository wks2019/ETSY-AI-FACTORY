# TYPOGRAPHY_SYSTEM.md

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY
Authority: Rank 7 — `systems/` · `PROJECT_RULES.md` §3

---

# TABLE OF CONTENTS

1. [Purpose](#1-purpose) · 2. [Typography Philosophy](#2-typography-philosophy) · 3. [Design Principles](#3-design-principles)
4. [Font Selection Criteria](#4-font-selection-criteria) · 5. [Approved Font Families](#5-approved-font-families) · 6. [Font Fallback Strategy](#6-font-fallback-strategy)
7. [Token Reference](#7-token-reference) · 8. [Heading Scale](#8-heading-scale) · 9. [Body Text Scale](#9-body-text-scale)
10. [Caption Scale](#10-caption-scale) · 11. [Label Scale](#11-label-scale) · 12. [Navigation Typography](#12-navigation-typography)
13. [Table Typography](#13-table-typography) · 14. [Form Typography](#14-form-typography) · 15. [Hyperlink Typography](#15-hyperlink-typography)
16. [Number Formatting](#16-number-formatting) · 17. [Date Formatting](#17-date-formatting) · 18. [Line Height Standards](#18-line-height-standards)
19. [Letter Spacing Standards](#19-letter-spacing-standards) · 20. [Paragraph Spacing Rules](#20-paragraph-spacing-rules) · 21. [Alignment Rules](#21-alignment-rules)
22. [Text Hierarchy](#22-text-hierarchy) · 23. [Emphasis Rules](#23-emphasis-rules) · 24. [Accessibility Requirements](#24-accessibility-requirements)
25. [Print Optimisation](#25-print-optimisation) · 26. [Digital Optimisation](#26-digital-optimisation) · 27. [Unicode and Multilingual Support](#27-unicode-and-multilingual-support)
28. [Font Embedding Rules](#28-font-embedding-rules) · 29. [Licensing Requirements](#29-licensing-requirements) · 30. [Future Expansion Rules](#30-future-expansion-rules)
31. [Definitions](#31-definitions) · 32. [Cross References](#32-cross-references) · 33. [Change History](#33-change-history)

---

# 1. PURPOSE

The single approved source of typography for every AIDPF product.

No product, spec or template may introduce a face, weight, size or spacing value that does not originate here.

This document owns size, weight, spacing and family. It owns **no colour** — see `systems/COLOR_SYSTEM.md` §22.

---

# 2. TYPOGRAPHY PHILOSOPHY

In a planner, typography is not the content. The customer's handwriting is.

That inverts the usual priority. Type here has three jobs: name the page, label the fields, and then get out of the way. A planner whose typography is memorable is a planner with too little writing space.

The serif appears exactly once per page — the title — because that single moment carries the entire perceived value of the product. Everything else is a quiet sans.

---

# 3. DESIGN PRINCIPLES

| # | Principle |
|---|---|
| 1 | Two families. Three weights. Four sizes. The cap is not a guideline |
| 2 | The display face titles. It never labels, never runs as body |
| 3 | Legibility is set at Half Letter, the smallest size — not at A4 |
| 4 | Hierarchy comes from weight and space before it comes from size |
| 5 | No synthesised weights. Every weight is a real axis instance |
| 6 | Type never fills space. Space is the design |
| 7 | If a label needs explaining, rewrite the label — do not style it |

---

# 4. FONT SELECTION CRITERIA

A candidate face must satisfy every criterion. One failure disqualifies it.

| # | Criterion | Test |
|---|---|---|
| 1 | Licence permits commercial embedding and redistribution | OFL, Apache-2.0, or explicit commercial grant |
| 2 | Available in Canva | Verified in the Canva font list, not assumed |
| 3 | Embeds reliably in PDF as a subset | Test render, inspect the font table |
| 4 | Unicode coverage — Latin Extended minimum | Test render of the target character set |
| 5 | Real weight range, not synthesised | Variable axis or discrete weight files |
| 6 | Legible at 7pt | Physical print test at Half Letter |
| 7 | Consistent across platforms | Same metrics from the same file everywhere |
| 8 | Timeless, not trend-led | Would not read as dated in five years |
| 9 | Tabular figures available for tables | Inspect `tnum` feature support |

Criterion 2 is the one most often skipped and most expensive to discover late — a font absent from Canva breaks `PROJECT_RULES.md` §6 after the product is built.

---

# 5. APPROVED FONT FAMILIES

Two. No third family may be added without amending this document.

## 5.1 Display — Cormorant Garamond

| | |
|---|---|
| Role | Page titles. Cover title. Nothing else |
| Classification | Old-style serif, high contrast, light default weight |
| Licence | SIL Open Font License 1.1 |
| Canva | Available |
| Axis | Variable, weight 300–700 |
| Approved weights | 300 Light · 500 Medium |
| Prohibited | Body text, labels, tables, any size below 14pt, uppercase |

Cormorant is a display face with fine hairlines. Below roughly 14pt those hairlines break up in print. This is a hard floor, not a preference.

## 5.2 Body and UI — Inter

| | |
|---|---|
| Role | Everything that is not a page title |
| Classification | Neutral grotesque, designed for screen legibility |
| Licence | SIL Open Font License 1.1 |
| Canva | Available |
| Axis | Variable, optical size and weight 100–900 |
| Approved weights | 400 Regular · 500 Medium |
| Prohibited | Page titles, weights above 500, italics |

## 5.3 Weight budget

Three weights total across the product: **Cormorant 300**, **Cormorant 500**, **Inter 400**, **Inter 500** — four axis instances, but only three perceptual weights, since Cormorant 300 and Inter 400 read as the same tone at their respective sizes.

A fourth perceptual weight requires amending this document.

---

# 6. FONT FALLBACK STRATEGY

Fallback in a PDF is a **defect**, not a feature. A correctly built file never falls back, because the fonts are embedded.

Fallback matters in three places only:

| Context | Chain | Behaviour |
|---|---|---|
| Build environment missing the font file | Build **fails** | Never silently substitutes |
| HTML preview before PDF render | `'Cormorant Garamond', Georgia, serif` / `'Inter', -apple-system, 'Segoe UI', sans-serif` | Approximate only |
| Canva after import | Canva resolves the named family | Both faces exist in Canva. If either is unavailable, the import has failed |

**Rules**

- The build halts on a missing font. It does not proceed with a substitute — a substituted planner ships wrong metrics and broken pagination.
- Fallback stacks never appear in a delivered PDF's font table. Inspect the font table at build verification.
- If a PDF's font table shows a face outside §5, the build is rejected.

---

# 7. TOKEN REFERENCE

Products reference **tokens**. Sizes are stated in points at reference scale (A4 and US Letter). See §25.1 for the small-size multiplier.

| Token | Family | Weight | Size | Line height | Tracking | Use |
|---|---|---|---|---|---|---|
| `display` | Cormorant | 300 | 44pt | 1.05 | −0.01em | Cover title only |
| `headline` | Cormorant | 500 | 26pt | 1.10 | 0 | Page title |
| `title` | Cormorant | 500 | 18pt | 1.15 | 0 | Section title within a page |
| `subtitle` | Inter | 500 | 8pt | 1.30 | 0.14em | Page subtitle, uppercase |
| `section` | Inter | 500 | 9pt | 1.30 | 0.10em | Group heading, uppercase |
| `body-large` | Inter | 400 | 11.5pt | 1.50 | 0 | Prose on Read Me and Licence |
| `body` | Inter | 400 | 10.5pt | 1.45 | 0 | Default text |
| `body-small` | Inter | 400 | 9pt | 1.40 | 0 | Dense prose |
| `caption` | Inter | 400 | 7.5pt | 1.35 | 0 | Explanatory notes |
| `label` | Inter | 500 | 6.6pt | 1.25 | 0.12em | Panel and field labels, uppercase |
| `table` | Inter | 400 | 8.5pt | 1.35 | 0 | Table cell content |
| `table-head` | Inter | 500 | 6.8pt | 1.25 | 0.12em | Table headers, uppercase |
| `button` | Inter | 500 | 6.8pt | 1.20 | 0.10em | Tabs and chips |
| `footnote` | Inter | 400 | 6.5pt | 1.30 | 0 | Footer text |
| `metadata` | Inter | 400 | 6.5pt | 1.30 | 0.04em | Page numbers, version marks |

## 7.1 Size budget

The ≤ 4 sizes cap in `BRAND_SYSTEM.md` applies **per page**, not per system. Any single page uses at most four distinct sizes from this table.

A typical interior page uses four: `headline`, `subtitle`, `label`, `footnote`. Adding a fifth means the page is doing too much.

## 7.2 Usage example

```
Correct    panel label  = label
Wrong      panel label  = Inter 500 6.6pt uppercase
Wrong      panel label  = small caps grey text
```

---

# 8. HEADING SCALE

| Token | Size | Where |
|---|---|---|
| `display` | 44pt | Cover, once |
| `headline` | 26pt | Every page, once |
| `title` | 18pt | Only on pages with genuine internal sections |
| `section` | 9pt | Group headings inside a page |

**Rules**

- One `headline` per page. It is the bookmark label and the page's identity.
- `title` is rare. Most pages have no internal sections.
- Headings are never uppercase in the display face. Cormorant's proportions are drawn for mixed case.
- No heading is centred except on the cover and back cover.

---

# 9. BODY TEXT SCALE

| Token | Size | Where |
|---|---|---|
| `body-large` | 11.5pt | Read Me, Licence — pages actually read |
| `body` | 10.5pt | Default |
| `body-small` | 9pt | Dense prose, only where `body` will not fit |

**Rules**

- Reaching for `body-small` to fit content is a signal to cut content, not shrink type.
- Body text is never `text-muted` — `COLOR_SYSTEM.md` §22.
- Measure is capped at 75 characters. Full-width body text on A4 is prohibited — use columns.

---

# 10. CAPTION SCALE

| Token | Size | Where |
|---|---|---|
| `caption` | 7.5pt | Explanatory notes beneath a component |
| `footnote` | 6.5pt | Page footer |
| `metadata` | 6.5pt | Page numbers, version marks |

6.5pt is the absolute floor at reference scale, which becomes **4.3pt at Half Letter**. Nothing smaller is permitted anywhere in the system. See §25.2.

---

# 11. LABEL SCALE

| Token | Size | Tracking | Where |
|---|---|---|---|
| `label` | 6.6pt | 0.12em | Panel and field labels |
| `table-head` | 6.8pt | 0.12em | Column headers |
| `subtitle` | 8pt | 0.14em | Page subtitle |
| `section` | 9pt | 0.10em | Group heading |

**Rules**

- Labels are uppercase Inter with tracking. Uppercase without tracking is unreadable at these sizes.
- Labels are nouns. "Top Three Priorities", never "What matters most today?"
- A label never wraps to a second line. If it would, the label is too long.

---

# 12. NAVIGATION TYPOGRAPHY

| Element | Token | Case |
|---|---|---|
| Tab | `button` | Uppercase |
| Chip | `button` at 7.2pt | Title Case |
| Index row | `body-small` | Title Case |
| Index type column | `caption` | Lowercase |
| Footer link | `footnote` | Title Case |

**Rules**

- Tab labels are one word. Two-word tabs break the bar at Half Letter.
- Chips carry the destination's exact title. A chip reading "Jan" linking to a page titled "January" is a defect.
- Navigation type is never italic, never underlined, never coloured — `COLOR_SYSTEM.md` §19.

---

# 13. TABLE TYPOGRAPHY

| Element | Token |
|---|---|
| Header | `table-head`, uppercase |
| Cell content | `table` |
| Numeric cell | `table`, tabular figures, right-aligned |
| Totals row | `table`, weight 500 |
| Row label | `table`, left-aligned |

**Rules**

- **Tabular figures are mandatory in every table.** Proportional figures cause columns of numbers to misalign, which looks like a manufacturing defect.
- Numeric columns right-align. Text columns left-align. Nothing centres.
- Header rows never use the display face.
- A table cell never contains two type sizes.

---

# 14. FORM TYPOGRAPHY

"Form" here means the fields the customer writes into — the actual product.

| Element | Token | Rule |
|---|---|---|
| Field label | `label` | Above the field, never inside it |
| Writing line | — | 19pt minimum spacing at reference scale |
| Field hint | `caption` | Rare. Most fields need none |
| Placeholder text | — | **Prohibited.** Never pre-fill a field the customer writes in |

## 14.1 Writing space — binding constraint

| Size | Minimum line spacing |
|---|---|
| A4, US Letter | 19pt |
| A5, Half Letter | 13pt |

Adult handwriting needs roughly 6–7mm of vertical space. Below this, the customer writes smaller than is comfortable, and the product joins the pile of abandoned planners — `BRAND_SYSTEM.md` §4.2.

**Writing space is never reduced to fit more rows.** Remove rows instead.

---

# 15. HYPERLINK TYPOGRAPHY

Internal links receive **no typographic treatment at all**. No underline, no italic, no weight change.

Every navigational element in the product is a link. Styling them would mark the entire page.

| Link | Treatment |
|---|---|
| Tab, chip | Shape carries the affordance — a bordered pill |
| Index row | Table row structure carries it |
| Footer link | Position carries it |
| External link | `body`, underlined — the only underline permitted in the system |

Affordance is taught once on the Read Me page, not repeated visually on every element.

---

# 16. NUMBER FORMATTING

| Context | Format |
|---|---|
| Tables and trackers | Tabular figures, `tnum` enabled |
| Running prose | Proportional figures |
| Calendar day cells | Tabular, top-left aligned |
| Hour labels | `06:00` — 24-hour, zero-padded, tabular |
| Page numbers | Tabular |
| Currency | **No symbol.** The product sells internationally |
| Decimals | Two places where money is implied. Never mixed within a column |
| Thousands | No separator in handwriting fields. The customer chooses |
| Ranges | En dash, no spaces — `1–31` |

**No currency symbol** is a deliberate market decision, not an omission. A `$` on a finance page halves the addressable market, and a symbol chooser is a support burden.

---

# 17. DATE FORMATTING

Products are **undated**. Dates appear only as labels and as fields the customer completes.

| Context | Format | Reason |
|---|---|---|
| Month names | Full — `January` | Unambiguous in every market |
| Weekday headers | Three letters — `MON` | Fits at Half Letter |
| Week start | Monday default; Sunday for the US edition | Regional expectation |
| Date fields | Empty, unformatted | The customer writes it |
| Printed sample dates | **Prohibited** | `01/02` means two different days in US and UK |
| Quarter labels | `Q1`–`Q4` | Universal |
| Year references | None anywhere | Undated catalogue |

Numeric date formats never appear pre-printed. This is the most common localisation defect in planner products.

---

# 18. LINE HEIGHT STANDARDS

| Context | Multiple |
|---|---|
| Display, headline | 1.05–1.15 |
| Title | 1.15 |
| Body prose | 1.45–1.50 |
| Dense prose | 1.40 |
| Table cells | 1.35 |
| Labels, buttons | 1.20–1.30 |
| Writing lines | Fixed pt, not a multiple — §14.1 |

**Rules**

- Larger type takes tighter leading. Smaller type takes looser.
- Line height is a unitless multiple everywhere except writing lines, which are fixed physical spacing.
- Body leading is never below 1.4. Long-session reading depends on it.

---

# 19. LETTER SPACING STANDARDS

| Context | Tracking |
|---|---|
| Display, cover title | −0.01em |
| Headline, title | 0 |
| Body | 0 |
| Uppercase labels | 0.12em |
| Uppercase subtitle | 0.14em |
| Uppercase section | 0.10em |
| Tabs, chips | 0.10em |
| Metadata | 0.04em |

**Rules**

- All uppercase text is tracked. Untracked uppercase is unreadable at label sizes.
- Lowercase body text is never tracked.
- Negative tracking appears only at display sizes, and only slightly.

---

# 20. PARAGRAPH SPACING RULES

| Relationship | Space (8-point system) |
|---|---|
| Between paragraphs | 8pt |
| Heading to its content | 12pt |
| Content to next heading | 24pt |
| Between panels | 10pt |
| Page title to body | 16pt |
| Above the footer | 16pt |

**Rules**

- Space above a heading always exceeds space below it. Proximity binds the heading to what it introduces.
- Paragraphs are separated by space, never by first-line indent.
- No orphan or widow lines. A heading never sits alone at the foot of a column.
- All values are multiples of 8 — `BRAND_SYSTEM.md` §14.

---

# 21. ALIGNMENT RULES

| Content | Alignment |
|---|---|
| Page titles | Left |
| Body prose | Left, ragged right |
| Labels | Left |
| Table text | Left |
| Table numbers | Right |
| Cover title | Centre |
| Back cover | Centre |
| Footer | Justified between edges |

**Prohibited**

- **Justified text.** Word spacing becomes uneven, and rivers appear at the narrow measures used at A5 and Half Letter.
- Centred body text.
- Centred labels.
- Right-aligned prose.

Centring is reserved for the cover and back cover. Everywhere else it breaks the left reading edge the grid depends on.

---

# 22. TEXT HIERARCHY

Establish hierarchy in this order. Reach for a level only when the one above cannot do the job.

| Level | Means |
|---|---|
| 1 | Position — what comes first |
| 2 | Space — what stands apart |
| 3 | Weight — 500 against 400 |
| 4 | Case and tracking — uppercase tracked label |
| 5 | Size — a larger token |
| 6 | Family — the display face |
| 7 | Colour — `COLOR_SYSTEM.md` §16 |

A hierarchy that needs levels 5, 6 and 7 simultaneously is a layout problem, not a typography problem.

---

# 23. EMPHASIS RULES

| Method | Status |
|---|---|
| Weight 500 | **Approved** — the primary method |
| Uppercase with tracking | Approved for labels only |
| Size increase | Approved sparingly |
| Position | Approved |
| Italic | **Prohibited** |
| Bold above 500 | **Prohibited** |
| Underline | Prohibited except external links |
| Colour | Prohibited for emphasis |
| Highlight fill | Prohibited |
| Letter-spacing lowercase | Prohibited |
| ALL CAPS in prose | Prohibited |
| Exclamation marks | Prohibited — `BRAND_SYSTEM.md` §7.3 |

**Italics are prohibited system-wide.** Cormorant's italic is a distinctly different texture that breaks page tone, and Inter's italic is a slanted roman rather than a true italic. Emphasis uses weight.

---

# 24. ACCESSIBILITY REQUIREMENTS

| Requirement | Rule |
|---|---|
| Minimum size | 6.5pt at reference — 4.3pt at Half Letter, metadata only |
| Minimum body size | 10.5pt at reference — 6.9pt at Half Letter |
| Body leading | ≥ 1.4 |
| Measure | ≤ 75 characters |
| Body face | Neutral sans. No decorative face carries body text |
| Case | No sustained uppercase. Word-shape recognition is lost |
| Alignment | Left ragged. Justified prohibited — §21 |
| Live text | Never rasterised, never outlined. Text must remain selectable and machine-readable |
| Structure | One bookmark per page for outline navigation |
| Greyscale | All hierarchy survives with colour removed — this is why hierarchy is built on weight and space |

The greyscale requirement is the reason §22 ranks colour last. A hierarchy built on colour collapses in monochrome print; one built on position and weight does not.

---

# 25. PRINT OPTIMISATION

## 25.1 Size scaling

Sizes in §7 are reference values. Small formats apply a multiplier.

| Size | Multiplier | Reason |
|---|---|---|
| A4 | 1.00 | Reference |
| US Letter | 1.00 | Comparable area |
| A5 | 0.66 | Page area is 50% of A4; margins scale too |
| Half Letter | 0.66 | Comparable to A5 |

Margins scale with the same factor. A5 is not A4 photocopied down — the type scale and the margin scale move together, or the page count diverges between sizes.

**Verified:** at 0.66, all 42 pages of Product 1 render identically across all four sizes. At 0.72 they did not — A5 and Half Letter overflowed to 46 pages.

## 25.2 Resulting small-format sizes

| Token | Reference | At 0.66 |
|---|---|---|
| `headline` | 26pt | 17.2pt |
| `body` | 10.5pt | 6.9pt |
| `table` | 8.5pt | 5.6pt |
| `label` | 6.6pt | 4.4pt |
| `footnote` | 6.5pt | 4.3pt |

4.3pt is small. It is acceptable **only** because it is used for uppercase tracked metadata in Inter, which holds its counters at that size, and because it carries no essential information. Nothing below `label` may be used at small formats for content the customer must read.

## 25.3 Print rules

| Rule | Detail |
|---|---|
| Hairlines | ≥ 0.5pt. Thinner rules vanish on inkjet |
| Display weight | Cormorant 300 at `display` size only. At smaller sizes use 500 — hairlines break up |
| Ink | No reversed type blocks. White-on-dark consumes ink and bleeds on absorbent paper |
| Scale | Prints correctly at 100%. Never requires "fit to page" |
| Verification | A new page type is physically printed and read before first release |

---

# 26. DIGITAL OPTIMISATION

| Rule | Detail |
|---|---|
| Screen legibility | Inter is drawn for screen. It carries all UI and body text |
| Ground | Never pure white — `COLOR_SYSTEM.md` §3 |
| Tap targets | Tabs and chips sized for a finger, not a cursor |
| Zoom | Live text reflows on zoom in annotation apps. Rasterised text does not — another reason §28 is absolute |
| Search | Live text is searchable in GoodNotes and Notability. A significant unadvertised feature |
| File size | Subset embedding keeps files small. Product 1: 42 pages, 632 KB |
| Canva | Both faces exist in Canva. Text remains editable after import |

---

# 27. UNICODE AND MULTILINGUAL SUPPORT

## 27.1 Current coverage

| Script | Cormorant Garamond | Inter | Status |
|---|---|---|---|
| Latin basic | Yes | Yes | Supported |
| Latin Extended-A | Yes | Yes | Supported — Western and Central European |
| Latin Extended-B | Partial | Yes | Verify per product |
| Cyrillic | Yes | Yes | Supported |
| Greek | Yes | Yes | Supported |
| CJK | No | No | **Not supported** |
| Arabic, Hebrew | No | No | **Not supported** |
| Devanagari, Thai | No | No | **Not supported** |

## 27.2 Rules

- Localisation adapts copy, never structure or palette — `BRAND_SYSTEM.md` §20.
- A target language must be verified against the embedded subset **before** the product is built. A missing glyph renders as a blank box in the delivered PDF.
- Right-to-left scripts require layout changes, not font changes. They are out of scope for this system version.
- CJK requires a third family and would break the two-family rule. It is a system amendment, not a product decision.
- Smart quotes and true dashes throughout. Straight quotes and hyphens-as-dashes are defects.

---

# 28. FONT EMBEDDING RULES

| Rule | Detail |
|---|---|
| Embedding | Mandatory. Every face, every file |
| Method | Subset. Only the glyphs used |
| Format | TrueType or OpenType, embedded as Type0 with CID mapping |
| Outlining | **Prohibited.** Text is never converted to paths |
| Rasterisation | **Prohibited.** Text is never converted to image |
| Verification | Inspect the PDF font table at every build |
| Rejection | A font table containing any face outside §5 fails the build |
| Licence compliance | OFL permits embedding and redistribution. Verified for both faces |

**Verified in Product 1:** the font table contains exactly four subsets — `Cormorant-Garamond-Light`, `Cormorant-Garamond-Medium`, `Inter`, `Inter-Medium` — all Type0, all subset, with live extractable text.

Outlining text would satisfy "vector PDF" while destroying searchability, screen-reader access, and Canva editability. It is prohibited for all three reasons.

---

# 29. LICENSING REQUIREMENTS

| Requirement | Detail |
|---|---|
| Licence | SIL Open Font License 1.1 for both faces |
| Embedding | Permitted without restriction |
| Redistribution in a PDF | Permitted |
| Selling the document | Permitted. The OFL restricts selling the *font*, not documents using it |
| Attribution in product | Required in `LICENCE.md`, stating OFL and that it covers the fonts only |
| Renaming | Prohibited if modified and redistributed — the Reserved Font Name clause |
| Font file distribution | **Prohibited.** Never ship `.ttf` files in a customer package |

The last rule matters: embedding a font inside a PDF is permitted; shipping the font file alongside it is redistribution of the font itself and is not covered by the product's licence grant.

---

# 30. FUTURE EXPANSION RULES

| Rule | Reason |
|---|---|
| A third family requires amending §5 and re-auditing every product | The two-family rule is the brand's strongest consistency mechanism |
| New tokens extend §7. They never redefine an existing one | Shipped products must keep rendering |
| Sizes may be added; the per-page cap of four stands | The cap is what prevents visual noise |
| A new page format adds a row to §25.1 with a **verified** multiplier | 0.72 was assumed and failed. 0.66 was tested and passed |
| A new script requires a font audit before any product is planned | A missing glyph is discovered too late at build time |
| Changes require evidence from real production | `PROJECT_RULES.md` §14 |

## 30.1 Adding a size format

1. Add the page geometry.
2. Derive a candidate multiplier from page area.
3. **Render a full product and compare page counts against A4.** A mismatch means the multiplier is wrong.
4. Physically print and read the smallest token.
5. Record the verified multiplier in §25.1.

Step 3 is not optional. It is the step that caught the 0.72 error.

---

# 31. DEFINITIONS

| Term | Definition |
|---|---|
| **Token** | A semantic type style products reference |
| **Reference scale** | A4 and US Letter, multiplier 1.00 |
| **Multiplier** | Factor applied to all type and margins at small formats |
| **Tracking** | Letter spacing, in em |
| **Leading** | Line height, as a unitless multiple |
| **Measure** | Line length, in characters |
| **Tabular figures** | Fixed-width numerals that align in columns |
| **Subset embedding** | Embedding only the glyphs used |
| **Synthesised weight** | A faked bold produced by outline expansion. Prohibited |
| **Outlining** | Converting text to vector paths. Prohibited |
| **Perceptual weight** | How heavy type reads, independent of its numeric value |

---

# 32. CROSS REFERENCES

| Document | Relationship |
|---|---|
| `PROJECT_RULES.md` | Rank 1. Overrides this document |
| `FACTORY_PROTOCOL.md` | Rank 2. Conflict resolution |
| `engines/QUALITY_ENGINE.md` | Rank 3. Audits typography at release |
| `systems/BRAND_SYSTEM.md` | Sets voice, restraint, legibility constraints this document implements |
| `systems/COLOR_SYSTEM.md` | Owns text colour. This document owns size, weight, spacing |
| `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` | Consumes §7 and §25 |

**Non-duplication:** `BRAND_SYSTEM.md` states "≤ 2 families" and names no sizes. `COLOR_SYSTEM.md` states which token colours a label and names no size. This document names sizes and no colours. Three documents, one subject, no overlap.

---

# 33. CHANGE HISTORY

| Version | Date | Change | Reason |
|---|---|---|---|
| 1.0 | 2026-08-02 | Initial system. 15 tokens, 2 families, verified scaling | Foundation. Completes the Stage 1 systems set |

## 33.1 Verified at v1.0

| Finding | Evidence |
|---|---|
| 0.66 multiplier holds page parity across four sizes | Product 1 renders 42 pages at every size |
| 0.72 multiplier does not | A5 and Half Letter overflowed to 46 pages |
| Fonts embed as four Type0 subsets with live text | PDF font table inspected |
| Both faces available in Canva | Verified in the Canva font list |

## 33.2 Amendment rules

- Patch: clarification, corrected cross reference
- Minor: a new token or a verified new size format
- Major: a changed family, weight budget, or scale — requires re-audit of every shipped product

A new size multiplier is recorded only after the page-parity test in §30.1.

---

# FINAL DIRECTIVE

No product decides a type size. It selects a token.

The customer's handwriting is the content. Typography names the page, labels the fields, and stops.
