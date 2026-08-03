# Deep Work Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 010

---

## Numbering

Directory `09-` is build order. Collection number is `010`. Catalogue numbers
007 (Daily Productivity) and 008 (Time Blocking) remain unbuilt, so the
directory/collection offset retired at product 08 stays retired. Neither
number can be inferred from the other; read `collection_number` in
`manifest.json`.

---

## Overlap analysis — the reason this product needed rewriting

The requested page list for this product overlapped 008 Focus Planner by
roughly **70%**: Time Blocking, MIT, Interruptions Log, Recovery Plan, Energy
Tracker, Break Schedule, Progress Dashboard, Daily Reflection and Weekly
Review all appeared in both. Shipped as written, the two listings would
compete for the same search terms and the same buyer, and anyone who bought
both would have grounds to say so publicly.

### The line

**008 plans one session. 009 plans a project across thirteen weeks.**

Every shared-name page was rebuilt to run at the project scale:

| Page | 008 Focus Planner | 009 Deep Work Planner |
|---|---|---|
| Time Blocking | `day` — hourly grid, 06:00–21:00, one day | `timeline` — seven days × eight two-hour bands, one week |
| MIT | Three tasks for today | Three per week, each tied to a session and a milestone |
| Session page | Plan the next block | Prepare a session that continues a project, with a warm restart point |
| Session log | Date, goal, minutes, depth | Date, milestone served, minutes, flow, output |
| Distraction | Log what pulled you away | Record the countermeasure applied and whether it held for weeks |
| Interruptions | Individual events with minutes lost | Sources by frequency per week, with the boundary and whether it broke |
| Recovery | The hour that wobbled | The week that collapsed |
| Energy | Seven days, hour by hour | Thirteen weeks against deep hours achieved |
| Breaks | A log of breaks taken | A protocol decided once |
| Dashboard | Deep hours, sessions, distractions | Target hours against actual, flow sessions, milestone progress |

### Unique to this product

Welcome · Deep Work Method · Deep Work Goals · Priority Matrix (four
quadrants) · Weekly Planning · Focus Environment Checklist · Flow State
Tracker · Completion Review.

### Unique to 008, deliberately absent here

Today's Focus · Focus Principles · Daily Notes · Future Focus · Tools And
Environment.

**Verdict: passes, conditionally.** The distinction holds structurally, but it
is the narrowest gap in the collection. The listing copy for both products
must state which is which in the first two lines of the description — recorded
as an outstanding item in `manifest.json`.

---

## Build

```bash
python _ENGINE/planner_engine.py products/09-deep-work-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,754 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 9 of 15, all existing. No new renderer |
| File size | ~0.85 MB (A4) |

First use of `week` and `timeline` in the Business Productivity Bundle. Both
rendered correctly at Half Letter without modification.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover / Back Cover | 2 | `cover` |
| Welcome | 1 | `prose` |
| Licence | 1 | `prose` |
| Instructions | 1 | `prose` |
| Deep Work Method | 1 | `prose` |
| Contents × 3 | 3 | `index` |
| Deep Work Goals | 3 | `panels` |
| Priority Matrix | 3 | `panels` |
| Weekly Planning | 4 | `week` |
| Daily Planning | 4 | `panels` |
| MIT Planner | 4 | `panels` |
| Time Blocking Planner | 4 | `timeline` |
| Session Preparation | 4 | `panels` |
| Focus Environment Checklist | 2 | `record` |
| Deep Work Session Log | 4 | `record` |
| Flow State Tracker | 3 | `tracker` |
| Distraction Elimination Tracker | 3 | `record` |
| Interruptions Log | 3 | `record` |
| Recovery Plan | 2 | `panels` |
| Energy Level Tracker | 3 | `tracker` |
| Break Schedule | 2 | `panels` |
| Completion Review | 3 | `panels` |
| Daily Reflection | 3 | `panels` |
| Weekly Review | 3 | `panels` |
| Progress Dashboard | 2 | `record` |
| Notes | 2 | `notes` |

All 25 requested sections are present.

---

## Design decisions

**Thirteen weeks is the spine.** Goals set a week-four and a week-thirteen
milestone, the dashboard runs thirteen rows, the energy tracker runs thirteen
columns, and Completion Review is run at each milestone rather than only at
the end. A planner for long work needs a horizon written into the pages.

**Time blocking is weekly, in two-hour bands.** A daily hour grid belongs to
008. At project scale the question is not "what happens at 14:00 on Tuesday"
but "which eight bands this week belong to the project" — so the `timeline`
renderer takes seven day rows against eight bands, and the buyer shades them.

**The session log records output, not effort.** Minutes and a flow rating sit
beside "what was produced" and the milestone it served. Hours alone reward
endurance; a four-hour session that moved nothing is the entry that matters.

**Flow is tracked as conditions, not as a feeling.** Nine binary conditions
across fourteen sessions — single goal, difficulty matched to skill, no device
in reach, warm start, ended by choice. Flow is reproducible when you know
which conditions preceded it.

**Distraction Elimination is a countermeasure record.** Source, rule applied,
date, weeks held, still working. 008 logs the distraction; this logs the fix
and whether it survived contact with a bad week.

**Session Preparation ends by asking where you will stop.** Stopping at a
natural break makes the next session cold. Stopping mid-thought makes it warm.
The field exists because restarting is the expensive part.

**Shallow work is given a slot rather than condemned.** Daily Planning batches
it into one block. A planner that treats email as a character flaw gets
abandoned in week three.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass (after label fix) |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,754 × 4 |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 939 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

**First build failed validation**, correctly: four panel labels exceeded the
40-character schema cap. Caught before rendering, fixed in the spec, no engine
change. Worth noting that the cap is doing real work — those labels would have
wrapped and pushed panels past the fold at Half Letter.

Visual spot-checks at Half Letter: the `timeline` weekly grid, the `week`
seven-panel layout, the 30-entry Contents — Execution page, and the
fourteen-column Flow State Tracker. No clipping, no overflow, no column
collapse.

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

**Tablet size.** Engine v2.1 defines four sizes in `_ENGINE/assets.py` and has
no tablet entry. A5 and Half Letter ship as the tablet-appropriate sizes.
Unchanged from product 08.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/09-deep-work-planner.md`, keyword-separated from 008
4. Mockups
5. Listing copy stating the 008 / 009 distinction in the first two lines
6. Reconcile the bundle catalogue with the retired directory/collection offset
