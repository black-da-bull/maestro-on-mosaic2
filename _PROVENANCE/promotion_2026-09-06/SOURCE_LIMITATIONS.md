# Source limitations — promotion 2026-09-06, resolved in the resume run
Doctrine: **Your Vision. Our Mission.**
Authored 2026-09-06 (resume run). Append-only: this file records what the objects
actually are, not what a prior session guessed they were.

## Status of this file
LEDGER `PROMOTION-2026-09-06 — application checkpoint and limited validation` cites
`promotion_2026-09-06/SOURCE_LIMITATIONS.md` as the record naming the two historical
text blobs that blocked V1. **That file was never committed.** Neither were
`IMPACT.csv`, `DECISION_OUTCOMES.json`, `VALIDATION.md`, or
`CONTINUATION_2026-09-06.md`, all of which the same run's records cite as existing.
Every one of them lived only in the run's conversation — the exact failure STATE rule 7
(M1) names: *nothing operative lives only in conversation.* The citations were written
as if the artifacts had landed; they had not.

This file is therefore **not a recovery of that text**, which no longer exists in any
retrievable form, and it does not reconstruct or paraphrase it. It is a fresh audit,
performed from the corpus itself in the resume run, of the objects that fit the
recorded description. The dangling-citation defect is registered separately in OPEN;
it is not silently harmonized away here.

## Identification
The blocking description was "exact raw-byte retrieval/audit of two historical text
objects." The corpus at baseline `88cd150` tracks exactly two `.txt` objects that
cannot be decoded as UTF-8 — i.e. exactly two text objects whose coverage depends on
raw-byte handling rather than ordinary reading:

| # | Object | Bytes | sha256 |
|---|---|---|---|
| 1 | `code/D-Maestro/maestro-ai-music-system-main/Today.txt` | 184,731 | `e79cbe79b4bb915ae0c64f6c3d0ef7f7f95c9bee5c30d2f0d71a55111438c57f` |
| 2 | `code/D-Maestro/maestro-ai-music-system-main/legacy/~$Today.txt` | 162 | `9a5277b5281b61c51c9c3c04c9d5d600dbb101170fd8f7e59099ca5a9a4d7403` |

That identification is inference from a matching description, not a recovered
statement, and it is recorded in that lane (PROBABLE, M16). It is also no longer
load-bearing: the resume run audits **every** object the commit tracks, so V1's
coverage does not depend on which two the earlier run meant.

## Audit 1 — `Today.txt`
- **Encoding:** Windows-1252 (CP1252). Not UTF-8: byte `0xE9` at offset 5092 is a
  bare `é`, which is an invalid UTF-8 start of a continuation sequence. Decodes
  cleanly and completely under CP1252 — no replacement characters, no data loss.
- **Full non-ASCII inventory** (38 bytes, all typographic, all accounted for):
  `0x95` ×3 (`•`), `0xA6` ×5 (`¦`), `0xB1` ×1 (`±`), `0xB7` ×6 (`·`), `0xD7` ×20 (`×`),
  `0xE9` ×3 (`é`). No control bytes, no embedded binary, no truncation.
- **Threshold occurrences:** **zero.** Neither the `97.5` family nor the `G≥7.0`
  family appears anywhere in the object, in raw bytes or decoded text.
- **Disposition:** historical dev-session notes (council roster sketch, gate math with
  its own weights `theory 0.25 / structure 0.25 / lyrics_gender 0.20 / timbre_mix 0.20 /
  compliance 0.10`, threshold `weighted_total = 0.88`). That 0.88 gate is a **separate
  historical mechanism on its own scale** — it is neither the song-local 97.5 target nor
  the G-Card ≥7.0 scalar, and DEC-PROMO-01/02 make no claim about it. Recorded here so a
  later reader does not mistake it for either, and does not promote it to a current
  default. Preserved byte-intact; not edited.

## Audit 2 — `~$Today.txt`
- **What it is:** a Microsoft Office owner/lock file (the `~$` sidecar Word writes while
  a document is open). All 162 bytes read: a length-prefixed owner name `gamer` in ASCII,
  the same name again in UTF-16LE, then uninitialized process memory used as padding.
- **Not a text document.** It holds no document content of any kind, and its padding is
  not reproducible data.
- **Threshold occurrences:** **zero**, in raw bytes and in every decoding attempted.
- **Disposition:** classified `none-office-owner-file` by the sweep — raw-scanned, no
  text layer to extract. Preserved byte-intact.

## Effect on V1
Neither object contains an occurrence of either disputed threshold. Neither can
contradict DEC-PROMO-01 or DEC-PROMO-02, because neither mentions them. The blocking
limitation recorded on 2026-09-06 is **resolved, not waived**: the bytes were retrieved
and audited in full, and the answer is negative.

## Residues that remain (not resolved, recorded)
1. **`untracked/momoneystudios-Exporting to Vercel`** — a gitlink to commit
   `f13aa940e6649ddb2b539f501a4750a94ee10f7e` with no `.gitmodules` entry and no
   checked-out bytes. Nothing exists in this commit to audit. It is a deployment-export
   pointer, not a Maestro doctrine source. Waived explicitly and by name in the sweep's
   `WAIVED` register so the waiver is auditable rather than tacit; carried in OPEN.
2. **Four non-textual assets** — `mosaic.paint` (HEIF), `favicon.ico`, a PNG cache blob,
   and a Windows `.lnk` shortcut. Raster and shell-link formats hold no text layer to
   extract. Raw-byte scanned; listed by hash in `V1_OBJECTS.csv`.
3. **PDF text extraction is extraction, not ground truth.** A scanned or image-only page
   yields no text and would read as an absence. The corpus PDFs audited here all yielded
   real text, but this remains a bounded limitation of the method, stated rather than
   assumed away (M16: absence is never assumed, only recorded).
