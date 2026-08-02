"""
version.py
ETSY-AI-FACTORY / _ENGINE

Single source of truth for the engine version.

Every module that stamps a version into output imports from here. A literal
version string anywhere else is a defect: manifests shipped `2.0` while the
engine was `2.1` because the string was duplicated.
"""

from __future__ import annotations

ENGINE_NAME = "planner_engine"
ENGINE_VERSION = "2.1"
ENGINE_STAMP = f"{ENGINE_NAME} {ENGINE_VERSION}"

# Package layout revision. Bump when the deliverable structure changes, so a
# customer support query can be tied to a known folder shape.
PACKAGE_FORMAT = "1.0"
