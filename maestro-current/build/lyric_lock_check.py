#!/usr/bin/env python3
"""Lyric-lock comparator v0.2 — sequence + multiplicity preserving.
Locked and derived quoted-lyric SEQUENCES must be identical after whitespace normalization
(performance-spacing transform is display-layer only, DEC-26). Detects deletions, insertions,
duplication changes, and reordering. Usage: lyric_lock_check.py LOCKED DERIVED"""
import sys, re
def seq(p): return [re.sub(r"\s+"," ",m).strip() for m in re.findall(r'"([^"]+)"', open(p,encoding="utf-8").read())]
def main(locked, derived):
    L, D = seq(locked), seq(derived)
    if L == D:
        print(f"PASS ({len(L)} quoted lines, sequence+multiplicity identical)"); return 0
    for i,(a,b) in enumerate(zip(L,D)):
        if a!=b: print(f"FAIL at line {i+1}: locked={a!r} derived={b!r}"); return 2
    print(f"FAIL: length mismatch locked={len(L)} derived={len(D)} (deletion/insertion)"); return 2
if __name__=="__main__": sys.exit(main(sys.argv[1], sys.argv[2]))
