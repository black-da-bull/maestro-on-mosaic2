# Acceptance & Deferred-Runtime Test Plan — Current v0.1 (O-16 Stage 3)
## Executable now (workspace-native oracle checks)
A1 schema parse: MANIFEST + all yaml blocks parse. A2 internal references: every cross-file
reference in 00–10 resolves. A3 axis parity: PER everywhere (the retired four-letter variant must not appear); MAP never an active axis;
VIS only in module contexts. A4 source anchors: each file cites its ruling/source basis.
A5 gate arithmetic: SEM weights sum 100; composite formula stated; 97.5 floor present.
A6 container rules consistency: 02 rules match the persisted floor. A7 post-application hashes
(T8): on-device hashes of the 5 annotated files match annotation_hashes.json.
A8 cold-LOAD validation: a cold workspace reloads this folder + manifest and re-validates
A1–A6 without originating context. [relabeled per O16B — proves portability/parse/comprehension]
A9 deterministic cold regeneration: run build/build_maestro_current.py in a CLEAN directory;
the produced bundle must be byte-identical to the accepted bundle (diff = empty). A2 is extended
to shorthand references ("documented in 08" style), not only NN_FILE.md tokens.
## Deferred until executable runtime (obligations, not failures)
D1 QAF/PD enforcement wiring · D2 lyric-lock behavioral fixture · D3 CAP 4960–4999 live emission ·
D4 SEG gate execution + representative end-to-end triad fixture (seed → locked UST → three
surfaces → Suno prompt) — the triad fixture graduates to executable-now once the runtime exists;
until then a DRY-RUN fixture (template instantiation walk) stands in.
