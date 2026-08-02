# collections

Status: Active
Version: 1.1
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

| Collection | File | Products | Built | Listed |
|---|---|---|---|---|
| Business Productivity Bundle | [`business.md`](business.md) | 20 | 5 | 0 |

Add a row when a collection file is created. The index and the directory must always match.

---

# REQUIRED SECTIONS

Every collection file carries the same structure so they stay comparable:

| Section | Contents |
|---|---|
| Tree | The collection as a plain hierarchy |
| Members | Numbered table with directory, page count and per-product status |
| Collection rules | What binds these products together |
| Engine coverage | Which renderer page types each product needs, and what is missing |
| Overlap risk | Members that could collapse into each other, and what distinguishes them |
| Build order | Sequence, with the reason for the first and last entries |
| Prerequisites | What must exist before the next product starts |

Engine coverage separates products that are a spec file from products that need renderer work. Overlap risk is what stops a collection becoming one product sold under several covers.

---

# COLLECTION RULES

Applies to every collection in this directory.

- One palette, one type pairing, one component set across all members
- Each member recognisable as belonging, without reading the title
- Each member stands alone as a purchase
- Each member cross-sells at least two others
- **Each member differs by method, not only by cover and title**
- Shared page types use the same architecture across members
- The bundle offers clear value over buying members individually

---

# CREATING A COLLECTION

1. Create `libraries/collections/<slug>.md` using the required sections
2. Add a row to the index above
3. Map every member against the current renderer before committing to a build order
4. Identify overlap risk before the first spec is written
5. Confirm the required `systems/` files exist

Define a collection only when its anchor product is ready to build. A directory of unbuilt collections is the same failure as a repository of unused governance documents.

---

# SUPERSEDING A COLLECTION

A collection may be redefined. When it is:

- Increment the version in the collection file
- State plainly what it supersedes
- Preserve the status of members already built — a rewritten list does not unbuild anything
- Update the index row
