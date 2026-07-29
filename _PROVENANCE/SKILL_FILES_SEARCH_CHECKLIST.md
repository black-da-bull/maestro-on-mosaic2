# Skill-Files Search Checklist (DEC-03 / O-03)
For each PC and Windows account (school, work, home). Check the box when a location is searched; note hits with full path + file date. Found originals outrank any reconstruction.

## Exact filenames to search (Windows Search / Everything / OneDrive web search)
- [ ] `00_OPERATOR_ABOUT_ME.md`
- [ ] `OPERATOR_CONTEXT.md`
- [ ] `01_METHODOLOGY.md`
- [ ] `02_FAILURE_MODES.md`  ← highest value (18 failure modes, "most important file")
- [ ] `03_WHY_AI_DEFAULTS_HERE.md` (draft already in repo — look for later versions)
- [ ] `04_KERNEL.md` (ancestor recovered: `_PROVENANCE/recovered/KERNEL_from_im_dead_kb_2026-05-20.md` — look for the numbered/final version)
- [ ] `05_WORKFLOW.md`
- [ ] folders named `patterns`, `examples` near any of the above
- [ ] python files: anything like `parse_*.py`, `phantom*.py`, `fold_*.py` beyond fold_laminate_v0_1.py
- [ ] any zip named like `maestro*skill*.zip`, `forensic*.zip`, `transcript*.zip`

## Content search terms (if filenames were renamed)
`INV-17` · `INV-18` · `phantom commitment` · `FM-16` · `FM-18` · `skeleton file` · `W0` `W9` · `Fabric pattern` · `not-novel` · `Tandy` (OPERATOR_CONTEXT anchor) · `narrative-as-method`

## Locations per machine/account
- [ ] `%USERPROFILE%\Downloads` (skills were likely downloaded from Claude sessions)
- [ ] `%USERPROFILE%\Documents`, `Desktop`
- [ ] `%USERPROFILE%\.claude\skills\` (any machine that ran Claude Code)
- [ ] `%APPDATA%\Claude\` (Claude Desktop data dirs)
- [ ] OneDrive web (each account: school/work/home) — search each filename above, INCLUDING the Recycle bin
- [ ] Other sync roots: old `OneDrive - <school/employer>` folders left on disk after unlinking
- [ ] Any USB/external drives used for the June 18 consolidation
- [ ] Browser download history around **2026-05-20 → 2026-06-18** (the skill-forging window) — filenames appear even if files were moved

## When done
Report per file: FOUND (path + date) / NOT FOUND. Anything not found after this sweep gets reclassified in OPEN.md O-03 from "possibly extant" to "never externalized — reconstruction target."

---

## RECORDED SEARCH — 2026-07-20 (Claude cowork session, operator-invoked `/maestro-forensic-transcript`)

**Locations searched (3 of the location list):**
- [x] `%APPDATA%\Claude\...\skills-plugin\...\skills\maestro-forensic-transcript\` — **enumerated: `SKILL.md` ONLY.** M5 confirmed live: 1 of 10 components installed.
- [x] `D:\maestro-on-mosaic\` — full recursive, filename patterns + content terms
- [x] `D:\Maestro\` — full recursive, filename patterns

**Per-file result (within searched locations only):**

| Component | Result | Path |
|---|---|---|
| `00_OPERATOR_ABOUT_ME.md` | NOT FOUND | — |
| `OPERATOR_CONTEXT.md` | NOT FOUND | (only unrelated `02_OPERATOR_CONFIRMED_CANON.md` matched) |
| `01_METHODOLOGY.md` | NOT FOUND | — |
| `02_FAILURE_MODES.md` | **NOT FOUND** (highest value) | — |
| `03_WHY_AI_DEFAULTS_HERE.md` | **FOUND** (draft) | `artifacts/D-Maestro/drafts/03_WHY_AI_DEFAULTS_HERE.md` (dup at `D:\Maestro\drafts\`) — later version still sought |
| `04_KERNEL.md` | ancestor only | `_PROVENANCE/recovered/KERNEL_from_im_dead_kb_2026-05-20.md`; numbered/final NOT FOUND |
| `05_WORKFLOW.md` | NOT FOUND | — |
| `patterns/`, `examples/` | NOT FOUND | — |
| python extractors | **1 of 3** | `code/forensic-pipeline/python/fold_laminate_v0_1.py`. `parse_*`/`phantom*` NOT FOUND (confirms O-07) |

**Content-term sweep (renamed-file check) across `D:\maestro-on-mosaic`:**
- `Tandy` · `narrative-as-method` · `not-novel` → **only 2 hits**: this checklist, and
  `_PROVENANCE/T14_extractions/bda23828_build_harvest.md`.
- `phantom commitment` · `FM-16` · `FM-18` · `skeleton file` → 30+ hits, all *citations inside
  sessions/artifacts*, none a component original.
- Conclusion: **no renamed original of any missing component exists in the filestore.**

**Recovery leads (for reconstruction, only after the search concludes):**
1. `_PROVENANCE/T14_extractions/bda23828_build_harvest.md` — carries the OPERATOR_CONTEXT anchor (`Tandy`).
2. `_PROVENANCE/skill_v1_1/BOOTSTRAP_INPUT_CHATGPT.md` — an existing skill-reconstruction workspace.
3. `artifacts/D-Maestro/sources/claude-session051526.md` — dense in INV-17/INV-18/phantom-commitment emergence.

**Lane:** the NOT FOUND results are scoped to the three locations above (M16 — completeness scopes to
reached strata). The checklist's unsearched locations (Downloads/Documents/Desktop per account,
OneDrive web incl. recycle bin, other sync roots, USB/external, browser history 2026-05-20 →
2026-06-18) remain OPEN. **Do not reclassify O-03 to "never externalized" until those are swept.**

---

## SUPERSEDING FINDING — full-drive mechanical sweep, 2026-07-27 (`o03_sweep.ps1`)
The earlier same-session block above was scoped to 3 hand-searched locations that **did not include
`AppData\Local\Temp`**. The mechanical sweep reached it. Result: **ALL SEVEN components FOUND**, intact,
same timestamp (2026-07-20 18:56):

| Component | Verdict |
|---|---|
| 00_OPERATOR_ABOUT_ME.md | **FOUND** |
| OPERATOR_CONTEXT.md | **FOUND** |
| 01_METHODOLOGY.md | **FOUND** |
| 02_FAILURE_MODES.md | **FOUND** (the "most important file") |
| 03_WHY_AI_DEFAULTS_HERE.md | **FOUND** |
| 04_KERNEL.md | **FOUND** |
| 05_WORKFLOW.md | **FOUND** |

**Location:** `C:\Users\gamer\AppData\Local\Temp\claude\--wsl-localhost-ubuntu-home-wsl-projects-rebirth\4abffa73-…\scratchpad\upload\maestro-forensic-transcript\`
— a full copy of the skill was uploaded into a rebirth session on 2026-07-20. This is the **master**;
the installed skill cache holds only `SKILL.md` (skeleton). Report: `O03_SWEEP_20260727-132614.md`.

**🔴 VOLATILITY:** the master is in `Temp` and can be cleared by Windows at any time.
**Action = `rescue_skill.ps1`** copies it to `_PROVENANCE/skill_recovered_2026-07-20/` (git-safe) with
count+size verification and a manifest. Run before doing anything else.

**O-03 disposition:** recovery satisfies the reconstruction target WITHOUT reconstruction (found
originals outrank reconstruction — checklist rule). O-03 may be **CLOSED by operator statement** once
the rescue copy verifies. The three still-manual locations (OneDrive web, browser history, USB) are
**moot for recovery** now that intact originals exist — pursue only if you want a second provenance
witness. Recommend also folding the recovered `02_FAILURE_MODES.md` against the extraction lead in
`_PROVENANCE/T14_extractions/bda23828_build_harvest.md` as a cross-check.
