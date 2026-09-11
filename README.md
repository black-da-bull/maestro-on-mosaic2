Current Maestro v5-c entry: [_PROVENANCE/CONTINUATION_2026-09-09.md](_PROVENANCE/CONTINUATION_2026-09-09.md).
The consolidation record below is historical; current acceptance and state are tracked in `_PROVENANCE/`.

# maestro-on-mosaic — consolidated single source of truth

**Built:** 2026-06-18 • **Method:** content-verified (md5) consolidation across all known Maestro locations.
**Principle:** *there is no pre-blessed canon.* Nothing here is authoritative by label — every file earned its place by being **unique content** (proven by hash). Organization is by **type/purpose**, not by any folder's "canon/frozen" claim.

## What this is
One deduplicated, organized copy of every unique Maestro/MoMoney document, session, artifact, and code file found across `D:\Maestro`, `E:\Downloads\maestro`, `C:\Users\gamer\Downloads`, and `D:\HYDRA 2.0D PRO`. Every file was hashed; identical copies were collapsed to one; the original location of every copy is recorded so nothing is silently lost.

- **667 unique files** kept (from 924 considered — **257 redundant copies eliminated**, 167 duplicate groups collapsed).
- **Every file byte-verified** after copy (667/667 md5 match).
- **Originals untouched** — this is an additive consolidation. Source folders still exist until you bless this tree.

**2026-07-01 update:** added `artifacts/aisonggenerator/` — full text+metadata recovery of 3623 song generations from aisonggenerator.ai (see that folder's README/PROVENANCE). Index grew 676 → 4305 records.

## Layout (by type, not authority)
```
maestro-on-mosaic/
  system/      38   prompts, knowledge spines, custom instructions, configs, blueprints, personas
  sessions/    26   raw dev-session transcripts & conversation logs (provenance evidence)
  artifacts/ 3868   generated docs + aisonggenerator recovery (3629 song files/manifests/raw)
  code/       333   rebirth + both maestro-ai-music-system versions, scripts
  media/       31   images / svg / pdf (small). NOTE: 17 GB v4.5+ audio + aisonggenerator audio NOT here yet — see Phase 2/3.
                    media/aisonggenerator/  reserved for aisonggenerator audio/wav batch pull
  _PROVENANCE/      INDEX.json, DEDUP_MANIFEST.json — full traceability
```
Inside each bucket, files are grouped by **origin tag** (`D-Maestro`, `C-Downloads`, `HYDRA`, `E-scatter`) and keep their original sub-paths, so provenance is visible in the tree itself, not just the index.

## Provenance & traceability
- `_PROVENANCE/INDEX.json` — every kept file: path, bucket, origin, md5, size, and the full list of duplicate origins it represents.
- `_PROVENANCE/DEDUP_MANIFEST.json` — the 167 duplicate groups and exactly which copies were collapsed into each kept file.

## What is deliberately excluded
- Tool/editor cruft: `.history/`, `.obsidian/`, `.smart-env/`, `node_modules/`, `.git/` (91 files).
- `rebirth_backup_2026-05-17\` — proven 100% byte-identical to `rebirth\`.
- The 17 GB `v4.5+` audio media (Phase 2 — kept out of the corpus so it never pollutes chat context).

## Distinctions preserved (not collapsed)
- **Both `maestro-ai-music-system` versions are kept** — they share 104 paths but 96 differ in content; they are *different versions*, not duplicates.
- OneDrive holds 8 unique files + 4 newer-version files not in D: — pending Phase 2 ingest.

## Status / next steps
1. ~~Consolidate the text/code/doc corpus~~ ✅ done & verified (this tree).
2. **Phase 2 (pending):** move the 17 GB `v4.5+` media into `media/`, and pull the 12 OneDrive-only deltas in.
3. **Relocate (optional):** this is at `D:\Maestro\maestro-on-mosaic`; moving it up to `D:\maestro-on-mosaic` is a one-drag same-drive move.
4. **Retire the scatter:** once you bless this tree, the source copies can be quarantined reversibly.
6. **Phase 3 (aisonggenerator):** text+metadata recovery ✅ done (3623 records, `artifacts/aisonggenerator/`). Audio/WAV binary pull → `media/aisonggenerator/` pending.
# maestro-on-mosaic2
