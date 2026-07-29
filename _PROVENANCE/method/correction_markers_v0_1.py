#!/usr/bin/env python3
"""correction_markers v0.1 — the R2 omission-sweep marker set, persisted.

PURPOSE: coverage sweeps — find operator turns bearing correction markers and
check each is covered in a replay. This is the instrument R2 used (2026-07-19).

NOT the density-ordering metric: the marker set behind the original
session-selection density figures (0.32/KB etc.) was never persisted and is NOT
reconstructed here. Operator ruling pending (elicitation E-5): persist a fresh
density definition or retire density as ordering authority. Until ruled, no
session ordering may cite density.
"""
import re

CORRECTION_MARKERS = re.compile(
    r"\b(no[,.]|wrong|incorrect|you changed|not what|stop|pause|failing|"
    r"you didn'?t|that'?s not|re-?read|mistake|correction)\b",
    re.IGNORECASE,
)

def bears_correction_marker(operator_text: str, head_chars: int = 600) -> bool:
    """Check the operator-authored head of a segment (limits assistant-bleed noise)."""
    return bool(CORRECTION_MARKERS.search(operator_text[:head_chars]))
