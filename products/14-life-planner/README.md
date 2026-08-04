# Life Planner

Status: Built — awaiting Canva verification and print test
Version: 1.0
Last Updated: 2026-08-04
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 015

---

## Catalogue position

**No conflict. This is the first personal-life product in the catalogue.**

Every other product built so far is business or work-productivity facing. This
is the only one covering health, sleep, nutrition, relationships, family,
personal finance and wellbeing. Nothing needs deciding before it is listed.

It is worth noting that the collection is named the Business Productivity
Bundle and this product does not belong to that theme. Either the bundle name
needs widening or this product sits outside it as a standalone listing. Flagged,
not decided.

Slug `life-planner` was free.

---

## Build

```bash
python _ENGINE/planner_engine.py products/14-life-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,594 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Page types | 41 — the widest of any product in the collection |
| Sizes | A4, A5, US Letter, Half Letter |
| Layouts used | 10 of 15, all existing. No new renderer |

One validation failure on the first pass: a panel label at 42 characters
against the 40-character cap. Caught before rendering, shortened, no engine
change.

---

## Page structure — 70 pages

| Section | Pages | Layout | Section | Pages | Layout |
|---|---|---|---|---|---|
| Cover / Back Cover | 2 | `cover` | Sleep Tracker | 2 | `record` |
| Welcome, Licence, Instructions | 3 | `prose` | Mental Wellness Journal | 2 | `notes` |
| Contents × 3 | 3 | `index` | Gratitude Journal | 2 | `notes` |
| Life Vision | 2 | `panels` | Self-Care Planner | 1 | `panels` |
| Personal Mission Statement | 1 | `panels` | Relationship Planner | 2 | `record` |
| Core Values | 1 | `panels` | Family Planner | 1 | `panels` |
| Wheel of Life Assessment | 2 | `tracker` | Financial Overview | 1 | `panels` |
| Annual Life Goals | 2 | `panels` | Budget Planner | 2 | `ledger` |
| Quarterly Planning | 1 | `panels` | Savings Goals | 1 | `record` |
| Monthly Planner | 3 | `month` | Personal Development | 2 | `panels` |
| Weekly Planner | 3 | `week` | Reading Tracker | 2 | `record` |
| Daily Planner | 3 | `panels` | Learning Planner | 2 | `record` |
| Morning Routine | 2 | `panels` | Travel Planner | 1 | `record` |
| Evening Routine | 2 | `panels` | Bucket List | 1 | `record` |
| Habit Tracker | 2 | `tracker` | Reflection Pages | 2 | `panels` |
| Health & Wellness | 2 | `panels` | Monthly Review | 2 | `panels` |
| Fitness Tracker | 2 | `record` | Annual Review | 1 | `panels` |
| Nutrition Planner | 2 | `record` | Life Dashboard | 2 | `record` |
| Water Intake Tracker | 1 | `tracker` | Notes | 2 | `notes` |

All 39 requested sections are present.

---

## Design decisions

**The wheel comes before the goals, and the Welcome page says why.** Effort in
an area already scoring eight returns very little; the same effort in an area
scoring three changes the year. The annual goals page then asks which life area
each goal serves.

**Single-page sections are deliberate.** Mission, values, quarterly planning,
self-care, family, financial overview, savings, travel, bucket list and the
annual review are one page each. A life planner that gives twelve pages to
everything becomes a book nobody finishes. The Welcome page tells the buyer
outright that they will not use all of it — that honesty is what keeps a
personal planner in use past February.

**The relationship page records when you last spoke.** Not birthdays — those
are in a phone. The column that matters is how often you want to be in touch
against when you actually were.

**Self-care asks what you mistake for rest.** The distinction between restoring
and numbing is the useful one, and no planner asks it.

**The health pages carry a disclaimer in the licence.** Record keeping, not
medical advice. Worth having in writing on a product that tracks sleep,
nutrition and medication.

**The Life Dashboard is twelve rows, not thirteen weeks.** This is the only
product where the natural review cycle is monthly rather than weekly, because
the things it tracks move slowly.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass (after label fix) |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,594 × 4 |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 859 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

No `agenda` layout is used, so the US Letter overflow class that affected
products 05 and 10 does not apply here.

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

41 page types across 10 renderers is the strongest evidence so far that the
layout library generalises — an entire personal-life product was built without
touching the engine that was written for business planners.

---

## Outstanding before release

1. Decide whether this sits inside the Business Productivity Bundle or outside it
2. Canva import verification — manual
3. Physical print test
4. SEO package — `_SEO/14-life-planner.md`, personal-life keywords, not business
5. Mockups — warmer and more domestic than the business products
