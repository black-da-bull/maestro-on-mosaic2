# aisonggenerator — recovered works

**Recovered:** 2026-07-01 · **Source:** aisonggenerator.ai account `black.dabull@gmail.com` via authenticated `/api/my-music` endpoint (Claude-in-Chrome session).

**Principle (inherited from parent corpus):** raw capture is the source of truth; everything else here is a derived projection for browsability. Nothing is authoritative by label.

## What this is

Complete text + metadata recovery of **3623 song generations** (3375 live + 248 soft-deleted) spanning 2025-02-15 → 2026-03-23. Captures the full evolution of every song: lyrics, style/prompt (tags), model, timestamps, and asset URLs.

## Layout

```
aisonggenerator/
  _raw/
    aisonggenerator_songs_master.json   SOURCE OF TRUTH — 3623 records, raw API capture (cleaned of network/token noise)
  songs/                                3623 per-song .md files (title, metadata, prompt, lyrics)
                                        named: YYYY-MM-DD__slug__shortid.md (chronological, unique)
  EVOLUTION_INDEX.md                    songs grouped into 357 title-families, chronological within each
  manifest.csv                          one row per generation; family, seq, flags, asset URLs, file link
  COUNT_RECONCILIATION.md               3623 vs 3375 vs 3161 explained; capture-completeness notes
  PROVENANCE.md                         capture method, field policy, hashes
```

## Status

- Text + metadata: **COMPLETE**
- Audio/WAV binaries: **DEFERRED** — URLs preserved for a later batch-download pass (`media/aisonggenerator/`).

## Derived-vs-source discipline

`_raw/aisonggenerator_songs_master.json` is canon. The `songs/*.md`, `EVOLUTION_INDEX.md`, and `manifest.csv` are **regenerable projections** — if they ever disagree with the raw JSON, the JSON wins.
