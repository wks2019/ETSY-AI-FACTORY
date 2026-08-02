# CEO Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business — flagship executive product

---

## Build

```bash
python _ENGINE/planner_engine.py products/03-ceo-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 78, identical across all four sizes |
| Internal links | 2,370 per file, identical across all four sizes |
| Bookmarks | 78 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `slate` — first product to use it |
| Layouts used | 14 of 15, all existing. No new renderer |
| File size | ~971 KB (A4) |

---

## Product research summary

Market scan, August 2026.

**The finding that shaped the product:** the CEO segment is dominated by **spreadsheets, not planners**. Listings returned for CEO and executive queries are overwhelmingly Excel and Google Sheets dashboards — auto-calculating KPI trackers, financial scorecards, departmental metrics. The `ceo_planner` category itself is thin.

**Strengths of the incumbents**

- Auto-calculation and charting, which no PDF can match
- Genuinely comprehensive metric coverage — revenue, margin, CSAT, attrition, utilisation
- Clear positioning toward founders and growth-stage executives

**What they cannot do**

| Gap | Why it matters |
|---|---|
| Require a laptop and a spreadsheet application | A spreadsheet is not opened in a board meeting or on a plane |
| Optimised for reporting, not thinking | A dashboard tells you the number. It does not ask what you will do about it |
| No place for a decision, only for data | The reasoning behind a decision is the thing worth keeping |
| No leadership or delegation surface | Running a company is mostly people, and spreadsheets have no page for that |
| Nothing printable or annotatable | Handwriting a number forces you to look at it |

**Personal-productivity planners** fill the other half of the market and fail the opposite way: they plan the individual's day and have no vision page, no OKRs, no delegation, no team review.

**The opportunity**

A planner that occupies the space between them — executive scope with a planner's format. This product does not compete with a spreadsheet on arithmetic. It competes on the part a spreadsheet is worst at: deciding, delegating, and reviewing honestly.

That position is stated plainly in the Read Me, which tells the buyer what the product deliberately does not do.

**Differentiation for the listing**

1. Executive scope — vision, OKRs, KPIs, delegation, team review, decision log
2. A decision log recording the reasoning, not just the outcome
3. Delegation planner with authority granted, not just a task assigned
4. Quarterly OKRs with target and actual side by side
5. 2,370 working links across 78 pages
6. Four sizes, print and digital parity
7. Undated — buy once

No competitor design, wording or layout was copied.

---

## Page structure — 78 pages

| # | Section | Pages | Layout |
|---|---|---|---|
| 1 | Cover | 1 | `cover` |
| 2 | Licence | 1 | `prose` |
| 3 | Read Me | 1 | `prose` |
| 4 | Contents — planning horizons | 1 | `index` |
| 5 | Contents — operations and review | 1 | `index` |
| 6 | The Vision | 1 | `panels` |
| 7 | Annual Objectives | 1 | `panels` |
| 8 | Quarterly OKRs | 4 | `record` |
| 9 | Quarterly Planning | 4 | `quarter` |
| 10 | Monthly Strategy | 12 | `month` |
| 11 | Weekly Executive Planner | 5 | `week` |
| 12 | Daily CEO Planner | 7 | `day` |
| 13 | Priority Matrix | 1 | `panels` |
| 14 | Decision Log | 2 | `record` |
| 15 | Meeting Planner | 4 | `agenda` |
| 16 | Leadership Notes | 2 | `notes` |
| 17 | Project Roadmaps | 4 | `timeline` |
| 18 | KPI Dashboard | 2 | `record` |
| 19 | Revenue Tracker | 3 | `ledger` |
| 20 | Expense Summary | 2 | `ledger` |
| 21 | Team Performance | 2 | `record` |
| 22 | Delegation Planner | 2 | `record` |
| 23 | Client Relationships | 2 | `record` |
| 24 | Business Ideas | 2 | `notes` |
| 25 | Habit Tracker | 2 | `tracker` |
| 26 | Learning and Reading Log | 2 | `record` |
| 27 | Reflection and Review | 2 | `panels` |
| 28 | Notes | 3 | `notes` |
| 29 | Tools and Advisors | 1 | `record` |
| 30 | Back Cover | 1 | `cover` |

---

## Design decisions

**`slate` theme.** First product to use it. Cool grey with a single blue accent — the corporate and consulting positioning defined in `systems/COLOR_SYSTEM.md` §12. Distinguishes the executive tier from the Business Productivity Planner's warm neutral without breaking collection consistency: same tokens, same type, same components.

**Two index pages.** Sixty-two entries overflowed a single page at A4 and US Letter. Split by horizon — planning, then operations — rather than shrinking type below the legibility floor. A spec-level fix using the existing renderer.

**Decision log records the reasoning.** Columns are Date, The Decision, What I Believed At The Time, Alternative Rejected, Revisit On. Recording only the outcome makes the log useless a year later, when the question is whether the reasoning held.

**Delegation records authority, not just the task.** Handing over a task without stating the decision rights is why delegation returns to the desk.

**Week has "This Week's Numbers" and "Working On The Business".** Both are the first things displaced by client work.

**Habits include "No decision made while tired".** Executive habit tracking that ignores decision quality tracks the wrong thing.

**Passwords page omitted.** Standard §8.1. Tools and Advisors carries a printed caution instead.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

One blocker surfaced and was resolved at spec level (index overflow). Two schema constraints were enforced and respected — the 40-character panel label cap rejected seven labels, all shortened rather than the cap raised.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/03-ceo-planner.md`
4. Mockups
