# ETSY AI FACTORY ENGINE

Version: 1.1

## PURPOSE

This repository is an AI production factory.

Its purpose is to consistently produce premium digital products for Etsy that are commercially viable, visually consistent, easy to edit in Canva, and ready for immediate sale.

Claude must behave as a production system, not as a conversational assistant.

---

# CORE DIRECTIVE

Every decision must increase one or more of:

- Product quality
- Customer value
- Etsy conversion rate
- Production speed
- Reusability
- Brand consistency
- Scalability

Never sacrifice quality for speed.

---

# STARTUP

Loading is governed by `FACTORY_PROTOCOL.md`. This file no longer lists resources.

1. Read `FACTORY_PROTOCOL.md`
2. Read `PROJECT_RULES.md`
3. Read `SKILL_REGISTRY.md`
4. Identify the task type
5. Look up required resources in the Task Routing table
6. Load only those engines, systems, and libraries — whole files
7. Query databases. Never load them whole
8. Run the integrity check. Report any missing file
9. Resolve conflicts by the precedence hierarchy. Log every conflict
10. Begin production

Adding an engine, system, or library requires no edit to this file.

---

# PRODUCT PIPELINE

For every product execute:

Market Research

↓

Keyword Validation

↓

Product Planning

↓

Page Planning

↓

Layout Selection

↓

Component Selection

↓

Design

↓

Typography

↓

Colour System

↓

Icons

↓

Illustrations

↓

Vector Build

↓

PDF Export

↓

Canva Compatibility Check

↓

SEO Generation

↓

Mockups

↓

Packaging

↓

Quality Audit

↓

Ready For Sale

Stage detail lives in `engines/AUTOMATION_ENGINE.md`.

---

# DESIGN RULES

Always produce:

Luxury

Minimal

Professional

Modern

Editorial

Apple Inspired

Scandinavian

Clean

Balanced

High whitespace

Never produce:

Clipart

Crowded pages

Poor spacing

Random colours

Random fonts

Low resolution

Amateur layouts

---

# CANVA ENGINE

Use Canva-compatible fonts only.

Never rasterize text.

Export vector PDF.

Keep text editable.

Avoid clipping masks.

Avoid transparency effects.

Avoid unsupported gradients.

Group related elements.

Maintain consistent spacing.

Maintain editable structure.

Assume every PDF will be imported into Canva and refined before publication.

---

# PRINT ENGINE

Always support:

A4

A5

US Letter

Half Letter

300 DPI

Vector PDF

Selectable text

Professional margins

Print safe zones

---

# SEO ENGINE

Generate:

SEO Title

Short Title

Long Title

Description

13 Tags

Primary Keywords

Secondary Keywords

Bundle Suggestions

Cross Sell Suggestions

Frequently Asked Questions

Target English-speaking markets unless instructed otherwise.

---

# BRAND ENGINE

Every product belongs to the same brand family.

Maintain:

Typography

Colour palette

Spacing

Icon style

Page style

Cover style

Naming conventions

---

# COMPONENT ENGINE

Reuse components whenever possible.

Never recreate an existing component.

Update libraries when improvements are made.

---

# QUALITY ENGINE

Before completion verify:

✓ Typography

✓ Alignment

✓ Spacing

✓ Colour consistency

✓ Margins

✓ Hyperlinks

✓ Canva compatibility

✓ Editable text

✓ Vector quality

✓ PDF quality

✓ SEO

✓ Mockups

✓ Packaging

✓ File naming

If any item fails, fix it before continuing.

Full audit and scoring in `engines/QUALITY_ENGINE.md`. Minimum release score is 95/100.

---

# TECHNOLOGY

Use when appropriate:

Markdown

HTML5

CSS3

SVG

JSON

YAML

CSV

Vector PDF

Google Fonts that are available in Canva

Design Tokens

Reusable Components

Git

GitHub

Never introduce technology that breaks Canva compatibility.

---

# ASSET POLICY

Only use:

Original work

Commercial-use assets

Open-source assets

Public-domain assets

Never use copyrighted graphics or fonts without an appropriate license.

---

# OUTPUT

Every completed product must include:

Production PDF

Canva-ready PDF

Cover

Preview Images

SEO Package

Mockups

Instructions

Commercial License Notes

Folder Structure

Ready-to-upload Etsy package

No placeholders.

No unfinished work.

Every output must be production-ready.
