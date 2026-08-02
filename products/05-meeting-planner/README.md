# Meeting Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business — meeting management product

---

## Build

```bash
python _ENGINE/planner_engine.py products/05-meeting-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 77, identical across all four sizes |
| Internal links | 2,132 per file, identical across all four sizes |
| Bookmarks | 77 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 8 of 15, all existing. No new renderer |
| File size | ~878 KB (A4) |

---

## Product research summary

Market scan, August 2026.

**What the market sells**

The meeting category is dominated by **single templates, not planners**. Listings are typically one meeting-minutes sheet offered in a few orientations — portrait, landscape, two-page — or an editable Word or Google Docs file. The largest bundle found was 20 pages covering preparation, agenda, notes, voting, action plan and summary.

**Strengths worth respecting**

- Editability. Word and Google Docs versions let buyers change field names, which a PDF cannot
- Prompts on the template. One review specifically credits prompts and a worked example for making minute-taking easier
- Multiple print sizes are standard in this category — A4, A5, Letter and Half Letter appear routinely
- Reviews are strong and specific: buyers use these weekly and rebuy from the same shop

**What is missing everywhere**

| Gap | Consequence |
|---|---|
| Actions live at the foot of each meeting's notes page | Nobody re-reads twelve notes pages to find what was owed |
| No cross-meeting action tracker | Accountability dies between meetings, which is where meetings actually fail |
| One generic template for every meeting type | A board meeting, a one-to-one and a brainstorm need different pages |
| No meeting calendar or schedule | Templates record meetings; they never help you hold fewer |
| No recurring-meeting review | Standing meetings are never audited out of existence |
| Decisions recorded as outcomes without reasoning | Six months later the reasoning is the part that matters |

**The opportunity**

A meeting *system* rather than a meeting *template*. The category competes on how well a single sheet captures one meeting. This product competes on what happens between meetings — the action tracker, the follow-up planner, and the recurring-meeting audit.

That position is stated in the Read Me, which explains plainly why the action tracker is a separate section rather than a footer block.

**Differentiation for the listing**

1. Cross-meeting action tracker — every action from every meeting in one place
2. Follow-up planner recording what was chased and when to chase again
3. Eight meeting types, each with its own page: agenda, project, client, one-to-one, board, brainstorm, workshop, training, video
4. Recurring meeting tracker with hours per month and a *Still Needed* column
5. Meeting Review page — what your meetings cost and return
6. Year, quarter, month and week scheduling, absent across the category
7. 2,132 working links across 77 pages, four sizes
8. Undated — buy once

No competitor design, wording or layout was copied.

---

## Page structure — 77 pages

| Section | Pages | Layout |
|---|---|---|
| Cover | 1 | `cover` |
| Licence | 1 | `prose` |
| Read Me | 1 | `prose` |
| Contents — plan and prepare | 1 | `index` |
| Contents — record and follow up | 1 | `index` |
| Meeting Dashboard | 1 | `record` |
| The Meeting Year | 1 | `year` |
| Quarterly Meeting Planner | 4 | `quarter` |
| Monthly Meeting Calendar | 12 | `month` |
| Weekly Meeting Schedule | 5 | `week` |
| Preparation Checklist | 2 | `record` |
| Meeting Agenda | 6 | `agenda` |
| Attendee Register | 2 | `record` |
| Meeting Notes | 3 | `notes` |
| Discussion Log | 2 | `record` |
| Decision Log | 2 | `record` |
| Action Item Tracker | 3 | `record` |
| Follow-up Planner | 2 | `record` |
| Project Meeting Notes | 2 | `agenda` |
| Client Meeting Notes | 2 | `agenda` |
| One-to-One Meeting Notes | 3 | `agenda` |
| Board Meeting Notes | 2 | `agenda` |
| Brainstorm Session Notes | 2 | `notes` |
| Workshop Notes | 2 | `panels` |
| Training Session Notes | 2 | `panels` |
| Video Conference Notes | 2 | `agenda` |
| Recurring Meeting Tracker | 2 | `record` |
| Meeting Review | 1 | `record` |
| Communication Log | 2 | `record` |
| Notes | 3 | `notes` |
| Tools and Rooms | 1 | `record` |
| Back Cover | 1 | `cover` |

All 30 requested sections are present.

---

## Design decisions

**The action tracker is a separate section, not a footer.** This is the product's central argument. Every meeting page still carries its own action table, but every action also lands in a tracker carrying *From Which Meeting*. The Read Me explains why, because the buyer needs to understand the difference before they judge the product against a cheaper single template.

**Eight distinct meeting types.** A board meeting needs quorum, apologies and papers circulated. A one-to-one needs their agenda first. A client meeting needs what was committed. A video call needs who was silent — the failure mode specific to remote meetings. One generic sheet serves none of these well.

**One-to-one puts their agenda first, literally.** The panel is labelled *Their Agenda, Discussed First*. A one-to-one that opens with the manager's list is a status update wearing a different name.

**Board actions column reads "Carried".** Board resolutions are proposed and carried, not assigned and completed. Using the wrong vocabulary on that page would signal the product was never used in a real board meeting.

**Recurring tracker has "Hours Per Month" and "Still Needed".** A standing meeting is the most expensive thing on a calendar and the least often questioned. Costing it in hours is what makes cancelling it possible.

**Week includes "Meeting-Free Time".** Scheduling the gaps is the only way they survive.

**Passwords omitted; dial-in codes explicitly named.** Standard §8.1. The Tools and Rooms caution names meeting PINs and dial-in codes specifically, because those are the credentials a meeting planner actually invites.

---

## Engine reuse

No engine modification. No schema modification. No new renderers.

One blocker found and resolved at spec level: the one-to-one page overflowed at US Letter, which is shorter than A4. Panel content was trimmed until page and link parity held across all four sizes. The link-parity gate added during the Product 001 build caught the second, subtler failure — equal page counts with six links missing.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/05-meeting-planner.md`
4. Mockups
