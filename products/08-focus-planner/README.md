# Focus Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 009

---

## Numbering — read this first

This product was built **out of catalogue order**. Collection numbers 007
(Daily Productivity Planner) and 008 (Time Blocking Planner) are still
unbuilt.

Until now the directory number and the collection number differed by exactly
one, because build order and catalogue order happened to coincide. They no
longer do.

| Field | Value |
|---|---|
| Directory | `products/08-focus-planner` — eighth product built |
| Collection number | `009` — ninth product in the bundle |

From here, **the directory number is build order and `collection_number` in
`manifest.json` is catalogue position**. The offset rule is retired, not
broken. Do not infer one number from the other.

The differentiation table below is written against two siblings that do not
yet exist. Re-check it when 007 and 008 are built.

---

## Build

```bash
python _ENGINE/planner_engine.py products/08-focus-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,884 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 8 of 15, all existing. No new renderer |
| File size | ~0.8 MB (A4) |

Third product to build clean on the first attempt.

---

## Overlap analysis — mandatory check

This product sits in the 006–010 cluster flagged as highest overlap risk in
`libraries/collections/business.md`. The check was run before the spec was
written, and it is the tightest check in the collection so far: 007, 008 and
010 are all adjacent to this product.

### Why this planner deserves to exist

**The focus session is the unit.** Not the day, not the calendar slot, not the
project. The session is planned in the two minutes before it starts, logged in
the three minutes after it ends, and reviewed until the pattern is visible.
No other product in the collection plans the inside of a block of time.

### The problem it solves

Every planner in this category schedules attention and none of them protects
it. A buyer allocates 09:00–11:00 to deep work, gets pulled away four times,
and the planner records none of it — so next week the same two hours are
allocated to the same work with the same result. Allocation without a
distraction record is a plan that cannot learn.

### Why another planner cannot solve it

| Product | Unit | Why it fails this buyer |
|---|---|---|
| 001 Business Productivity | The business | Focus is one section among twenty |
| 005 Goal Planner | The goal | Plans the outcome, not the hour that produces it |
| 006 Weekly Productivity | The week | Weekly time allocation, no session-level record |
| 007 Daily Productivity | The day | Plans the whole day; does not open the block |
| 008 Time Blocking | The calendar slot | Allocates the slot. This plans what happens inside it |
| 010 Deep Work | The deep-work project | Longer horizon; this is session-level execution |

The clean line: **008 decides when the block happens. This decides whether the
block works, and records why when it does not.**

### Shared pages

`panels` · `record` · `tracker` · `notes` · `prose` · `index` · `cover`
renderers are shared with the rest of the collection, as the collection rules
require. Priority Planner and Future Focus appear in reduced form as context
above the session.

### Unique pages

Focus Session Planner · Deep Focus Log (depth rating and stated output) ·
Distraction Tracker (internal versus external) · Interruption Log (separate
from distraction, because the fix is different) · Recovery Plan · Break
Planner · Energy Tracker at hour granularity · Progress Dashboard across
thirteen weeks · Focus Principles.

**Verdict: passes.** Distinct unit of planning, distinct failure mode
addressed, no page duplicated from an adjacent product.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover | 1 | `cover` |
| Licence | 1 | `prose` |
| Read Me | 1 | `prose` |
| How To Use | 1 | `prose` |
| Focus Principles | 1 | `prose` |
| Contents — the system | 1 | `index` |
| Contents — sessions | 1 | `index` |
| Contents — review | 1 | `index` |
| Priority Planner | 3 | `panels` |
| Today's Focus | 6 | `panels` |
| Most Important Tasks | 6 | `panels` |
| Time Blocking | 6 | `day` |
| Focus Session Planner | 5 | `panels` |
| Deep Focus Log | 4 | `record` |
| Distraction Tracker | 3 | `record` |
| Interruption Log | 3 | `record` |
| Recovery Plan | 2 | `panels` |
| Energy Tracker | 3 | `tracker` |
| Break Planner | 2 | `record` |
| Reflection | 4 | `panels` |
| Daily Notes | 3 | `notes` |
| Weekly Focus Review | 4 | `panels` |
| Progress Dashboard | 2 | `record` |
| Future Focus | 2 | `panels` |
| Notes | 2 | `notes` |
| Tools And Environment | 1 | `record` |
| Back Cover | 1 | `cover` |

All 21 requested sections are present.

---

## Design decisions

**Distraction and interruption are separate logs.** They look alike and are
fixed differently. A distraction comes from inside and is answered by rest or
by removing a trigger. An interruption comes from outside and is answered by a
boundary. Merging them into one tracker — which the category does — produces a
list that proves you were interrupted and suggests nothing.

**The session plan is filled before the block, not after.** Goal, finish line,
length, what is switched off, what to do when stuck, and the break already
booked. A session with no stated finish line ends when energy runs out.

**Deep Focus Log carries a depth rating and a stated output.** Minutes alone
reward sitting still. Depth plus output is the only pair that distinguishes
two hours of work from two hours of presence.

**Breaks are planned before the block starts.** The Break Planner asks whether
the break was screen-free and whether it restored anything. A break spent
scrolling is a context switch wearing a rest label.

**Energy is tracked at waking, ten, one, three and five.** Daily granularity
hides the afternoon collapse, which is exactly where the schedule is wrong.

**Progress Dashboard runs thirteen weeks.** Deep hours, sessions, MITs
completed, distractions logged, best block, verdict. Two or three weeks of
focus data is noise; a quarter is a pattern.

**Time Blocking uses the `day` renderer** — 06:00 to 21:00 hour rows on the
left, deep/shallow/fixed/buffer panels on the right. First use of `day` in the
Business Productivity Bundle. No renderer change was needed.

**Recovery Plan is written once and used repeatedly.** Deciding what to do
about broken concentration while concentration is broken does not work.

**Focus Principles is a prose page, not a quote page.** Six rules with the
reasoning attached. The collection does not ship motivational filler.

---

## Deviation from products 001–007

**The three Contents pages cross-link to each other.** In products 001–007,
sibling index pages were reachable only through the bookmark outline — the
Index tab always lands on the first one. Here each Contents page carries chips
to the other two, and the two secondary pages carry distinct titles
(`Contents — Sessions`, `Contents — Review`) so the chips and the bookmark
outline are readable rather than three identical `Contents` entries.

This is spec-level `links` only. No engine change, no schema change, +12 link
annotations. It is back-portable to 001–007 as a spec-only edit and should be
considered during the next validation sweep.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,884 × 4 |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 1,004 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

Visual spot-checks at Half Letter, the binding size: `day` layout, the
seven-column Progress Dashboard, and the densest prose page. No clipping, no
overflow, no column collapse.

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

**Note on the tablet size.** The build request asked for a tablet version "if
supported by current engine". Engine v2.1 defines four sizes in
`_ENGINE/assets.py`; there is no tablet entry. A5 and Half Letter are the
tablet-appropriate sizes and both are included. Adding a true tablet aspect
ratio is an engine change affecting all twenty products and was not made
unilaterally.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/08-focus-planner.md`
4. Mockups
5. Reconcile the bundle catalogue with the retired directory/collection offset
