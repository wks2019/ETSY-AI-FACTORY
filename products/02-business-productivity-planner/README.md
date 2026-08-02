# Business Productivity Planner

Status: Built — awaiting Canva verification
Version: 1.0
Last Updated: 2026-08-02
Standard: `products/_STANDARDS/BUSINESS_PLANNER_STANDARD.md` 1.0
Collection: Business — anchor product

---

## Build

```bash
python _ENGINE/planner_engine.py products/02-business-productivity-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 58, identical across all four sizes |
| Internal links | 1,880 per file, identical across all four sizes |
| Bookmarks | 58 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | All 15 |
| File size | ~772 KB (A4) |

---

## Product research summary

Market scan of leading Etsy business and digital planners, August 2026.

**What the market does**

- Business planners are typically a flat list of trackers — one listing advertises twenty independent sections with no relationship between them
- Most competitors are dated, forcing an annual reprint and an annual repurchase
- Almost all are optimised for one medium. Digital-first files print cramped; print-first files navigate badly
- Etsy-seller planners dominate the "business planner" tag, crowding out the general small-business buyer
- Password and website trackers appear routinely, in files that get synced and printed

**Documented buyer complaints**

- Note and writing space too small — the most common criticism in reviews
- Layouts optimised for digital "look cramped or awkwardly spaced" when printed
- Confusion between an app's read mode and write mode, which makes links appear broken
- Products that turn out to be a plain PDF when the listing implied an application

**Gaps this product targets**

| Gap | Response |
|---|---|
| No quarterly layer — planners jump from year to month | Four dedicated quarter pages with an objective and a stated non-goal |
| Meetings recorded as free notes with no accountability | Action table carrying Owner, By When and Done |
| Trackers with no relationship to each other | Year → quarter → month → week → day → review, one continuous chain |
| Projects with no time dimension | Twelve-week timeline grid per project |
| Cramped writing space | 19pt line spacing at reference scale, enforced by the engine |
| Print or digital, rarely both | Four sizes from one source, verified page and link parity |
| Dated products expiring each year | Undated. Sells indefinitely |
| Password pages in a synced file | Omitted. The tools page carries an explicit caution instead |

**Differentiation stated for the listing**

1. A planning chain, not a folder of trackers
2. Quarterly planning, which most competitors skip entirely
3. Meeting actions with an owner and a date
4. 1,880 working links and a complete bookmark outline
5. Four sizes, genuine print and digital parity
6. Undated — buy once

No competitor design, wording or layout was copied. All page content is original.

---

## Page structure — 58 pages

| # | Section | Pages | Layout |
|---|---|---|---|
| 1 | Cover | 1 | `cover` |
| 2 | Licence | 1 | `prose` |
| 3 | Read Me | 1 | `prose` |
| 4 | Contents | 1 | `index` |
| 5 | The Year | 1 | `year` |
| 6 | Quarter Planning | 4 | `quarter` |
| 7 | Monthly Planning | 12 | `month` |
| 8 | Weekly Planning | 5 | `week` |
| 9 | Daily Planning | 7 | `day` |
| 10 | Meeting Notes | 4 | `agenda` |
| 11 | Project Timelines | 4 | `timeline` |
| 12 | Goal Planning | 2 | `panels` |
| 13 | Habit Tracking | 2 | `tracker` |
| 14 | Expense Tracking | 3 | `ledger` |
| 15 | Notes and Ideas | 4 | `notes` |
| 16 | Contacts | 2 | `record` |
| 17 | Tools and Subscriptions | 1 | `record` |
| 18 | Review | 2 | `panels` |
| 19 | Back Cover | 1 | `cover` |

---

## Design decisions

**Passwords page omitted.** The standard makes it conditional (§8.1). A planner sold to business owners invites them to record client and banking credentials into a file that is synced, printed and left on desks. The tools page carries a printed caution instead.

**No currency symbol.** The product sells internationally. A symbol halves the addressable market and a symbol chooser is a support burden.

**Seven-day week with two named differently.** Five weekdays, one weekend block, and one block labelled *Working On The Business* — the work that gets displaced by client work every week.

**Expense columns include Tax and Receipt.** Recording tax at entry and marking whether a receipt is held is what makes the page usable at year end rather than a second reconstruction job.

**Quarter pages state a non-goal.** *What I Will Not Do This Quarter* is the field most likely to change behaviour, and the one no competitor includes.

**Hour range 07:00–19:00.** A working day, not a life. Thirteen rows leaves room for the priority panels beside them.

---

## Verification

Every engine gate passes:

- Page parity across all four sizes
- Link parity across all four sizes
- Bookmark count equals page count
- Nine WCAG contrast pairings
- Schema validation
- Zero literal colour values in the spec

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test of the six page types new to this product
3. SEO package — `_SEO/02-business-productivity-planner.md`
4. Mockups — cover, desk, tablet, lifestyle, thumbnail
