# FACTORY_PROTOCOL.md

Status: Active
Version: 1.1
Repository Schema: 2.0
Last Updated: 2026-08-01
Owner: ETSY-AI-FACTORY

---

# PURPOSE

The Factory Protocol defines **how the repository is read**.

Every other file defines *what to do*. This file defines *what to load, in what order, and which rule wins when two rules disagree*.

It replaces the fixed startup sequence, the manifest, the dependency map, and the task router. One file, one source of truth.

---

# HOW THIS ACTUALLY WORKS

There is no automatic boot process. Every session starts with no repository context. Files are fetched individually through the GitHub connector.

This protocol is therefore a **routing table**, not boot logic. At the start of a task, identify the task type, look up its required resources below, and fetch only those.

Do not fetch the whole repository. Do not guess. Look it up.

---

# CONTENT CLASSES

Two kinds of content, two retrieval methods. This distinction is the core of the architecture.

| Class | Contents | Retrieval | Why |
|---|---|---|---|
| **Rules** | Engines, systems, standards, PROJECT_RULES | **Load whole file** | A rule read partially is a rule broken. Loading three relevant lines of a quality gate and skipping the threshold is worse than not loading it |
| **Facts** | Keywords, niches, competitors, market research, personas | **Search. Return matches only** | Unbounded growth. Fragments are sufficient and correct |

Never bulk-load a file in `databases/`.

---

# LOAD TIERS

| Tier | Contents | Rule |
|---|---|---|
| **0** | `FACTORY_PROTOCOL.md`, `PROJECT_RULES.md`, `SKILL_REGISTRY.md` | Always. First |
| **1** | `engines/*.md` | Load only the engines the task requires |
| **2** | `systems/*.md` | On demand, by task type |
| **3** | `libraries/*.md` | On demand, by task type |
| **4** | `databases/*.md` | **Search only. Never load whole** |

Tier 1 is discovered dynamically: list `engines/` and read what is there. Adding an engine requires no edit to this file or any other.

---

# PRECEDENCE HIERARCHY

The canonical hierarchy is defined in `PROJECT_RULES.md` §3. It is reproduced here for routing convenience only. If the two ever differ, `PROJECT_RULES.md` prevails.

| Rank | Authority | Role |
|---|---|---|
| 1 | `PROJECT_RULES.md` | Constitution of the factory |
| 2 | `FACTORY_PROTOCOL.md` | Routing, loading, integrity, conflict resolution |
| 3 | `engines/QUALITY_ENGINE.md` | Final release authority. Holds veto |
| 4 | `engines/DECISION_ENGINE.md` | Determines choices before production |
| 5 | `ENGINE.md` | Coordinates execution |
| 6 | Domain engines | Design, Research, Automation, and any future engine |
| 7 | `systems/` | Brand, typography, colour, print, Canva, SEO |
| 8 | `libraries/` | Components, layouts, icons, pages, prompts |
| 9 | `databases/` | Search-only factual information |

**Authority flows downward only. Lower-ranked documents may extend higher-ranked rules but must never contradict them. If a conflict exists, the higher-ranked document always prevails without exception.**

A failed quality audit cannot be overridden by any document ranked 4 or lower.

Two files of equal rank must not contradict each other. If they do, that is a defect — log it, do not silently pick one.

---

# TASK ROUTING

| Task | Engines | Systems | Libraries | Databases |
|---|---|---|---|---|
| **New product (full build)** | All | All | All relevant to niche | Keyword, Niche, Market |
| **Niche selection** | RESEARCH, DECISION | — | — | Niche, Market, Keyword |
| **Page/layout design** | DESIGN | DESIGN, COLOR, TYPOGRAPHY, BRAND | PAGE, LAYOUT, COMPONENT, ICON | — |
| **Cover / mockups** | DESIGN | BRAND, COLOR, TYPOGRAPHY | — | — |
| **SEO / listing copy** | RESEARCH | SEO, ETSY_OPTIMIZATION | — | Keyword, Market |
| **PDF export** | AUTOMATION | PRINT_STANDARDS, PDF_EXPORT_RULES | — | — |
| **Canva build / import check** | AUTOMATION | CANVA_STANDARDS, TYPOGRAPHY | COMPONENT | — |
| **Quality audit** | QUALITY | All standards | — | — |
| **Packaging / release** | AUTOMATION, QUALITY | — | — | — |
| **Repository maintenance** | — | — | — | — |

Tier 0 loads for every task. It is not listed per row.

If a task does not match a row, load Tier 0, state which resources you judge necessary and why, then proceed.

---

# INTEGRITY CHECK

Before starting production work, verify the expected files exist. A dynamic scan silently succeeds when a file is missing — this check is what replaces the safety of a fixed list.

**Expected at root**

```
README.md
FACTORY_PROTOCOL.md
ENGINE.md
PROJECT_RULES.md
MASTER_INSTRUCTIONS.md
SKILL_REGISTRY.md
VERSION.md
CHANGELOG.md
ROADMAP.md
```

**Expected directories**

```
engines/
systems/
libraries/
databases/
products/
_ENGINE/
_SEO/
_CANVA/
docs/
```

If a required file is missing: **report the gap explicitly and proceed without it.** Never substitute an assumption for a missing rule file.

Known gaps at Schema 2.0: `CHANGELOG.md`, `ROADMAP.md`, and all contents of `systems/`, `libraries/`, `databases/`.

---

# CONFLICT LOGGING

When two files contradict:

1. Resolve using the precedence hierarchy
2. State the conflict in the response — which files, which rule won
3. Record it in `CHANGELOG.md` under `Conflicts`
4. Fix the losing file in a follow-up commit

Silent resolution is prohibited. An unlogged conflict recurs every session.

---

# SKILL INVOCATION

Skills are resolved through `SKILL_REGISTRY.md`, never invoked from an engine's own description.

1. Task routes to an engine
2. Engine names required skills
3. Check registry status
4. **Active** → invoke. **Planned** → do the work manually and state the gap
5. Weigh registry Cost against task value before invoking

---

# DIRECTORY CONTRACT

| Path | Contains | Class |
|---|---|---|
| `/` | Operational files only — how the repo works | Rules |
| `engines/` | Production logic | Rules |
| `systems/` | Standards — design, brand, colour, type, print, Canva, SEO | Rules |
| `libraries/` | Reusable assets — pages, layouts, components, icons, prompts | Rules |
| `databases/` | Evidence — keywords, niches, market, competitors, personas | Facts |
| `products/` | One directory per product | Artifacts |
| `_ENGINE/` | Python generation code | Code |
| `_SEO/` | Listing copy per product | Artifacts |
| `_CANVA/` | Canva track notes | Artifacts |
| `docs/` | Build notes, runbooks | Docs |

`_ENGINE/` holds executable code, not documentation. It is deliberately separate from `engines/`.

---

# FILE HEADERS

Every major document carries:

```
Status: Draft | Active | Deprecated
Version: X.Y
Last Updated: YYYY-MM-DD
Owner: ETSY-AI-FACTORY
```

Apply on next edit. Do not rewrite a file solely to add a header — the cost exceeds the benefit.

---

# EXTENSION RULES

| Change | Required edit |
|---|---|
| New engine | None. Drop it in `engines/` |
| New system or library | Add a row to Task Routing |
| New database | Add to Integrity Check. Never to a load tier |
| New skill | `SKILL_REGISTRY.md` only |
| New precedence rank | `PROJECT_RULES.md` §3, then mirror here |

If a change requires editing three files, the architecture is wrong. Fix the architecture.

---

# FUTURE: RETRIEVAL LAYER

Graph or vector indexing is **deferred, not rejected**.

It applies to `databases/` only — the Facts class. Rules must continue loading whole.

Revisit when both are true:

- A database file exceeds roughly 2,000 lines and GitHub search is no longer sufficient
- A retrieval layer is actually reachable from the working environment (MCP server, local vector store, or equivalent)

Until both hold, an index would be unreachable and would add a component with no consumer.

---

# ARCHITECTURE FREEZE

Schema 2.0 is complete. Per `PROJECT_RULES.md` §14, no further structural change without evidence from real production.

The next change to this file should be caused by a problem encountered while building a product — not by a better idea.

---

# FINAL DIRECTIVE

Load the minimum required to be correct. Never less.

Token efficiency never justifies loading a rule partially. Completeness never justifies loading a database whole.

The protocol exists so the hundredth file costs the same to add as the tenth.
