# PROJECT_RULES.md

Status: Active
Version: 2.1
Last Updated: 2026-08-01
Owner: ETSY-AI-FACTORY

---

# 1. PURPOSE

The ETSY-AI-FACTORY exists to create premium commercial digital products suitable for immediate sale on Etsy and other digital marketplaces.

The factory is designed for consistency, scalability, quality, and continuous improvement.

---

# 2. SINGLE SOURCE OF TRUTH

This repository is the authoritative source for all production standards.

No rule may exist outside the repository.

If a reusable rule is discovered during production, it must be added to the appropriate system or library.

---

# 3. RULE PRECEDENCE

This is the canonical authority hierarchy for the entire factory. Every other document defers to it.

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

Databases are evidence, never authority.

---

# 4. PRODUCT STANDARD

Every product must be:

Commercial quality

Professionally designed

Easy to use

Easy to print

Easy to edit

Consistent with the brand

Ready for immediate sale

No placeholders.

No unfinished work.

---

# 5. DESIGN STANDARD

Every design must be:

Luxury

Minimal

Modern

Timeless

Editorial

Balanced

Readable

Whitespace-driven

No clutter.

No decorative elements without purpose.

---

# 6. PDF & CANVA STANDARD

The official production workflow is:

Design

↓

Vector PDF

↓

Import into Canva

↓

Quality Review

↓

Minor refinement if required

↓

Save Canva Template

↓

Export final customer deliverables

Rules:

Use Canva-supported fonts only.

Export vector PDFs.

Keep text editable.

Avoid rasterized typography.

Avoid clipping masks.

Avoid unsupported transparency.

Maintain editable structure.

The PDF-first workflow is mandatory unless explicitly overridden for a specific product.

---

# 7. ASSET POLICY

Only use:

Original assets

Commercial-use assets

Open-source assets

Public-domain assets

Never use copyrighted material without an appropriate commercial license.

---

# 8. CANVA COMPATIBILITY

Every product must import into Canva with minimal adjustments.

Design decisions must prioritize editability over visual effects.

---

# 9. REUSABILITY

Before creating anything new:

Search existing systems.

Search libraries.

Reuse existing components whenever possible.

Only create new assets when no suitable reusable asset exists.

Every reusable asset must be documented.

---

# 10. QUALITY

A product is complete only when it passes the Quality Engine.

Products below the required quality threshold must not be released.

---

# 11. SEO

Every product must include:

SEO Title

Optimized Description

13 Etsy Tags

Keywords

Bundle Suggestions

Cross-Sell Suggestions

---

# 12. DOCUMENTATION

Whenever reusable knowledge is created:

Update the relevant system.

Update the relevant library.

Update documentation.

Never rely on memory.

---

# 13. CONTINUOUS IMPROVEMENT

Every completed product must improve the factory.

Reusable discoveries become permanent repository knowledge.

The same mistake should never occur twice.

---

# 14. PRODUCT-FIRST PRINCIPLE

The purpose of this repository is to produce sellable products.

Architecture exists to support production.

Do not redesign the factory without evidence from real production.

Ship products.

Learn.

Improve.

Repeat.

---

# 15. FILE STATUS HEADERS

Every major document carries a header:

```
Status: Draft | Active | Deprecated
Version: X.Y
Last Updated: YYYY-MM-DD
Owner: ETSY-AI-FACTORY
```

Apply the header when a file is next edited. Do not rewrite files solely to add one.

---

# 16. FINAL RULE

Every decision must increase one or more of:

Customer value

Product quality

Brand consistency

Automation

Scalability

Commercial success

If a decision improves none of these, reject it.
