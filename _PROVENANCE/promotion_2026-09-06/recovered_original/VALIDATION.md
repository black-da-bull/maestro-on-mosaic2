# Promotion validation — 2026-09-06

**PARTIAL — NOT PROMOTION COMPLETE.** Current repairs pass; full occurrence coverage does not.

| Check | Result | Evidence |
|---|---|---|
| V1 | FAIL | Current universal floor removed; 2771 baseline 97.5 matches classified in reached source text. Complete repository coverage blocked by two unreadable historical text objects; SOURCE_LIMITATIONS.md. |
| V2 | PASS | Historical G≥7 source bytes preserved; current 05/STRATA separate mechanisms, no reinstatement. |
| V3 | PASS | 01 remains canonical; 02/03 and their templates unchanged by SHA256; regression verifies lock before reverse compilation. |
| V4 | PASS | 04 and its template unchanged by SHA256; 13 audio plus separate visual-module scope verified. |
| V5 | PASS | Current 05 and STATE mark Q1–Q16 phantom; earlier history preserved. |
| V6 | PASS | STATE current fold and appended OPEN classifications reconcile O-03/O-13 closed; O-04 provenance-only; O-05 replay; O-12 external preservation. |
| V7 | PASS | 15 explicit source/current-file references resolve with recorded migration aliases; bundle validator checks numbered and shorthand references. No referenced current artifact removed. |
| V8 | PASS | 40 manifest MD5 entries checked against actual bytes; hash-tamper negative test fails as expected; 41-member SHA256 inventory stored. |
| V9 | PASS | Two clean full regenerations byte-identical to repaired source bundle: 41 members including manifest; source compiler reproduces all three topology members exactly. |
| V10 | PASS | False-PASS review: sources repaired before generation; tests changed; history preserved; actual enforcement limited to build validators; full-audit limitation explicitly blocks promotion verdict. |

## Reproduce
From repository root:
```sh
PYTHONDONTWRITEBYTECODE=1 python _PROVENANCE/promotion_2026-09-06/verify_promotion.py .
```
The command reruns bundle validation, 33 regression checks, two clean rebuilds, three compiled topology comparisons, source-reference resolution, no-change hashes and current state markers. Exact outputs and 41 SHA256 values: VALIDATION_RESULTS.json. It does not waive SOURCE_LIMITATIONS.md.

## Diff and historical preservation
BASELINE_DIFF.patch records all original edited files. Git changes use the baseline tree and change only explicit paths: no historical deletions or source rewrites. Source templates were repaired before full bundle regeneration; the first build exit 3 correctly reported expected source-vs-generated drift, then installation of full builder output followed by two clean builds returned exit 0. No generated prose was hand-edited.

To reproduce source searching separately (requires the full checkout; never writes product files):
```sh
python _PROVENANCE/promotion_2026-09-06/scan_occurrences.py . /tmp/maestro-occurrence-review
```
The scanner reports unreadable sources and requires review of current matches. It cannot turn incomplete coverage into PASS. Before/after occurrence CSVs record their specific scan snapshots; final report echoes are correction evidence, not newly applicable source policy.
