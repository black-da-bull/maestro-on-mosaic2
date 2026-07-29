#!/usr/bin/env python3
"""CAP validator v0.2 — two modes. draft: max cap only. terminal: creative MUST land in
4960-4999 (mandatory packaging band). Usage: cap_validator.py FILE ROLE [draft|terminal]"""
import sys
CAPS={"creative":5000,"show":1000,"ar_style":150,"ar_profile":2000}
BAND=(4960,4999)
def main(p, role, mode="draft"):
    n=len(open(p,encoding="utf-8").read()); cap=CAPS[role]
    if mode=="terminal" and role=="creative":
        ok=BAND[0]<=n<=BAND[1]
        print(f"terminal creative: {n} in {BAND}: {'PASS' if ok else 'FAIL'}"); return 0 if ok else 2
    ok=n<=cap
    print(f"{mode} {role}: {n}/{cap} {'PASS' if ok else 'FAIL'}"); return 0 if ok else 2
if __name__=="__main__": sys.exit(main(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv)>3 else "draft"))
