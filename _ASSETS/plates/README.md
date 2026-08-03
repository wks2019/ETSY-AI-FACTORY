# Photographic plates

Base photographs used by `_ENGINE/mockup_renderer.py` for listing slots
02 (tablet) and 03 (desk). Seven of the ten slots are generated from code and
need nothing here. Without plates the renderer skips those two slots and
reports them — it never fails.

---

## Licensing — read before sourcing anything

**Stock photography is not permitted.** Etsy's Listing Image Requirements
policy requires that listing images be your own photos: taken by you, or
taken by someone on your behalf. Unsplash, Pexels and paid stock libraries
grant a copyright licence, which is a different question from Etsy's rule
about whose photo it is. A permissive copyright licence does not make a
stock photo compliant here.

This corrects earlier guidance in this project that suggested sourcing plates
from free stock libraries. It was wrong.

**Photograph the three plates yourself.** A phone camera on a windowsill is
sufficient. They are shot once and reused across all twenty products.

When shooting:

- No visible brand marks or logos on any device. An identifiable tablet logo
  in a commercial listing is a trademark exposure with no upside.
- No other person's work in frame — no posters, book covers, magazine pages.
- Shoot at 2667x2000 or larger, landscape, in even indirect daylight.
- Leave the screen or paper area blank and light. The renderer composites
  onto it; it does not remove what is already there.
- Keep the composition loose. Etsy crops to 3:4, 4:3 and 1:1 depending on
  where the image appears, and only the central 70% survives all three.

---

## Plate definition format

Each plate is two files: the photograph, and a JSON descriptor naming it and
giving the four corners the page is warped onto.

`tablet.json`

```json
{
  "image": "tablet.jpg",
  "quad": [[812, 604], [1918, 641], [1874, 1520], [768, 1478]],
  "note": "Screen corners, clockwise from top-left, in pixels."
}
```

Corner order is **clockwise from top-left**: top-left, top-right,
bottom-right, bottom-left. Order matters; a wrong order produces a mirrored
or folded composite rather than an error.

To read the corner coordinates, open the photograph in any editor and note
the pixel position of each corner of the screen or paper area.

If the photograph is not exactly 2667x2000 the renderer resizes it to that
canvas first — so measure the corners **after** resizing, or shoot at exactly
that size.

---

## Expected files

| Plate | Shows | Descriptor |
|---|---|---|
| `tablet` | A tablet on a desk, screen blank and lit | `tablet.json` |
| `desk` | Printed pages on a desk surface | `desk.json` |

A third lifestyle plate can be added later; it is not wired into the renderer
yet, and the seven generated slots plus these two make nine of the ten Etsy
image positions.
