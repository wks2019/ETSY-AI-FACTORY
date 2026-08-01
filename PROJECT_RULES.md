# PROJECT RULES

Binding constraints. Applies to every product and every commit.

---

## 1. Pipeline over one-offs

Every product is produced by a reusable engine driven by a spec. If a task cannot be expressed as a spec, fix the engine — do not hand-build the artefact.

Saving a generator as a reusable engine file measurably reduces cost on subsequent products. This pattern is repeated for each new product type.

---

## 2. Repository

| Rule | Detail |
|---|---|
| Source of truth | `wks2019/ETSY-AI-FACTORY` (private) |
| Binaries | Never committed. `dist/`, PDF, PNG, JPG are gitignored |
| Secrets | Never committed, never pasted into chat |
| Structure | `_ENGINE/`, `_SCHEMA/`, `products/`, `_SEO/`, `_CANVA/`, `docs/` |

---

## 3. Naming

| Item | Convention |
|---|---|
| Product directory | `NN-kebab-case-name` |
| Engine file | `<type>_engine.py` |
| SEO file | `_SEO/NN-kebab-case-name.md` |
| Commit message | Conventional commits — `feat:`, `fix:`, `chore:`, `docs:` |

---

## 4. Licensing

- Fonts must be OFL, Apache-2.0, or explicitly commercially licensed. Current set: Cormorant Garamond, Inter.
- No stock asset ships without a verified commercial licence.
- No copyrighted character, brand, or quotation in any product or listing image.

---

## 5. Quality gates

A product does not ship until:

- All four sizes render clean
- Every internal link resolves
- Bookmark tree is complete
- Fonts are embedded, no substitution
- SEO package is complete — all 13 tags, full description, full attributes
- Mockups exist

No partial listings.

---

## 6. Canva

- PDF import is prohibited. Native build only.
- AI generation is a style and structure approximation, never a final deliverable.
- Grids, tracker columns, and schedule rows always get a manual correction pass.

---

## 7. Scope discipline

- Simplest working solution first.
- No abstraction without a second real consumer.
- No dependency without a concrete need.
- No refactor of a shipped product's engine without a stated reason.

---

## 8. Differentiation

Each of the 20 products must stand alone as a distinct offering. Palette swaps and cover changes do not constitute a new product.

---

## 9. Credentials

- GitHub access is via the Claude Github MCP Connector GitHub App, scoped to this repository.
- Personal Access Tokens are never pasted into chat. If one is exposed, revoke immediately at `github.com/settings/tokens`.
