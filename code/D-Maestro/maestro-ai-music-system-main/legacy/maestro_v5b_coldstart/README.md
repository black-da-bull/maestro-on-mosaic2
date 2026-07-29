# Maestro v5-b — Cold Start Pack (v5-b.coldstart.1)

This bundle is a minimal, auditable starting point for running Maestro v5-b as a Custom GPT or project workspace.

## What Maestro is
- A monolithic execution engine that runs one end-to-end workflow with hard gates.
- A virtual label/studio council that reaches decisions via contested consensus (challenge/defend), not convenience.
- A compiler that transforms Creative intent (Affect) into Technical constraints (Physics) and then into Suno-facing prompts.

## Key concepts
- Creative UST (Macro.Micro.{x+1}): captures affect, intent, textures (artist language).
- Technical UST (Macro.Micro.Tactical.{x+1}): internal worksheet with addressable subkeys (SME fill-in-the-blanks).
- Stop-the-line: if any gate fails, Maestro emits only diagnostics and missing work items.

## How to install (Custom GPT Builder)
1. Paste `SYSTEM_PROMPT.md` into the GPT System Instructions.
2. Upload the remaining `.md` and `.txt` files as Knowledge (or store them in a project workspace).
3. Ensure the Creative template used is `templates/CREATIVE_UST_TEMPLATE.txt` (includes MAP parity patch).
4. Ensure the Technical UST canonical files are uploaded (both canon + governance addendum).

## How to run (Artist Call)
Paste an Artist Call such as:

```text
[ArtistCall | ProjectName | Date | Version]
[Affect | ...]
[Story/Intent | ...]
[References | ...]
[Non-Negotiables | ...]
[Flex Zones | ...]
[Lyrics | ...]  (set LYRICS_LOCK = ON if locked)
```

Maestro will:
- Phase 0: initialize dual scaffolds
- Phase 1: map input into Creative UST and assemble the packet
- Phase 2: generate work items and begin NULL hunting per axis

## Future-proofing
See `docs/MODEL_PROFILE.md` for capability flags and degradation rules when context/precision changes across model upgrades.
