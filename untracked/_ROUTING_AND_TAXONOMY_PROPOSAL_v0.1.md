# ROUTING + TAXONOMY PROPOSAL v0.1
**Rung: PROPOSED** (AI output — not accepted, not operative, nothing moved)
**Date:** 2026-07-20 · Author: Claude (cowork session) · Basis: STATE v0.7, OPEN, EXECUTIVE ARCHITECTURAL SYNTHESIS, maestro architecture session

---

## PART 0 — Why other AI sessions keep misreading the filestore

Not a dedup problem. A **self-description** problem. The store has **two orthogonal axes**:

- **ROLE** — `artifacts/ code/ sessions/ system/ media/`
- **SOURCE-ORIGIN** — `D-Maestro/ OneDrive-v45/` (provenance of ingest)

The folder names express only the first, and **neither expresses the RUNG or the DOMAIN**. So a fresh session:
- reads `artifacts/` as "outputs" — it's actually mixed evidence + canon + sealed packs;
- reads `code/` as "the app" — it's actually imported copies of three different systems;
- reads `system/` as OS config — it's actually Custom-GPT knowledge files;
- finds no rung marker anywhere, flattens everything to "files," and **dedups** — destroying the
  thinning evidence O16E exists to recover.

**Fix = make the structure self-describing, not rearranged.** A root `TAXONOMY.md` + a 5-line
contract per folder does more than any reorganization. Renaming is *not* proposed.

---

## PART 1 — Architecture → folder map (the missing layer)

This is what makes a session "get it." Derived from EXECUTIVE ARCHITECTURAL SYNTHESIS.

| Domain (synthesis) | Purpose | Lives in |
|---|---|---|
| **Knowledge** (knows) — K1–K10, SEG, Technical UST schema, personas, pattern library | immutable, versioned, referenced | `canon/` + `evidence` layer (`artifacts/<source>/`) |
| **Execution** (does) — runtime, councils, governance, validation | produces *Canonical Project Truth* | `code/` + `_PROVENANCE/` (governance) |
| **Compilation** (transforms) — LOCK → FOIL → Coverage → Projection | separate from reasoning | `derived/graph/` + `code/` |
| **Presentation** (exports) — Show Summary, Creative UST, Bio, images, exports | ZERO creative reasoning; projects only | `media/` + `projects/` |

**Engine A** (truth formation) never merges with **Engine B** (truth distribution). Anything under
`media/` or `projects/` is Engine-B output — *derived, never authoritative*.

---

## PART 2 — Proposed structural additions (additive, reversible, no renames)

```
maestro-on-mosaic/
  CLAUDE.md              (exists — boot)
  TAXONOMY.md            ← NEW: the contract. Read after CLAUDE.md.
  _PROVENANCE/           (exists — governing register)
      method/fold/       ← NEW: FOLD tooling joins the validator already here
  artifacts/             (exists — ingest evidence, per-source; IMMUTABLE)
      packs/             ← NEW: sealed archives pending extraction
      transfer/          ← NEW
  derived/               ← NEW: AI-produced. Rung = PROPOSED until operator accepts.
      architecture/
      graph/fold/
  code/  sessions/  system/  media/  recovered/  T14_extractions/   (all exist)
  projects/              (per O-12)
  _TRIAGE/               ← NEW: unclassified. MUST be read before routing. Never auto-route.
  _SANDBOX/attempt-NN/   ← NEW: experiments. May never write outside itself.
  untracked/             ← reclassified as INBOX with a drain rule
```

**Rule additions proposed:**
1. `untracked/` is an **inbox**, not storage. Everything drains to a rung-marked home.
2. `artifacts/<source>/` is **immutable evidence** — never reorganized, never deduped, ever.
3. `derived/` is always rung=PROPOSED until an operator statement promotes it.
4. Every top-level folder carries `_FOLDER_CONTRACT.md` (5 lines: what belongs, what doesn't, rung, axis, who may write).
5. **Variant-preservation law:** name-collisions across layers are hash-compared. Byte-identical → safe to collapse. **Differing → preserve ALL copies and route to O16E as thinning evidence.** (DEC-28 / M18)

---

## PART 3 — Routing table for `untracked/` (139 items)

Nothing moved. Proposal only.

| Item | Proposed destination | Rung | Note |
|---|---|---|---|
| `run_fold_phase2.ps1`, `run_fold_phase3.ps1`, `run_fold_phase3_1.ps1` | `_PROVENANCE/method/fold/` | tooling | Joins validator already persisted there. 3 phases = version chain — **keep all three**. |
| `FOLD_INPUT.json` | `derived/graph/fold/` | derived | Input snapshot |
| `FOLD_MANIFEST.json` + `FOLD_MANIFEST_CLASSIFIED.json` | `derived/graph/fold/` | derived | **Pair — raw vs classified. Keep both.** Classification is a reduction. |
| `MUTATION_CHAIN.json` | `derived/graph/fold/` | derived | **High value** — cross-reference against LEDGER mutation IDs (M4 coverage) |
| `TRACE_VALIDATION.json` | `derived/graph/fold/` | derived | Validation output |
| `SYSTEM_GRAPH.json` + `SYSTEM_GRAPH_IMPROVED.json` | `derived/graph/` | derived | **DO NOT COLLAPSE.** "IMPROVED" implies the other was superseded/thinned — textbook O16E signal. |
| `maestro architecture session.md` (327 KB) | `sessions/chatgpt-customgpt/` | **evidence (DEC-02)** | Raw Custom-GPT admin-preview transcript. Primary source for the synthesis. |
| `EXECUTIVE ARCHITECTURAL SYNTHESIS.md` | `derived/architecture/` | **PROPOSED** | Doctrine-grade but AI-derived. **Not canon until operator accepts.** See M1 flag below. |
| `Maestro_Session_Transfer_Packet.md` / `.yaml` | `artifacts/transfer/` | artifact | Human + machine readable pair — treat as the authoritative rendering |
| `Maestro_Session_Transfer_Packet.docx` / `.pdf` / `.xlsx` | `media/exports/transfer/` | projection | Engine-B renderings. **Verify content-equivalence before calling redundant** — different formats are never byte-identical. |
| `Maestro_Migration_Package.zip`, `Maestro_Phase2_Working_Set.zip` | `artifacts/packs/` | sealed | **Extract + inventory BEFORE any dedup verdict** (M16 search-burden) |
| `art/` (110 images) | `media/art/` | presentation | Cross-check against **O-12** `campaigns/run-it-to-me/` covers — some may discharge that item |
| `AI Music.md`, `AI Music - lyrics.md` | `_TRIAGE/` | triage | **Name collision** with `code/D-Maestro/maestro-ai-music-system-main/legacy/AI Music.md` → hash-compare; preserve both if differing |
| `Maestro - Fabric - Rebirth.md` | `_TRIAGE/` | triage | Fabric pre-ingestion + Rebirth runner — read before routing |
| `Untitled 1–6.md` (6 files) | `_TRIAGE/` | triage | Never auto-route unnamed files |

---

## PART 4 — Flags

**🔴 M1 exposure (active).** `EXECUTIVE ARCHITECTURAL SYNTHESIS.md` is doctrine-grade — it reframes
Maestro as compiler / Suno as external renderer / Project as canonical object — yet it sits in
`untracked/`, invisible to STATE and LEDGER. Per M1, *if it isn't in `_PROVENANCE/` or a
runtime-consumed artifact, it doesn't exist next session.* **Recommend a LEDGER entry regardless of
where the file lands.**

**🔴 Second filestore.** `D:\Maestro\maestro-on-mosaic\` also exists — a nested copy inside the old
vault, alongside the real `D:\maestro-on-mosaic\`. Two stores claiming the same role is an SSOT
hazard (M11/DEC-07). Needs an operator ruling on which is live; **do not merge silently.**

**🟡 SSOT contradiction still open.** 6/17 operator selection named the WSL `rebirth` repo as source
of truth; STATE rule 10 names *this folder*, with Rebirth as the *executable runner* to be reconciled
to maestro-current grammar. Logged as a contradiction, not harmonized.

**🟡 mtimes flattened ~2026-06-18 (M7).** Any routing decision must use **internal dates**, never
filesystem timestamps.

---

## PART 5 — Fail-safe experiment protocol (operator has disk space)

```
_SANDBOX/attempt-01/
    PLAN.md      what this attempt tests, and its falsification criterion
    tree/        the trial layout (hardlinks or copies — same drive = near-zero cost)
    RESULT.md    what broke, what held, verdict
```

Rules: the sandbox **may never write outside itself**; source material is only ever *copied in*;
attempts are numbered and never deleted (failed attempts are evidence too — M16). Calibration first
per M9/M10: prove the frame on one small folder before any corpus-scale pass.

---

## PART 6 — Suggested order

1. Operator ruling on the **two SSOT contradictions** (Part 4) — everything downstream depends on it.
2. Write `TAXONOMY.md` + folder contracts. **This alone fixes most AI misreads.**
3. Drain `untracked/` per Part 3 — tooling and evidence first, `_TRIAGE/` last.
4. Extract the two zips and inventory them (discharges an M16 search burden).
5. Hash-compare the flagged collision pairs; route differing variants to O16E.
