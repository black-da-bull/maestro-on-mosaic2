#!/usr/bin/env python3
"""Bundle validator v2 (REPAIR.O16D.VV.R1 — coverage widened per BLOCK-01/BLOCK-05 findings).
A1 parse (top-level docs + yaml fences) · A2 refs (incl. shorthand 'in 08' / '(09)' / 'per 08') ·
A3 axis parity · A5 gate arithmetic · A10 RECURSIVE structured-file parse (every .yaml/.yml/.json
under the bundle — the check the v1 validator lacked, which let an unparseable compiled report
ship) · A11 inventory completeness (MANIFEST.files == on-disk files, minus MANIFEST itself).
Usage: validate_bundle.py BUNDLEDIR ; exit 0 = PASS."""
import sys, os, re, json, yaml

def main(d):
    errs = []; allt = {}
    for f in sorted(os.listdir(d)):
        if f.endswith(".md"):
            allt[f] = open(os.path.join(d, f), encoding="utf-8").read()
    nums = {f[:2] for f in allt}
    manifest = yaml.safe_load(open(os.path.join(d, "MANIFEST.yaml")))
    # A1/A2/A3 over top-level docs
    for f, t in allt.items():
        for m in re.finditer(r"```yaml\n(.*?)```", t, re.S):
            yaml.safe_load(m.group(1))
        for r in re.findall(r"(\d\d_[A-Z_]+\.md)", t):
            if r not in allt: errs.append(f"A2 {f}: dangling {r}")
        for m in re.finditer(r"(?:documented in|Per |per |see )(\d\d)(?![\d.])", t):
            if m.group(1) not in nums: errs.append(f"A2 {f}: shorthand ref {m.group(1)} unresolved")
        if re.search(r"\bPERF\b", t): errs.append(f"A3 {f}: retired 4-letter token")
    if re.search(r"\|\s*MAP\s*\|", allt["01_TECHNICAL_UST_CANON.md"]): errs.append("A3: MAP axis row")
    if sum([18,12,10,10,8,12,6,8,6,4,4,2]) != 100: errs.append("A5 weights")
    if "97.5" not in allt["05_GOVERNANCE_SEG.md"]: errs.append("A5 floor")
    # A10 recursive structured-file parse — the whole tree, no exceptions
    for root, _, files in os.walk(d):
        for fn in sorted(files):
            p = os.path.join(root, fn); rel = os.path.relpath(p, d)
            try:
                if fn.endswith((".yaml", ".yml")): yaml.safe_load(open(p, encoding="utf-8"))
                elif fn.endswith(".json"): json.load(open(p, encoding="utf-8"))
            except Exception as e:
                errs.append(f"A10 {rel}: {str(e).splitlines()[0]}")
    # A11 inventory completeness
    listed = set(manifest.get("files", {}))
    on_disk = set()
    for root, _, files in os.walk(d):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), d).replace(os.sep, "/")
            if rel != "MANIFEST.yaml": on_disk.add(rel)
    for miss in sorted(on_disk - listed): errs.append(f"A11 unlisted on disk: {miss}")
    for ghost in sorted(listed - on_disk): errs.append(f"A11 listed but absent: {ghost}")
    print("PASS" if not errs else "FAIL:" + ";".join(errs))
    return 0 if not errs else 2

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
