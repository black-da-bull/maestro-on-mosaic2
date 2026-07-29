#!/usr/bin/env python3
"""
phantom_detect_v0_1.py — W6 gate. Flags AI state-change claims lacking ROOT ratification (Q+A without F).
Lineage: INV-04 (mosaic_engine_v0.1.md), R-RT-PD-01 [FIRM] (session 13 U52/U56), operator protocol U31/U43/U45.

Usage: python3 phantom_detect_v0_1.py segments.jsonl
Scans role=assistant segments for commitment phrases; looks for a LATER role=user turn containing
ratification signal (explicit approval or build-upon reference). Everything unratified is FLAGGED —
this tool never resolves; a human (or replay classification with operator evidence) discharges flags.
Exit 0 always (reporting tool); the fold gate consumes the JSON on stdout.
"""
import json, re, sys

COMMIT = re.compile(r"\b(I have (?:updated|created|persisted|locked|fixed|added|applied)|"
                    r"going forward I will|is now (?:locked|canon|persisted|updated)|"
                    r"has been (?:updated|persisted|locked)|promotion(?:s)? executed|done\.)", re.I)
RATIFY = re.compile(r"\b(yes|correct|approved|good|proceed|continue|confirmed|F\b|ratif)", re.I)

def main():
    segs = [json.loads(l) for l in open(sys.argv[1])]
    flags = []
    for idx, s in enumerate(segs):
        if s["role"] != "assistant":
            continue
        for m in COMMIT.finditer(s["text"]):
            later_users = [u for u in segs[idx + 1:] if u["role"] == "user"]
            ratified = any(RATIFY.search(u["text"][:400]) for u in later_users[:2])
            flags.append({
                "seg": s["i"], "claim": m.group(0),
                "ctx": s["text"][max(0, m.start() - 80):m.start() + 120].replace("\n", " "),
                "status": "pending-F" if ratified else "PHANTOM-CANDIDATE",
                "note": "ratification heuristic only — discharge requires cited operator ROOT turn or artifact write",
            })
    print(json.dumps({"claims": len(flags),
                      "phantom_candidates": sum(1 for f in flags if f["status"] == "PHANTOM-CANDIDATE"),
                      "flags": flags}, indent=1))

if __name__ == "__main__":
    main()
