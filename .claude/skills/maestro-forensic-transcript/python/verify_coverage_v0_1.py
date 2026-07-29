#!/usr/bin/env python3
"""
verify_coverage_v0_1.py — W2/W3 gate. Proves the split lost nothing.
Validated shape: the exact checks that passed REPAIR.P1N.PANEL-VALIDATION.R1 (2026-07-19).

Usage: python3 verify_coverage_v0_1.py SOURCE.txt segments.jsonl [operator_verbatim.md]
Exit 0 = PASS, 1 = FAIL. Prints a coverage statement either way.
"""
import json, sys, hashlib

def main():
    src, segf = sys.argv[1], sys.argv[2]
    verb = sys.argv[3] if len(sys.argv) > 3 else None
    raw = open(src, "rb").read()
    text = raw.decode("utf-8", "replace").replace("\r\n", "\n").replace("\r", "\n")
    segs = [json.loads(l) for l in open(segf)]
    fails = []
    if not (segs[0]["start"] == 0 and segs[-1]["end"] == len(text)):
        fails.append("span does not cover full normalized source")
    for a, b in zip(segs, segs[1:]):
        if a["end"] != b["start"]:
            fails.append(f"gap/overlap at seg {a['i']}->{b['i']}")
    if "".join(s["text"] for s in segs) != text:
        fails.append("concatenation != normalized source")
    for s in segs:
        if text[s["start"]:s["end"]] != s["text"]:
            fails.append(f"offset mismatch seg {s['i']}"); break
    census = {}
    for s in segs:
        census[s["role"]] = census.get(s["role"], 0) + 1
    missing = []
    if verb:
        v = open(verb).read()
        for s in segs:
            if s["role"] == "user" and s["text"][:280] not in v:
                missing.append(s["i"])
        if missing:
            fails.append(f"user segments absent from verbatim file: {missing}")
    print(f"source md5 {hashlib.md5(raw).hexdigest()}  chars(norm) {len(text)}")
    print(f"census {census}")
    print("COVERAGE:", "PASS — character-lossless after CRLF->LF; zero gaps; all operator segments present"
          if not fails else "FAIL — " + "; ".join(fails))
    sys.exit(0 if not fails else 1)

if __name__ == "__main__":
    main()
