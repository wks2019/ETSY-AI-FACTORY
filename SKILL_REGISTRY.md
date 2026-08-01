# SKILL_REGISTRY.md

Version: 1.1

Repository:
ETSY-AI-FACTORY

---

# PURPOSE

The Skill Registry is the single source of truth for every custom Claude skill used by the factory.

Engines reference this registry. Engines never define skills themselves.

---

# STATUS LEGEND

| Status | Meaning |
|---|---|
| **Active** | Skill file exists and is invocable now |
| **Planned** | Specified but not yet built. Do not invoke |
| **Deprecated** | Superseded. Do not invoke |

**Rule:** Confirm status here before invoking. Never invoke a Planned skill — do the work manually and state the gap.

---

# COST LEGEND

Cost is the context and time a skill consumes. Weigh it against task value before invoking.

| Cost | Meaning |
|---|---|
| Low | Text reasoning only |
| Medium | Multi-step reasoning or several file reads |
| High | Image generation, multi-asset production, or external calls |

Do not invoke a High-cost skill for a task a Low-cost one resolves.

---

# ACTIVE SKILLS

## banana-pro-director

| Field | Value |
|---|---|
| Status | **Active** |
| Priority | Critical |
| Cost | Medium |
| Purpose | Creative direction and premium visual review |
| Tasks | Creative review, hierarchy, layout, typography direction, cover concepts |
| Invoke when | A cover, page layout, or visual asset is designed or reviewed |
| Inputs | Design brief, brand context, target niche, existing page or concept |
| Outputs | Direction with fixed composition, lighting, camera, palette, branding |
| Used by | DESIGN_ENGINE, AUTOMATION_ENGINE (Stage 8), QUALITY_ENGINE |
| Depends on | systems/BRAND_SYSTEM, COLOR_SYSTEM, TYPOGRAPHY_SYSTEM |
| Success criteria | Reads as premium, hierarchy clear, nothing decorative survives without purpose |

Creative direction, not production.

---

## cinema-world-builder

| Field | Value |
|---|---|
| Status | **Active** |
| Priority | Critical |
| Cost | High |
| Purpose | Cohesive visual identity across a set of assets |
| Tasks | Collections, bundles, brand development, mood definition |
| Invoke when | Multiple images must share one identity. Not for single assets |
| Inputs | Brand context, niche, mood target, asset list |
| Outputs | Locked visual world — style, atmosphere, palette, recurring motifs |
| Used by | DESIGN_ENGINE, RESEARCH_ENGINE (product expansion) |
| Depends on | systems/BRAND_SYSTEM |
| Success criteria | Every asset recognisably from the same world without repeating |

High cost. Invoke once per collection, not once per asset.

---

# PLANNED — CRITICAL

| Name | Cost | Tasks | Invoke when | Used by |
|---|---|---|---|---|
| `etsy-seo-master` | Low | Titles, descriptions, 13 tags, keyword strategy | Stage 16, any listing copy | AUTOMATION, RESEARCH, QUALITY |
| `market-research-analyst` | High | Competitors, trends, pricing, opportunity scoring | Stages 1–2, any new niche | RESEARCH, DECISION |
| `canva-production-expert` | Medium | Import validation, editability, grouping | Stage 15, before export | AUTOMATION, QUALITY, DESIGN |
| `print-production-master` | Medium | PDF quality, margins, bleed, safe zones | Stage 14, before release | AUTOMATION, QUALITY |

---

# PLANNED — HIGH

| Name | Cost | Tasks | Used by |
|---|---|---|---|
| `typography-director` | Low | Font pairing, hierarchy, readability | DESIGN, QUALITY |
| `color-psychology-expert` | Low | Luxury palettes, emotional design | DESIGN |
| `ux-forms-designer` | Medium | Usability, writing experience | DESIGN |
| `information-architect` | Medium | Page flow, navigation, organisation | DESIGN, AUTOMATION (Stage 5) |
| `accessibility-auditor` | Low | Contrast, readability, inclusive design | QUALITY |
| `brand-guardian` | Low | Catalogue-wide consistency | QUALITY, DESIGN |
| `mockup-art-director` | High | Thumbnails, lifestyle mockups | AUTOMATION (Stage 17) |
| `product-packager` | Low | Folder structure, deliverables | AUTOMATION (Stage 18) |
| `quality-assurance-inspector` | Medium | Final pass/fail before release | QUALITY (Stage 19) |

---

# PLANNED — MEDIUM

| Name | Cost | Tasks | Used by |
|---|---|---|---|
| `prompt-optimizer` | Low | Improves internal prompts | All |
| `asset-librarian` | Low | Maintains icons, layouts, components | AUTOMATION, DESIGN |
| `trend-watcher` | Medium | Emerging Etsy opportunities | RESEARCH |
| `bundle-strategist` | Low | High-value bundles | RESEARCH, DECISION |
| `localization-manager` | Medium | Multi-language and region adaptation | RESEARCH, AUTOMATION |

---

# FUTURE CANDIDATES

Not specified. Add only when a real constraint demands them.

`ai-art-director` — visual direction per niche
`template-architect` — reusable page systems
`revenue-optimizer` — pricing, upsells, bundles
`customer-review-analyzer` — improvement ideas from reviews
`collection-designer` — cohesive collections
`release-manager` — versioning, changelogs, release notes

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

Dependency order. Do not start a phase until the previous one is in use on a real product.

**Phase 1 — Revenue gate**
`etsy-seo-master`, `market-research-analyst`

Determines what enters the pipeline and whether it ranks. Highest return per build hour.

**Phase 2 — Release gate**
`canva-production-expert`, `print-production-master`, `quality-assurance-inspector`

Prevents defective products shipping.

**Phase 3 — Design depth**
`typography-director`, `color-psychology-expert`, `information-architect`, `brand-guardian`

**Phase 4 — Presentation and scale**
`mockup-art-director`, `product-packager`, `accessibility-auditor`, `ux-forms-designer`

**Phase 5 — Medium priority**
Only when a repeated manual task justifies automating it.

---

# SKILL AUTHORING RULES

- One responsibility per skill. If it needs an "and", split it.
- Invocable without the conversation that created it.
- Inputs declared explicitly. No implicit context.
- Reads from system files. Never hardcodes brand values.
- Duplicating an existing skill's function is rejected. Extend the original.

---

# MAINTENANCE

| Event | Action |
|---|---|
| Skill built | Status → Active, record in CHANGELOG.md |
| Skill superseded | Mark Deprecated, name the replacement |
| New skill proposed | Add as Planned with full schema before any build work |
| Engine adds a reference | Update the Engine → Skill Map here |

Never define a skill inside an engine file.

---

# FINAL DIRECTIVE

The registry exists so that adding the twentieth skill costs the same as adding the third.

Two skills are Active. Eighteen are specified and unbuilt. Any engine instruction depending on a Planned skill must be executed manually until that skill exists — and the gap must be visible, not silently ignored.
