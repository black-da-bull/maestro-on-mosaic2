# Maestro audio-analysis execution process v0.6

This process turns the audio-analysis roadmap into an evidence-producing implementation sequence. It is intentionally recursive: every new model result is compared with existing project evidence, contradictions are retained, and only the smallest justified next capability is promoted.

## Authority invariant

The execution order is:

```text
immutable source artifact
-> deterministic measurement
-> labeled model inference
-> cross-surface calibration
-> advisory synthesis
-> operator listening judgment
-> replicated observation
-> candidate renderer heuristic
-> operator-approved policy/canon change, if any
```

No model worker may directly mutate Technical UST, Creative UST, canon, renderer policy, keeper status, master status, release status, or numbered operator-close items.

## Gate 0 — Freeze the evidence target

Before model execution, record:

- project and artifact logical IDs;
- exact source SHA-256;
- artifact role as observed from content, not provider label alone;
- renderer/model/version and known Studio state when relevant;
- existing deterministic analysis ID;
- comparison evidence that must remain distinct (for example Studio header tempo versus MIDI tempo map).

If the artifact hash changes, the analysis is a different run.

## Gate 1 — Worker-core proof

The worker must pass all of the following without a heavyweight model:

1. authenticated gateway-to-worker request;
2. immutable source retrieval;
3. source SHA verification before and after analysis;
4. durable queued/running job recovery;
5. strict result envelope;
6. explicit authority boundary;
7. core container build.

The always-available statistical descriptor exists only to prove this path. It is non-semantic and is never promoted as a quality score.

## Gate 2 — Artifact transport proof

A remote worker may retrieve a missing object only from a configured trusted base using the SHA-derived path:

```text
<base>/objects/<first-two-sha-characters>/<full-sha256>
```

The request cannot provide an arbitrary URL. HTTPS is required except for localhost testing. Credentials, query strings, fragments, and redirects are refused. The downloaded bytes are streamed through a size limit, hashed, and imported into the immutable store only when the expected SHA matches.

For large Suno/Studio packages, transport and analysis remain separate. The artifact store may contain multi-GB packages while individual analysis jobs select only the files they need.

## Gate 3 — Model-profile provisioning

Each heavyweight model receives its own dependency environment even when it runs in the same deployable worker image. This prevents one research stack from changing the worker-core runtime.

A profile is not `configured` merely because source code imports. Production readiness requires:

- pinned upstream repository/package revision;
- locally provisioned model/checkpoint artifact where the upstream permits it;
- checkpoint/model-directory hash in the result;
- explicit CPU/CUDA/MPS execution condition;
- one real inference smoke;
- output schema validation;
- license/provenance record.

Current profiles:

- Beat This — beat/downbeat and tempo evidence;
- SongFormer — song-section inference;
- ChordMini — chord-segment inference;
- Basic Pitch — lightweight AMT;
- tsumugi — advanced instrument-agnostic AMT;
- CLAP — audio/text embeddings;
- audio-language reasoner — advisory synthesis over already measured evidence.

## Gate 4 — Bitter Thank You calibration

`Bitter Thank You` is the current real-project calibration target. The calibration record must keep each evidence surface separate.

### Beat This

Run on the exact source WAV and record beats, downbeats, raw median-IBI tempo, interval variation, checkpoint hash, backend, and runtime version. Compare rather than collapse:

- Studio project/header BPM observation;
- Suno MIDI tempo-event distribution;
- deterministic fallback tempo estimates;
- Beat This result.

Half-time and double-time relationships are valid hypotheses and must not be coerced into an exact BPM match merely to make the sources agree.

### SongFormer

Infer sections from the exact audio artifact and compare the detected sequence/boundaries with the declared lyrics/MAP structure. Preserve label disagreement and boundary error. Model output is structure evidence, not a replacement for MAP.

### Harmony and AMT

Run ChordMini, Basic Pitch, and tsumugi on the most appropriate surfaces. Prefer stem-level AMT where model guidance indicates simpler single-instrument material is more reliable. Compare generated transcription summaries with Suno-exported MIDI while preserving timing, pitch, instrument, and tempo disagreements.

## Gate 5 — Embedding calibration

CLAP embeddings are stored as model outputs with model/checkpoint provenance. Similarity thresholds are project-specific.

A threshold cannot be promoted until the labeled corpus is large enough to evaluate positives and negatives independently. The current A/B preference from one song is evidence for corpus construction, not enough evidence for a universal threshold. Silent or malformed artifacts are excluded or explicitly labeled invalid; they are not silently reused as musical negatives.

No `quality_score` is permitted.

## Gate 6 — Audio-language advisory synthesis

The reasoner consumes references to DSP/MIR/model evidence rather than being asked to re-invent those measurements. Every claim must carry evidence references. Contradictions are first-class output and are never deleted merely because one interpretation sounds cleaner.

A useful advisory result says, for example, that two tempo surfaces disagree and why that may matter. It must not rewrite the evidence into a single invented truth.

## Gate 7 — Controlled Suno v6 experiment

For renderer-learning experiments:

1. freeze the starting state;
2. capture exact renderer/version/settings;
3. define one meaningful independent variable;
4. generate repeated takes for each condition;
5. preserve every returned artifact and provider response;
6. measure outputs using the same analysis pipeline;
7. collect operator listening decisions separately;
8. mark first-run findings as `observation` only.

For the staged Bitter Thank You experiment, the independent variable is tempo instruction strategy while lyrics, style/reference material, model and other settings remain fixed. Replication is required before a renderer heuristic can be proposed.

## Gate 8 — Promotion decision

A capability may move from experimental to normal Maestro use when:

- the runtime path is reproducible;
- checkpoint/model identity is recoverable;
- failure/unavailability is represented honestly;
- output has been calibrated against real project evidence;
- false-confidence conditions are documented;
- the result improves a real operator decision or reduces repeated manual analysis.

A renderer heuristic may move from `observation` to `candidate` only after replication. Moving from `candidate` to renderer policy requires operator approval and must preserve the evidence that supported and contradicted it.

## Recursive continuation rule

After every completed gate, recompute the blocker set:

```text
what is now proven?
what remains only configured?
what failed?
what new contradiction appeared?
what is the smallest next experiment that can resolve it?
```

Do not advance a model because it is fashionable or available. Advance it when its output closes a concrete Maestro decision gap.
