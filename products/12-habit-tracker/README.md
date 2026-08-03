# Habit Tracker

Status: Built — awaiting Canva verification and print test
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 013

---

## Catalogue position

**This is a genuinely new product**, not a shadow of an existing one. It is the
first such product since 09.

The only prior habit content in the catalogue is a three-page 31-day tracker
sitting beneath the goals in `06-goal-planner`, and a single Habit Alignment
page in `11-goal-achievement-planner`. Neither is a habit system. Overlap is
under five per cent of this product's pages and no catalogue decision is
required before listing.

Slug `habit-tracker` was free.

---

## Build

```bash
python _ENGINE/planner_engine.py products/12-habit-tracker/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,674 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 7 of 15, all existing. No new renderer |

Clean first build.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover / Back Cover | 2 | `cover` |
| Welcome | 1 | `prose` |
| Licence | 1 | `prose` |
| Instructions | 1 | `prose` |
| Habit Building Guide | 1 | `prose` |
| Contents × 3 | 3 | `index` |
| Habit Assessment | 2 | `tracker` |
| Keystone Habits | 2 | `panels` |
| Habit Categories | 2 | `record` |
| Morning Habits | 2 | `panels` |
| Evening Habits | 2 | `panels` |
| Daily Habit Tracker | 3 | `panels` |
| Weekly Habit Tracker | 4 | `tracker` |
| Monthly Habit Tracker | 4 | `tracker` |
| Annual Habit Overview | 2 | `tracker` |
| 30-Day Challenge | 2 | `tracker` |
| 66-Day Habit Builder | 2 | `tracker` |
| Habit Streak Tracker | 2 | `record` |
| Consistency Calendar | 2 | `tracker` |
| Success Rate Dashboard | 2 | `record` |
| Trigger Identification | 3 | `record` |
| Cue Routine Reward | 3 | `panels` |
| Habit Stacking Planner | 3 | `record` |
| Accountability Tracker | 2 | `record` |
| Reward Planner | 2 | `record` |
| Obstacle Log | 2 | `record` |
| Missed Habit Analysis | 2 | `record` |
| Reflection | 2 | `panels` |
| Weekly Review | 3 | `panels` |
| Monthly Review | 2 | `panels` |
| Progress Dashboard | 2 | `record` |
| Notes | 2 | `notes` |

All 31 requested sections are present.

---

## Design decisions

**Five tracking granularities, each a different shape.** Daily is `panels`
split by time of day, because a day is a sequence, not a grid. Weekly is seven
columns × twelve habits. Monthly is thirty-one × ten. Annual is twelve months
× twelve habits. The Consistency Calendar inverts the axes entirely — one
habit, twelve month rows of thirty-one days — which is the only view that shows
a year of a single behaviour at once.

**The builder runs sixty-six days, not twenty-one.** The twenty-one-day figure
traces to a plastic surgeon's anecdote about patients adjusting to a new
appearance and has no basis as a habit-formation interval. The measured median
is closer to sixty-six with wide variance. Two pages of thirty-three columns
cover it, and the Welcome page explains why rather than asserting it.

**Missed Habit Analysis has a Missed Twice column and a notice.** One missed
day is noise; two consecutive is the new pattern. That column is the single
most diagnostic field in the product and the notice tells the buyer to rebuild
the cue before adding anything else.

**Stacking carries a warning about the anchor.** Anchoring a new habit to
another habit you are still building collapses both. That failure is common
enough to warrant a printed notice rather than a line in the guide.

**Success Rate converts streaks into percentages.** Nineteen days out of
thirty reads as failure and is sixty-three per cent against a baseline of zero.
The page exists to correct that distortion, which is the most common reason
people quit in month two.

**Rewards are checked for whether they undo the habit.** The Reward Planner has
an explicit column for it. A reward that reverses the behaviour is the standard
failure of reward-based habit systems.

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

### Note on the 33-column grid

The 66-Day Habit Builder is the densest grid shipped in this collection — 33
columns against a previous maximum of 31. It was inspected at Half Letter, the
worst case: the grid renders correctly and the columns are even, but the cells
are small enough that ticking by hand on a printed Half Letter sheet will be
fiddly. It is comfortable at A4 and US Letter and on a tablet at any size.

This is a usability observation, not a defect, and it is recorded in
`metadata.json` under print compatibility so the listing can say so. **The
physical print test should start with this page.**

---

## Engine reuse

No engine modification. No schema modification. No new renderers. No blockers.

**Tablet size.** Engine v2.1 defines four sizes in `_ENGINE/assets.py` and has
no tablet entry. A5 and Half Letter ship as the tablet-appropriate sizes.

---

## Outstanding before release

1. Physical print test — start with the 66-day builder at Half Letter
2. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
3. SEO package — `_SEO/12-habit-tracker.md`
4. Mockups
