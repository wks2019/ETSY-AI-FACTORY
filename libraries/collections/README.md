# collections

Status: Active
Version: 1.0
Last Updated: 2026-08-02
Owner: ETSY-AI-FACTORY

---

# RULE

**Every product category the factory creates is saved here as its own file.**

One collection, one file. Never a shared list, never inline in an engine.

```
libraries/collections/<collection-slug>.md
```

This directory is the catalogue map. A product that does not belong to a collection in this directory should not be built — `engines/RESEARCH_ENGINE.md` BRAND FIT.

---

# INDEX

| Collection | File | Products | Status |
|---|---|---|---|
| Business | [`business.md`](business.md) | 10 | Not started |

Add a row when a collection file is created. The index and the directory must always match.

---

# REQUIRED SECTIONS

Every collection file carries the same structure so they stay comparable:

| Section | Contents |
|---|---|
| Tree | The collection as a plain hierarchy |
| Members | Numbered table with per-product status |
| Collection rules | What binds these products together |
| Engine coverage | Which renderer page types each product needs, and what is missing |
| Build order | Sequence, with the reason for the first and last entries |
| Prerequisites | What must exist before the first product starts |

Engine coverage is the section that matters most. It separates products that are a spec file from products that need renderer work, which is the difference between a day and a week.

---

# COLLECTION RULES

Applies to every collection in this directory.

- One palette, one type pairing, one component set across all members
- Each member recognisable as belonging, without reading the title
- Each member stands alone as a purchase
- Each member cross-sells at least two others
- Shared page types use the same architecture across members
- The bundle offers clear value over buying members individually

---

# CREATING A COLLECTION

1. Create `libraries/collections/<slug>.md` using the required sections
2. Add a row to the index above
3. Map every member against the current renderer before committing to a build order
4. Confirm the required `systems/` files exist — without them members drift and the collection stops being one

Define a collection only when its anchor product is ready to build. A directory of unbuilt collections is the same failure as a repository of unused governance documents.
