# _SCHEMA

Machine-readable definitions the engine enforces at build time.

| File | Purpose |
|---|---|
| `spec.schema.json` | JSON Schema draft-07. Validates every product spec. Rejects unknown keys, unknown layouts, malformed ids |
| `themes.json` | Token bindings for `neutral`, `mono`, `slate`, `dark`, plus the contrast rules the engine enforces |

## Relationship to `systems/`

`systems/COLOR_SYSTEM.md` is **canonical**. `themes.json` is its machine-readable mirror.

If the two disagree, the Markdown is correct and the JSON is defective. Correct the JSON; never amend the Markdown to match a drifted mirror.

The same applies to `systems/TYPOGRAPHY_SYSTEM.md` and the `TYPE` table in `_ENGINE/layout_renderer.py`.

## Enforcement

Three checks run before any render:

1. **Schema validation** — structure, required keys, enumerated layouts
2. **Literal colour rejection** — any hex value anywhere in a spec fails the build. Colour belongs to the theme
3. **Contrast enforcement** — every rule in `themes.json` is computed and must pass

A build that cannot satisfy all three does not produce a PDF.
