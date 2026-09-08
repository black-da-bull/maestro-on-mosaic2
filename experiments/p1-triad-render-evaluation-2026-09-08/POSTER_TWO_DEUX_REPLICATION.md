# Poster Two Deux — independent renderer-instruction replication

**Date:** 2026-09-08  
**Status:** empirical calibration evidence; not canon; no promotion decision.  
**Doctrine:** Your Vision. Our Mission.

## Operator-corrected objective

This replication tests the primary empirical question for the current P1 work window:

> **Do renderer-facing Maestro instructions in the Creative UST / Lyrics surface and the external Style surface produce detectable musical and production behavior in Suno output?**

This is not primarily a test of whether Suno reproduces an exact manufacturer-specific Hammond B3 sound. Exact named-instrument identity is a narrower semantic-fidelity question and must not be allowed to reopen the broader renderer-instruction-uptake premise.

The Run It To Me calibration already established layer-specific prompt-to-audio adherence and named Poster Two Deux as the independent replication corpus. This document executes that replication against the Poster Two Deux assets preserved in the current work window.

## 1. Corpus normalization

### 1.1 Render-family views retained

The available Poster Two Deux evidence is normalized to the following generation-level lineage/views:

1. `base`
2. `v2`
3. `v4`
4. `v6b`
5. `style_change`

### 1.2 Export-mode duplicates are not independent generations

The following labels are treated as **derived export / analysis views**, not additional Suno generations:

- `fixed tempo`
- `follow tempo`
- `strict tempo`
- `follow timing`
- `strict timing`

Reason: decoded PCM comparison of sampled corresponding stems shows identical audio within the base fixed/follow, v4 follow/strict, and v6b follow/strict pairs even where compressed MP3 bytes differ. For v4, the follow/strict MIDI members are also byte-identical. For v6b, the follow/strict MIDI packages differ as MIDI extraction/interpretation views while corresponding decoded audio remains identical.

**False-PASS protection:** export multiplicity may not be counted as render replication.

## 2. Preserved provenance

### 2.1 Archive / full-render hashes

| Evidence object | SHA-256 | Notes |
|---|---|---|
| base MIDI follow | `7e3ea4d4b492de41ebc8907db203231877d08c274df54957ddde36d8be515a18` | 6 MIDI parts |
| base MP3 fixed | `9e10bb7e527fec84b3004f87b8ed6a12e50794ed0eedf224b7399a9c2ad458a5` | 7 separated stems |
| base MP3 follow | `1e31f23ec62e06e1872ad4c556ebc53f6d10ccf0cad1367a5cc17cfbcd6a29a6` | same render, alternate export view |
| v2 MIDI follow | `b7965b5db7445d383edcb01431ebe023f16cb99a90c4bb1871f0564bc6730ca3` | 7 MIDI parts |
| v2 MP3 stems follow | `3c2facb7222f4bd1dc9744f3c5fe61959f5e6f4fab709792499d9dee00e693a3` | 7 separated stems |
| v4 MIDI follow | `f326bb59b65fb0e24ad5dd92f4ab72ae425ac60e953d804778c77bcd8857cd00` | 11 MIDI parts |
| v4 MIDI strict | `ceb9863eccf574a8464ea9ff2bf936fc1de818d4e1e1a354c4bbbeec186bf804` | members byte-identical to follow view |
| v4 stems follow | `09517b478556b96b67b7ccce2f87e75ae15c9fb3880a77c40118bdc17bb84ba5` | 11 separated stems |
| v4 stems strict | `830b0196dd86a2aaf2dcc9c562880bbb908bbc5eb5823e63bf86a3301804c585` | same decoded audio, alternate export view |
| v4 full MP3 | `8d1da000148e7889c5420c0998e2167e7ca71a727eaf58cfb2fe0e1a67d5c8cf` | Suno asset ID below |
| v6b MIDI follow | `b47b282d45315717c3697cdf94eeeb5b19b6fc43f495daf3490a2ed5f8ade133` | 11 MIDI parts |
| v6b MIDI strict | `724df57ee62afe1d8b3ffdd991f9cacc2f6a0c8858ecb557182e1825b85a1979` | alternate MIDI extraction view |
| v6b stems follow | `a46cd06973d768dd93416f5b773d81aa2a833414daadc61ab9e33a307c6f7718` | 10 separated stems |
| v6b stems strict | `2163b024bb43a7e12d30ed2d37d00a8977f08002ec7d7d4640a76ebf4668b4f4` | same decoded audio, alternate export view |
| v6b full MP3 | `fe479496f082e229c209f174aeea7af0c306d09897793fa461363d960585ecd3` | Suno asset ID below |
| style-change stems | `e682fc90a60526c1bd6f70aa61cc481f914d3b5698009518231ca8e239e08630` | 10 separated stems |
| style-change full MP3 | `294d6dc08f6a08197f7eff162e010a421ebabae6c1dc0c4a883d4537f3c6aadf` | Suno asset ID below |

### 2.2 Full-render identities

| Render | Suno asset ID recovered from MP3 metadata | Full duration |
|---|---|---:|
| v4 | `976f0652-06a4-4e62-9e41-7ac7c16afc99` | ~213.17 s |
| v6b | `ac6e0fd3-1020-43f2-96f6-aa9c152b1443` | ~236.59 s |
| style_change | `544d4a09-736d-4615-a790-eef6a44ef19e` | ~240.89 s |

The full MP3 provenance also exposes Suno C2PA provider data with `systemVersion=chirp-fenix-t4`. This is recorded as embedded provenance only; it is not promoted here into an unsupported marketing-model/version equivalence claim.

## 3. Prompt recovery

### 3.1 v4 — lyrics-less Creative UST transformation grammar

The v4 full MP3 embeds a Creative UST / Lyrics-surface payload with SHA-256:

`4e560b17f2f17fbbcdc740c6ef32be410cfc2260351df61d12202ea75d28c3c6`

The payload is approximately 1,111 characters and is not a normal lyric body. It is transformation/execution grammar. It begins with the instruction that the orchestra must grow from the rhythm section rather than become a detached cinematic layer, then carries permitted transformation, arrangement, harmony, duration, performance-scale, drum, microtiming, dynamic-variation, and related execution directions.

**Evidence consequence:** a real Suno render exists whose Lyrics surface carries Creative UST execution grammar rather than ordinary lyric text. This directly supports the Maestro renderer-interface model that the Lyrics field can carry non-lyrical execution grammar.

It does **not** by itself prove that every instruction was obeyed. Adherence must still be assessed against the output.

### 3.2 v6b and style-change — near-controlled Creative UST pair

Recovered Lyrics-surface payloads:

- v6b SHA-256: `4e5c7c6de1c7577d36564ef3ae7088a895d05d0423882d95131430546da886b5`
- style-change SHA-256: `e850306d0ff6df22acbf1ead88750d82d3688b7626e3b442de1ad9ca3989c783`

The two payloads are materially the same structured lyric/control package. The observed text delta is one extra repeated final lyric line in the style-change payload:

`"We ain’t performin’—we activate."`

The shared control tail includes, among other directives:

- 5/8 feel at 142 BPM;
- trap-bounce behavior;
- three-tier low-end architecture;
- sub emphasis around 27–45 Hz;
- bass emphasis around 50–80 Hz;
- mid-bass emphasis around 100–160 Hz;
- mono low-frequency behavior below 120 Hz;
- narrower verses / wider choruses;
- choir lateral width and centered leads;
- detailed mix and performance behavior.

The exact external Style-box text is not embedded in these MP3s. The preserved asset is explicitly named `style change`, which is admissible provenance that this was a style-change work product, but the exact changed Style text remains a separate provenance gap. Therefore this pair can support **surface participation / sensitivity**, but not exact phrase-level causation.

## 4. Analysis method

The metric family is intentionally aligned with the Run It To Me calibration rather than changed after seeing the Poster Two Deux results.

Measurements include:

- audio rhythm autocorrelation / tempo family;
- MIDI tempo-map cross-check where MIDI is available;
- pitch-class description where useful, without inventing a tonal target not present in the recovered prompt;
- Bass-stem spectral energy below 100 Hz;
- stem activity proxies for guitar, keyboard, synth, and backing vocals;
- lead-vocal versus accompaniment RMS correlation as a conversational/responsive-arrangement proxy;
- p90–p10 RMS dynamic contrast;
- full-render duration where a full MP3 is present;
- provenance and prompt-payload comparison.

Separated-stem labels are treated as partition labels from Suno's separator, not proof of exact semantic instrument identity.

Stem files appear activity-trimmed, so stem-horizon duration is not treated as full-render duration.

## 5. Core measurement table

| Render | Analysis horizon / full duration | Tempo evidence | Bass <100 Hz | Guitar activity | Keyboard activity | Synth activity | BGV activity | Lead↔band corr | Dynamics |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|
| base | 138.90 s stem horizon | audio ~140.63; MIDI ~140.78 | 0.885 | n/a | n/a | 0.273 | 0.195 | -0.220 | 14.18 dB stem bus |
| v2 | 238.89 s stem horizon | audio ~140.63; MIDI ~71.23 (~142.47 double) | 0.815 | n/a | n/a | 0.559 | 0.185 | -0.149 | 14.53 dB stem bus |
| v4 | 129.54 s stem horizon / ~213.17 s full | audio ~140.63; MIDI ~68.49 (~136.97 double) | 0.619 | 0.092 | 0.076 | 0.551 | 0.156 | -0.231 | 10.76 dB full mix |
| v6b | 139.93 s stem horizon / ~236.59 s full | audio ~140.63; MIDI ~69.09 (~138.17 double) | 0.712 | 0.079 | 0.272 | 0.382 | 0.153 | -0.243 | 9.51 dB full mix |
| style_change | 170.08 s stem horizon / ~240.89 s full | audio ~140.63 | 0.758 | 0.013 | 0.001 | 0.369 | 0.208 | -0.178 | 10.91 dB full mix |

Activity numbers are relative threshold proxies inside the separated part, not instrument-performance scores.

## 6. Criterion-level replication verdicts

### 6.1 Creative UST use through the Lyrics surface — SUPPORTED

**Evidence:**

- v4 embeds a lyrics-less Creative UST transformation grammar in the Lyrics-surface metadata and has a corresponding real full render.
- v6b and style-change embed long structured lyric + execution-control payloads, again tied to real rendered MP3s.
- The generated audio contains measurable rhythm, low-end, dynamic, ensemble, and part-allocation behavior corresponding to classes of control present in those payloads.

**Limit:** this does not establish deterministic line-by-line obedience. It establishes renderer-facing use and output correspondence sufficient for an instruction-uptake claim.

### 6.2 Approximate / relational tempo control — SUPPORTED

Where the recovered v6b/style-change control specifies 142 BPM, the measured audio tempo family centers around ~140.6 BPM. Available MIDI frequently exposes the same behavior through half-time values near 68–71 BPM, corresponding to roughly 137–142 BPM when doubled.

This independently replicates the Run It To Me finding that the renderer preserves an approximate rhythmic/half-double relationship more reliably than an exact integer tempo lock.

### 6.3 Low-end architecture — SUPPORTED

Across the five Poster Two Deux render views, roughly 61.9%–88.5% of Bass-stem spectral energy falls below 100 Hz under the current analysis definition.

The v6b/style-change Creative UST explicitly asks for a tiered sub/bass/mid-bass architecture and mono low-frequency control. The output family therefore supplies strong signal-level evidence that the low-end instruction class survives into rendered behavior.

This independently replicates the strong low-end uptake observed in Run It To Me.

### 6.4 Responsive accompaniment / vocal-space behavior — SUPPORTED AS PROXY

Lead-versus-accompaniment RMS correlation is negative for every Poster Two Deux render view measured here (approximately -0.15 to -0.24).

That is consistent with accompaniment that changes around lead-vocal activity rather than maintaining one constant energy wall. It is signal-level proxy evidence, not a substitute for semantic listening judgments about taste or musicianship.

### 6.5 External Style-surface participation — SUPPORTED AS REPLICATION; EXACT PHRASE CAUSATION OPEN

The strongest Poster Two Deux comparison is v6b versus the explicitly labeled style-change render:

- Creative UST is nearly controlled: the only observed payload text delta is one repeated final lyric line.
- full duration changes from ~236.59 s to ~240.89 s;
- backing-vocal activity increases from ~0.153 to ~0.208;
- keyboard partition activity changes from ~0.272 to ~0.001;
- guitar partition activity changes from ~0.079 to ~0.013;
- full-mix dynamic contrast changes from ~9.51 dB to ~10.91 dB;
- v6b separator output includes Woodwinds while the style-change output includes Brass instead.

These are material renderer-output differences under a near-controlled Creative UST condition. Combined with the work-product identity `style change`, they independently support the Run It To Me conclusion that the external Style surface materially participates in the generated result.

**Not claimed:** which exact Style phrase caused which exact difference. The exact Style-box body is not embedded in the received binaries, and stochastic generation remains a confound.

### 6.6 Named instrument / manufacturer fidelity — SEPARATE SEMANTIC-FIDELITY PROBE

The primary instruction-uptake conclusion does not depend on proving exact manufacturer-specific Hammond B3 identity or any other named instrument from separator labels or spectral proxies.

Named-timbre fidelity can still be tested when musically useful, but it is a narrower criterion:

- separator `Keyboard`, `Synth`, `Brass`, `Woodwinds`, or `Guitar` labels are not sufficient semantic proof;
- exact timbral identity requires direct perceptual or stronger semantic-audio evidence;
- failure to establish a branded instrument identity must not erase demonstrated uptake in tempo, low-end, dynamics, ensemble behavior, or surface sensitivity.

## 7. Cross-corpus replication with Run It To Me

The two independent work windows now support the following evidence matrix:

| Claim | Run It To Me | Poster Two Deux | Cross-corpus state |
|---|---|---|---|
| Creative UST is present in real renderer-facing output lineage | supported | supported | **replicated** |
| Creative UST / Lyrics-surface execution grammar corresponds to measurable output behavior | supported | supported, including lyrics-less v4 grammar | **replicated** |
| approximate / half-double tempo behavior survives better than exact numeric lock | partial/supporting | supported | **replicated pattern** |
| low-end intent survives strongly | observed | observed | **replicated** |
| backing/ensemble response is detectable | generally supported | proxy supported | **replicated at signal-proxy level** |
| external Style surface materially participates in output | supported by B/C/D with controlled Creative UST serialization | supported by near-controlled v6b/style-change work product | **independently replicated** |
| exact Style phrase → exact audible consequence | unresolved | unresolved | **not established** |
| exact named-instrument / manufacturer fidelity | open where relevant | separate semantic probe | **not required for uptake conclusion** |
| deterministic exact render repeatability | not claimed | not claimed | **not established** |

## 8. False-PASS protections

Do not:

1. count fixed/follow/strict exports as separate generations;
2. infer exact instrument identity from separator labels;
3. infer exact phrase-level Style causation without the external Style text and a stronger control;
4. treat stochastic variation as eliminated;
5. use activity-trimmed stem duration as full-song duration;
6. infer a tonal-center failure where the recovered prompt does not specify the target;
7. collapse `instruction uptake`, `semantic timbre fidelity`, and `deterministic repeatability` into one binary score;
8. promote this calibration evidence into Maestro law without a separate promotion/acceptance action.

## 9. Replication conclusion

**Poster Two Deux independently replicates the central Run It To Me renderer-adherence finding.**

The combined evidence is sufficient to support the empirical conclusion that:

- Suno receives real Maestro Creative UST execution material through the Lyrics surface;
- classes of those instructions correspond to detectable musical/render behavior;
- the external Style surface materially participates in output variation under substantially controlled Creative UST conditions;
- instruction adherence is layer-specific rather than all-or-nothing;
- approximate/relational controls can be stronger than exact numeric controls;
- named-instrument authenticity is a narrower semantic-fidelity question and is not the general empirical gate.

The remaining provenance gap is chiefly the exact external Style-box text for the Poster Two Deux style-change comparison. That gap limits phrase-level causal attribution; it does **not** erase the replicated surface-participation evidence.

## 10. Result state

- **Creative UST / Lyrics-surface uptake:** SUPPORTED / REPLICATED
- **Style-surface participation:** SUPPORTED / INDEPENDENTLY REPLICATED
- **Approximate/relational tempo uptake:** SUPPORTED / REPLICATED
- **Low-end instruction uptake:** SUPPORTED / REPLICATED
- **Responsive ensemble behavior:** SUPPORTED AT SIGNAL-PROXY LEVEL / REPLICATED
- **Exact phrase-level causal mapping:** OPEN
- **Exact named-instrument identity:** SEPARATE / OPEN WHERE NEEDED
- **Deterministic repeatability:** NOT CLAIMED
- **Canon/runtime promotion:** NOT PERFORMED
