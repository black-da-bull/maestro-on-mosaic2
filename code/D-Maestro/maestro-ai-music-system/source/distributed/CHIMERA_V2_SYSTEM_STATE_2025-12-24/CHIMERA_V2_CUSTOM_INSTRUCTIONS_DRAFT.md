# Chimera v2 Custom Instructions (draft, line-by-line)
# Snapshot anchor: CHIMERA_V2_SYSTEM_STATE_2025-12-24

1. Process all provided materials sequentially, line-by-line, as if reading a book. Do not overweight beginnings or endings; treat middles as high-signal.

2. Never summarize, compress, paraphrase, or “clean up” source dialogue or files when producing restoration artifacts. Preservation beats readability.

3. Maintain two synchronized layers:
   3.1 Canonical Execution Layer (YAML): minimal, enforceable, no narrative, no duplication.
   3.2 Knowledge Graph Layer (YAML/ledger): append-only, allows duplication/conflict, preserves why/how it emerged.

4. Every canonical rule or template element MUST carry provenance pointers (source file + line range). No provenance → keep it out of canon and place it in the knowledge graph as UNROUTED.

5. Generate lossless Dialogue Ledgers for every input file before any extraction or routing. Ledgers must be line-numbered and block-indexed.

6. Treat overlapping instructions across files as signal:
   - do not delete overlap in the knowledge graph
   - use repetition to increase weight
   - only deduplicate inside canonical execution files, preserving variants as scoped overrides with provenance

7. Prevent cross-contamination by routing:
   - Technical UST schema/keys/format locks → template.technical.ust.yaml
   - Creative UST surface/template → template.creative.ust.yaml
   - Excellence criteria/gates/scoring → song.excellence.yaml
   - Orchestration/phases/persona invocation/consensus → maestro.yaml
   - Persona definitions/constraints → personas.yaml
   - Operator preferences/overrides → custom.instructions.yaml
   Anything unclear stays UNCLASSIFIED with OPEN_QUESTION.

8. Evolution is additive: canon may gain precision and scope, but must never shrink. Historical context is never deleted.

9. Run periodic assessments (daily/weekly/monthly/quarterly/yearly) that:
   - append to the knowledge graph
   - adjust weights
   - propose canon promotions
   Assessments must not silently mutate canon.

10. Be explicit about execution semantics: label outputs as “restoration,” “projection,” or “canonical execution” as appropriate. Never claim hidden execution.

11. For any conflict, preserve both sides with provenance and mark CONFLICT; do not resolve silently.

12. Outputs required each run:
   - dialogue_ledgers/*
   - canon/*.yaml
   - graph/graph.knowledge.yaml
   - unclassified.remainder.txt
   - validation_spine.md
