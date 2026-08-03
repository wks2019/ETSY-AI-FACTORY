# Goal Achievement Planner

Status: Built — catalogue decision required before listing
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 012

---

## Read this before listing

This product overlaps `products/06-goal-planner`. The overlap was raised before
the build and the build was authorised anyway. Recorded here so it is not later
read as an oversight.

It is the **third** product built this way, after `10-meeting-planner-pro`.
The shop now holds three pairs competing in the same categories:

| Original | Shadow |
|---|---|
| `05-meeting-planner` | `10-meeting-planner-pro` |
| `06-goal-planner` | `11-goal-achievement-planner` |
| `08-focus-planner` | `09-deep-work-planner` (narrow but distinct) |

Resolve these as a set rather than one at a time. For each pair: retitle and
re-angle both, delist the original, or merge. Doing this once across three
pairs is an afternoon; doing it three times separately, after listings are
live and ranked, is not.

---

## The distinction from 06

**06 answers how to plan a goal you have already chosen. This answers which
goal to choose, and whether it survives contact with your life.**

### What 06 has that this does not

OKR planning with start / target / actual · Twelve named month calendars ·
Seven hour-gridded day pages · Habit tracker across 31 days · Lessons Learned ·
Celebration Log · The Next Goal · Tools And Support.

### What this has that 06 does not

| Page | Why it was missing from 06 |
|---|---|
| Life Areas Assessment | 06 opens at vision; nothing scores where you currently are |
| Gap Analysis | No mechanism for turning a low score into a candidate goal |
| Priority Matrix | 06 says "three slots, that is the point" but gives no method for choosing which three |
| Risk Assessment | 06 has an obstacle log with "how likely"; no impact score, no threshold |
| Habit Alignment | 06 tracks habit completion; nothing asks which goal a habit serves |
| Weekly Review | 06 has generic reflection pages on no cadence |
| Monthly Review | Absent entirely |
| Progress Dashboard | 06 tracks one number per week; nothing shows three goals plus habits together |
| Goal Setting Guide | 06 carries the guidance inside Read Me |

Pages shared with 06 are held to two or three each so the weight sits on the
gaps.

---

## Build

```bash
python _ENGINE/planner_engine.py products/11-goal-achievement-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,660 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 8 of 15, all existing. No new renderer |
| Slug | `goal-achievement-planner` — 06 owns `goal-planner` |

Clean first build. Fourth product in the collection to pass validation,
rendering and verification on the first attempt.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover / Back Cover | 2 | `cover` |
| Welcome | 1 | `prose` |
| Licence | 1 | `prose` |
| Instructions | 1 | `prose` |
| Goal Setting Guide | 1 | `prose` |
| Contents × 3 | 3 | `index` |
| Life Areas Assessment | 2 | `tracker` |
| Gap Analysis | 1 | `record` |
| Vision Planning | 2 | `panels` |
| SMART Goals Planner | 3 | `panels` |
| Annual Goals | 2 | `panels` |
| Quarterly Goals | 3 | `panels` |
| Monthly Goals | 3 | `panels` |
| Weekly Goals | 3 | `week` |
| Daily Goals | 3 | `panels` |
| Priority Matrix | 3 | `panels` |
| Milestone Planner | 2 | `record` |
| Action Plan | 2 | `record` |
| Habit Alignment | 3 | `record` |
| Resource Planner | 2 | `record` |
| Obstacle Planning | 2 | `record` |
| Risk Assessment | 3 | `record` |
| Accountability Tracker | 2 | `record` |
| Progress Tracker | 2 | `record` |
| Success Metrics | 2 | `record` |
| Motivation Log | 2 | `notes` |
| Achievement Journal | 2 | `record` |
| Reflection | 2 | `panels` |
| Weekly Review | 3 | `panels` |
| Monthly Review | 2 | `panels` |
| Progress Dashboard | 3 | `record` |
| Notes | 2 | `notes` |

All 30 requested sections are present.

---

## Design decisions

**The assessment comes first, and it is a `tracker`, not a form.** Twelve life
areas against a one-to-ten scale, ticked in ninety seconds. A written
self-assessment invites essays; a grid invites an answer. The Gap Analysis page
then turns the three lowest scores into candidate goals.

**The Priority Matrix ends with a panel listing the three survivors.** Impact
against effort produces four quadrants and a decision, not a diagram. 06 asserts
three goals is the right number without giving a method for cutting to three.

**Risk is scored, with a threshold.** Likelihood one to five, impact one to
five, and a notice saying anything at twelve or above needs a mitigation written
the same day. An unscored risk register is a worry list.

**Habit Alignment asks which goal each habit serves.** The notice on that page
is deliberate: a habit serving no goal is fine, it just should not be counted as
progress. That distinction is where most goal planners quietly mislead people.

**Weekly and Monthly Reviews are separate pages on separate cadences.** They ask
different questions — the weekly asks what moved and what slipped, the monthly
asks whether the life-area scores changed and what needs restructuring.

**The Progress Dashboard carries three goal columns plus habits.** Thirteen
weeks. Seeing three goals side by side is what exposes the one that has been
quietly abandoned since week four.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,660 × 4 |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 892 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

Visual spot-checks at US Letter, the size that has now caused two overflow
failures elsewhere in the collection: the twelve-row Life Areas tracker at ten
columns, and the six-column Risk Assessment page with its notice. Both fit with
margin. No `agenda` layout is used in this product, which is where both previous
US Letter failures occurred.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

**Tablet size.** Engine v2.1 defines four sizes in `_ENGINE/assets.py` and has
no tablet entry. A5 and Half Letter ship as the tablet-appropriate sizes.
Unchanged since product 08.

---

## Outstanding before release

1. **Catalogue decision across all three overlapping pairs** — blocking
2. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
3. Physical print test
4. SEO package — `_SEO/11-goal-achievement-planner.md`, keyword-separated from 06
5. Mockups, visually distinct from 06
