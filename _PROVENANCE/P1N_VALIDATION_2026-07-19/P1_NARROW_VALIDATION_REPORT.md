# P1N Validation Report — Session 13 Narrow Replay
**Work item:** `REPAIR.P1N.PANEL-VALIDATION.R1` · **Date:** 2026-07-19 · **Verdict: PASS**
**Validator:** independent Cowork session (cloud container). All checks scripted against byte-verified staged copies of `D:\maestro-on-mosaic` evidence; the device copies were hashed in place before staging and re-hashed after transfer. Nothing in the Maestro runtime canon was created, modified, or patched. This report and its five companion files are the only writes, all inside `_PROVENANCE\P1N_VALIDATION_2026-07-19\`.

This session is a different validator than the one that produced the replay (separate context, no access to that session's memory), so the reproduction below is independent in the sense that matters: everything was re-derived from the primaries, not from the replay's self-description. It is not independent in the deeper sense the panel report already conceded — same model family, same corpus.

---

## 1. Inputs located (all ten present)

| Work-item input | Found at | Status |
|---|---|---|
| Session 13 W1 primary | `artifacts/D-Maestro/sources/claud3.txt` (407,408 B, md5 `faecdb76…`) | verified |
| Session 13 W2 primary | `artifacts/D-Maestro/sources/claude-session13-window2.txt` (927,063 B, md5 `94989f7f…`) | verified |
| Archive copies | `archive/maestro_v3_documents051226-05142026/` — 4 files | verified byte-identical |
| Impact map | `_PROVENANCE/P1_narrow/P1_NARROW_IMPACT_MAP.md` | read in full |
| Replay windows | `session13_window1_replay.md`, `session13_window2_replay.md` | read in full |
| Split work products | `_work/` — 2× segments.jsonl + 2× operator_verbatim.md | mechanically re-verified |
| Ledger / contradiction entries | `LEDGER.md` (M1–M11, V1), replay footers | read in full |
| Persistence-search targets | `canon/`, `drafts/`, `HYDRA/`, `system/`, `ws_*.yaml`, `untracked/`, root | re-searched |
| Mediated-decision records | `T14_extractions/63122c11…` CM-5/6/7 footer | verified |
| Split/extraction scripts | **not persisted** — no splitter script found in `_PROVENANCE` | gap, absorbed (see §7) |

## 2. Pass 1 — Provenance: PASS
DEC-02's claim that `claud3.txt` ≡ `claud3-window1.txt` ≡ `claude-session13-window1.txt` (one file, three names) verified by digest: all three archive copies plus the primary share md5 `faecdb760a6248fd08d9cce4e6e738ca`. Window 2's archive copy is likewise identical to its primary. INDEX.json's recorded MD5s and duplicate_origins match computed reality for both primaries. INDEX.json holds exactly 4,305 records. A deterministic 41-file sample (every 107th record) verified 41/41 against recorded hashes, zero missing — 47/47 total including the session-13 set. The consolidation hash chain holds everywhere it was tested.

## 3. Pass 2 — Coverage: PASS (one restatement, one minor event gap)
The mechanical split was reproduced end-to-end. Segments are contiguous with zero gaps or overlaps; concatenating all segments reproduces the source **exactly** after CRLF→LF normalization, which is the split's only transformation (W1: 6,418 CR characters; W2: 8,647). So "byte-lossless" should be restated as **character-lossless after newline normalization** — offsets index the normalized text (393,821 / 914,340 chars), not raw bytes (MF-1). No content is lost by this; it just needs saying precisely.

Segment census matches the replay exactly: W1 = 36 segments (17 user), W2 = 58 (32 user), and the replay's U-numbers equal the jsonl indices one-for-one. Every user segment's text is present in the operator-verbatim work files. REC-A (`GENERATE STATE CAPSULE AND THEN A.`) and REC-B (the R-LIST v0.1 paste + K-2 selection) were confirmed at the tails of assistant segments 2 and 18, exactly as claimed, with the K-2 attribution in segment 19.

An adversarial sweep of all 43 assistant segments for further embedded operator inputs found **none** — every unflagged `You said:` inside assistant text is a quotation of the *inner* 4_5_5.txt transcript's speaker markers, a transcript-within-transcript effect the replay handles correctly. One minor gap: W2 seg 16's tail carries file-attachment chrome (`4.5.5.txt / txt / 2:15 PM`) — an operator *attach action* between U15 and U18 that the replay does not enumerate. No operator text was lost, but under M8's own logic (operator acts that don't render as user turns still count), attachment events should join the coverage rule (MF-3).

## 4. Pass 3 — Mutations: PASS
Exactly 27 + 34 = **61** unique, contiguous mutation IDs; the status tallies (24+1+2 / 23+6+2+3) match the inline classifications. Twenty-two verbatim probes covering every high-authority mutation — the U13 no-parse flagship, U15 stop-stuck, U20 Config B relay, U32/U34 version rulings, U30 two-systems, U39 rebirth, U41 MODE prompt lines, U45, U51, U53, U56 locks, U57 triangulation, REC-A/REC-B — were all found in source at the claimed character positions. The P0-b byte citation for the flagship (~107,529) is accurate to 4 bytes (actual 107,525). The R-list v0.2 totals block exists verbatim in the U20 attachment: `TOTAL: 96 / FIRM: 92 / CAND: 3 / OPEN: 1`, category sums equal 96. SM13-W1-11's accepted-but-unexecuted status is supported by both `Claude's response was interrupted.` markers exactly where the replay says they are.

## 5. Pass 4 — Contradictions: PASS
All nine (W1 CR-1..4, W2 C1..5) reproduce from source with both sides traceable; the omission sweep (every operator turn bearing correction markers) found no unregistered corrective turn, and the held-open items (CB-02/04/06, OPEN-Q5–Q8) are carried, not closed. Nothing was silently harmonized — CR-2's unresolved promotion order is explicitly preserved. Two side-quotes flatten source line breaks/column whitespace (content identical); the replay should note its quote-normalization convention (MF-4).

## 6. Pass 5 — Persistence: CONFIRMED, with a sharpened finding
The V1 zero-occurrence claims reproduce: `R-RT-QAF-01`, `R-RT-PD-01`, `Config B`, and any `R-list` reference — **zero** files across `canon/`, `drafts/`, `HYDRA/`, `system/`, `code/D-Maestro/drafts/`, `ws_*.yaml`, `untracked/`, and root docs. All nine text-searchable canon files contain **zero** references to v4.5.5 — the staleness ruling stands. (Scope caveat: the canon zip and one PDF are not text-searchable — MF-5.)

What this audit adds, per the work item's near-match mandate: the *concepts* behind the two FIRM rules have April-era ancestors in persisted drafts — `cumulative_deltas_qaf.md` (Q-A-F ledger practice), `mosaic_engine_v0.1.md` (INV-04, emit-time phantom detection), `maestro_v0.md` ("Phantom commitments blocked at emit time", §10 Q-A-F Provenance). The identifiers, the 96-entry FIRM R-list, Config B, and the version trinity still never persisted anywhere. And one genuinely new fact: **`maestro_v0.md` defines K7 = Arrangement and K8 = Commercial, in direct conflict with session 13's FIRM Config B (K7 = External viability, K8 = Visual coherence)** — a persisted artifact actively contradicting operator-ratified canon (MF-6). That is V1's failure class caught in a second location, and it belongs in the O-13 reconstruction brief.

Related verifications: Revised INV-18 confirmed in claud2.txt at byte 255,842 (original at 252,444) and confirmed absent from the installed SKILL.md; the recovered kernel is byte-identical to `KERNEL.md` inside `archive/im_dead_kb.zip` (zip-dated 2026-05-20); `projects/` does not exist, so the Run It To Me export (O-12) is still pending; the T14 coverage lines and CM-5/6/7 mediated-decision footer are present and correctly marked provisional.

## 7. What did not reproduce
One method claim failed reproduction: the **correction-density metric** that selected session 13 (claimed ≈0.32/KB window2, 0.25 claud3, 0.18 eldrik). The marker set was never persisted. Under an independently chosen marker set the *selection-driving* result reproduces — window 2 is by far the most correction-dense (0.286/KB vs 0.083 and 0.106) — but the specific numbers and the claud3-vs-eldrik ordering do not (MF-2). Same class of gap: no splitter script is persisted in `_PROVENANCE`, so the split had to be validated by its outputs rather than re-run (it passed, but O-14's repair should land the script itself). Both go to the method file before the full P1 sweep.

## 8. Panel adjudication (five bounded roles)
**Forensic provenance:** PASS — hash chain intact device→index→staged copy; DEC-02 equivalences digest-verified. **Maestro architecture:** PASS, noting no runtime object was touched and MF-6 routes to O-13 as a proposal, not a patch. **Context/authority:** PASS — authority classes survive relay, quote-back, and bleed regions; nothing structured outranked source. **Falsifiability/QA:** PASS — every claim reproduced, scoped, or explicitly downgraded (c07 as-recorded, c09 partial); nothing promoted on trust. **Adversarial simplification:** PASS — the validation attacked the primaries directly; its one reproduction failure is reported as such, and this report should not itself be treated as replacing the replay files or the sources it validates.

## 9. Verdict and stopping point
**PASS.** Per the work item, this authorizes staged replay of the next small session batch (entry into the T01–T13 sweep) — an authorization that remains the operator's to exercise, with MF-1–MF-4 folded into the method first and the splitter repair (O-14) still due. Full claim-by-claim scorecard in `P1_NARROW_VERDICT.yaml`; machine-readable evidence in the four companion files.

Stopped at verdict. No Maestro runtime artifact was patched.
