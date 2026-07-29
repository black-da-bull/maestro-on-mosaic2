# SCHEMA_SET

## USTF Schema (structure-only; content inserted at run-time)
- ordered_sections: [Intro, Verse, PreChorus, Chorus, PostChorus, Bridge, Outro]
- constraints:
  - no_cross_bar_fills: true
  - topline_suppression_for_rehearsal_beds: true
  - spatial_plan_enforced: true
  - negative_space_windows: "configured per section"
  - syllabic_window: "6-10"

## Validator Schema
metric_family -> { inputs, method, thresholds, pass_fail }
- CLAP / FAD / MFCC / Motif / DFA / MOS

## Gate Schema (N12..N16)
finding -> { evidence, metrics_slice, recommendation }

## E2E Run Schema
{ intake, ToT, UST, validators, rights, remix, HPA, DSP, packaging, versions }

## Artifact Schema
filename -> { purpose, producer, consumer, required_before, required_after }
