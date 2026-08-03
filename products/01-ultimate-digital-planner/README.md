# Ultimate Digital Planner

Status: Built — awaiting Canva verification
Version: 1.1
Last Updated: 2026-08-02
Standard: none — this product predates `products/_STANDARDS/`
Collection: The Ultimate Collection — first product

---

## Build

```bash
python _ENGINE/planner_engine.py products/01-ultimate-digital-planner/spec.json
```

| Metric | Value |
|---|---|
| Pages | 42, identical across all four sizes |
| Internal links | 1,598 per file, identical across all four sizes |
| Bookmarks | 42 — one per page |
| Sizes | A4, A5, US Letter, Half Letter |
| Theme | `neutral` |
| Layouts used | 9 of 15 |
| File size | ~645 KB (A4) |

All figures re-measured from a live build on 2026-08-02. Earlier records
citing 943 links describe the v1.0 spec and are superseded.

---

## Page structure — 42 pages

| # | Section | Pages | Layout |
|---|---|---|---|
| 1 | Cover | 1 | `cover` |
| 2 | Contents | 1 | `index` |
| 3 | Year at a Glance | 1 | `year` |
| 4 | Monthly Planning | 12 | `month` |
| 5 | Weekly Planning | 5 | `week` |
| 6 | Daily Planning | 7 | `day` |
| 7 | Trackers — habit, mood, sleep | 3 | `tracker` |
| 8 | Goal Planning — annual, quarterly | 2 | `panels` |
| 9 | Finance — budget, savings | 2 | `panels` |
| 10 | Project Planning | 2 | `panels` |
| 11 | Review — monthly, quarterly | 2 | `panels` |
| 12 | Notes, Ideas, Lists | 4 | `notes` |

---

## Design decisions

**Year page uses quarter columns, not twelve mini-months.** The `year` layout
renders a 4-column × 3-row grid labelled Q1–Q4. A twelve-month miniature at A5
produces date cells too small to write in, and the page then exists only to be
looked at.

**Hour range 06:00–21:00.** Sixteen rows. This is a personal planner rather
than a work planner, so the range covers a day rather than a shift.

**Trackers at 31 columns.** Full-month width, so one page covers any month
regardless of length. Short months leave unused cells; the alternative is
month-specific pages and a twelvefold page count.

**Chips link to months from every page.** Every non-cover page carries chip
links to all twelve months, which is where the bulk of the 1,598 link
annotations comes from. It is the reason a reader can reach any month from
anywhere without returning to the index.

---

## Verification

Every engine gate passes:

- Page parity across all four sizes
- Link parity across all four sizes
- Bookmark count equals page count
- Nine WCAG contrast pairings
- Schema validation against `_SCHEMA/spec.schema.json`
- Zero literal colour values in the spec

---

## Known gaps against products 02–07

This product was built before the standard existed and is behind it in three
respects. None affect build integrity; all affect the customer's experience of
the file.

| Gap | Products 02–07 | Here |
|---|---|---|
| In-PDF Licence page | present, `prose` layout | absent |
| In-PDF Read Me page | present, `prose` layout | absent |
| Back cover | present | absent |

The delivered package now carries `README.pdf` and `LICENSE.pdf` as separate
files, so the customer is not left without terms. Folding them into the PDF
itself is a spec change of three page entries and would take the product to 45
pages.

This product also has no market research record. Products 02–07 each carry a
research summary in their README; this one was built before that step was part
of the process, and no retrospective research has been done.

---

## Outstanding before release

1. Canva import verification — manual, `engines/AUTOMATION_ENGINE.md` Stage 15
2. Physical print test
3. SEO package — `_SEO/01-ultimate-digital-planner.md`
4. Mockups — cover, desk, tablet, lifestyle, thumbnail
5. Optional: add Licence, Read Me and back cover pages to reach parity with 02–07
