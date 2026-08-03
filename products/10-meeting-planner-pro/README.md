# Meeting Planner Pro

Status: Built — catalogue decision required before listing
Version: 1.0
Last Updated: 2026-08-03
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business Productivity Bundle — 011

---

## Read this before listing

This product overlaps `products/05-meeting-planner`, which shipped on
2026-08-02 at 77 pages. The overlap was flagged before the build and the build
was authorised anyway. That decision is recorded here so nobody later assumes
it was an oversight.

**Nothing about this product is broken. The risk is commercial, not
technical.** Two Meeting Planner listings in the same shop compete for the same
search terms, split their own ranking, and expose the shop to buyers who
purchase both and find them close.

Before either goes live, choose one:

1. **Retitle and re-angle both.** 05 becomes the meeting-type template library;
   this becomes the accountability system. The distinction must appear in the
   first two lines of both descriptions, not paragraph four.
2. **Delist 05 and treat this as its replacement.** Cleanest, but 05 has eight
   meeting types this product does not carry.
3. **Merge.** One larger product built from both specs. Costs a rebuild.

Recorded as the first outstanding item in `manifest.json`.

---

## What 05 has that this does not

Board meeting minutes with quorum and resolutions · Workshop template ·
Training session template · Video call template · Communication log ·
Recurring meeting audit with hours-per-month · Rooms and tools register ·
Meeting KPI review · Twelve named month pages · Quarterly decision planning.

## What this has that 05 does not

| Page | Why it was missing from 05 |
|---|---|
| Daily Meeting Planner | 05 goes year → quarter → month → week and stops |
| Team Meeting Log | 05 covers project, client, one-to-one, board, video — no standing team meeting |
| Responsibility Assignment | No RACI anywhere in 05; owner is a single column on the action tracker |
| Deadline Tracker | Dates live inside the action tracker; nothing collects hard deadlines across meetings |
| Meeting Objectives | The objective is one panel on the agenda page, written in the room rather than before it |
| Reflection | 05 has no post-meeting reflection |
| Weekly Review | 05 reviews monthly via the KPI page |
| Meeting Planning Guide | 05 carries the guidance inside Read Me |

Pages shared with 05 are held to one or two each so the weight sits on the
gaps.

---

## Build

```bash
python _ENGINE/planner_engine.py products/10-meeting-planner-pro/spec.json
```

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,724 per file, identical across all four sizes |
| Bookmarks | 70 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 10 of 15, all existing. No new renderer |
| Slug | `meeting-planner-pro` — 05 owns `meeting-planner` |

### Slug

The slug drives PDF and ZIP filenames. Reusing `meeting-planner` would have
shipped two different products whose files are all named
`meeting-planner-a4.pdf` and `meeting-planner.zip`. A customer holding both
could not tell them apart in a downloads folder, and neither could support.

---

## Page structure — 70 pages

| Section | Pages | Layout |
|---|---|---|
| Cover / Back Cover | 2 | `cover` |
| Welcome | 1 | `prose` |
| Licence | 1 | `prose` |
| Instructions | 1 | `prose` |
| Meeting Planning Guide | 1 | `prose` |
| Contents × 3 | 3 | `index` |
| Annual Meeting Overview | 1 | `year` |
| Monthly Meeting Planner | 3 | `month` |
| Weekly Meeting Schedule | 3 | `week` |
| Daily Meeting Planner | 5 | `panels` |
| Meeting Objectives | 3 | `panels` |
| Meeting Agenda Template | 3 | `agenda` |
| Attendee List | 2 | `record` |
| Preparation Checklist | 2 | `record` |
| Discussion Topics | 2 | `record` |
| Notes Pages | 2 | `notes` |
| Decision Log | 2 | `record` |
| Action Items Tracker | 3 | `record` |
| Responsibility Assignment | 3 | `record` |
| Deadline Tracker | 3 | `record` |
| Follow-up Planner | 2 | `record` |
| Client Meeting Log | 2 | `agenda` |
| Team Meeting Log | 4 | `agenda` |
| One-to-One Meeting Notes | 2 | `agenda` |
| Project Meeting Notes | 2 | `agenda` |
| Brainstorm Session | 2 | `notes` |
| Reflection | 3 | `panels` |
| Weekly Review | 3 | `panels` |
| Progress Dashboard | 2 | `record` |
| Notes | 2 | `notes` |

All 29 requested sections are present.

---

## Design decisions

**The trackers are the product.** Agenda, team, client and project pages all
carry an `On Tracker` column in their action table rather than `Done`. The
question at the end of a meeting is not whether the action is finished — it is
whether it has been moved somewhere it will be chased.

**One name in the Accountable column.** The RACI page carries a notice saying
so. Two names in that column is the single most common cause of a missed
deliverable, and the page is worthless if it lets you record the problem it
exists to prevent.

**The Deadline Tracker has a Chase On column before the Hard Deadline column.**
Deliberate ordering. Chasing after the date has passed is not follow-up.

**The Team Meeting Log opens with last week's actions.** First panel, before
blockers, before anything new. A standing team meeting that does not start
there becomes a status round.

**The Weekly Review counts actions closed, not meetings held.** So does the
Progress Dashboard: meetings, hours, opened, closed, overdue. A full calendar
and a full backlog is the pattern worth surfacing.

**The Daily Meeting Planner asks which meeting could be declined.** Every day.
It is the only page in either meeting product that pushes back on the calendar.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` — schema | pass (after label fix) |
| `validate_spec` — dead nav tab targets | 0 |
| `validate_spec` — literal colours | 0 |
| Duplicate page ids | 0 |
| Page parity across four sizes | 70 / 70 / 70 / 70 |
| Link parity across four sizes | 1,724 × 4 (after agenda fix) |
| Bookmark parity | 70 per file |
| Dead internal link targets | 0 of 924 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast pairings | 9 checked, 0 failures |
| Archive extraction test | passed — 9 entries |

### Two defects found during the build

**1. Panel label over cap.** `Objective, Copied From The Objectives Page` was
42 characters against a 40-character schema limit. Caught by `validate_spec`
before rendering. Shortened.

**2. Link parity failed at US Letter — 1,718 against 1,724.** Isolated by
counting link annotations per page across both files: pages 24, 25 and 26, the
three agenda pages, each lost two links. US Letter is 17.6mm shorter than A4 at
the same type scale, and the chip row at the foot of the agenda page fell off
the bottom. Page count and bookmark count both still passed — only the link
parity gate caught it.

Fixed at spec level by reducing agenda density from `lines` 5 / `rows` 7 to
`lines` 4 / `rows` 6. No engine change. This is the second time a page carrying
four panels plus a notes block plus an action table has failed at US Letter
(product 05 hit it on the one-to-one page), which is worth remembering when
using the `agenda` renderer: four panels is the practical ceiling if the page
also carries chips.

Visual spot-checks at US Letter, the binding size here: the fixed agenda page
and the six-column Responsibility Assignment page with its notice. Both fit
with margin.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

**Tablet size.** Engine v2.1 defines four sizes in `_ENGINE/assets.py` and has
no tablet entry. A5 and Half Letter ship as the tablet-appropriate sizes.
Unchanged since product 08.

---

## Outstanding before release

1. **Catalogue decision on 05 versus this product** — blocking
2. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
3. Physical print test
4. SEO package — `_SEO/10-meeting-planner-pro.md`, keyword-separated from 05
5. Mockups, visually distinct from 05
