# 07_FRAME_CORRECTIONS_LIVE

Operator framings issued this session that are NOT yet captured in any artifact in `/mnt/project` or in the birth certificate. These are the highest-risk-of-loss items.

Each entry: framing · context · authority · risk · disposition.

---

## FC1. Executive committee = 4 department heads → 4 output surfaces

**Operator framing (verbatim, 2026-05-06 dev window):**

> "the executive committee are the 4 department heads and map to 4 output domains (triad + new vig + mo). referred to in previous dialogue as executive committee, the council or others but each represent an output surface."

**Context:**
This turn followed the structured 9-section forensic report. Operator's framing collapses three prior labels (executive committee, the council, others) into one role layer and binds it to output surface ownership.

**Best-parse decomposition:**

- Layer label: 4 department heads. Prior labels (executive committee, council, executive red pen) are aliases for this same role layer.
- Count: 4
- Maps to: 4 output surfaces
- Surface enumeration: 3 triad surfaces (Show Summary, Creative UST, A/R Persona Surface) + new VIG = 4
- "+ mo": Mo identifying himself as one of the 4 heads (most likely owning A/R Persona Surface given the excellence-ratchet role in MOSAIC v2.3 diagram). NOT a 5th domain — that would break the count of 4.

**Authority:** T1 (OP-DIRECT, current session). Not yet ratified into cumulative_deltas_qaf.md.

**Risk of loss:** HIGH. This framing exists only in this dev session transcript and in this transfer package. It is not present in:
- maestro.md (kernel)
- cumulative_deltas_qaf.md
- MMR.v0 (which lists Options A–E without resolution)
- the birth certificate
- any other dev-workspace artifact

**Disposition:**
- DO capture this framing into cumulative_deltas_qaf.md as a Q-A-F entry at operator's next ratification turn
- DO NOT select which 4 personas hold the heads (frozen per WRVV §10, FC1 does not resolve D1)
- DO NOT assume which head owns which surface (mapping head→surface is also D1-pending)
- DO carry this framing forward to all future workspaces until ratified

**Open derived questions:**
- Q1: Which 4 personas hold the head roles?
- Q2: Which head owns which surface? (likely intuitive mappings but not confirmed)
- Q3: Does "+ mo" mean Mo's role is one of the 4 heads, or is Mo's authority a wrapper around the 4 heads' decisions?
- Q4: Is VIG a layer (Plane-2 / Plane-4 governor) or an output surface or both?

---

## FC2. SDG.v0.1 worker schema (declared canonical: 9-element flat)

**Context:** Mentioned earlier in dev session but tied to SDG itself being CANDIDATE.

**Status:** This is in files6 (SDG.v0.1) as CANDIDATE, not in this section because it's not fresh — but flagged here because it interacts with FC1 if the 4 heads are drawn from the 9-element schema.

**Disposition:** Reference only; not a fresh correction.

---

## FC3. Birth certificate post-export turns as canonical operator memory

**Context:** Operator uploaded the birth certificate (559 KB) mid-session and instructed Claude to read it. Lines 4888–8569 (post-export turns + Restore Packs) constitute operator-canonical memory that may not have been previously visible to this dev workspace.

**Status:** READ this session. Key sections cross-referenced into `02_OPERATOR_CONFIRMED_CANON.md`.

**Disposition:**
- DO treat birth certificate §II + §V as operator-canonical (T1)
- DO NOT treat birth certificate §I (Clarity Architect GPT config) as runtime canon — it is the Claire/Itty persona configuration, not Maestro/Mosaic canon
- DO recognize that the Kernel/Operating Instructions/Knowledge Spine I produced mid-session matched the operator's pre-existing Zero-Day Restore Pack — confirming no drift, not novel synthesis

---

## FC4. (placeholder for future framings)

When the operator issues new frame corrections in subsequent sessions before ratification into artifacts, add them here.

---

## How to handle FC entries

1. **On loader cold-start:** read every FC entry as if the operator just said it.
2. **On operator ratification:** the entry moves out of this file and into `02_OPERATOR_CONFIRMED_CANON.md` or into a cumulative_deltas_qaf.md entry. The FC entry is then deleted from this file.
3. **On operator correction:** the FC entry is updated or removed per the new framing.
4. **Never** treat an FC entry as canon without operator ratification, but **always** preserve it as carried-state.
5. **Never** silently merge an FC entry into existing canon. The point of this file is that these framings have NOT been ratified yet, and that status is load-bearing.
