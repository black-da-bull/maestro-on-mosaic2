#!/usr/bin/env python3
"""persistence_sweep v0.1 — word-boundary persistence search (MF-7 hygiene).

Searches text files under given roots for identifier terms using word-boundary
regexes, prints every hit with file:line context so raw hits are INSPECTED,
never blindly counted. The V1-class zero-occurrence claim is only valid over
an explicitly listed scope with this script's word-boundary matching.

Usage: persistence_sweep_v0_1.py ROOT [ROOT...] --terms 'R-RT-QAF-01' 'Config B' ...
Default exclusions: .git, node_modules, _PROVENANCE, sources/, archive transcripts.
Stdlib-only.
"""
import sys, os, re, argparse

TEXT_EXT = {".md", ".txt", ".yaml", ".yml", ".json", ".py", ".html", ".csv"}
EXCL_DIRS = {".git", "node_modules", "_PROVENANCE", "sources", ".history", ".obsidian", ".claudian"}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("roots", nargs="+")
    ap.add_argument("--terms", nargs="+", required=True)
    ap.add_argument("--include-excluded", action="store_true")
    a = ap.parse_args()
    pats = [(t, re.compile(r"(?<![\w-])" + re.escape(t) + r"(?![\w-])")) for t in a.terms]
    hits = 0
    for root in a.roots:
        for dirpath, dirnames, filenames in os.walk(root):
            if not a.include_excluded:
                dirnames[:] = [d for d in dirnames if d not in EXCL_DIRS]
            for fn in filenames:
                if os.path.splitext(fn)[1].lower() not in TEXT_EXT:
                    continue
                p = os.path.join(dirpath, fn)
                try:
                    lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
                except OSError:
                    continue
                for i, line in enumerate(lines, 1):
                    for term, pat in pats:
                        if pat.search(line):
                            hits += 1
                            print(f"HIT [{term}] {p}:{i}: {line.strip()[:160]}")
    print(f"\n{hits} word-boundary hit(s). Zero hits over a declared scope = 'not found in scope', never 'not persisted anywhere'.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
