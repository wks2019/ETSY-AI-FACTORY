# Weekly Productivity Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 006

---

## Build

```bash
python _ENGINE/planner_engine.py products/07-weekly-productivity-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 112, identical across all four sizes |
| Internal links | 4,138 per file, identical across all four sizes |
| Bookmarks | 112 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 11 of 15, all existing. No new renderer |
| File size | ~1.6 MB (A4) |

Largest product in the catalogue. Passed every gate on the first build.

---

## Overlap analysis — mandatory check

This product sits in the 006–010 cluster flagged as highest overlap risk in
`libraries/collections/business.md`. The check was run before the spec was written.

### Why this planner deserves to exist

**The week is the unit, and it repeats thirteen times.** Every other product
treats the week as one section among many — five weekly pages inside a
fifty-to-seventy-page planner. This product contains the full weekly cycle
**thirteen times**, a complete quarter of weeks in one file.

### The problem it solves

A buyer review in this category states it exactly: *"I wish the daily ones
were able to be duplicated... I need weekly ones, weekly. Whereas the front
of these are W/M/QT, which I don't need weekly."*

That is the category's structural failure. Competitors give one weekly spread
and expect reprinting, so review pages are never kept and nothing accumulates.
Another review describes the workaround: planners that end up
*"Frankensteined"* from pages mixed across products.

### Why another planner cannot solve it

| Product | Weekly pages | Why it fails this buyer |
|---|---|---|
| 001 Business Productivity | 5 | Weekly is one section. No weekly review, no trackers |
| 002 CEO Planner | 5 | Executive scope. Quarterly rhythm, not weekly |
| 003 Project Planner | 5 progress reviews | Tied to one project, not to a life |
| 005 Goal Planner | 5 | The goal is the unit; the week only serves it |
| 007 Daily Productivity | — | The day is the unit |
| 008 Time Blocking | — | The calendar slot is the unit |

None of them repeat the weekly cycle, and none contain health, water, meal or
exercise tracking — which is the second difference: this is a **whole-life
week**, not a business week.

### Shared pages

`quarter` · `month` · `week` · `tracker` · `notes` · `panels` · `ledger`
renderers are shared with the rest of the collection, as the collection rules
require. Annual Vision, Quarterly Focus and Monthly Objectives appear in
reduced form as context above the week.

### Unique pages

Weekly Calendar (hour grid across seven day columns) · Weekly Time Allocation
(planned against actual hours) · Weekly Health Tracker · Weekly Water Tracker
· Weekly Exercise Tracker · Weekly Meal Planner · Weekly Wins · Weekly
Challenges · Next Week Planning · How To Use.

**Verdict: passes.** Distinct unit of planning, distinct scope, distinct
volume. Build approved.

---

## Research summary

The weekly planner category is enormous and shallow. Typical listings include
<cite>a dated or undated weekly grid, a priorities section, a to-do checklist,
space for appointments and notes, a weekly goals area, and habit or water
trackers</cite>, with some adding meal planning or fitness.

**Strengths across the category:** multi-size printing is standard
(A4/A5/Letter/Half); undated formats are common; habit and water trackers are
expected; reviews are strong and specific, and one notes the habit tracker as
*"a great feature that's not easy to find in other planners."*

**Complaints that shaped this product:**

| Complaint | Response |
|---|---|
| Weekly pages not repeated; front matter you don't need weekly | Thirteen full weekly cycles; front matter appears once |
| "Frankensteined" planners assembled from several products | One coherent system, one file |
| Weekly review usually absent or one line | Wins, Challenges, Reflection, Lessons, Next Week — five distinct review pages |
| Trackers present but disconnected from planning | Time Allocation feeds the Task Manager; Reflection feeds Next Week |

**Feature recommendations acted on:** habit and water trackers at seven
columns rather than thirty-one; a real hour-by-day calendar grid; meal
planning included rather than sold separately; a stated weekly ritual with
timings.

---

## Page structure — 112 pages

| Section | Pages | Layout |
|---|---|---|
| Cover | 1 | `cover` |
| Licence | 1 | `prose` |
| Read Me | 1 | `prose` |
| How To Use | 1 | `prose` |
| Contents — horizons | 1 | `index` |
| Contents — running the week | 1 | `index` |
| Contents — tracking and reviewing | 1 | `index` |
| Annual Vision | 1 | `panels` |
| Quarterly Focus | 4 | `quarter` |
| Monthly Objectives | 12 | `month` |
| Weekly Overview | 13 | `week` |
| Weekly Priorities | 6 | `panels` |
| Top Three Goals | 4 | `panels` |
| Weekly Calendar | 6 | `record` |
| Weekly Time Allocation | 4 | `record` |
| Weekly Task Manager | 6 | `record` |
| Weekly Habit Tracker | 6 | `tracker` |
| Weekly Health Tracker | 4 | `tracker` |
| Weekly Water Tracker | 2 | `tracker` |
| Weekly Exercise Tracker | 4 | `record` |
| Weekly Meal Planner | 6 | `record` |
| Weekly Finance Snapshot | 4 | `ledger` |
| Weekly Wins | 3 | `panels` |
| Weekly Challenges | 3 | `panels` |
| Weekly Reflection | 6 | `panels` |
| Lessons Learned | 2 | `panels` |
| Next Week Planning | 4 | `panels` |
| Notes | 3 | `notes` |
| Tools and Contacts | 1 | `record` |
| Back Cover | 1 | `cover` |

All 28 requested sections are present.

---

## Design decisions

**Thirteen weekly overviews.** One quarter of weeks. This is the product's
reason to exist and its answer to the category's central complaint.

**A stated weekly ritual with timings.** How To Use gives Friday 30 minutes,
Sunday 30 minutes, five minutes daily. Competitors supply pages and no method.
A weekly system that requires daily planning is a daily system mislabelled,
and the page says so.

**Time Allocation comes before the Task Manager.** Hours are the budget.
Assigning tasks before allocating hours is how a week gets overcommitted on
Sunday afternoon.

**Weekly Calendar is an hour grid across seven day columns**, built from the
`record` renderer with Time plus Mon–Sun as columns. No new renderer.

**Trackers use seven columns, not thirty-one.** Every other product in the
collection uses monthly trackers. Here the tracker matches the planning unit.

**Wins are written before Challenges.** Reviewing a week critic-first produces
a demoralising record. The order is deliberate and stated in How To Use.

**Health tracker measures energy at waking and at three.** The afternoon dip
is where a week is actually lost.

**Meal planning included.** Sold as a separate product across the category.
A week that ignores Wednesday dinner is not a weekly system.

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

Second product to build clean on the first attempt.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/07-weekly-productivity-planner.md`
4. Mockups
