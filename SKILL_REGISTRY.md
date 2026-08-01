# SKILL_REGISTRY.md

Version: 1.0

Repository:
ETSY-AI-FACTORY

---

# PURPOSE

The Skill Registry is the single source of truth for every custom Claude skill used by the factory.

Engines reference this registry. Engines never define skills themselves.

This keeps skill definitions in one place, prevents drift between engines, and makes the skill set extensible without editing every engine file.

---

# STATUS LEGEND

| Status | Meaning |
|---|---|
| **Active** | Skill file exists and is invocable now |
| **Planned** | Specified but not yet built. Do not invoke |
| **Deprecated** | Superseded. Do not invoke |

**Rule:** Before invoking any skill, confirm its status here. Never invoke a Planned skill. If an engine requires a Planned skill, perform the work manually and note the gap.

---

# REGISTRY SCHEMA

Every entry defines:

| Field | Description |
|---|---|
| Name | Skill identifier, kebab-case |
| Status | Active / Planned / Deprecated |
| Priority | Critical / High / Medium |
| Purpose | What it does, one line |
| Invoke when | The trigger condition |
| Inputs | What it needs to run |
| Outputs | What it returns |
| Used by | Which engines call it |
| Depends on | Prerequisite skills or files |
| Success criteria | How to tell it worked |

---

# ACTIVE SKILLS

## banana-pro-director

| Field | Value |
|---|---|
| Status | **Active** |
| Priority | Critical |
| Purpose | Creative direction and premium visual review |
| Invoke when | Any cover, page layout, or visual asset is designed or reviewed |
| Inputs | Design brief, brand context, target niche, existing page or concept |
| Outputs | Prompt or direction with fixed composition, lighting, camera, palette, branding |
| Used by | DESIGN_ENGINE, AUTOMATION_ENGINE (Stage 8), QUALITY_ENGINE |
| Depends on | BRAND_SYSTEM.md, COLOR_SYSTEM.md, TYPOGRAPHY_SYSTEM.md |
| Success criteria | Output reads as premium, hierarchy is clear, nothing decorative survives without purpose |

Responsible for creative direction, not production.

---

## cinema-world-builder

| Field | Value |
|---|---|
| Status | **Active** |
| Priority | Critical |
| Purpose | Cohesive visual identity and brand storytelling across a set of assets |
| Invoke when | Building a collection, a bundle, or a new brand direction — anywhere multiple images must share one identity |
| Inputs | Brand context, niche, mood target, asset list |
| Outputs | Locked visual world: style, atmosphere, palette, recurring motifs |
| Used by | DESIGN_ENGINE, RESEARCH_ENGINE (product expansion) |
| Depends on | BRAND_SYSTEM.md |
| Success criteria | Every asset in the set is recognisably from the same world without repeating |

Use especially for collections, bundles, wedding products, luxury planners, and brand development.

---

# PLANNED SKILLS — CRITICAL

Build these first. Each directly gates revenue or release.

| Name | Purpose | Invoke when | Used by |
|---|---|---|---|
| `etsy-seo-master` | Titles, descriptions, 13 tags, keyword strategy, bundles | Stage 16, any listing copy | AUTOMATION, RESEARCH, QUALITY |
| `market-research-analyst` | Competitor analysis, trends, pricing, opportunity scoring | Stages 1–2, any new niche | RESEARCH, DECISION |
| `canva-production-expert` | Native Canva optimisation and editability validation | Stage 15, before any export | AUTOMATION, QUALITY, DESIGN |
| `print-production-master` | PDF quality, margins, bleed, print validation | Stage 14, before release | AUTOMATION, QUALITY |

---

# PLANNED SKILLS — HIGH

| Name | Purpose | Used by |
|---|---|---|
| `typography-director` | Font pairing, hierarchy, readability | DESIGN, QUALITY |
| `color-psychology-expert` | Luxury palettes and emotional design | DESIGN |
| `ux-forms-designer` | Planner usability and writing experience | DESIGN |
| `information-architect` | Page flow, navigation, organisation | DESIGN, AUTOMATION (Stage 5) |
| `accessibility-auditor` | Contrast, readability, inclusive design | QUALITY |
| `brand-guardian` | Enforces consistency across the catalogue | QUALITY, DESIGN |
| `mockup-art-director` | Etsy thumbnails and lifestyle mockups | AUTOMATION (Stage 17) |
| `product-packager` | Final folder structure and customer deliverables | AUTOMATION (Stage 18) |
| `quality-assurance-inspector` | Final pass/fail inspection before release | QUALITY (Stage 19) |

---

# PLANNED SKILLS — MEDIUM

| Name | Purpose | Used by |
|---|---|---|
| `prompt-optimizer` | Improves internal prompts and workflow efficiency | All |
| `asset-librarian` | Maintains reusable icons, layouts, components | AUTOMATION, DESIGN |
| `trend-watcher` | Identifies emerging Etsy opportunities | RESEARCH |
| `bundle-strategist` | Creates high-value product bundles | RESEARCH, DECISION |
| `localization-manager` | Adapts products for multiple languages and regions | RESEARCH, AUTOMATION |

---

# FUTURE CANDIDATES

Not specified. Add only when a real constraint demands them.

| Name | Purpose |
|---|---|
| `ai-art-director` | Selects visual direction per niche |
| `template-architect` | Builds reusable page systems and component libraries |
| `revenue-optimizer` | Pricing, upsells, bundles |
| `customer-review-analyzer` | Extracts improvement ideas from Etsy reviews |
| `collection-designer` | Ensures products work as cohesive collections |
| `release-manager` | Versioning, changelogs, release notes |

---

# ENGINE → SKILL MAP

| Engine | Skills |
|---|---|
| RESEARCH_ENGINE | market-research-analyst, etsy-seo-master, trend-watcher, bundle-strategist |
| DESIGN_ENGINE | banana-pro-director, cinema-world-builder, typography-director, color-psychology-expert, ux-forms-designer, information-architect |
| AUTOMATION_ENGINE | canva-production-expert, print-production-master, mockup-art-director, product-packager, asset-librarian |
| QUALITY_ENGINE | quality-assurance-inspector, accessibility-auditor, brand-guardian, print-production-master, canva-production-expert |
| DECISION_ENGINE | market-research-analyst, bundle-strategist |

---

# BUILD PLAN

Build in dependency order. Each phase is independently useful — do not start a phase until the previous one is in use on a real product.

**Phase 1 — Revenue gate**

1. `etsy-seo-master`
2. `market-research-analyst`

These determine what enters the pipeline and how it ranks. Highest return per hour of build effort.

**Phase 2 — Release gate**

3. `canva-production-expert`
4. `print-production-master`
5. `quality-assurance-inspector`

These prevent defective products shipping. Build once Phase 1 is producing candidates.

**Phase 3 — Design depth**

6. `typography-director`
7. `color-psychology-expert`
8. `information-architect`
9. `brand-guardian`

**Phase 4 — Presentation and scale**

10. `mockup-art-director`
11. `product-packager`
12. `accessibility-auditor`
13. `ux-forms-designer`

**Phase 5 — Medium priority**

Remaining Medium skills, built only when a repeated manual task justifies automating it.

---

# SKILL AUTHORING RULES

- One responsibility per skill. If a skill needs an "and", split it.
- A skill must be invocable without the conversation that created it.
- Every skill declares its inputs explicitly. No implicit context.
- Skills read from system files; they do not hardcode brand values.
- A skill that duplicates an existing skill's function is rejected. Extend the original.

---

# MAINTENANCE

| Event | Action |
|---|---|
| Skill built | Change Status to Active, record in CHANGELOG.md |
| Skill superseded | Mark Deprecated, name the replacement |
| New skill proposed | Add as Planned with full schema before any build work |
| Engine adds a skill reference | Update the Engine → Skill Map here |

Never define a skill inside an engine file. The registry is the only place.

---

# FINAL DIRECTIVE

The registry exists so that adding the twentieth skill costs the same as adding the third.

Two skills are Active. Eighteen are specified and unbuilt. Any engine instruction that depends on a Planned skill must be executed manually until that skill exists — and the gap must be visible, not silently ignored.
