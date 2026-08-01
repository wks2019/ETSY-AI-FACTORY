# _CANVA

Native Canva template track.

PDF import degrades quality — editable templates must be built natively in Canva.

## Workflow

1. `generate-design` with a page-by-page prompt (hex values, typography, grid)
2. Select one of the returned candidates
3. `create-design-from-candidate` to convert to an editable design
4. Manual correction pass — calendar grids, tracker columns, and hourly rows are consistently wrong as generated
