# Project Execution Planner

Status: Built — catalogue decision required before listing
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 014

---

## Read this before listing

This product overlaps `products/04-project-planner`, and **the distinction is
the thinnest in the catalogue.** That is a change from the previous two shadow
products and it is worth stating plainly rather than burying.

`04` was checked page by page before this spec was written. Of the thirty-three
sections requested for this product, **twenty-seven already exist in 04**. Only
six are genuinely absent:

| Absent from 04 | Substance |
|---|---|
| Responsibility Matrix (RACI) | Real gap — 04 has owners on tasks but no accountability matrix |
| Project Closure Checklist | Real gap — 04 ends at lessons learned |
| Final Project Review | Real gap — 04's retrospective is about process, not outcome against promise |
| Weekly Project Planner | Generic execution page |
| Daily Task Planner | Generic execution page |
| Time Blocking | Generic execution page |

Three real gaps and three generic pages is a weaker basis for a separate
product than either `10-meeting-planner-pro` (eight gaps) or
`11-goal-achievement-planner` (eight gaps).

**Recommendation: merge.** Fold RACI, the closure checklist, the final review
and the daily/weekly cadence into `04` as a v2.0 and ship one large Project
Planner rather than two competing ones. This product's spec is the source for
that merge — nothing here needs rewriting, only relocating.

If you list both anyway, the titles and first two description lines must carry
the distinction: 04 plans a project, this one runs and closes it.

---

## The axis, as built

**04 defines and controls a project. This runs and closes one.**

Definition pages here are deliberately one page each — overview, charter,
scope, objectives, success criteria, work breakdown, priority matrix. They give
the project a spine without repeating 04's planning depth. The weight sits
after the kick-off: RACI three pages, weekly four, daily four, time blocking
four, closure three, final review three.

---

## Build

```bash
python _ENGINE/planner_engine.py products/13-project-execution-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,674 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 11 of 15 — the widest layout spread of any product so far |
| Slug | `project-execution-planner` — 04 owns `project-planner` |

Clean first build.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover / Back Cover | 2 | `cover` |
| Welcome, Licence, Instructions | 3 | `prose` |
| Contents × 3 | 3 | `index` |
| Project Overview | 1 | `panels` |
| Project Charter | 1 | `panels` |
| Project Scope | 1 | `panels` |
| Vision And Objectives | 1 | `panels` |
| Success Criteria | 1 | `record` |
| Stakeholder Register | 2 | `record` |
| Team Directory | 2 | `record` |
| Responsibility Matrix | 3 | `record` |
| Milestone Planner | 2 | `record` |
| Work Breakdown Structure | 1 | `record` |
| Task Planner | 3 | `record` |
| Priority Matrix | 1 | `panels` |
| Timeline Planner | 2 | `timeline` |
| Weekly Project Planner | 4 | `week` |
| Daily Task Planner | 4 | `panels` |
| Time Blocking | 4 | `day` |
| Budget Tracker | 2 | `ledger` |
| Resource Planner | 2 | `record` |
| Risk Register | 2 | `record` |
| Issue Log | 2 | `record` |
| Decision Log | 2 | `record` |
| Change Request Log | 2 | `record` |
| Meeting Notes | 3 | `agenda` |
| Progress Tracker | 2 | `record` |
| KPI Dashboard | 2 | `record` |
| Lessons Learned | 2 | `panels` |
| Project Closure Checklist | 3 | `record` |
| Final Project Review | 3 | `panels` |
| Notes | 2 | `notes` |

All 33 requested sections are present.

---

## Design decisions

**The closure checklist names what actually leaks.** Access and licences
revoked, invoices raised and paid, contractors released, files archived, team
formally stood down. Projects that are "basically finished" carry subscription
cost and open access for months. The notice on that page lists the categories so
the buyer does not have to remember them.

**The final review asks whether you would take the project again.** Separate
from lessons learned, which is about process. This one is about outcome against
promise: delivered against promised, final cost against budget, final date
against original, and what the client actually said.

**Time blocking uses the `day` renderer at 07:00 to 19:00.** Project work loses
every unstructured contest with reactive work. Booking it is the only defence,
and it needs an hour grid rather than a list.

**RACI carries the one-name-accountable notice.** Same rule as
`10-meeting-planner-pro`, deliberately consistent across the collection.

**Definition pages are single pages on purpose.** This is the clearest signal of
the product's position, and it is also what keeps it from being a straight
reprint of 04.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,674 × 4 |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 899 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

### The agenda ceiling was respected

Products 05 and 10 both overflowed at US Letter on `agenda` pages. The ceiling
established after the second failure — four panels plus notes plus an action
table plus chips does not fit — was applied here in advance: the Meeting Notes
page carries two panels and no chip row. Verified visually at US Letter, and the
link parity gate confirms it across all four sizes.

The Contents — Execute page carries 33 entries, the longest index in the
collection. It splits cleanly into two columns and fits with room to spare.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

This product uses eleven of the fifteen renderers — the widest spread yet, and
reasonable evidence that the layout library is now sufficient for the remaining
products in the collection.

**Tablet size.** Engine v2.1 defines four sizes and has no tablet entry. A5 and
Half Letter ship as the tablet-appropriate sizes.

---

## Outstanding before release

1. **Merge decision with 04** — blocking, and recommended rather than optional
2. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
3. Physical print test
4. SEO package — `_SEO/13-project-execution-planner.md`
5. Mockups, visually distinct from 04
