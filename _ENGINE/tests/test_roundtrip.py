"""Regression: every shipped spec must survive decompile -> expand unchanged.

This is the test that matters for Engine 2.1. A suite that only exercises
hand-written samples proves the samples work. Round-tripping every product in
the repository proves the language is complete enough to express the real
collection, and it keeps proving it as products are added.

Run:
    python _ENGINE/tests/test_roundtrip.py

Exit code 0 means every spec.json in products/ decompiles to DSL and expands
back to a structurally identical dictionary.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import expand_spec as E  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
specs = sorted(ROOT.glob("products/*/spec.json"))
fails = 0
print(f"{'product':32} {'json B':>8} {'dsl B':>8} {'saved':>7}  result")
total_json = total_dsl = 0

for path in specs:
    original = json.loads(path.read_text(encoding="utf8"))
    dsl = E.decompile(original)
    try:
        produced = E.expand(dsl)
    except Exception as exc:  # noqa: BLE001
        print(f"{path.parent.name:32} {'':>8} {'':>8} {'':>7}  EXPAND ERROR: {exc}")
        fails += 1
        continue
    diffs = E.differences(original, produced)
    json_bytes, dsl_bytes = len(path.read_bytes()), len(dsl.encode())
    total_json += json_bytes
    total_dsl += dsl_bytes
    status = "identical" if not diffs else f"{len(diffs)} DIFFS"
    if diffs:
        fails += 1
        for d in diffs[:5]:
            status += f"\n      - {d}"
    print(f"{path.parent.name:32} {json_bytes:>8} {dsl_bytes:>8} "
          f"{100 - dsl_bytes * 100 // json_bytes:>6}%  {status}")

if total_json:
    print(f"\n{'TOTAL':32} {total_json:>8} {total_dsl:>8} "
          f"{100 - total_dsl * 100 // total_json:>6}%")
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
