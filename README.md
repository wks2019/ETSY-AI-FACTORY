# ETSY-AI-FACTORY

A production system for premium digital products sold on Etsy.

The repository is not documentation about a process — it *is* the process. Every rule, standard, and reusable asset lives here. Nothing authoritative exists outside it.

**Factory Version 1.0.0 · Repository Schema 2.0**

---

## Start here

| Order | File | Purpose |
|---|---|---|
| 1 | [`FACTORY_PROTOCOL.md`](FACTORY_PROTOCOL.md) | **How to read this repository.** Load tiers, precedence, task routing, integrity checks |
| 2 | [`PROJECT_RULES.md`](PROJECT_RULES.md) | Hard constraints. Highest precedence |
| 3 | [`MASTER_INSTRUCTIONS.md`](MASTER_INSTRUCTIONS.md) | Operating model and mission |
| 4 | [`SKILL_REGISTRY.md`](SKILL_REGISTRY.md) | Every skill, its status, cost, and trigger |
| 5 | [`ENGINE.md`](ENGINE.md) | Master coordinator |

Do not load the whole repository. Identify the task, look it up in the Task Routing table, load only what it requires.

---

## Structure

```
/                    operational files — how the repo works
engines/             production logic
systems/             standards — design, brand, colour, type, print, Canva, SEO
libraries/           reusable assets — pages, layouts, components, icons, prompts
databases/           evidence — keywords, niches, market, competitors, personas
products/            one directory per product
_ENGINE/             Python generation code
_SEO/                listing copy per product
_CANVA/              Canva track notes
docs/                build notes and runbooks
```

`_ENGINE/` holds executable code. `engines/` holds rules. They are deliberately separate.

---

## Engines

| Engine | Responsibility |
|---|---|
| [`DECISION_ENGINE`](engines/DECISION_ENGINE.md) | How to choose between valid options |
| [`RESEARCH_ENGINE`](engines/RESEARCH_ENGINE.md) | What to build and why |
| [`DESIGN_ENGINE`](engines/DESIGN_ENGINE.md) | Visual identity and perceived value |
| [`AUTOMATION_ENGINE`](engines/AUTOMATION_ENGINE.md) | The 20-stage production pipeline |
| [`QUALITY_ENGINE`](engines/QUALITY_ENGINE.md) | Release authority. Can veto |

Engines are discovered dynamically. Adding one requires no edit elsewhere.

---

## Two content classes

The distinction that keeps context usage low as the repository grows:

| Class | Where | Retrieval |
|---|---|---|
| **Rules** | root, `engines/`, `systems/`, `libraries/` | Load the whole file. A partially-read rule is a broken rule |
| **Facts** | `databases/` | Search. Return matches only. **Never bulk-load** |

---

## Production workflow

```
Research → Keywords → Architecture → Page Planning → Design
→ Vector PDF → Canva import → Quality review → Canva template
→ SEO → Mockups → Packaging → Quality Audit → Ready for Sale
```

PDF-first is mandatory. Minimum release score: **95/100**.

Full detail in [`engines/AUTOMATION_ENGINE.md`](engines/AUTOMATION_ENGINE.md).

---

## Current state

| Area | Status |
|---|---|
| Architecture | Schema 2.0 complete |
| Engines | 5 live |
| Systems | Not yet written |
| Libraries | Not yet written |
| Databases | Not yet populated |
| Skills | 2 active, 18 planned |
| Products | 1 shipped, 19 remaining |

**Product 1 — Ultimate Digital Planner:** 42 undated pages, four sizes, 943 internal links, 42 bookmarks.

---

## Governing principle

> The purpose of this repository is to produce sellable products. Architecture exists to support production. Do not redesign the factory without evidence from real production.

Ship products. Learn. Improve. Repeat.
