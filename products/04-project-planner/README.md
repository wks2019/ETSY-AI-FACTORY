# Project Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business — project delivery product

---

## Build

```bash
python _ENGINE/planner_engine.py products/04-project-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,428 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 10 of 15, all existing. No new renderer |
| File size | ~669 KB (A4) |

Passed every gate on the first build.

---

## Product research summary

Market scan, August 2026.

**The market splits three ways**

| Type | Strength | Weakness |
|---|---|---|
| Printable packs | Cheap, ink-friendly, binder-ready. One competitor ships 23 pages | Loose sheets. No lifecycle, no link between pages |
| Spreadsheets | Auto-calculating Gantt, Kanban and dashboards | Need a laptop. Not usable in a site meeting or a workshop |
| Hyperlinked PDFs | The closest competitor — PMI-based, stakeholder registers, built-in Gantt, 20 project slots | Coverage is broad but thin. Twenty projects means each gets a summary card |

**What buyers praise**

Flexibility, clean design, ink economy, and the Gantt chart specifically. Reviews repeatedly single out the Gantt and the amount of room for description and notes.

**What is missing across all three**

| Gap | Why it matters |
|---|---|
| Charter and scope treated as optional extras | Most projects fail at the boundary, not the schedule |
| No change log | Scope moves silently and becomes creep |
| Risk registers where they exist, issue logs almost never | A risk that happened needs different handling from one that might |
| Decision records absent | Six months on, the reasoning matters more than the outcome |
| Twenty shallow projects instead of one complete one | A project needs its sections filled, not sampled |
| Weekly review missing | Projects slip one week at a time |

**The opportunity**

One project, covered end to end — charter through lessons learned — rather than twenty projects covered as summary cards. That is stated openly in the Read Me: *one planner, one project*. It sets an honest expectation and removes the comparison with 20-slot competitors rather than losing it.

**Differentiation for the listing**

1. Full lifecycle — charter, scope, WBS, delivery, sign-off, lessons
2. Change log and issue log, both rare in this category
3. Decision log recording the reasoning, not just the outcome
4. Risk register with mitigation owner and review date
5. Budget planned against actual with a variance column
6. Weekly progress review — five of them
7. 1,428 working links across 70 pages, four sizes
8. Undated — reusable on every project

No competitor design, wording or layout was copied.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover | 1 | `cover` |
| Licence | 1 | `prose` |
| Read Me | 1 | `prose` |
| Contents — define and plan | 1 | `index` |
| Contents — deliver and review | 1 | `index` |
| Project Overview | 1 | `panels` |
| Project Charter | 1 | `panels` |
| Objectives | 1 | `panels` |
| Success Criteria | 1 | `record` |
| Stakeholder Register | 2 | `record` |
| Project Scope | 1 | `panels` |
| Requirements | 2 | `record` |
| Work Breakdown Structure | 2 | `record` |
| Milestone Planner | 2 | `record` |
| Timeline Planner | 2 | `timeline` |
| Gantt Overview | 2 | `timeline` |
| Task Planner | 4 | `record` |
| Priority Matrix | 1 | `panels` |
| Sprint Planner | 2 | `panels` |
| Kanban Board | 3 | `quarter` |
| Meeting Planner | 4 | `agenda` |
| Action Items | 2 | `record` |
| Risk Register | 2 | `record` |
| Issue Log | 2 | `record` |
| Budget Planner | 2 | `ledger` |
| Expense Tracker | 2 | `ledger` |
| Resource Planner | 2 | `record` |
| Team Planner | 2 | `record` |
| Communication Plan | 1 | `record` |
| Decision Log | 2 | `record` |
| Change Log | 2 | `record` |
| Deliverables Checklist | 2 | `record` |
| Project Dashboard | 1 | `record` |
| Weekly Progress Review | 5 | `panels` |
| Lessons Learned | 2 | `panels` |
| Notes | 3 | `notes` |
| Tools and Suppliers | 1 | `record` |
| Back Cover | 1 | `cover` |

All 36 requested sections are present.

---

## Design decisions

**Kanban uses the `quarter` renderer.** A Kanban board is three labelled columns of writing space — structurally identical to a quarter's three months. Columns are relabelled To Do, In Progress, Done in the spec. No new renderer, and the WIP limit sits in a panel beneath, because a Kanban board without a WIP limit is just a list in three parts.

**Gantt and Timeline are separate pages, both `timeline`.** Timeline works at phase level with a critical-path panel; Gantt works at task level with eight rows. Cells stay empty for the customer to shade — a pre-filled bar would be decoration.

**Budget carries a variance column.** Planned and actual without variance forces mental arithmetic on the page you are least likely to do it on.

**Change log is a first-class section.** Scope creep is not a failure of discipline so much as a failure of record-keeping. Effect on cost and effect on date are separate columns because they move independently.

**Issue log is separate from the risk register.** A risk is a forecast; an issue is a fact. Merging them loses the distinction that makes either useful.

**Read Me states "one planner, one project".** The nearest competitor advertises twenty project slots. Rather than matching that shallowly, the product commits to depth and says so — an honest expectation set before purchase, not a discovery after it.

**Passwords page omitted.** Standard §8.1. Tools and Suppliers carries a printed caution instead.

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

This is the first product to build clean on the first attempt — the panel-label cap and index overflow lessons from Products 001 and 002 were applied at authoring time rather than discovered at build time.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/04-project-planner.md`
4. Mockups
