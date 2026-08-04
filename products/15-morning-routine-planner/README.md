# Morning Routine Planner

Status: Built — awaiting Canva verification and print test
Version 1.0 · Collection 016 · Directory `products/15-morning-routine-planner`

Build, QA, packaging and repository conventions:
`_ENGINE/documentation/README_STANDARD.md`

---

## Source

**This is the first product authored in the Engine 2.1 specification
language.** `product.dsl` is the source and is what is committed. `spec.json`
is generated and is not stored:

```bash
python _ENGINE/expand_spec.py expand product.dsl --out spec.json
python _ENGINE/planner_engine.py spec.json
```

This is a deliberate amendment to the repository standard, which previously
required `spec.json` to be committed. Committing both would have stored the
same product twice and thrown away the entire point of the upgrade. Products
001–015 keep their committed `spec.json` and are not migrated.

| | Bytes |
|---|---|
| `product.dsl` (committed) | 14,917 |
| generated `spec.json` | 30,206 |
| Reduction | **52%** |

The product is included in `_ENGINE/tests/test_roundtrip.py`, which passes.

---

## Catalogue position

No conflict at build time. The only prior morning content is two pages inside
`12-habit-tracker` and two inside `14-life-planner`, both as one section of a
wider product.

**The risk is 017, not the existing catalogue.** Morning Routine and Evening
Routine are natural mirror images, and built as such they would become the
fifth overlapping pair in the shop. The line, recorded here before 017 is
written:

| | 016 Morning | 017 Evening |
|---|---|---|
| Direction | Forward — what today will be | Backward — what today was |
| Core question | What am I preparing for | What actually happened |
| Body pages | Waking, water, movement, breath | Wind-down, screens, sleep preparation |
| Measurement | Energy gained | Energy spent |
| Failure it addresses | The day starting without you | The day never ending |

017 must not simply reverse these 70 pages.

---

## Build

| Metric | Value |
|---|---|
| Pages | 70, identical across all four sizes |
| Internal links | 1,636 per file, identical across all four sizes |
| Bookmarks | 70 |
| Page types | 35 |
| Layouts | 8 of 15, all existing. No new renderer |

Clean first build.

---

## Design decisions

**The wake time is treated as the whole routine.** The Wake-Up Tracker records
planned against actual, snooze count, and whether the phone was touched in the
first ten minutes — three facts, no self-assessment. Whether you got up when
you said is a fact; whether the morning felt good is weather.

**A short version for bad mornings is written in advance.** On the same page as
the full sequence. Every routine meets a bad night; improvising a fallback at
the time is how routines end.

**Body work and mind work are separated.** They fail for different reasons —
body work fails to tiredness, mind work to noise — and the guide page puts
them in order: water and movement first, mind second, screens last.

**Time blocking starts at 05:00, not 06:00.** This is the one product where
the hour before six is the point.

**The guide states an add-nothing-for-two-weeks rule.** The urge to expand
peaks in week one and is the most common cause of collapse in week three.

**The Why page says what a morning routine does not do.** It will not fix a job
you hate or compensate for six hours of sleep. A product that overclaims here
earns refunds.

---

## Verification

| Gate | Result |
|---|---|
| `validate_spec` | pass, first run |
| Page / link / bookmark parity | 70 / 1,636 / 70 across four sizes |
| Dead internal link targets | 0 of 880 anchors |
| Unresolved PDF destinations | 0 across all four files |
| Named destinations | 70 = page count |
| Contrast | 9 checked, 0 failures |
| Archive extraction | passed — 9 entries |
| Round-trip regression | passed |

No `agenda` layout, so the US Letter overflow ceiling does not apply.

---

## Outstanding

1. Canva import verification
2. Physical print test
3. SEO package — `_SEO/15-morning-routine-planner.md`
4. Mockups — early cool light, so 017's warm lamp light distinguishes them at
   thumbnail size
5. Build 017 against the distinction table above, not as a mirror
