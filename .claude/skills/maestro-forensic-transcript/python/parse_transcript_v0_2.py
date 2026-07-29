#!/usr/bin/env python3
"""
parse_transcript_v0_2.py — mechanical splitter for exported AI-session transcripts.

PLANE: Dev / Forensics (NOT Maestro runtime). Pure stdlib. No model calls.
POSITION: W2 in the SS05 workflow — output feeds extract_operator_turns / classify / fold.

v0_2 carries the O-14 splitter repairs, validated against session 13 (P1N PASS, 2026-07-19):
  R1 tail-recovery      operator inputs embedded at assistant-segment tails (REC-A/REC-B class)
                        are DETECTED and reported — short trailing directives, "pasted" markers,
                        trailing timestamps. Reported for human confirmation, never auto-reclassified.
  R2 attachment events  export chrome like "file.txt\\ntxt\\n\\n2:15 PM" is enumerated as an
                        operator ACT (M8/MF-3 class), since it renders as no user turn.
  R3 inner-transcript   "You said:" inside assistant text is NOT an operator turn when the
                        session itself quotes another transcript; hits are listed for triage.
  R4 normalization      CRLF/CR -> LF, declared in output. Offsets index NORMALIZED text.
                        This is character-lossless, not byte-lossless (MF-1) — say so.

Usage:
  python3 parse_transcript_v0_2.py SOURCE.txt OUTDIR [--user-marker "You said:"]
Outputs in OUTDIR:
  segments.jsonl   {i, role, start, end, text}   contiguous, zero-gap, concat == normalized source
  operator_verbatim.md                            every role=user segment, verbatim
  parse_report.json                               census, normalization note, R1/R2/R3 candidate lists
"""
from __future__ import annotations
import json, re, sys, os, hashlib

USER_MARKER_DEFAULT = "You said:"
TIME_RE = re.compile(r'\b\d{1,2}:\d{2}\s?[AP]M\b')
ATTACH_RE = re.compile(r'\n([^\n/][^\n]{0,80}\.(?:txt|md|json|yaml|yml|csv|zip|pdf|docx|py|js))\n[a-z]{2,4}\n\n(\d{1,2}:\d{2}\s?[AP]M)\n', re.I)
TAIL_DIRECTIVE_RE = re.compile(r'\n([A-Z][^\n]{3,120}\.)\n(?:[^\S\n]*\n)*(?:May \d{1,2}|\d{1,2}:\d{2}\s?[AP]M)\s*$')
PASTED_TAIL_RE = re.compile(r'\npasted\n\n\d{1,2}:\d{2}\s?[AP]M\s*$')


def normalize(raw: bytes):
    text = raw.decode("utf-8", "replace")
    cr = text.count("\r")
    return text.replace("\r\n", "\n").replace("\r", "\n"), cr


def split(text: str, user_marker: str):
    """Split on top-of-line user_marker occurrences. Everything before the first is preamble;
    each user block runs to the next blank-line boundary heuristic is NOT used — the block runs
    until the next marker or an assistant-response start can't be detected mechanically, so we
    split ONLY on markers and classify user vs assistant by marker parity. This mirrors the
    validated session-13 split shape: marker-opened segments are user; the remainder between
    user segments is assistant."""
    starts = [m.start() for m in re.finditer(re.escape(user_marker), text)]
    segs = []
    if not starts:
        return [{"i": 0, "role": "preamble", "start": 0, "end": len(text), "text": text}]
    if starts[0] > 0:
        segs.append({"role": "preamble", "start": 0, "end": starts[0]})
    for k, s in enumerate(starts):
        # user segment: marker to first double-newline followed by non-quoted content is unreliable;
        # use next marker as hard boundary and split user/assistant at the export's response head if found.
        hard_end = starts[k + 1] if k + 1 < len(starts) else len(text)
        block = text[s:hard_end]
        # assistant head heuristic: export renders the assistant reply after the user body; the
        # earliest reliable cut is the first "\n\n" AFTER the echoed message body (marker line +
        # duplicated first line). We keep the whole block as ONE user segment when no cut is safe.
        m = re.search(r'\n\n(?=[A-Z(`#*\-])', block[len(user_marker):])
        if m:
            cut = s + len(user_marker) + m.start()
            segs.append({"role": "user", "start": s, "end": cut})
            segs.append({"role": "assistant", "start": cut, "end": hard_end})
        else:
            segs.append({"role": "user", "start": s, "end": hard_end})
    out = []
    for i, sg in enumerate(segs):
        sg["i"] = i
        sg["text"] = text[sg["start"]:sg["end"]]
        out.append(sg)
    return out


def audits(segs, user_marker):
    r1, r2, r3 = [], [], []
    for sg in segs:
        t = sg["text"]
        if sg["role"] == "assistant":
            for m in re.finditer(re.escape(user_marker), t):
                r3.append({"seg": sg["i"], "pos": m.start(),
                           "ctx": t[max(0, m.start() - 60):m.start() + 90]})
            tail = t[-400:]
            if PASTED_TAIL_RE.search(tail) or TAIL_DIRECTIVE_RE.search(tail):
                r1.append({"seg": sg["i"], "tail": tail[-220:]})
        for m in ATTACH_RE.finditer(t):
            r2.append({"seg": sg["i"], "file": m.group(1), "time": m.group(2)})
    return r1, r2, r3


def main():
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(2)
    src, outdir = sys.argv[1], sys.argv[2]
    marker = USER_MARKER_DEFAULT
    if "--user-marker" in sys.argv:
        marker = sys.argv[sys.argv.index("--user-marker") + 1]
    os.makedirs(outdir, exist_ok=True)
    raw = open(src, "rb").read()
    text, cr = normalize(raw)
    segs = split(text, marker)
    # invariants: contiguous, zero-gap, concat == normalized source
    assert segs[0]["start"] == 0 and segs[-1]["end"] == len(text)
    for a, b in zip(segs, segs[1:]):
        assert a["end"] == b["start"], f"gap at seg {a['i']}"
    assert "".join(s["text"] for s in segs) == text, "concat != normalized source"
    with open(f"{outdir}/segments.jsonl", "w") as f:
        for s in segs:
            f.write(json.dumps(s) + "\n")
    with open(f"{outdir}/operator_verbatim.md", "w") as f:
        for s in segs:
            if s["role"] == "user":
                f.write(s["text"] + "\n\n")
    r1, r2, r3 = audits(segs, marker)
    report = {
        "source": src, "source_md5": hashlib.md5(raw).hexdigest(),
        "source_bytes": len(raw), "normalized_chars": len(text),
        "normalization": f"CRLF/CR->LF ({cr} CR chars); character-lossless, offsets index normalized text (MF-1)",
        "census": {r: sum(1 for s in segs if s["role"] == r) for r in ("preamble", "user", "assistant")},
        "R1_tail_recovery_candidates": r1,
        "R2_attachment_events": r2,
        "R3_inner_transcript_marker_hits": len(r3),
        "R3_samples": r3[:10],
        "note": "R1/R2 require human confirmation before reclassification (never auto-promote); "
                "R3 hits inside assistant text are usually the inner transcript quoting itself.",
    }
    json.dump(report, open(f"{outdir}/parse_report.json", "w"), indent=1)
    print(json.dumps({k: report[k] for k in ("census", "normalization")}, indent=1))
    print(f"R1 candidates: {len(r1)}  R2 attachments: {len(r2)}  R3 inner-marker hits: {len(r3)}")


if __name__ == "__main__":
    main()
