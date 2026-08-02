# Goal Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business — goal achievement product

---

## Build

```bash
python _ENGINE/planner_engine.py products/06-goal-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 71, identical across all four sizes |
| Internal links | 2,086 per file, identical across all four sizes |
| Bookmarks | 71 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 11 of 15, all existing. No new renderer |
| File size | ~867 KB (A4) |

---

## Product research summary

Market scan, August 2026.

**This is the most crowded category the factory has entered.** Goal planners are everywhere on Etsy — printables, spreadsheets, bundles, vision-board kits, 12-week-year templates. A representative bestseller ships 30 pages across planning, task, habit and review sections in A4, A5 and US Letter.

**What the strong listings do well**

- Comprehensive coverage — brainstorming, vision board, SMART goal, quarterly action plans, habit assessment, weekly through quarterly reviews
- Multi-size printing as standard
- Undated formats, letting buyers date pages themselves. One review specifically praises being able to organise and date the pages personally
- Strong review volumes and repeat purchase

**The weakness the reviews reveal**

One buyer review is unusually diagnostic: the sheets are *"kinda similar"*, but it is *"a good option if you wanna try a bunch of goal planning formats and see what sticks."*

That is the category's defining flaw stated by a satisfied customer. These products are **format samplers**. They offer many ways to write down a goal and no opinion about which one works. The buyer is handed the problem they came to solve.

**Other gaps**

| Gap | Consequence |
|---|---|
| No limit on how many goals you set | Twelve goals is a wish list, and the product encourages it |
| Obstacles rarely appear at all | The single most common reason goals are abandoned goes unrecorded |
| No accountability structure | Goals kept private fail more often |
| Vision boards instead of vision statements | Images are easy to make and impossible to act on |
| Celebration and completion never recorded | Finished goals leave no evidence, so nothing compounds |
| Progress tracked as ticks, not numbers | A goal without a measured baseline cannot be evaluated |

**The opportunity**

An opinionated goal planner. Not more formats — one sequence, stated plainly, with the sections that actually change outcomes: three goals maximum, a named obstacle, a person told, a number tracked, and a record of what got finished.

The Read Me states the sequence and explains why the annual page has exactly three slots.

**Differentiation for the listing**

1. Three annual goal slots — a constraint, stated as a feature
2. Obstacle log recording early warning signs before the obstacle arrives
3. Accountability tracker — who was told, what was promised, whether it was kept
4. Progress tracked with baseline, target, actual and gap
5. Celebration log — finished things, recorded
6. Next Goal page chosen from evidence rather than enthusiasm
7. 2,086 working links across 71 pages, four sizes
8. Undated — buy once

No competitor design, wording or layout was copied.

---

## Page structure — 71 pages

| Section | Pages | Layout |
|---|---|---|
| Cover | 1 | `cover` |
| Licence | 1 | `prose` |
| Read Me | 1 | `prose` |
| Contents — define and plan | 1 | `index` |
| Contents — execute and review | 1 | `index` |
| Life Vision | 1 | `panels` |
| Annual Goals | 1 | `panels` |
| SMART Goal Worksheets | 4 | `panels` |
| OKR Planning | 2 | `record` |
| Quarterly Goals | 4 | `quarter` |
| Monthly Goals | 12 | `month` |
| Weekly Goals | 5 | `week` |
| Daily Priorities | 7 | `day` |
| Milestone Planner | 2 | `record` |
| Action Plan | 3 | `record` |
| Habit Tracker | 3 | `tracker` |
| Progress Tracker | 2 | `record` |
| Obstacle Log | 2 | `record` |
| Accountability Tracker | 2 | `record` |
| Motivation Journal | 2 | `notes` |
| Success Metrics | 1 | `record` |
| Reflection Pages | 3 | `panels` |
| Lessons Learned | 2 | `panels` |
| Celebration Log | 2 | `record` |
| The Next Goal | 1 | `panels` |
| Notes | 3 | `notes` |
| Tools and Support | 1 | `record` |
| Back Cover | 1 | `cover` |

All 27 requested sections are present.

---

## Design decisions

**Three annual goal slots, not an open list.** The constraint is the product. Every downstream page assumes three, and the Read Me explains why rather than leaving the buyer to discover it.

**Obstacle log has an "Early Warning Sign" column.** Recording what could go wrong is common advice; recording how you will notice it starting is what makes the page usable. The Read Me names this as the page most people skip.

**Accountability tracker records whether the promise was kept.** A tracker that logs only what you told someone is a diary. The final column is what makes it accountability.

**Progress uses baseline, target, actual and gap.** Goal planners overwhelmingly track completion as ticks. A number without a baseline cannot show movement.

**Celebration log includes "How Long It Took".** It turns the page from sentiment into calibration data for the next goal.

**Next Goal page reads from evidence.** First panel is *What The Last Period Proved*, before the goal is named. Choosing the next goal from enthusiasm is how the previous one was chosen.

**Week includes "Time On The Goal Itself".** The goal loses to the week's work otherwise — the same pattern as *Working On The Business* in Product 001.

**Passwords omitted.** Standard §8.1.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

One blocker: the Read Me overflowed at US Letter, which is shorter than A4. Six prose blocks were merged into five. Page counts were identical across all four sizes — only the link-parity gate caught it, for the third build running.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/06-goal-planner.md`
4. Mockups
