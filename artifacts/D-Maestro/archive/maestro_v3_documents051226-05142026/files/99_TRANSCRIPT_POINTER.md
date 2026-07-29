# 99_TRANSCRIPT_POINTER

For when the lossless package above is not sufficient and full session detail is needed.

---

## 1. What the transfer package omits by design

This package preserves operator-confirmed canon, current state, open decisions, frame corrections, corpus index, forbidden actions, and delivered artifacts.

It does NOT preserve:

- Full dialogue between Claude and operator turn-by-turn
- Claude's reasoning trace for each conclusion
- Intermediate drafts of the mid-session canon artifacts (Kernel / Operating Instructions / Knowledge Spine / Restore Checklist)
- The full 9-section forensic report text (key findings carried forward; full text not)
- Operator's exact wording on stance corrections beyond what's quoted in FC1
- Failed branches / reconsidered paths from mid-session
- Thinking-window content (operator was watching it; honest reasoning was the default)

These are intentionally omitted because they exceed what a new workspace needs to resume work, and including them would dilute signal-to-noise.

---

## 2. Where the source transcript lives

Source session transcript file:

```
/mnt/transcripts/2026-05-06-14-06-04-maestro-mosaic-dev-recovery.txt
```

Size: 1,295 lines as of package generation.

Prior session transcript (formalization-prep, immediately before):

```
/mnt/transcripts/2026-05-06-12-58-40-maestro-mosaic-formalization-prep.txt
```

---

## 3. When to retrieve the transcript

Retrieve only when:

- Operator explicitly asks "what did we say about X" and X is not in the package
- A current decision turns on the exact wording of a prior turn
- A claim in this package is challenged and provenance is needed
- The operator requests a forensic replay of a specific phase

Do NOT retrieve the transcript:

- As a default loading action
- To "be thorough" without specific need
- To verify package claims that are already cited to specific dev-workspace files (cite-walk those files instead)

---

## 4. Transcript retrieval guidance

If the new workspace has access to `/mnt/transcripts/`:

```bash
# Index by header
grep -n "^##\|^###\|^# " /mnt/transcripts/2026-05-06-14-06-04-maestro-mosaic-dev-recovery.txt

# Find a specific operator turn
grep -n "Human:" /mnt/transcripts/2026-05-06-14-06-04-maestro-mosaic-dev-recovery.txt

# Pull a line range
sed -n '500,600p' /mnt/transcripts/2026-05-06-14-06-04-maestro-mosaic-dev-recovery.txt
```

If the new workspace does NOT have access to `/mnt/transcripts/`:

- The transcript is unrecoverable from inside that workspace.
- Operator can re-upload if needed.
- The transfer package is designed to function without it.

---

## 5. Key transcript landmarks

For navigating the source transcript if accessed:

| Phase | Approximate location | Content |
|---|---|---|
| Operator OP-DIRECT request for forensic report | early | Structured 9-section output request |
| Forensic 9-section report delivery | early-mid | Full forensic output |
| Operator OP-DIRECT frame correction | late-mid | "4 department heads → 4 output domains (triad + new vig + mo)" |
| Birth certificate upload + read | late-mid | Operator instructs to read attachment |
| Birth certificate synthesis response | late | Section-by-section extraction, FC1 ambiguity flagged |
| Operator OP-DIRECT package request | final | "create a lossless session transfer package for a new project workspace" |
| Package generation | this turn | Eight files produced |

---

## 6. Relationship to prior packages

If a `session_handoff_*.md` file exists in `/mnt/project` from a prior session, that is a different artifact:

- Prior session handoffs (e.g., session_handoff_2026-04-11.md, session_handoff_2026-04-12.md) are **handoffs FROM prior sessions INTO this dev workspace**.
- This transfer package is **a handoff FROM this dev workspace OUT to a new workspace**.

Both should be loaded by the new workspace if available. They serve different purposes:

- Prior handoffs: history of what got built and frozen
- This package: current state and operator framings that need to ride forward

---

## 7. Closing

The package is designed to be loadable on any model, in any session, without requiring transcript access. The transcript is a fallback, not a dependency.

If anything in this package is unclear or inconsistent when loaded fresh, the resolution order is:

1. Operator's next turn supersedes
2. Files in `/mnt/project` (especially WRVV and SGL if present) override package claims
3. Birth certificate (operator memory) overrides package framings
4. Transcript reference (this file's instructions) for forensic detail
5. Default: surface the inconsistency, do not synthesize forward
