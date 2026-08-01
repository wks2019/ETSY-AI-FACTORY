# FACTORY_PROTOCOL.md

Version: 1.0
Repository Schema: 2.0

Repository:
ETSY-AI-FACTORY

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

When two files conflict, the higher rank wins. Conflicts resolve upward, never sideways.

```
1. PROJECT_RULES.md          — hard constraints, licensing, non-negotiables
2. FACTORY_PROTOCOL.md       — loading and precedence
3. engines/DECISION_ENGINE   — how to choose
4. engines/QUALITY_ENGINE    — release authority, can veto
5. engines/ENGINE            — master coordination
6. Domain engines            — RESEARCH, DESIGN, AUTOMATION
7. systems/                  — brand, colour, typography, print, Canva, SEO
8. libraries/                — pages, layouts, components, icons
9. databases/                — evidence, never authority
```

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
SKILL_REGISTRY.md
MASTER_INSTRUCTIONS.md
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

# EXTENSION RULES

| Change | Required edit |
|---|---|
| New engine | None. Drop it in `engines/` |
| New system or library | Add a row to Task Routing |
| New database | Add to Integrity Check. Never to a load tier |
| New skill | `SKILL_REGISTRY.md` only |
| New precedence rank | This file |

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

# FINAL DIRECTIVE

Load the minimum required to be correct. Never less.

Token efficiency never justifies loading a rule partially. Completeness never justifies loading a database whole.

The protocol exists so the hundredth file costs the same to add as the tenth.
