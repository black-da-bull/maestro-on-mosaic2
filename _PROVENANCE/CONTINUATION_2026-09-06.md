# Supersession pointer — 2026-09-08

Current continuation: [CONTINUATION_2026-09-08.md](CONTINUATION_2026-09-08.md).
The promotion below is complete and merged through PR #4; P0 is merged through PR #9. PR #10 is an open calibration draft. Earlier PARTIAL, merge-pending, O-19/O-20 and P0-next instructions below are historical, superseded by the promotion close, DEC-PROMO-14/15 and subsequent merge records. No repeat corpus audit is authorized. The original packet follows unchanged.

---
# Continuation packet — promotion 2026-09-06 (resume run)
Doctrine: **Your Vision. Our Mission.**
Branch `promotion/2026-09-06` → resume branch `claude/resume-promotion-2026-09-06-l35t85`.
Baseline `88cd150cceacaebe79a3a0e97edb50497cc59a47`.
STATE rung reached: **persisted**. Runtime-enforced: **not claimed.**

## Status
**V1 CLOSED. The promotion candidate's recorded blocker is discharged.**
Promotion completion beyond that is an operator decision, not a check result. Nothing
here merges to main, and no deployed song-runtime behavior is asserted.

## What the resume run found first
`PROMOTION_2026-09-06.md`, `STATE.md`, `OPEN.md` and `LEDGER.md` all cite five packet
artifacts as the run's evidence: `IMPACT.csv`, `DECISION_OUTCOMES.json`,
`VALIDATION.md`, `SOURCE_LIMITATIONS.md`, `CONTINUATION_2026-09-06.md`. **None of them
was ever committed.** Only `BASELINE.json` and `DECISIONS.json` landed. The citations
were written as though the artifacts existed.

That is STATE rule 7 (M1) failing on the record that was itself enforcing it: *nothing
operative lives only in conversation.* It is also REGISTRATION ≠ APPLICATION in a new
place — the 2026-07-19 lesson was about rulings recorded but not rebuilt through
artifacts; this is evidence *cited* but not written. The pattern survived the lesson
because the citation reads identically whether or not the file landed.

The defect is registered in OPEN as **O-19**, not harmonized away. The five names now
resolve, but only one of them (`SOURCE_LIMITATIONS.md`'s subject) could be re-derived
from the corpus; the others are fresh work, labelled as such in their own headers.
**No prior text was reconstructed, paraphrased, or invented.**

## What was done
1. **V1 executed in full.** `promotion_2026-09-06/v1_occurrence_sweep.py` — a two-layer
   (raw-byte + container-extracted) sweep of every object the commit tracks. 4,751
   objects, 3,284 occurrences, 23 on current surfaces and every one scoped, 0
   violations, 0 unresolved, 0 Layer-A/Layer-B discrepancies. Byte-identical across two
   independent runs. Evidence: `V1_OCCURRENCES.csv`, `V1_OBJECTS.csv`,
   `V1_COVERAGE.json`.
2. **The two blocked objects were retrieved and audited byte-for-byte.**
   `Today.txt` (CP1252, 184,731 bytes, 38 non-ASCII bytes all typographic) and
   `~$Today.txt` (162-byte Word owner file). Neither contains either threshold family.
   Resolved, not waived. See `SOURCE_LIMITATIONS.md`.
3. **V2–V10 re-executed**, not carried over on trust. `validate_bundle.py` PASS ·
   `test_promotion.py` 33/33 PASS · builder run twice into clean directories, 41 members
   byte-identical · `compile_current.py` run twice, 3 topology outputs byte-identical to
   `maestro-current/compiled/`. See `VALIDATION.md`.
4. **Packet completed:** `IMPACT.csv` and `DECISION_OUTCOMES.json` re-derived from
   `DECISIONS.json` plus commit evidence in `88cd150..5e701d8`; `VALIDATION.md`,
   `SOURCE_LIMITATIONS.md` and this file authored in the resume run.

**No bundle member was modified.** The V1 tool lives in `_PROVENANCE/`, outside
`maestro-current/`, so MANIFEST hashes are untouched and the 2026-09-06 build stands
exactly as it was recorded. This window authorized no next-phase development and none
was performed.

## Substantive finding to carry
The corpus's strongest surviving *universal-floor* phrasings — "97.5% release
threshold", "97.5% default threshold", "enforced at three layers (default param, ...)"
— live in `artifacts/D-Maestro/canon/who dat.pdf` and
`artifacts/D-Maestro/sources/claude-session051526.oxps`. **Both are container formats
that a text-only scan cannot read.** Every one is historical evidence and none sits on
a current surface, so DEC-PROMO-01/02 hold. But a corpus check that greps text files
would have reported clean while missing exactly the passages most likely to be
mistaken for current canon. Any future corpus claim — coverage, absence, "not found
anywhere" — must extract containers or state that it did not (M16: absence is never
assumed, only recorded).

## Open, and deliberately not closed here
- **O-19** — the unpersisted-artifact defect above. Method-level; needs an operator
  ruling on whether a citation-resolves check joins the V&V gate.
- **V6 and V7 are read-verified, not machine-gated.** No executable check asserts the
  provenance issue fold or the Suno boundary separation, so both can drift silently.
  Closing that means extending `test_promotion.py`, which changes a bundle member and
  its MANIFEST hash — next-phase work, outside this window.
- **V1 residues, recorded and hash-pinned in `V1_COVERAGE.json`:** one unresolvable
  gitlink (`untracked/momoneystudios-Exporting to Vercel` → `f13aa940…`, no
  `.gitmodules`, no bytes) and five non-textual assets. PDF extraction is extraction,
  not ground truth: an image-only page would read as an absence.
- Untouched by this run, per their recorded scopes: O-04, O-05, O-06, O-07, O-08, O-09,
  O-10 residue, O-11, O-12, O-14, O-15, O-17, O16E, and the external skill re-upload.

## Next-work order (unchanged from the 2026-09-06 fold; still gated on operator)
P0: executable 13-worker instances / workforce registry → Technical UST ownership and
crossstream dependency overlay → first genuine golden structural-interpretation fixture.
P1: empirical B3 baselines → O-05 suppressed-output / coverage replay.
P2: recover original O-12 assets → Seedance musical-fit experiments.

Ahead of P0, two items this run surfaced: close O-19 (operator ruling), and machine-gate
V6/V7 when a window authorizes touching bundle members.

## Six E's — session close
- **Extension:** V1 extended from a text-file grep to a two-layer sweep over every
  tracked object, containers included.
- **Enhancement:** magic-byte format dispatch, BOM-gated UTF-16, bounded numeric tokens
  (`997.55859` no longer reads as `97.5`), and a Layer-A/Layer-B cross-check that makes
  a missed extraction visible instead of silent.
- **Exemplification:** the two blocked objects, audited byte-for-byte, with the finding
  stated plainly — zero occurrences in either.
- **Explanation:** the citation-without-persistence defect named as O-19, with why it
  slipped past the REGISTRATION ≠ APPLICATION lesson that should have caught it.
- **Impact propagation:** STATE, OPEN and LEDGER appended; the five dangling citations
  now resolve; `DECISION_OUTCOMES.json` re-derives every decision's application status
  against the tree rather than restating the prior run's summary.
- **Application re-optimization:** the sweep is committed and reproducible, so V1 is a
  re-runnable gate rather than a one-time session result — and it excludes its own
  output so re-running it is idempotent.


## Promotion reconciliation — 2026-09-07 (supersedes prior completion interpretation)
PARTIAL — NOT PROMOTION COMPLETE. Exact operator V1–V10 bindings and current continuation: `promotion_2026-09-06/RECONCILIATION_2026-09-07.md`.
Original missing evidence has been recovered from this conversation workspace and persisted with Git hash verification (RECOVERED_FILES.json). Earlier statements that this evidence no longer existed are superseded; prior prose is retained.
O-19 missing-file aspect is repaired; no new universal governance rule is inferred. The actual second original retrieval gap was SYSTEM_GRAPH_IMPROVED.json, not the inferred Word owner file. Later raw-sweep records remain useful evidence, but this review cannot independently establish full-corpus V1. Current bundle checks pass, with all 41 members matching remote and two clean builds; no deployed-runtime claim. No merge or downstream work until V1 is established. The existing operator instruction already authorizes promotion once blocking checks pass.
O-03/O-13 CLOSED; O-04 provenance-only; O-05 forensic_replay_required; O-12 external_asset_preservation_blocker; Q1–Q16 PHANTOM. External preservation and experiments retain their non-audio-blocking scopes.
