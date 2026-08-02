# HANDOVER

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY

State of the factory at the end of the build session. Read this first in a
new session, then `FACTORY_PROTOCOL.md`.

---

# 1. WHERE THINGS STAND

| Layer | State |
|---|---|
| GitHub write access | Working. Claude Github MCP Connector installed and scoped |
| Governance | Complete — protocol, rules, 5 engines, skill registry |
| Systems | Complete — brand, colour, typography |
| Engine | v2.1, stable across 6 builds, zero modifications needed |
| Schema | v1.1, unchanged since the engine upgrade |
| Products built | **6** — 466 pages total |
| Products listed | **0** |

---

# 2. PRODUCTS BUILT

| # | Product | Directory | Pages | Links | Theme |
|---|---|---|---|---|---|
| — | Ultimate Digital Planner | `products/01-ultimate-digital-planner/` | 42 | 1,598 | neutral |
| 001 | Business Productivity Planner | `products/02-business-productivity-planner/` | 58 | 1,880 | neutral |
| 002 | CEO Planner | `products/03-ceo-planner/` | 78 | 2,370 | slate |
| 003 | Project Planner | `products/04-project-planner/` | 70 | 1,428 | neutral |
| 004 | Meeting Planner | `products/05-meeting-planner/` | 77 | 2,132 | neutral |
| 005 | Goal Planner | `products/06-goal-planner/` | 71 | 2,086 | neutral |
| 006 | Weekly Productivity Planner | `products/07-weekly-productivity-planner/` | 112 | 4,138 | neutral |

Every one: four sizes, page/link/bookmark parity verified, all gates passed.

**Numbering offset:** bundle number 001 is directory `02`, because
`products/01-ultimate-digital-planner/` belongs to a different collection.
Deliberate — do not "fix" it.

---

# 3. WHAT IS OUTSTANDING

Identical across all six products. Nothing can be listed until these clear.

| # | Task | Why it blocks |
|---|---|---|
| 1 | **Canva import verification** | Manual. Unverified across all six. If import degrades, six products need rework. Highest-risk item |
| 2 | Physical print test | New page types never printed |
| 3 | SEO packages | 0 of 6 written. `_SEO/` is empty |
| 4 | Mockups | 0 of 6. `preview_manifest.json` for product 006 specifies the five required contexts |
| 5 | **Revoke exposed PAT** | A live token was pasted into chat in an earlier session. Revoke at `github.com/settings/tokens` if not already done |

---

# 4. HOW TO BUILD A PRODUCT

```bash
python _ENGINE/planner_engine.py products/NN-slug/spec.json
python _ENGINE/planner_engine.py products/NN-slug/spec.json --validate-only
python _ENGINE/planner_engine.py products/NN-slug/spec.json --theme dark --sizes a4
```

Requires `weasyprint pypdf pillow jsonschema` and `poppler-utils`. Fonts
download on first run into `_ENGINE/fonts/` (gitignored).

**A new product is a `spec.json`.** No code. Then `README.md`, `LICENSE.md`,
`manifest.json`, and optionally `metadata.json` and `preview_manifest.json`.

## Available layouts — 15, all built

`cover` `prose` `index` `year` `month` `quarter` `week` `day` `agenda`
`ledger` `record` `timeline` `tracker` `panels` `notes`

All 14 remaining collection products map onto these. **No new renderer is
needed to finish the collection.**

---

# 5. HARD-WON LESSONS

These cost real debugging time. Do not rediscover them.

| Lesson | Detail |
|---|---|
| **Page parity is not enough** | Content that overflows at a smaller size is *clipped*, not pushed to a new page. Page counts match while links go missing. The link-parity gate is the only detector — it caught this on three separate builds |
| **US Letter is shorter than A4** | 279mm vs 297mm. Pages that fit A4 can overflow US Letter. Prose pages and dense panel pages are the usual casualties |
| **Panel labels cap at 40 characters** | Schema rejects longer. Shorten the label, never raise the cap |
| **Index overflows past ~40 entries** | Split into two or three index pages by theme. Spec-level fix, no engine change |
| **Scale multiplier is 0.66, verified** | 0.72 was assumed and produced 46 pages at A5 against 42 at A4 |
| **Spacing must scale with the page** | Fixed px spacing does not shrink at A5 and silently clips content |
| **Subtitles need `bookmark-level: none`** | WeasyPrint bookmarks every heading; without this the outline doubles |
| **No hex in a spec** | The engine rejects any literal colour anywhere in a spec. Use theme tokens |

---

# 6. PRODUCT CONVENTIONS

Applied consistently across all six. Keep them.

- **No passwords page.** `BUSINESS_PLANNER_STANDARD.md` §8.1. Resources pages
  carry a printed caution instead
- **No currency symbol** on financial pages — the catalogue sells internationally
- **No pre-printed numeric dates** — `01/02` means different days in US and UK
- **No red/green profit-loss coding** — fails in greyscale and for colour blindness
- **`neutral` theme default; `slate` reserved for executive-tier products**
- Every product includes Licence, Read Me, and at least one Contents page
- Read Me states the method, not just the mechanics

---

# 7. POSITIONING DECISION — IMPORTANT

Earlier in the session, overlap between products was treated as a defect to
engineer around. **That was corrected.**

The operator's position, which is correct: most buyers purchase **one**
product. Each listing competes against the rest of Etsy, not against the
other listings in this shop. Twenty products with shared DNA is how a shop
covers twenty search terms.

Overlap costs only at two points:

1. **The bundle listing** — the one place a buyer sees all twenty and can
   notice repeated trackers
2. **Listing copy** — if two descriptions read identically, a buyer who lands
   on both bounces

Both are solved in SEO and bundle copy, not by redesigning pages.

**Therefore: differentiation checks are positioning work, not a build gate.**
Use them to decide what a product *leads with*. Do not use them to block a
build or to force pages apart.

---

# 8. THE COLLECTION — 14 REMAINING

Full detail in `libraries/collections/business.md`.

| # | Product | Status |
|---|---|---|
| 007 | Daily Productivity Planner | Next |
| 008 | Time Blocking Planner | |
| 009 | Focus Planner | |
| 010 | Deep Work Planner | |
| 011 | Business Dashboard Planner | |
| 012 | Client Management Planner | |
| 013 | Invoice & Payment Tracker | |
| 014 | KPI & Business Analytics Planner | |
| 015 | Business Operations Planner | |
| 016 | Business Startup Planner | |
| 017 | Business Strategy Planner | |
| 018 | Marketing Campaign Planner | |
| 019 | Content Creator Planner | |
| 020 | Social Media Planner | |
| — | Business Productivity Bundle | Requires all 20 |

---

# 9. THE STANDING SCRIPT PATTERN

Every product script follows:

**Research → Differentiate → Build → Validate → Package → Release**

Research is a real web search of the category, not an assumption. The
resulting README carries a Product Research Summary with what competitors do
well, what buyers complain about, and what this product answers.

Every collection or category the operator defines is saved to
`libraries/collections/<slug>.md` — standing rule.

---

# 10. REPOSITORY MAP

```
/                    FACTORY_PROTOCOL · PROJECT_RULES · MASTER_INSTRUCTIONS
                     ENGINE · SKILL_REGISTRY · VERSION · README
engines/             DECISION · RESEARCH · DESIGN · AUTOMATION · QUALITY
systems/             BRAND · COLOR · TYPOGRAPHY
libraries/           collections/business.md · collections/README.md
databases/           contract only — empty
_ENGINE/             6 Python modules + tests/renderer_fixture.json
_SCHEMA/             spec.schema.json · themes.json
products/            _STANDARDS/ + 7 product directories
_SEO/  _CANVA/  docs/
```

**Precedence** (`PROJECT_RULES.md` §3): PROJECT_RULES > FACTORY_PROTOCOL >
QUALITY_ENGINE > DECISION_ENGINE > ENGINE > domain engines > systems >
libraries > databases. Authority flows downward only.

---

# 11. KNOWN GAPS

| Gap | Impact |
|---|---|
| No brand name | `BRAND_SYSTEM.md` §8–9 provisional, uses `{BRAND}` |
| No logo | Covers rely on typography alone |
| `CHANGELOG.md`, `ROADMAP.md` missing | Named in the integrity check |
| `systems/` incomplete | Only 3 of the 10 named files exist |
| `libraries/`, `databases/` | Contracts only |
| 18 of 20 skills unbuilt | Registry marks them Planned; work is manual |

None block production.

---

# 12. FIRST ACTIONS IN A NEW SESSION

1. Read this file, then `FACTORY_PROTOCOL.md` and `PROJECT_RULES.md`
2. If building: read `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` and an
   existing `spec.json` as a worked example — `products/07-.../spec.json` is
   the most complete
3. If validating: Canva import first. It gates everything
4. Confirm the PAT was revoked
