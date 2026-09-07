# Validation — promotion 2026-09-06 (resume run)
Doctrine: **Your Vision. Our Mission.**
Baseline `88cd150cceacaebe79a3a0e97edb50497cc59a47` · branch `promotion/2026-09-06`.
Build-time validation of a workspace bundle. **No deployed song-runtime enforcement is
claimed by any check below.**

## What this file is, and is not
`PROMOTION_2026-09-06.md` and LEDGER `PROMOTION-2026-09-06 — application checkpoint`
cite `promotion_2026-09-06/VALIDATION.md` as the final run evidence. **It was never
committed.** This file does not reconstruct it and does not restate its verdicts on
trust. Every result below was produced by re-executing a check in the resume run
against the working tree at this branch's head.

The labels V1–V10 come from the decision records (`DECISIONS.json`
`required_validation`). The file that defined them is among the unpersisted artifacts,
so **the bindings below are the resume run's own**, derived from each decision's
subject matter. Where a check is read-verified rather than machine-gated, it says so.

## V1 — full-corpus threshold-occurrence coverage · **PASS**
The check that was `PARTIAL` on 2026-09-06 and blocked promotion completion.

**Question.** Does any occurrence of the two disputed threshold token families,
anywhere in the corpus, assert a *current* universal numeric release floor — which
would contradict DEC-PROMO-01/02?

**Method.** `v1_occurrence_sweep.py` (committed beside this file) enumerates every
occurrence across every object the commit tracks, in two layers:
- **Layer A** raw-byte scan — `latin-1` never fails, so every literal ASCII form is seen.
- **Layer B** decoded / container-extracted scan — reaches forms Layer A cannot see:
  UTF-16 text, deflate-compressed OOXML and OXPS parts, PDF content streams.
Format is decided by **magic bytes first, extension second**. That is load-bearing: two
corpus PDFs decode cleanly as `cp1252`/`utf-16` by coincidence, and routing them to a
text scan would have read their compressed streams as noise and missed their real text.
A Layer A hit in an object where Layer B found nothing is reported as a discrepancy
rather than silently trusted.

**Result.** Figures from the sweep as committed, run at this branch head; the audited
promotion candidate's figures are shown beside them.

| | at branch head (committed evidence) | at audited candidate `5e701d8` |
|---|---|---|
| Objects scanned | 4,750 | 4,751 |
| Objects needing a fallback encoding or a container extractor | 32 | 32 |
| Occurrences enumerated | 3,283 | 3,284 |
| — historical record (preserved evidence, unconstrained) | 3,142 | 3,142 |
| — provenance record (`_PROVENANCE/`, append-only) | 118 | 119 |
| — **current surfaces (`maestro-current/`)** | **23, every one scoped** | **23, every one scoped** |
| Unqualified current-surface occurrences (violations) | **0** | **0** |
| Superseded phrasing on current documentation surfaces | **0** | **0** |
| Layer A / Layer B discrepancies | **0** | **0** |
| Objects unresolved | **0** | **0** |
| Objects waived (named, hash-pinned) | 1 gitlink + 5 non-textual assets | same |

Encodings actually required: UTF-8 ×4,718 · UTF-16 (BOM-gated) ×7 · CP1252 ×1.

**Why two columns.** The sweep excludes its own packet directory: `V1_OCCURRENCES.csv`
quotes thousands of matched snippets verbatim, so scanning it would count this check's
output as corpus evidence and the totals would grow on every run. That exclusion landed
after the first measurement. The committed `V1_*` files are the branch-head run, so
re-running the tool as committed reproduces them exactly; the right-hand column is the
audited promotion candidate. The difference is one provenance object and one provenance
occurrence — this run's own records, plus the two packet files that moved inside the
exclusion. **Every constrained figure is identical in both columns**, which is what the
verdict rests on: nothing skipped by the exclusion is a class the check constrains.
Records outside the packet directory carry the resume run's prose deliberately
threshold-token-free, so appending to them does not move these counts.

**Two findings worth carrying forward.**
1. The strongest surviving *universal-floor* phrasings in the whole corpus — "97.5%
   release threshold", "97.5% default threshold", "enforced at three layers (default
   param, ...)" — live in `artifacts/D-Maestro/canon/who dat.pdf` and
   `artifacts/D-Maestro/sources/claude-session051526.oxps`: **container formats a
   text-only scan cannot read.** All are historical evidence; none sits on a current
   surface. Preserved byte-intact, per DEC-PROMO-01's preservation clause.
2. The blocking limitation is **resolved, not waived**. Both blocked objects were
   retrieved and audited byte-for-byte; neither contains either threshold family at
   all. See `SOURCE_LIMITATIONS.md`.

**Reproduce.** `python3 _PROVENANCE/promotion_2026-09-06/v1_occurrence_sweep.py .`
Exit 0 = PASS. Two independent runs in this session produced byte-identical
`V1_OCCURRENCES.csv`, `V1_OBJECTS.csv` and `V1_COVERAGE.json`.

## V2–V10 — re-executed this run

| Check | Subject | Result |
|---|---|---|
| V2 | SEM configuration and arithmetic | **PASS** — `validate_bundle.py`: 12 weights summing to 100, `score_max: 5`, `threshold_selection: explicit_applicable_context`, `default_threshold: null`, composite formula present |
| V3 | Technical UST authority chain and Suno boundary | **PASS** — `test_promotion.py`: "Creative is derived from locked Technical"; "lock precedes reverse compilation" |
| V4 | Workforce scope | **PASS** — `test_promotion.py`: 13 audio workers, visual roles a separate module set |
| V5 | Phantom Q1–Q16 | **PASS** — `test_promotion.py`: `05_GOVERNANCE_SEG.md` carries "Q1–Q16 = PHANTOM (never fabricate)" |
| V6 | Provenance issue fold | **PASS (read-verified)** — STATE "Current issue fold" (7 rows) and OPEN "Current classification fold — 2026-09-06" both present and mutually consistent |
| V7 | Suno boundary separation | **PASS (read-verified)** — `00_ROOT_SPEC.md:61-64` keeps generation/model adapter, renderer grammar and Studio/editing distinct from canonical UST |
| V8 | Scoped-policy gate | **PASS** — `test_promotion.py`: a policy missing any of threshold/scope/context_ref/authority_ref is rejected, as are `scope: global`/`universal`, NaN/inf/bool/out-of-range thresholds, and an absent policy |
| V9 | Deterministic regeneration | **PASS** — `build_maestro_current.py` into two clean directories: 41 members, both byte-identical to each other and to source (exit 0). `compile_current.py` twice: 3 topology outputs byte-identical to `maestro-current/compiled/` |
| V10 | Hash map and inventory completeness | **PASS** — `validate_bundle.py` A9/A10/A11 |

Aggregate re-runs: `validate_bundle.py` → `PASS`; `test_promotion.py` → `PASS: 33
promotion checks`.

**V6 and V7 are read-verified, not machine-gated.** No executable check asserts them,
so they can drift silently. That gap is carried in `CONTINUATION_2026-09-06.md`, not
closed here — extending the bundle's own test surface is next-phase work, and this
promotion window authorizes none.

## Verdict
**V1 through V10 PASS at their recorded scope.** The condition the 2026-09-06 record
named as the blocker on promotion completion is discharged.

What that does **not** settle, and no check here claims: deployed song-runtime
enforcement (never asserted), the O-05 forensic replay, O-12 asset recovery, the
Seedance experiment, or any next-phase build item. Merge remains an operator decision.
