#!/usr/bin/env python3
"""Hash-pinned Technical UST compiler; DEC-PROMO-16 preserves internal MAP.

Creative surface Roadmap removal never readdresses Technical UST. Source bytes and
all eight axes/33 keys/165 subkeys survive verbatim. No song values are invented.
Usage: compile_current.py SOURCE OUTDIR
"""
import hashlib
import os
import re
import sys

EXPECT_MD5 = "eaf18e1101c7a5814850fe0c62743b3a"
AXES = ["THY", "VOC", "STY", "TIM", "PER", "POST", "MAP", "LYR"]


def topology(text):
    axes = re.findall(r'axis_id:\s*"([A-Z]+)"', text)
    keys = re.findall(r'key_id:\s*"([A-Z]+\.K\d+)"', text)
    subs = re.findall(r'subkey_id:\s*"([A-Z]+\.K\d+\.S\d+)"', text)
    return axes, keys, subs


def main(src, outdir):
    raw = open(src, "rb").read()
    digest = hashlib.md5(raw).hexdigest()
    if digest != EXPECT_MD5:
        print(f"FAIL: source hash {digest} != expected {EXPECT_MD5}")
        return 2
    text = raw.decode("utf-8")
    marker = "# TECHNICAL.UST"
    if text.count(marker) != 1:
        print("FAIL: unique Technical UST skeleton marker required")
        return 2
    skeleton = text[text.index(marker):]
    axes, keys, subs = topology(skeleton)
    if axes != AXES or len(keys) != 33 or len(subs) != 165:
        print("FAIL: pinned Technical topology shape changed")
        return 2
    if len(set(keys + subs)) != 198 or any(s.rsplit('.', 1)[0] not in keys for s in subs):
        print("FAIL: duplicate or orphan source address")
        return 2
    map_addresses = sorted(a for a in keys + subs if a.startswith("MAP."))
    os.makedirs(outdir, exist_ok=True)
    header = (
        "# Technical UST — MATERIALIZED Current Canon (compiled)\n"
        f"# Compiled by compile_current.py from predecessor md5 {EXPECT_MD5}\n"
        "# DEC-PROMO-16: retain Technical MAP; Creative surface omission is downstream.\n"
        "# Coverage: 8 source axes -> 8 current; 33 keys, 165 subkeys; 198 identity addresses.\n"
        "# Scope: this pinned source; no claim to flatten other historical strata.\n\n"
    )
    with open(os.path.join(outdir, "TECHNICAL_UST_TOPOLOGY_MATERIALIZED.md"), "w", encoding="utf-8") as f:
        f.write(header + skeleton)
    with open(os.path.join(outdir, "TECHNICAL_UST_ADDRESS_MIGRATION.yaml"), "w", encoding="utf-8") as f:
        f.write(f"source_md5: {EXPECT_MD5}\nauthority: DEC-PROMO-16\nidentity_addresses: 198\nmigrated: {{}}\npreserved_map_addresses:\n")
        for address in map_addresses:
            f.write(f"  - {address}\n")
        f.write("superseded_interpretation: Technical MAP-to-PER migration; retained only in historical checkpoints\n")
    with open(os.path.join(outdir, "FULL_CANON_COVERAGE_MATRIX.yaml"), "w", encoding="utf-8") as f:
        f.write(
            f"source_axes: [{', '.join(axes)}]\ncurrent_axes: [{', '.join(axes)}]\n"
            "source_keys: 33\nsource_subkeys: 165\nidentity_addresses: 198\n"
            "migrated_addresses: 0\nunexplained_omissions: 0\n"
            "map_disposition: retained internal Technical UST axis; no Creative Road-Map container\n"
            "scope: hash-pinned source only\n"
        )
    print("COMPILED: 8 axes, 33 keys, 165 subkeys, 198 identity addresses, 0 omissions")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1], sys.argv[2]))
