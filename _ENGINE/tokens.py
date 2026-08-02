"""
tokens.py
ETSY-AI-FACTORY / _ENGINE

Semantic colour token resolution and contrast verification.

Products reference tokens. This module binds a token to a value for the
selected theme, and refuses to proceed when a binding breaches the contrast
floors defined in systems/COLOR_SYSTEM.md.

No product may contain a literal colour value. That rule is enforced here,
not documented and hoped for.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
THEMES_FILE = ROOT / "_SCHEMA" / "themes.json"

HEX = re.compile(r"^#[0-9A-Fa-f]{6}$")


class TokenError(ValueError):
    pass


class ContrastError(ValueError):
    pass


# ----------------------------------------------------------------------
# COLOUR MATHS
# ----------------------------------------------------------------------

def _channels(value: str) -> tuple[int, int, int]:
    if not HEX.match(value):
        raise TokenError(f"Not a 6-digit hex colour: {value!r}")
    v = value.lstrip("#")
    return int(v[0:2], 16), int(v[2:4], 16), int(v[4:6], 16)


def relative_luminance(value: str) -> float:
    """WCAG 2.1 relative luminance."""
    def channel(c: int) -> float:
        s = c / 255
        return s / 12.92 if s <= 0.03928 else ((s + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in _channels(value))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(a: str, b: str) -> float:
    """WCAG 2.1 contrast ratio, 1.0 to 21.0."""
    high, low = sorted((relative_luminance(a), relative_luminance(b)), reverse=True)
    return round((high + 0.05) / (low + 0.05), 2)


def greyscale_value(value: str) -> int:
    """Perceptual luminance 0-255. Predicts monochrome print behaviour."""
    r, g, b = _channels(value)
    return round(0.299 * r + 0.587 * g + 0.114 * b)


# ----------------------------------------------------------------------
# THEME
# ----------------------------------------------------------------------

class Theme:
    """A resolved set of token bindings."""

    def __init__(self, name: str, bindings: dict[str, str], rules: list[dict]):
        self.name = name
        self._bindings = bindings
        self._rules = rules

    def __getitem__(self, token: str) -> str:
        try:
            return self._bindings[token]
        except KeyError:
            raise TokenError(
                f"Unknown token '{token}' in theme '{self.name}'. "
                f"Valid: {', '.join(sorted(self._bindings))}"
            ) from None

    def get(self, token: str, default: str | None = None) -> str | None:
        return self._bindings.get(token, default)

    @property
    def bindings(self) -> dict[str, str]:
        return dict(self._bindings)

    def css_variables(self) -> str:
        lines = [f"  --{name}: {value};" for name, value in sorted(self._bindings.items())]
        return ":root {\n" + "\n".join(lines) + "\n}"

    # ------------------------------------------------------------------

    def verify(self) -> list[dict]:
        """Check every contrast rule. Returns the full audit, passes included."""
        audit = []
        for rule in self._rules:
            fg, bg = self[rule["fg"]], self[rule["bg"]]
            ratio = contrast_ratio(fg, bg)
            audit.append(
                {
                    "fg": rule["fg"],
                    "bg": rule["bg"],
                    "ratio": ratio,
                    "min": rule["min"],
                    "pass": ratio >= rule["min"],
                }
            )
        return audit

    def enforce(self) -> None:
        """Raise on any contrast failure. Called before every render."""
        failures = [row for row in self.verify() if not row["pass"]]
        if failures:
            detail = "; ".join(
                f"{f['fg']} on {f['bg']} = {f['ratio']}:1, needs {f['min']}:1"
                for f in failures
            )
            raise ContrastError(f"Theme '{self.name}' fails contrast: {detail}")

    def greyscale_report(self) -> dict[str, int]:
        return {name: greyscale_value(value) for name, value in self._bindings.items()}


# ----------------------------------------------------------------------
# LOADING
# ----------------------------------------------------------------------

def _load_file() -> dict:
    if not THEMES_FILE.exists():
        raise TokenError(f"Theme definitions not found: {THEMES_FILE}")
    return json.loads(THEMES_FILE.read_text(encoding="utf8"))


def available_themes() -> list[str]:
    return sorted(_load_file()["themes"])


def load_theme(name: str = "neutral", overrides: dict[str, str] | None = None) -> Theme:
    """Resolve a named theme, optionally with per-product token overrides.

    Overrides must target existing tokens. A product cannot invent a token,
    because a token no other product knows about is not a system.
    """
    data = _load_file()
    themes = data["themes"]

    if name not in themes:
        raise TokenError(
            f"Unknown theme '{name}'. Available: {', '.join(sorted(themes))}"
        )

    bindings = dict(themes[name])

    declared = set(data["tokens"])
    missing = declared - set(bindings)
    if missing:
        raise TokenError(
            f"Theme '{name}' is incomplete. Missing: {', '.join(sorted(missing))}"
        )

    if overrides:
        unknown = set(overrides) - declared
        if unknown:
            raise TokenError(
                f"Override targets unknown tokens: {', '.join(sorted(unknown))}. "
                "Adding a token requires amending systems/COLOR_SYSTEM.md."
            )
        for token, value in overrides.items():
            if not HEX.match(value):
                raise TokenError(f"Override for '{token}' is not a hex colour: {value!r}")
            bindings[token] = value

    return Theme(name, bindings, data["contrast_rules"])


def assert_no_literal_colours(spec: dict) -> None:
    """Reject any hex value inside a product spec.

    Colour belongs to the theme. A spec containing a hex value has bypassed
    the system, and the breach is silent unless something looks for it.
    """
    found: list[str] = []

    def walk(node, path: str) -> None:
        if isinstance(node, dict):
            for key, value in node.items():
                walk(value, f"{path}.{key}")
        elif isinstance(node, list):
            for index, value in enumerate(node):
                walk(value, f"{path}[{index}]")
        elif isinstance(node, str) and HEX.match(node):
            found.append(f"{path} = {node}")

    walk(spec, "spec")

    if found:
        raise TokenError(
            "Literal colour values found in spec. Use semantic tokens instead:\n  "
            + "\n  ".join(found)
        )
