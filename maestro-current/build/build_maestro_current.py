#!/usr/bin/env python3
"""Deterministic builder v2 for the maestro-current bundle (A9a, full member set).
REPAIR.O16D.VV.R1 — the v1 builder regenerated only the 11 O16B-era docs and stamped v0.2
(BLOCK-02 of REVIEW.O16D.VV.R1). v2 regenerates EVERY bundle member:
  runtime_docs  <- build/templates/ (byte-identical copies; 13 docs)
  build_tools, fixture <- packaged from the source bundle tree
  compiled topology <- compile_current.py + hash-pinned Technical UST source
  compiled status reports <- build/report_templates (authoritative report sources)
  MANIFEST.yaml <- build/manifest_meta.yaml (verbatim metadata) + computed md5 map (sorted)
Byte-identical output on every run from the same source tree; stdlib only.
Usage: build_maestro_current.py OUTDIR [SRCDIR] [TECHNICAL_SOURCE]
SRCDIR defaults to this script's bundle; TECHNICAL_SOURCE defaults to its repository source.
Exit 0 = built + byte-identical to source; exit 3 = built but drift found (report printed)."""
import os, sys, hashlib, shutil, tempfile
from compile_current import main as compile_topology

DOCS = ["00_ROOT_SPEC.md","01_TECHNICAL_UST_CANON.md","02_CREATIVE_UST_TEMPLATE.md",
        "03_PHASE_CHAIN.md","04_COUNCIL_TOPOLOGY.md","05_GOVERNANCE_SEG.md",
        "06_RUNTIME_RULES.md","07_ADDRESS_REGISTRY.md","08_PORTABILITY_ATP.md",
        "09_LOGS_AND_CONTINUATION.md","10_TEST_PLAN.md",
        "STRATA_MIGRATION_MAP.md","SCOPE_CORRECTION_v0_4.md"]
TREES = ["build","compiled","fixture"]

def md5(p):
    h = hashlib.md5(); h.update(open(p,"rb").read()); return h.hexdigest()

def main(outdir, srcdir=None, technical_source=None):
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.abspath(srcdir) if srcdir else os.path.dirname(here)
    if os.path.abspath(outdir) == src:
        print("FAIL-CLOSED: output must differ from the source bundle"); return 2
    technical_source = technical_source or os.path.join(os.path.dirname(src), "artifacts", "D-Maestro", "Maestro", "technical.ust.template.txt")
    if not os.path.isfile(technical_source):
        print("FAIL-CLOSED: hash-pinned Technical source required; pass TECHNICAL_SOURCE explicitly"); return 2
    # Validate and compile before creating output. A stale or absent source can never PASS.
    with tempfile.TemporaryDirectory() as compiled:
        if compile_topology(technical_source, compiled) != 0: return 2
        topology_outputs = {name: open(os.path.join(compiled, name), "rb").read()
                            for name in os.listdir(compiled)}
    tdir = os.path.join(src, "build", "templates")
    os.makedirs(outdir, exist_ok=True)
    missing = [n for n in DOCS if not os.path.exists(os.path.join(tdir, n))]
    if missing:
        print("FAIL-CLOSED: templates missing:", ",".join(missing)); return 2
    for n in DOCS:
        shutil.copyfile(os.path.join(tdir, n), os.path.join(outdir, n))
    for t in TREES:
        dst = os.path.join(outdir, t)
        if os.path.exists(dst): shutil.rmtree(dst)
        shutil.copytree(os.path.join(src, t), dst)
    # Status/interpretation reports have explicit sources; do not hand-patch compiled copies.
    for name in ("OMISSION_AUDIT.yaml", "BUILD_REGENERATION_REPORT.yaml", "DEPENDENCY_CLOSURE_REPORT.yaml"):
        shutil.copyfile(os.path.join(src, "build", "report_templates", name),
                        os.path.join(outdir, "compiled", name))
    for name, content in topology_outputs.items():
        with open(os.path.join(outdir, "compiled", name), "wb") as f: f.write(content)
    # deterministic manifest: meta verbatim (comments stripped) + sorted md5 map of every member
    meta = open(os.path.join(src, "build", "manifest_meta.yaml"), encoding="utf-8").read()
    body = [l for l in meta.splitlines() if not l.lstrip().startswith("#")]
    members = []
    for root, _, files in os.walk(outdir):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), outdir).replace(os.sep, "/")
            if rel != "MANIFEST.yaml": members.append(rel)
    lines = body + ["files:"] + [f"  {r}: {md5(os.path.join(outdir, r))}" for r in sorted(members)]
    open(os.path.join(outdir, "MANIFEST.yaml"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"built {len(members)} members + MANIFEST -> {outdir}")
    # drift check against source (A9 evidence)
    drift = []
    for r in sorted(members) + ["MANIFEST.yaml"]:
        s = os.path.join(src, r)
        if not os.path.exists(s): drift.append(f"only-in-out: {r}")
        elif md5(s) != md5(os.path.join(outdir, r)): drift.append(f"differs: {r}")
    for root, _, files in os.walk(src):
        for fn in files:
            rel = os.path.relpath(os.path.join(root, fn), src).replace(os.sep, "/")
            if not os.path.exists(os.path.join(outdir, rel)): drift.append(f"only-in-src: {rel}")
    if drift:
        print("A9 DRIFT vs source:"); [print("  " + x) for x in drift]; return 3
    print("A9 PASS: regenerated bundle is byte-identical to source"); return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "out",
                  sys.argv[2] if len(sys.argv) > 2 else None,
                  sys.argv[3] if len(sys.argv) > 3 else None))
