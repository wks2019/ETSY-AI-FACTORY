# Business Productivity Bundle

Status: Active — 5 of 20 built
Version: 2.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY

Supersedes the 10-product Business Collection defined in v1.0.

---

# TREE

```
Business Productivity Bundle
│
├── 001 Business Productivity Planner
├── 002 CEO Planner
├── 003 Project Planner
├── 004 Meeting Planner
├── 005 Goal Planner
├── 006 Weekly Productivity Planner
├── 007 Daily Productivity Planner
├── 008 Time Blocking Planner
├── 009 Focus Planner
├── 010 Deep Work Planner
├── 011 Business Dashboard Planner
├── 012 Client Management Planner
├── 013 Invoice & Payment Tracker
├── 014 KPI & Business Analytics Planner
├── 015 Business Operations Planner
├── 016 Business Startup Planner
├── 017 Business Strategy Planner
├── 018 Marketing Campaign Planner
├── 019 Content Creator Planner
└── 020 Social Media Planner
```

The Bundle itself is a twenty-first listing, priced below the sum of its members.

---

# MEMBERS

| # | Product | Directory | Pages | Status |
|---|---|---|---|---|
| 001 | Business Productivity Planner | `products/02-business-productivity-planner/` | 58 | **Built** — unlisted |
| 002 | CEO Planner | `products/03-ceo-planner/` | 78 | **Built** — unlisted |
| 003 | Project Planner | `products/04-project-planner/` | 70 | **Built** — unlisted |
| 004 | Meeting Planner | `products/05-meeting-planner/` | 77 | **Built** — unlisted |
| 005 | Goal Planner | `products/06-goal-planner/` | 71 | **Built** — unlisted |
| 006 | Weekly Productivity Planner | — | — | Not started |
| 007 | Daily Productivity Planner | — | — | Not started |
| 008 | Time Blocking Planner | — | — | Not started |
| 009 | Focus Planner | — | — | Not started |
| 010 | Deep Work Planner | — | — | Not started |
| 011 | Business Dashboard Planner | — | — | Not started |
| 012 | Client Management Planner | — | — | Not started |
| 013 | Invoice & Payment Tracker | — | — | Not started |
| 014 | KPI & Business Analytics Planner | — | — | Not started |
| 015 | Business Operations Planner | — | — | Not started |
| 016 | Business Startup Planner | — | — | Not started |
| 017 | Business Strategy Planner | — | — | Not started |
| 018 | Marketing Campaign Planner | — | — | Not started |
| 019 | Content Creator Planner | — | — | Not started |
| 020 | Social Media Planner | — | — | Not started |

**Built total: 354 pages across five products. Listed: none.**

## Numbering note

Bundle numbers and repository directory numbers are offset by one, because
`products/01-ultimate-digital-planner/` belongs to a different collection.
Bundle 001 is directory 02, and so on. The offset is deliberate; the
directory number orders the catalogue, the bundle number orders the
collection.

---

# ENGINE COVERAGE

All fifteen remaining products build on the existing fifteen renderers. **No
new renderer is required to complete this collection.**

| # | Product | Primary layouts |
|---|---|---|
| 006 | Weekly Productivity | `week` `day` `panels` `tracker` |
| 007 | Daily Productivity | `day` `panels` `tracker` |
| 008 | Time Blocking | `day` `panels` |
| 009 | Focus Planner | `day` `panels` `tracker` |
| 010 | Deep Work | `day` `tracker` `panels` `record` |
| 011 | Business Dashboard | `record` `ledger` |
| 012 | Client Management | `record` `agenda` `timeline` |
| 013 | Invoice & Payment | `ledger` `record` |
| 014 | KPI & Analytics | `record` `ledger` `panels` |
| 015 | Business Operations | `record` `panels` `timeline` |
| 016 | Business Startup | `panels` `record` `timeline` `ledger` |
| 017 | Business Strategy | `panels` `quarter` `record` |
| 018 | Marketing Campaign | `timeline` `record` `panels` `month` |
| 019 | Content Creator | `month` `record` `timeline` `notes` |
| 020 | Social Media | `month` `record` `tracker` `panels` |

This is the payoff from the six renderers built during the engine upgrade.
Every remaining product is a spec file.

---

# OVERLAP RISK

Products 006–010 are five variations on the same underlying idea — planning
and protecting personal working time. They share `day`, `panels` and
`tracker` almost entirely.

They must be differentiated by **method**, not by page count:

| Product | The distinct method |
|---|---|
| 006 Weekly Productivity | The week as the unit of planning |
| 007 Daily Productivity | The day, executed |
| 008 Time Blocking | Calendar-first — every task gets a slot |
| 009 Focus Planner | Attention management — interruptions, energy, context switching |
| 010 Deep Work | Long uninterrupted sessions, tracked and defended |

If two of these end up with the same page list under different covers, they
are one product sold twice, and the collection rule in
`libraries/collections/README.md` is broken. Decide the method before the
spec, not during it.

The same applies to 011 vs 014 (dashboard vs analytics) and 015 vs 017
(operations vs strategy).

---

# COLLECTION RULES

Inherits `libraries/collections/README.md`.

Collection-specific:

- Tone is professional, not decorative. This customer buys a tool
- Every tracker legible when printed at A5
- Financial pages carry no currency symbol — the collection sells internationally
- No passwords page in any member — `BUSINESS_PLANNER_STANDARD.md` §8.1
- `neutral` theme by default; `slate` reserved for executive-tier products

---

# BUILD ORDER

The first five are done. Remaining order prioritises products that are
distinct from what already exists over products that are variations.

| Phase | Products | Reason |
|---|---|---|
| **Validate** | 001–005 | Five built, none listed. Canva import is unverified across all five — if it degrades, five products need rework |
| A | 013, 011, 014 | Financial and metric products. Distinct from everything built. Strong standalone search demand |
| B | 012, 016, 017 | Client, startup, strategy. Distinct customers |
| C | 019, 020, 018 | Content and marketing. A different buyer from the rest of the collection |
| D | 006–010 | Productivity variants. Build last, once the method for each is decided — highest overlap risk |
| E | Bundle | Requires all twenty |

---

# PREREQUISITES

| Requirement | Status |
|---|---|
| `systems/BRAND_SYSTEM.md` | ✅ |
| `systems/COLOR_SYSTEM.md` | ✅ |
| `systems/TYPOGRAPHY_SYSTEM.md` | ✅ |
| Engine and schema | ✅ Stable across five builds, zero modifications |
| Canva import verified | ❌ **Blocks every listing** |
| Print test | ❌ |
| SEO packages | ❌ 0 of 5 |
| Mockups | ❌ 0 of 5 |

The bundle cannot be listed until all twenty members exist. The five built
members can be listed individually as soon as validation clears.
