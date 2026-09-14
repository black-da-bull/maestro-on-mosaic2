# Maestro P0 Workforce + Technical UST Runtime

This directory materializes the accepted **13 audio workers**, the P0.2 Technical UST ownership/dependency overlay, the P0.3 executable structural-interpretation layer, and the v0.5 **audio-analysis orchestration boundary**.

The runtime keeps two things separate on purpose:
- employee descriptors define bounded worker identity, domain authority, writable lanes, challenges, and non-authority;
- `technical_ust_ownership_dependency_overlay.yaml` binds actual Technical UST axes/keys/subkeys and crossstream dependencies.

A broad worker dispatch is **not** proof of canonical address ownership. `technical_ust_runtime.py` must resolve the requested Technical UST address through the overlay before an address-authorized dispatch or mutation can occur.

## Files
- `canonical_employee_module_spec.yaml` — schema for one bounded employee module.
- `canonical_13_employee_instances.yaml` — exactly 13 current audio-worker instances.
- `employee_workforce_registry_contract.yaml` — registry/runtime boundary after P0.2 integration.
- `technical_ust_ownership_dependency_overlay.yaml` — materialized address ownership, required reviewers, and dependency edges.
- `workforce_runtime.py` — list/show/broad dispatch-envelope runtime.
- `technical_ust_runtime.py` — address dispatch, state mutation guard, dependency propagation, lawful peer blocking, lyric lock, and `MAP.K3` reference invalidation.
- `golden_structural_interpretation_fixture.py` — P0.3 executable proof fixture.
- `audio_analysis_gateway.py` — lightweight v0.5 worker contract, strict renderer-learning validation, and fail-closed proxy boundary for Beat This/SongFormer/harmony/AMT/embeddings/audio-language analysis.
- `audio_analysis_contract_fixture.py` — deterministic gateway/authority regression fixture.
- `validate_workforce.py` — fail-closed integrated validator.
- `requirements.txt` — runtime Python dependency for YAML parsing. Heavy MIR/model dependencies are intentionally not installed in the web runtime.

## P0.3 golden fixture

The fixture executes a controlled structural delta and must prove all five behaviors:
1. `THY.K3.S2` dispatches to Dave from explicit overlay ownership rather than role-name inference.
2. A Dave-owned rhythmic-theory change reopens the supported `THY.K3 -> LYR.K4` dependency.
3. Vanessa can own integrated `PER.K2`, while Dave's lawful rhythmic objection still blocks final acceptance.
4. Dependency review does not authorize a lyric rewrite: locked `LYR` state remains unchanged without explicit operator authorization.
5. When `MAP.K3.S1` references `THY.K3.S2`, changing that upstream address reopens the exact referenced section entry (`MAP.K3.S1@Chorus`).

## Audio-analysis v0.5 integration boundary

The deployed web runtime does **not** execute heavyweight MIR/GPU models inline. It validates identity/provenance and submits jobs to a separately deployed durable worker through `MAESTRO_AUDIO_WORKER_URL`.

Supported experimental adapter IDs are:

- `beat_this`
- `songformer`
- `chordmini`
- `basic_pitch`
- `advanced_amt`
- `clap`
- `audio_language`
- `statistical_embedding`

Every audio-analysis request must reference an already-completed deterministic analysis and a lowercase SHA-256 source identity. Unknown fields or adapters fail closed. When no worker is configured, job submission returns an explicit unavailable state rather than pretending inference ran.

Authority is fixed at the gateway:

```text
deterministic measurement
-> labeled model inference
-> calibration evidence
-> operator listening judgment
```

Experimental output cannot directly mutate Technical UST, promote canon, approve a keeper/master/release, or create a renderer policy.

### HTTP surfaces

- `GET /api/audio-analysis/capabilities` — adapter registry, worker configuration state, and authority boundary.
- `POST /api/audio-analysis/jobs` — submit a validated asynchronous analysis job to the external worker.
- `GET /api/audio-analysis/jobs?job_id=...` — retrieve external worker job state.
- `POST /api/renderer-learning/validate` — validate experiment, operator-assessment, or heuristic records without persistence or automatic promotion.

### Worker configuration

- `MAESTRO_AUDIO_WORKER_URL` — base URL of the durable analysis worker. Absence is a valid fail-closed configuration and causes job submission to return 503.
- `MAESTRO_AUDIO_WORKER_TOKEN` — optional bearer token for the worker transport. It remains server-side.

This gateway does not claim that Beat This, SongFormer, ChordMini, Basic Pitch, advanced AMT, CLAP, or an audio-language model has executed merely because the adapter exists. Adapter availability and successful inference are separate evidence states.

## Run
```bash
cd runtime/maestro-workforce
python -m pip install -r requirements.txt
python validate_workforce.py
python golden_structural_interpretation_fixture.py
python audio_analysis_contract_fixture.py
python workforce_runtime.py list
python workforce_runtime.py dispatch Dave --task "evaluate pocket readability"
```

The four visual-module roles remain outside this audio runtime. Historical Isla/Huan and Melony records remain historical strata and are not silently added or conflated.

The P0 workforce runtime still does not claim 13 autonomous LLM processes. The audio-analysis worker boundary is separately scoped and may host model-backed MIR inference without widening workforce or Technical UST authority.
