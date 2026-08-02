# COLLECTION_LIBRARY.md

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY

---

# PURPOSE

Defines product collections — groups of products that share a brand identity, a customer, and a bundle path.

A collection is not a list of ideas. It is a planned catalogue segment where every product cross-sells the others.

---

# BUSINESS COLLECTION

```
Business Collection
│
├── Business Planner
├── Project Planner
├── KPI Tracker
├── Meeting Planner
├── Client Tracker
├── Invoice Tracker
├── CRM Tracker
├── Goal Planner
├── Productivity Planner
└── Business Bundle
```

## Members

| # | Product | Status |
|---|---|---|
| 1 | Business Planner | Not started |
| 2 | Project Planner | Not started |
| 3 | KPI Tracker | Not started |
| 4 | Meeting Planner | Not started |
| 5 | Client Tracker | Not started |
| 6 | Invoice Tracker | Not started |
| 7 | CRM Tracker | Not started |
| 8 | Goal Planner | Not started |
| 9 | Productivity Planner | Not started |
| 10 | Business Bundle | Not started — requires 1–9 |

The Bundle is the commercial objective. The nine individual products are both standalone listings and the bundle's contents.

---

# COLLECTION RULES

Every product in a collection must:

- Share one palette, one type pairing, and one component set
- Be recognisable as a member on sight, without reading the title
- Stand alone as a purchase — a collection member is not a fragment
- Cross-sell at least two other members
- Use the same page architecture where the page type is shared

The Bundle must offer clear value over buying members individually. `engines/RESEARCH_ENGINE.md` BUNDLE ENGINE.

---

# ENGINE COVERAGE

Which existing renderer page types each product needs, and what is missing.

| Product | Covered by | New page type required |
|---|---|---|
| Business Planner | index, year, month, week, day, panels | — |
| Project Planner | index, panels, tracker | Gantt / timeline |
| KPI Tracker | index, tracker, panels | Numeric entry grid |
| Meeting Planner | index, panels, lines | Agenda / action-item split |
| Client Tracker | index, tracker, panels | Record card |
| Invoice Tracker | index, tracker | Ledger row with totals |
| CRM Tracker | index, tracker, panels | Pipeline stage columns |
| Goal Planner | index, panels, tracker | — |
| Productivity Planner | index, week, day, tracker, panels | — |
| Business Bundle | all of the above | — |

Three products — Business Planner, Goal Planner, Productivity Planner — need **no new renderer code**. They are spec files only.

The remaining six each need one new page type in `_ENGINE/layout_renderer.py`. Once written, a page type is permanently reusable across every future product.

---

# BUILD ORDER

Build the three zero-code products first. They validate the shared brand system before any renderer work is committed.

1. Business Planner — anchor product, defines the collection's look
2. Productivity Planner — reuses the anchor's components
3. Goal Planner — reuses the anchor's components
4. Meeting Planner — first new page type
5. Project Planner
6. Client Tracker
7. CRM Tracker
8. Invoice Tracker
9. KPI Tracker
10. Business Bundle — last. Requires all nine

---

# PREREQUISITE

This collection cannot start until `systems/BRAND_SYSTEM.md`, `COLOR_SYSTEM.md`, and `TYPOGRAPHY_SYSTEM.md` exist.

Without them the anchor product's palette and typography are hardcoded in its spec, and the other nine have nothing to inherit — which is exactly how a collection stops looking like a collection.

---

# FUTURE COLLECTIONS

Not yet defined. Candidates from `engines/DECISION_ENGINE.md` niche priority:

Wedding Collection · Home & Life Collection · Health & Fitness Collection · Student & Teacher Collection

Define a collection only when its anchor product is ready to build.
