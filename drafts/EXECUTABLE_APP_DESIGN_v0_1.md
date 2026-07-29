# Maestro Executable Application — System Design v0.1
**Work item:** DESIGN.O16.EXECUTABLE-APP.R1 · 2026-07-19 · rung: PROPOSAL (operator review gates
promotion; per P-4 the workspace-native bundle remains the accepted specification and test oracle
— this design implements it, never overrides it)
**Scope assumption (stated, per M12/unattended discipline):** design the executable Maestro
runtime (P-4 phase 2, discharging D1–D4) plus the two substrate subsystems this session proved
necessary — the history-grounded canon store (M17) and the ruling-propagation engine
(registration ≠ application). Chimera/Mosaic substrate modeling and the public website are out of
scope here.

---

## 0. The insights this design is built from

Every architectural choice below traces to something this session established the hard way:

1. **The compiler shape holds** (ontology): creative seed → Technical UST (IR) → Suno (target).
   One app; Mosaic is the substrate via contract (P-1). The executable is a compiler with a
   staffed, adversarial middle — not a chat wrapper.
2. **DEC-27:** the UST and its governance are ONE UNIT — gates act *as the nulls are replaced*.
   So gating is an event subscription on fills, not a pipeline stage after them.
3. **M17:** the derivation basis is the entire project history, never a version. So "current
   canon" must be a *computed fold over chronology-ordered strata*, and version labels are
   packaging only. The canon store is event-sourced by construction.
4. **M16:** bundle ≠ system; absence ≠ nonexistence. So identity is content-hash, manifests are
   first-class, and a MISSING verdict requires a recorded search (the displaced-file re-binding
   proved content-addressing heals scatter).
5. **Registration ≠ application** (the R1 audit's meta-finding): a ruling recorded in a ledger
   but not rebuilt through artifacts AND tooling is a live defect. So rulings carry declared
   obligations, and the build gate fails while any obligation is undischarged.
6. **Determinism is the trust mechanism** (A9a/A9b, the V&V rounds): every derived artifact must
   be regenerable byte-identically from hash-verified sources, and every release package ships
   its own falsification kit (harness + sums + manifest).
7. **The v5b coldstart stratum supplies the executable vocabulary** (by chronology, DEC-22):
   work items (WI.*), the pinned council matrix, the evidence contract, phased chain P0–P5,
   stop-the-line, triad caps 4960–4999 / 960–999 / ≤150+1960–1999.

## 1. Requirements

**Functional.** Run one song end-to-end: intake seed → lyric lock → dual-scaffold init →
staffed sequential zero-skip fill with live gates → congruency round-robin → executive red-pen →
loop-until-pass → LOCK → FOIL reverse-pass → triad emission under caps, linkage-bound.
Additionally: fold any new session/stratum into canon (the bridge), and produce V&V packages on
demand.

**Non-functional.** Single operator (ROOT authority, interactive gates per M12). Determinism and
auditability over throughput — one song per run, minutes-scale latency acceptable; every step
resumable from its ledger. Zero silent behavior: the only failure mode is stop-the-line with
diagnostics + missing work items + dissent references. All state survives model replacement
(MODEL_PROFILE degradation rules carried from v5b).

**Constraints.** Python stdlib-first (matches every persisted tool); the repo at
`D:\maestro-on-mosaic` is SSOT (DEC-07); file-based contracts, no server, no DB at this scale;
SME workers are AI sessions/subagents; Suno boundary is manual paste today (browser automation
later).

## 2. High-level design

```
                        ┌─────────────────────────────────────────────┐
                        │  CANON FOLD STORE (CFS)          [M16/M17]  │
                        │  strata (chronology) · content-hash objects │
                        │  fold() -> materialized views (A9b-style)   │
                        └───────┬─────────────────────────┬───────────┘
              obligations       │ topology, rules,        │ strata in
              discharged?       │ seats, caps (views)     │ (bridge)
┌───────────────────────┐      │                          │
│ RULING LEDGER +       │◄─────┤                ┌─────────┴──────────┐
│ PROPAGATION ENGINE    │      │                │ SESSION→MAESTRO    │
│ [registration ≠       │      │                │ BRIDGE             │
│  application]         │      │                │ replay ×2 · ledger │
└──────────┬────────────┘      │                │ elicit (M12) ·     │
           │ gate: no build    │                │ apply · sweep      │
           ▼ while undischarged▼                └────────────────────┘
┌──────────────────────────────────────────────────────────┐
│ RUN ENGINE (one RUN = one song)                          │
│ P0 dual-scaffold ─ P1 intake+LYRIC LOCK ─ P2 staffed     │
│ fill (work items, council routing, evidence contract)    │
│        │ every fill emits UST Δ + SEM Δ together         │
│        ▼                                                 │
│ INTERWOVEN GATE ENGINE [DEC-24/27]                       │
│ SEG physics · SEM live scoring · SE20 · CAP pre · LOCK   │
│ fail ⇒ STOP-THE-LINE (diagnostics only)                  │
│ P3 meetings/red-pen ─ loop-until-pass ─ LOCK             │
│ P4 FOIL REVERSE COMPILER ─ P5 triad + telemetry          │
└──────────┬───────────────────────────────────────────────┘
           ▼
┌────────────────────┐        ┌──────────────────────────┐
│ TRIAD (linkage-    │        │ V&V INTERFACE            │
│ bound): Creative   │        │ deterministic package +  │
│ UST · Show Summary │        │ self-verifying harness → │
│ · A&R pack → Suno  │        │ external reviewer rounds │
└────────────────────┘        └──────────────────────────┘
```

## 3. Components (deep dive)

### 3.1 Canon Fold Store — M17 as architecture
The store holds **strata**, not versions: each stratum is a set of content-addressed objects
(sha256) + a chronology position + provenance class (KNOWN / PROBABLE / HISTORICAL / UNVERIFIED,
the M16 lanes). `fold(strata, rulings) → views` computes current canon: the address topology,
rule registry, seat map, cap table. Views are caches with A9b discipline — regenerable,
hash-verified against their inputs, never authoritative. The existing `compiled/` directory is
the prototype. **Search-before-absence is enforced in code:** the store's `locate()` records
every search (term, scope, result) in the register; a MISSING classification without a matching
search record is rejected. O16E (history-grounded derivation) is exactly "run fold() with ALL
strata loaded and diff against the current views" — this component mechanizes it.

### 3.2 Ruling Ledger + Propagation Engine — the R1 audit as architecture
A ruling (M-record, DEC-record) is an event with **declared obligations**: the artifacts and
tools it must be rebuilt through (e.g. M17 ⇒ {00_ROOT_SPEC, MANIFEST class, builder meta, STATE
next-actions}). `propagation_check()` — the generalization of validator A10/A11 — walks
obligations and fails the build while any is undischarged. Supersession is by pointer with the
original preserved (the ~~struck-through~~ pattern from SCOPE_CORRECTION is the display form).
This turns the session's worst recurring failure into a machine-checked invariant.

### 3.3 Run Engine — v5b executable chain, mechanized
One RUN = one song, phased P0–P5, composed of atomic **work items** (`WI.P{n}.{scope}.R{round}`)
persisted to a run ledger before execution (crash-resumable: replay the ledger, skip completed
WIs). P2 fill order is sequential zero-skip over the folded topology; each WI routes to its
**council seat** (owner + ≥2 adjacent reviewers + tie-break from the imported matrix; MAP-era
row lives at PER.execution). The **evidence contract** is enforced at intake: a fill is rejected
unless it is one sentence + source binding (`binds:`/`raw:L#`) + a downstream `if X then Y`
prediction; challenge cycles and dissent are ledger entries, never smoothed. SME workers are
model subagents instantiated per-axis from STAFF.UST.CANON.V1 prompts + seat identity; the
orchestrator (V&V Marshal role) holds gate authority and cannot be overridden.

### 3.4 Interwoven Gate Engine — DEC-27 as architecture
Gates **subscribe to fill events**; every accepted fill emits `(UST delta, SEM delta)` together
— the preload ratchet. Live gates: SEG feasibility (physics override — taste cannot override),
SEM 12-criteria running composite (weights fixed; floor 97.5 terminal), SE20 checklist, CAP
projection (will the triad fit its bands?), lock compliance (D2 comparator: sequence +
multiplicity over quoted lyric text only — meta/spacing transformable per DEC-26). Terminal
close: composite ≥97.5 → G-Card decision artifact. Any FAIL = stop-the-line: the RUN halts and
emits only diagnostics, missing work items, and dissent references (D1 wires QAF/PD rule cards
here: authority declaration on artifact receipt, phantom-commitment scan pre-emit).

### 3.5 FOIL Reverse Compiler
Runs only after LOCK. The factoring rule is the routing rule: each Technical UST address routes
its content to the surface(s) that own it, producing the three surfaces CONCURRENTLY (never
sequential patches): Creative UST (4960–4999, performance-spacing transformation applied to
locked words), Show Summary (960–999), A&R pack (≤150 + 1960–1999) — D3 tests all three bands
live. Surfaces freeze before packaging. **No distribution without linkage:** every emitted file
embeds provenance bindings (source UST hash, ruling ids, run id); the packager refuses to emit a
file whose linkage set is incomplete — the v5 loss is the counterexample this guards against.

### 3.6 Session→Maestro Bridge
The pipeline this session executed by hand, as a subsystem: transcript capture → segment/replay
validation (dual witness, hash-anchored) → mutation ledger extraction → operator elicitation
(M12 interactive batches, M6 format) → apply (append-only, annotations insert-only) →
persistence sweep (word-boundary, before/after) → register updates with rungs named. Output of
every bridge run is a new stratum in the CFS.

### 3.7 V&V Interface
Release candidates are emitted only as **falsifiable packages**: deterministic zip (UTF-8 name
flags — learned the hard way), SHA256SUMS, manifest with inventory classes, embedded
`vv_harness.py`, and a report whose checklist is runnable. External reviewer rounds
(ChatGPT/Claude) return verdicts as work items; absorption is verify-then-repair, never trust.

## 4. Data model

Content-addressed object store (files; sha256 id) + five append-only registers: LEDGER (rulings
+ work-item records), OPEN (claims with evidence burdens), INDEX (object registry + provenance
lanes), STATE (the fold summary, versioned by fold not by product), RUN ledgers (per-song).
The Technical UST instance is a JSON/MD tree keyed by canonical addresses `AXIS.K{n}.S{m}{inst}`;
nulls are explicit reserved values (nulls are signal). Everything diffable, everything git-able.
No database until INDEX growth (4.3k records today) makes grep painful — then SQLite as a *view*
over the registers, never as truth.

## 5. Scale & reliability

Load is one RUN at a time: ~200 subkey fills × (1 owner + 2 reviewers) ≈ 600–900 model calls
worst case, minutes-to-hours wall clock — batching by key-group (the WI key-range pattern) cuts
this ~5×. Reliability comes from ledgers, not redundancy: every WI idempotent and resumable;
stop-the-line preserves full diagnostic state; degradation rules from MODEL_PROFILE apply when
context or counting degrades (axis-chunked P2; CAP treated as FAIL until counts verify). Backup =
git + the deterministic builders (any view reconstructs from sources).

## 6. Trade-offs (explicit)

Files + append-only registers over a database: chosen for SSOT-in-repo, diffability, and model-
agnostic survival; costs query convenience at scale. Fold-computed canon over materialized
snapshots: fold is truth, snapshots are hash-verified caches; costs fold compute per change,
buys M17 compliance by construction. Interwoven gating over terminal gating: ~3× the model
calls of a final-pass check; bought deliberately — DEC-24/27 say quality evaluation IS the
construction process, and the v5 era proved terminal gating ships defects. Human-interactive
gates (M12) over autonomy: slower, but ROOT-over-PROPOSAL is the constitution, and the two ROOT
corrections this session (DEC-27, M17) both arrived through exactly this channel. Subagent SMEs
over one-model-many-hats: costs orchestration complexity; buys genuine adversarial challenge
cycles (the evidence contract is meaningless if one context both claims and reviews).

## 7. Build phasing (maps to D1–D4)

**A — Substrate first (mechanize what exists):** CFS fold() + locate() + propagation_check()
over the current repo; O16E runs as its first workload. **B — Lock + IR:** UST instance format,
intake, D2 lyric-lock comparator as runtime enforcement. **C — Run engine:** WI ledger, council
routing, evidence contract, interwoven gates (D1 QAF/PD wiring, D4 generational release
surface). **D — FOIL compiler:** triad emission under D3 cap tests, linkage-bound packaging.
**E — Bridge + V&V automation:** today's manual pipelines as commands. Each phase ships with its
validator and its falsification kit; no phase claims completeness beyond its reached strata.

## 8. What to revisit as it grows

Multi-operator authority (today ROOT is one person; the rung ladder would need per-identity
signatures). Suno API/browser automation at the target boundary. SQLite views when registers
outgrow grep. Council-seat model refresh when the model roster changes (MODEL_PROFILE hooks).
And the open adjudications this design deliberately does NOT settle: the Chimera-era ↔ v5b unit
chronology (rides O16E), V&V Marshal ↔ STAFF.ROLE.GOVERNANCE correspondence, SE20 composition,
and the sub-gate threshold OQs — all held per the no-silent-harmonization law.
