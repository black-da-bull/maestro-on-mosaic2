# PROVENANCE — aisonggenerator recovery

## Capture

- **Date:** 2026-07-01
- **Method:** Claude-in-Chrome authenticated browser session; fetch of `/api/my-music?email=black.dabull@gmail.com` with session credentials.
- **Account:** black.dabull@gmail.com (Black Da'Bull)
- **Records:** 3623
- **Raw file md5:** `ee4b4448850fe95d2eb7a21a6ce7c346`

## Field policy

Dropped at capture (non-creative network/token noise): `ip_address`, `task_id`, `wav_task_id`, `separation_task_id`, `suandao_id`, `first_callback_time`, `complete_callback_time`, `first_interval_seconds`, `complete_interval_seconds`.

Retained: `id`, `song_id`, `title`, `lyrics`, `tags`, `model`, `created_at`, `updated_at`, `duration`, `status`, `is_delete`, `is_public`, `is_extend`, `is_merge`, `api_provider`, `message`, `user_email`, `user_name`, and all asset URLs (`audio_url`, `wav_url`, `cover_url`, `vocal_url`, `instrumental_url`, `pipe_url`).

## Two source downloads (both validated, identical record set)

- `aisonggenerator_songs_master.json` (24 fields, incl. pipe_url) — **kept as _raw source of truth**
- `aisonggenerator_songs_master (1).json` (23 fields, pipe_url dropped) — redundant; not carried into corpus

Both parsed to 3623 records with identical lyrics(3467)/tags(3622)/deleted(248) counts.

## Known open item

Sidebar figure **3161** unexplained (see COUNT_RECONCILIATION.md). Presumed credits balance, not a song count. No records dropped.
