#!/usr/bin/env python3
"""s13_split_validate v0.1 — mechanical proof of a transcript split (O-14 mitigation).

Validates a segments.jsonl against its source file:
  contiguity (zero gaps/overlaps), start==0, end==len(normalized),
  slice-text identity (norm[start:end]==text for every segment),
  concatenation == normalized source, role census.
Normalization per MF-1: CRLF->LF then lone CR->LF. Offsets index normalized text.

Usage: s13_split_validate_v0_1.py SOURCE SEGMENTS_JSONL
Exit 0 = PASS (prints census), nonzero = FAIL (prints first defect).
Stdlib-only, model-independent. Acceptance gate for any future splitter.
"""
import sys, json
from collections import Counter

def normalize(b: bytes) -> str:
    return b.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")

def main(src_path: str, segs_path: str) -> int:
    raw = open(src_path, "rb").read()
    norm = normalize(raw)
    segs = [json.loads(l) for l in open(segs_path) if l.strip()]
    segs.sort(key=lambda s: s["start"])
    if not segs:
        print("FAIL: no segments"); return 2
    if segs[0]["start"] != 0:
        print(f"FAIL: first segment starts at {segs[0]['start']}, not 0"); return 2
    if segs[-1]["end"] != len(norm):
        print(f"FAIL: last segment ends at {segs[-1]['end']}, source has {len(norm)} chars"); return 2
    for a, b in zip(segs, segs[1:]):
        if a["end"] != b["start"]:
            print(f"FAIL: gap/overlap between i={a['i']} (end {a['end']}) and i={b['i']} (start {b['start']})"); return 2
    for s in segs:
        if norm[s["start"]:s["end"]] != s["text"]:
            print(f"FAIL: slice-text mismatch at i={s['i']}"); return 2
    if "".join(s["text"] for s in segs) != norm:
        print("FAIL: concatenation != normalized source"); return 2
    census = Counter(s.get("role", "?") for s in segs)
    cr = raw.count(b"\r")
    print(f"PASS: {len(segs)} segments contiguous+lossless over {len(norm)} normalized chars "
          f"(raw {len(raw)} bytes, {cr} CR removed); roles={dict(census)}")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__); sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2]))
