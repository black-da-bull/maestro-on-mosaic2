# Count Reconciliation — aisonggenerator recovery

**Recovery date:** 2026-07-01 · **Source:** `https://aisonggenerator.ai/api/my-music` (authenticated, account black.dabull@gmail.com)

## The numbers

| Figure | Value | Meaning |
|---|---|---|
| API total records | **3623** | Everything the endpoint returns, including soft-deleted |
| Live (`is_delete=false`) | **3375** | Non-deleted; matches the ~3375 song cards the /songs page renders |
| Soft-deleted (`is_delete=true`) | **248** | Still recoverable; retained in this capture |
| Public (`is_public=true`) | **3326** | Marked public |
| With lyrics | **3467** | 156 have empty lyrics (instrumentals / stubs / failed gens) |
| With tags/prompt | **3622** | Only 1 record missing tags |
| Sidebar number | **3161** | UNRESOLVED — not equal to any song count above |

## The 3161 sidebar figure

The number shown top-right in the site header (3161) does **not** match total (3623), live (3375), or public (3326) counts. It is most likely a **credits/points balance** or a lagging cached stat, **not** a song count. Marked UNRESOLVED rather than forced to a song interpretation. No records were dropped on account of it.

## Capture completeness

- All **3623** records captured raw, including the 248 soft-deleted (most fragile).
- Fields dropped from raw at capture (network/token noise, non-creative): `ip_address`, `task_id`, `wav_task_id`, `separation_task_id`, `suandao_id`, and the four callback timing fields.
- `pipe_url` retained. (It is derivable as `https://musicfile.kie.ai/` + base64(`song_id`), so recoverable even where absent.)
- Creative payload fully intact: `lyrics`, `tags`, `title`, `model`, timestamps, and all asset URLs (`audio_url`, `wav_url`, `cover_url`, `vocal_url`, `instrumental_url`).

## Status

- **Text + metadata recovery: COMPLETE** (this pass).
- **Audio/WAV binary download: DEFERRED** to a later pass (URLs preserved in manifest + per-song files).
