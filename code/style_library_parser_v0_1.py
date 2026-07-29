#!/usr/bin/env python3
"""style_library_parser_v0_1 — PROPOSAL
Classifies the Saved Styles corpus (render-facing surfaces) into a
provenance-tagged index. Fail-closed: missing source or empty parse exits
non-zero. Append-only: never rewrites the source.

Run (Windows):  python code\\style_library_parser_v0_1.py
Run (WSL):      python3 /mnt/d/maestro-on-mosaic/code/style_library_parser_v0_1.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "style-library.md"
OUT = ROOT / "artifacts" / "style_library_index_v0_1.json"

DASH = r"[\u2013\u2014-]"  # en/em dash or hyphen

ERA_PATTERNS = [
    ("v5.5", re.compile(r"v5\.5", re.I)),
    ("v5-pro-beta", re.compile(r"v5\s*pro\s*beta", re.I)),
    ("v5+", re.compile(r"v5\+", re.I)),
    ("v5", re.compile(r"\bv5\b", re.I)),
    ("v4.5+", re.compile(r"v4\.5\+", re.I)),
    ("v4.5", re.compile(r"v4\.5", re.I)),
]

AXIS_CONTAINERS = {
    "THY": re.compile(r"\[\s*Theory\s*[\]|]", re.I),
    "VOC": re.compile(r"\[\s*Voices?\s*[\]|]", re.I),
    "STY": re.compile(r"\[\s*Style\s*[\]|]", re.I),
    "TIM": re.compile(r"\[\s*Timbre\s*[\]|]", re.I),
    "PER": re.compile(r"\[\s*Performance\s*[\]|]", re.I),
    "POST": re.compile(r"\[\s*Post[- ]?Production\s*[\]|]", re.I),
}
MAP_FOOTPRINT = re.compile(r"\[\s*Road\s*Map\s*\]", re.I)
EXECUTION_KEY = re.compile(r"\[\s*execution\s*\|", re.I)

HOUSE_LOWEND = [
    re.compile(rf"27{DASH}45\s*Hz", re.I),
    re.compile(rf"50{DASH}80\s*Hz", re.I),
    re.compile(rf"100{DASH}160\s*Hz", re.I),
    re.compile(rf"55{DASH}65\s*Hz", re.I),
    re.compile(r"three[- ]tier", re.I),
]
LAYER_DIRECTIVE = re.compile(
    r"(evolution(ary)?\s+layer|not\s+(a\s+)?replac|does\s+not\s+replace)", re.I
)
TRIAD_MARKERS = {
    "show_summary": re.compile(r"SHOW\s+SUMMARY\s*:", re.I),
    "bio": re.compile(r"\bBIO\s*:", re.I),
    "persona_profile": re.compile(r"PERSONA\s+PROFILE", re.I),
}
SPL_SQL = re.compile(r"\bSPL\b.*\bSQL?\b|\bSQL\b.*\bSPL\b", re.I | re.S)


def classify(entry: str) -> dict:
    era = "unmarked"
    for name, pat in ERA_PATTERNS:
        if pat.search(entry):
            era = name
            break
    axes = sorted(code for code, pat in AXIS_CONTAINERS.items() if pat.search(entry))
    lowend_hits = sum(1 for pat in HOUSE_LOWEND if pat.search(entry))
    triad = sorted(k for k, pat in TRIAD_MARKERS.items() if pat.search(entry))
    return {
        "sha1": hashlib.sha1(entry.encode("utf-8")).hexdigest()[:12],
        "chars": len(entry),
        "era": era,
        "axis_containers": axes,
        "map_footprint": bool(MAP_FOOTPRINT.search(entry)),
        "execution_key": bool(EXECUTION_KEY.search(entry)),
        "house_lowend_score": lowend_hits,
        "house_lowend": lowend_hits >= 3,
        "layer_directive": bool(LAYER_DIRECTIVE.search(entry)),
        "spl_sql": bool(SPL_SQL.search(entry)),
        "triad_markers": triad,
        "head": entry[:90],
    }


def main() -> int:
    if not SRC.exists():
        print(f"FAIL-CLOSED: source not found: {SRC}", file=sys.stderr)
        return 2
    raw = SRC.read_text(encoding="utf-8", errors="replace")
    entries = [b.strip() for b in re.split(r"\n\s*\n", raw) if b.strip()]
    # drop the "Saved Styles" banner line if it is its own block
    entries = [e for e in entries if e.lower() != "saved styles"]
    if not entries:
        print("FAIL-CLOSED: zero entries parsed", file=sys.stderr)
        return 3

    index = [classify(e) for e in entries]

    summary = {
        "source": str(SRC),
        "entry_count": len(index),
        "era_counts": {},
        "axis_container_entries": sum(1 for r in index if r["axis_containers"]),
        "map_footprints": sum(1 for r in index if r["map_footprint"]),
        "execution_keys": sum(1 for r in index if r["execution_key"]),
        "house_lowend_entries": sum(1 for r in index if r["house_lowend"]),
        "layer_directives": sum(1 for r in index if r["layer_directive"]),
        "spl_sql_entries": sum(1 for r in index if r["spl_sql"]),
        "triad_marked_entries": sum(1 for r in index if r["triad_markers"]),
    }
    for r in index:
        summary["era_counts"][r["era"]] = summary["era_counts"].get(r["era"], 0) + 1

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(
        json.dumps({"summary": summary, "entries": index}, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))
    print(f"index -> {OUT}")

    # invariants (fail-closed self-checks)
    failures = []
    if summary["map_footprints"] > 0 and summary["execution_keys"] == 0:
        failures.append("INV-1: MAP footprints exist but zero execution keys found")
    if summary["house_lowend_entries"] < 5:
        failures.append("INV-2: house low-end law under-detected (<5 entries)")
    illegal = [r["sha1"] for r in index
               if "LYR" in r["axis_containers"] or "END" in r["axis_containers"]]
    if illegal:
        failures.append(f"INV-3: LYR/END containers in style box: {illegal}")
    if failures:
        for f in failures:
            print("INVARIANT FAIL:", f, file=sys.stderr)
        return 4
    print("invariants: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
