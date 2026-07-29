#!/usr/bin/env python3
"""compile_current v0.1 — source-and-delta compiler (A9b) for the materialized Technical UST.
INPUTS (hash-verified): the predecessor master spec (technical.ust.template.txt, canon skeleton
block) + the accepted delta set (M13 Roadmap migration; DEC-26 axis re-expansion; PER coding).
TRANSFORM (deterministic): extract canon skeleton -> re-address every MAP.* to PER.EXEC keys
(MAP.Kn -> PER.K{n+4}, subkeys carried verbatim) -> emit materialized topology + address
migration map + coverage matrix. FAILS on any unmapped source address (zero-omission gate).
Usage: compile_current.py SOURCE OUTDIR"""
import sys, re, hashlib, os

EXPECT_MD5 = "eaf18e1101c7a5814850fe0c62743b3a"  # INDEX-recorded hash of the predecessor source
NAMES = {"THY":"Theory","VOC":"Voices","STY":"Style","TIM":"Timbre","PER":"Performance",
         "POST":"Post-Production","LYR":"Lyrics"}

def main(src, outdir):
    raw = open(src, "rb").read()
    h = hashlib.md5(raw).hexdigest()
    if h != EXPECT_MD5:
        print(f"FAIL: source hash {h} != expected {EXPECT_MD5}"); return 2
    t = raw.decode("utf-8")
    i = t.find("# TECHNICAL.UST")
    skel = t[i:]
    # inventory source addresses
    src_axes = re.findall(r'axis_id:\s*"([A-Z]+)"', skel)
    src_keys = re.findall(r'key_id:\s*"([A-Z]+\.K\d+)"', skel)
    src_subs = re.findall(r'subkey_id:\s*"([A-Z]+\.K\d+\.S\d+)"', skel)
    # deterministic migration: MAP.Kn -> PER.K(n+4); subkeys carry index
    def mig(addr):
        m = re.match(r"MAP\.K(\d+)(\.S\d+)?$", addr)
        if not m: return addr
        return f"PER.K{int(m.group(1))+4}{m.group(2) or ''}"
    migration = {a: mig(a) for a in src_keys + src_subs if a.startswith("MAP.")}
    # transform text: re-address MAP block into PER execution keys
    out = skel
    for a, b in sorted(migration.items(), key=lambda kv: -len(kv[0])):
        out = out.replace(f'"{a}"', f'"{b}"')
    out = out.replace('axis_id: "MAP"\n\ndescription: "Section order, bar counts, per-section axis overrides."',
        'axis_id: "PER"  # EXECUTION EXTENSION (migrated from retired MAP axis per M13)\n\n'
        'description: "Performance.execution: section order, transitions, per-section overrides '
        '(structure-reservation migrated from Roadmap; display timing lives in LYR section headers)."')
    out = out.replace('# e.g. THY, VOC, STY, TIM, PER, POST, MAP, LYR',
                      '# THY, VOC, STY, TIM, PER, POST, LYR (7 axes; MAP retired per M13 - its keys live at PER.K5-K8)')
    # coverage check: every source address accounted (identity or migrated)
    cur = set(re.findall(r'(?:key_id|subkey_id):\s*"([A-Z.KS0-9]+)"', out))
    missing = [a for a in src_keys + src_subs if (migration.get(a, a)) not in cur]
    if missing:
        print(f"FAIL: {len(missing)} unmapped source addresses e.g. {missing[:5]}"); return 2
    os.makedirs(outdir, exist_ok=True)
    hdr = ("# Technical UST — MATERIALIZED Current Canon (compiled)\n"
           f"# Compiled by compile_current.py from predecessor md5 {EXPECT_MD5}\n"
           "# Deltas applied: M13 Roadmap migration (MAP.Kn -> PER.K(n+4), verbatim subkeys);\n"
           "# DEC-26 canonical names = Creative containers; PER 3-letter coding (native in source).\n"
           f"# Coverage: {len(src_axes)} source axes -> 7 current; {len(src_keys)} keys, {len(src_subs)} subkeys — ZERO omissions.\n\n")
    open(os.path.join(outdir, "TECHNICAL_UST_TOPOLOGY_MATERIALIZED.md"), "w", encoding="utf-8").write(hdr + out)
    with open(os.path.join(outdir, "TECHNICAL_UST_ADDRESS_MIGRATION.yaml"), "w") as f:
        f.write("# every non-identity address migration (all other addresses carry forward verbatim)\n")
        f.write(f"source_md5: {EXPECT_MD5}\nidentity_addresses: {len(src_keys)+len(src_subs)-len(migration)}\nmigrated:\n")
        for a, b in sorted(migration.items()):
            f.write(f"  {a}: {b}\n")
    with open(os.path.join(outdir, "FULL_CANON_COVERAGE_MATRIX.yaml"), "w") as f:
        f.write(f"source_axes: {src_axes}\ncurrent_axes: [THY, VOC, STY, TIM, PER, POST, LYR]\n"
                f"source_keys: {len(src_keys)}\nsource_subkeys: {len(src_subs)}\n"
                f"migrated_addresses: {len(migration)}\nunexplained_omissions: 0\n"
                "map_disposition: retired axis; keys rehomed PER.K5-K8; display timing -> LYR section headers\n")
    print(f"COMPILED: 7 axes, {len(src_keys)} keys, {len(src_subs)} subkeys, {len(migration)} migrated addresses, 0 omissions")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
