# Upload build — 2026-07-20

Purpose: make the v1.1 skill package installable/uploadable so claude.ai stops reporting missing files. **No method content changed.** Two packaging faults repaired; every substantive file is byte-identical to the 2026-07-19 ATP (`../maestro-forensic-transcript_v1.1_ATP_2026-07-19.zip`).

## Root cause of the claude.ai "missing files" error
claude.ai still served the **v1.0 skeleton** (SKILL.md only); its loading order names ~10 companion files that were never uploaded beside it. The complete v1.1 package existed locally but was never uploaded as a new version (OPEN O-02: installed cache is read-only; a patch = a new skill version).

## Faults repaired (packaging only)
1. **Dropped YAML frontmatter.** The v1.0→v1.1 fold stripped the `---\nname:\ndescription:\n---` block from the active `SKILL.md`; claude.ai requires it. Restored **verbatim** from `SKILL_v1_ORIGINAL.md` (the operator's own v1.0 frontmatter) — nothing authored.
2. **Invalid slug + non-portable zip.** Root folder was `maestro-forensic-transcript-v1.1` (dots invalid for a skill slug); PowerShell `Compress-Archive` writes backslash path separators that Linux extractors flatten. Rebuilt: root folder `maestro-forensic-transcript/`, zip entries use forward slashes (`System.IO.Compression.ZipArchive`, explicit paths).

## Verification (all PASS)
- SKILL.md begins with `---`; `name: maestro-forensic-transcript` matches `^[a-z0-9-]+$`.
- Zero dangling file references — every `.md`/`.py` named in SKILL.md is present.
- Single correctly-named top-level folder; entry paths forward-slashed.
- 30 files, 72,045 bytes.

## Contents
`maestro-forensic-transcript_claude-ai-upload_2026-07-20.zip` — the upload artifact. Identical tree installed live at `.claude/skills/maestro-forensic-transcript/`.

## Standing lesson (folded to skill CLAUDE.md + LEDGER SKILL-REPKG-1)
Any future re-fold must **preserve the frontmatter** and emit a spec-compliant (forward-slash) zip. Registration ≠ application: a rebuilt SKILL.md is not shippable until it also passes the packaging gate.

SSOT note: this is a traveling build copy. `_PROVENANCE/` remains the truth; the DEC-03 original-file sweep (O-03) continues, and any found original supersedes these reconstructions by pointer.
