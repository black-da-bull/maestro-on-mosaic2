#!/usr/bin/env python3
"""
fold_laminate_v0_1.py - the fold/laminate engine (back half of the forensic pipeline).

PLANE: Dev / Forensics (NOT Maestro runtime). Container-only mechanical work.
       Pure stdlib. Model-independent: classification is UPSTREAM (Claude-as-classifier);
       this engine consumes already-typed events and never calls a model.

POSITION IN PIPELINE (skill SS05 W0-W9, local target: WSL2 + Python + Fabric):
    forensic_parse           -> eventlog_<KEY>.json   {id, role, sha8, chars, text}
    forensic_classify / pass1_chronology -> index      [{id, role, types[], sha8, chars}]
    >>> THIS ENGINE <<<  index (+ optional text)  ->  Fold per session  ->  Lamination
    emit                     -> typed provenance-bound graph + laminated canon projection
                                (+ 4-role diagram round-trip: NEXT INCREMENT, see diagram_roles)

WHAT IT AUTOMATES:
    The hand-walked back half. "fold = reduce WITH provenance"; each session -> one Fold;
    Folds laminate onto prior Folds append-only with under-layers PRESERVED (never flattened).
    This is the exact step whose failure produced the documented losses (FOIL -> a frequency
    count + one edge case). The engine makes that flatten structurally impossible (F1).

INVARIANTS (fail-closed; mirror guardrail.py discipline, specialized to fold/laminate):
    F1 no-flatten          laminating never drops an under-layer; re-fold links under=prior
    F2 provenance-complete every digest category carries >=1 source event id (anti-skeleton)
    F3 no-silent-fill      declared nulls carried unchanged; engine never assigns a value
    F4 no-silent-merge     contradictions parked to a conflict register, never collapsed
    F5 root-authority      INV-18: PROPOSAL supersessions recorded, never override ROOT / clear nulls
    F6 append-only         no mutation of folded event content; re-fold = new version

NULLS & CONFLICTS are DECLARED inputs, not detected here. The engine refuses to decide
what is a null or what resolves a conflict (that would be silent-fill in reverse). It
carries them as first-class state. Only a ROOT supersession referencing a null clears it.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import json, hashlib, sys

ROOT = "human_root"
PROPOSAL = "ai_proposal"
NOISE = {"ui_chrome"}

# this-session-derived outputs - excluded as fold SOURCE (from pass1_event_chronology_v0_4 MINE).
# folding our own outputs back in as evidence is circular; the engine refuses it.
MINE = {
    "song_excellence_governance_v0_1", "maestro_v5_ust_sem_interwoven_v0_1",
    "source_lineage_reconciliation_register_v0_1", "loss_demonstration_v0_1",
    "who_dat_runtime_assessment_v0_1", "maestro_month_synthesis_and_rebuild_blueprint_v0_1",
}


def _sha8(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", "replace")).hexdigest()[:8]


class InvariantError(AssertionError):
    """Raised when a fold/laminate invariant is violated. Fail-closed."""


# --------------------------------------------------------------------------- #
# data model
# --------------------------------------------------------------------------- #
@dataclass
class Event:
    id: str                                  # "<FILEKEY>:E####"
    role: str                                # human_root | ai_proposal | context | segment | ui_chrome
    types: list = field(default_factory=list)  # correction | test | failure | ...
    sha8: str = ""
    chars: int = 0
    text: str = ""

    def __post_init__(self):
        if not self.sha8 and self.text:
            self.sha8 = _sha8(self.text)

    @property
    def filekey(self) -> str:
        return self.id.split(":", 1)[0]


@dataclass
class Supersession:
    superseding: str
    superseded: Optional[str]                # None => target unresolved => parked, NOT guessed
    authority: str                           # "ROOT" | "PROPOSAL"
    note: str = ""


@dataclass
class Null:
    key: str
    note: str = ""
    cleared_by: Optional[str] = None         # set ONLY by a ROOT supersession referencing this key


@dataclass
class Conflict:
    key: str
    members: list                            # event ids in tension - kept side by side, never merged
    note: str = ""
    resolved_by: Optional[str] = None        # ROOT only


@dataclass
class Fold:
    filekey: str
    version: int
    covers: list                             # all event ids accounted for (provenance, complete)
    digest: dict                             # "role|type" -> [event ids]  (F2: no empty category)
    supersessions: list
    failures: list                           # event ids typed 'failure' (preserve the ugly parts)
    tests: list                              # event ids typed 'test'
    nulls: list                              # Null[] carried (NEVER engine-resolved)
    conflicts: list                          # Conflict[] parked (NEVER silent-merged)
    under: Optional["Fold"] = None           # prior version of THIS session's fold, preserved
    fold_sha: str = ""


# --------------------------------------------------------------------------- #
# fold: one session -> one Fold
# --------------------------------------------------------------------------- #
def fold_session(events, *, nulls=None, conflicts=None, supersession_targets=None,
                 prior: Optional[Fold] = None) -> Fold:
    """Fold one session's events into a Fold.

    events                : list[Event] sharing ONE filekey
    nulls / conflicts     : DECLARED inputs (Null[] / Conflict[]) - carried, never invented
    supersession_targets  : optional {superseding_id: superseded_id} linkage (from chronology
                            or Claude classification); a MISSING target => superseded=None
                            (parked, not guessed - no-silent-fill applies to links too)
    prior                 : prior version of this session's fold (re-fold => version+1, under=prior)
    """
    nulls = list(nulls or [])
    conflicts = list(conflicts or [])
    supersession_targets = dict(supersession_targets or {})

    keys = {e.filekey for e in events}
    if len(keys) != 1:
        raise ValueError(f"fold_session expects one filekey, got {keys}")
    fk = keys.pop()
    if fk in MINE:                                   # scope guard - refuse circularity
        raise ValueError(f"refusing to fold this-session output as source: {fk}")

    kept = [e for e in events if e.role not in NOISE]   # drop UI chrome, keep all else w/ provenance
    covers = [e.id for e in kept]

    digest: dict = {}
    failures, tests, supers = [], [], []
    for e in kept:
        for t in (e.types or ["_untagged"]):
            digest.setdefault(f"{e.role}|{t}", []).append(e.id)
        if "failure" in e.types:
            failures.append(e.id)
        if "test" in e.types:
            tests.append(e.id)
        if "correction" in e.types:
            auth = "ROOT" if e.role == ROOT else "PROPOSAL"
            supers.append(Supersession(e.id, supersession_targets.get(e.id), auth))

    digest = {k: v for k, v in digest.items() if v}     # F2: drop any empty category

    version = (prior.version + 1) if prior else 1
    f = Fold(filekey=fk, version=version, covers=covers, digest=digest,
             supersessions=supers, failures=failures, tests=tests,
             nulls=nulls, conflicts=conflicts, under=prior)
    f.fold_sha = _sha8(json.dumps(
        {"fk": fk, "v": version, "covers": covers,
         "digest": {k: v for k, v in sorted(digest.items())}}, sort_keys=True))
    _check_fold(f)
    return f


def _check_fold(f: Fold):
    # F2 - anti-skeleton + provenance closure
    refs = set()
    for cat, ids in f.digest.items():
        if not ids:
            raise InvariantError(f"F2 skeleton: empty digest category {cat!r}")
        refs |= set(ids)
    missing = refs - set(f.covers)
    if missing:
        raise InvariantError(f"F2 provenance gap: digest refs not in covers: {sorted(missing)}")
    # F5 - authority sanity
    for s in f.supersessions:
        if s.authority not in ("ROOT", "PROPOSAL"):
            raise InvariantError(f"F5 bad authority {s.authority!r}")
    # F6 - re-fold may not orphan its prior
    if f.version > 1 and f.under is None:
        raise InvariantError("F6 append-only: version>1 with no under-layer (orphaned prior)")
    if f.under is not None and f.under.filekey != f.filekey:
        raise InvariantError("F6 under-layer filekey mismatch")


# --------------------------------------------------------------------------- #
# laminate: fold-of-folds, append-only, under-layers preserved
# --------------------------------------------------------------------------- #
@dataclass
class Lamination:
    folds: list = field(default_factory=list)        # append-only, cross-session

    def laminate(self, fold: Fold) -> "Lamination":
        before_n = len(self.folds)
        before_ids = self._all_fold_ids()
        self.folds.append(fold)                       # APPEND ONLY - never replace a prior fold
        if len(self.folds) != before_n + 1:
            raise InvariantError("F1 flatten: lamination did not grow by exactly one")
        if not before_ids.issubset(self._all_fold_ids()):
            raise InvariantError("F1 flatten: a prior fold's coverage was lost")
        return self

    def _all_fold_ids(self) -> set:
        ids = set()
        for fo in self.folds:
            ids |= set(fo.covers)
            u = fo.under
            while u is not None:                      # walk the re-fold under-chain too
                ids |= set(u.covers)
                u = u.under
        return ids

    # carried first-class state ------------------------------------------------
    def nulls(self):      return [n for fo in self.folds for n in fo.nulls]
    def conflicts(self):  return [c for fo in self.folds for c in fo.conflicts]
    def open_nulls(self):     return [n for n in self.nulls() if n.cleared_by is None]
    def open_conflicts(self): return [c for c in self.conflicts() if c.resolved_by is None]

    # the ONLY way to clear a null: a ROOT supersession (F3 / F5 / INV-18) ------
    def clear_null(self, key: str, by_event_id: str, by_role: str):
        if by_role != ROOT:
            raise InvariantError(f"F3/F5: only ROOT may clear null {key!r}; got role {by_role!r}")
        hit = [n for fo in self.folds for n in fo.nulls if n.key == key]
        if not hit:
            raise InvariantError(f"clear_null: no such declared null {key!r}")
        for n in hit:
            n.cleared_by = by_event_id


# --------------------------------------------------------------------------- #
# emit
# --------------------------------------------------------------------------- #
def emit_graph(lam: Lamination) -> dict:
    """Typed provenance-bound FOLD graph: nodes (fold/null/conflict) + typed edges
    (covers / supersedes[ROOT|PROPOSAL] / under / conflict)."""
    nodes, edges = [], []
    for fo in lam.folds:
        fid = f"{fo.filekey}#v{fo.version}"
        nodes.append({"type": "fold", "id": fid, "sha": fo.fold_sha})
        for eid in fo.covers:
            edges.append({"type": "covers", "from": fid, "to": eid})
        for s in fo.supersessions:
            edges.append({"type": "supersedes", "authority": s.authority,
                          "from": s.superseding, "to": s.superseded})   # to=None => parked
        if fo.under is not None:
            edges.append({"type": "under", "from": fid,
                          "to": f"{fo.under.filekey}#v{fo.under.version}"})
        for n in fo.nulls:
            nodes.append({"type": "null", "id": n.key, "open": n.cleared_by is None})
        for c in fo.conflicts:
            nodes.append({"type": "conflict", "id": c.key, "open": c.resolved_by is None})
            for m in c.members:
                edges.append({"type": "conflict", "from": c.key, "to": m})
    return {"nodes": nodes, "edges": edges,
            "open_nulls": [n.key for n in lam.open_nulls()],
            "open_conflicts": [c.key for c in lam.open_conflicts()]}


def diagram_roles() -> dict:
    """4-role contract for the v2.x / arch diagrams (LOCKED). The round-trip itself is the
    NEXT INCREMENT - it needs each diagram's component manifest as DATA (the images are not
    parseable here) plus the orchestrator. Defined now so the engine exposes the seam."""
    return {
        "target_architecture":     "diagram component set = node set the lamination must cover; "
                                    "validate every component maps to >=1 fold digest entry.",
        "golden_fixtures":         "diagram-declared structures = expected outputs; lamination checked against them.",
        "dataflow_ui_spec":        "the pipeline's own stage DAG / data-flow + UI; orchestrator renders from it.",
        "regenerated_projection":  "emit a diagram-spec FROM the live lamination -> the diagram becomes a "
                                    "projection of canon, regenerated each fold (loop closed), not a static input.",
    }


# --------------------------------------------------------------------------- #
# self-test - fixtures drawn from the real schema + the documented FOIL loss
# --------------------------------------------------------------------------- #
def _selftest() -> int:
    fails = 0

    def check(name, cond, detail=""):
        nonlocal fails
        ok = bool(cond)
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}" + (f"  -- {detail}" if not ok else ""))
        if not ok:
            fails += 1

    print("fold_laminate_v0_1 self-test")
    print("-" * 66)

    # Session A: FOIL_DEV - the rich FOIL language is defined, then ROOT-corrected
    A = [
        Event("FOIL_DEV:E0001", ROOT, [],
              text="FOIL: full tier language. macro.micro.tactical.variable+1; "
                   "stanza.section.line.word; duplicate upshift; style-prompt = global macro container."),
        Event("FOIL_DEV:E0002", PROPOSAL, ["test"], text="Suno render of the tiered prompt."),
        Event("FOIL_DEV:E0003", ROOT, ["correction"], text="No - FOIL's factoring rule IS the routing rule."),
    ]
    # Session B: SYNTH - a later pass COLLAPSES FOIL to a frequency count (the documented loss)
    B = [
        Event("SYNTH:E0001", PROPOSAL, ["failure"], text="FOIL := frequency count + one edge case in synthesis."),
        Event("SYNTH:E0002", PROPOSAL, [], text="(unrelated) packaging note."),
    ]

    foil_null = Null("FOIL-OQ-2", note="scope-resolution sub-question - unresolved, declared signal")
    foil_conflict = Conflict("what-is-FOIL", members=["FOIL_DEV:E0001", "SYNTH:E0001"],
                             note="rich language vs frequency-count - parked, not merged")

    fa = fold_session(A, nulls=[foil_null], conflicts=[foil_conflict],
                      supersession_targets={"FOIL_DEV:E0003": "FOIL_DEV:E0001"})
    fb = fold_session(B)
    lam = Lamination().laminate(fa).laminate(fb)

    # F1 - the later frequency-count collapse did NOT drop the rich FOIL fold
    alive = lam._all_fold_ids()
    check("F1 no-flatten: rich FOIL survives the later collapse",
          "FOIL_DEV:E0001" in alive and "SYNTH:E0001" in alive)

    # F2 - no empty digest category; every digest ref is covered
    f2_ok = True
    for fo in lam.folds:
        refs = set()
        for ids in fo.digest.values():
            if not ids:
                f2_ok = False
            refs |= set(ids)
        if not refs.issubset(set(fo.covers)):
            f2_ok = False
    check("F2 provenance-complete: no skeleton categories", f2_ok)

    # F3 - declared null carried open; engine never fills it
    check("F3 no-silent-fill: FOIL-OQ-2 carried open",
          [n.key for n in lam.open_nulls()] == ["FOIL-OQ-2"])
    blocked = False
    try:
        lam.clear_null("FOIL-OQ-2", "SYNTH:E0001", PROPOSAL)
    except InvariantError:
        blocked = True
    check("F3/F5: PROPOSAL cannot clear a null", blocked)
    lam.clear_null("FOIL-OQ-2", "FOIL_DEV:E0003", ROOT)
    check("F3: ROOT clears the null explicitly", lam.open_nulls() == [])

    # F4 - the FOIL-definition contradiction is parked, not merged
    check("F4 no-silent-merge: 'what-is-FOIL' parked",
          [c.key for c in lam.open_conflicts()] == ["what-is-FOIL"])

    # F5 - failure preserved AS failure; ROOT correction is ROOT-authoritative; B has no ROOT supers
    root_super = [s for s in fa.supersessions if s.authority == "ROOT"]
    check("F5: failure preserved + ROOT correction authoritative",
          "SYNTH:E0001" in fb.failures and len(root_super) == 1
          and all(s.authority == "PROPOSAL" for s in fb.supersessions))

    # F6 - re-fold of A => v2 under v1, original event sha8 stable
    sha_before = A[0].sha8
    fa2 = fold_session(A, nulls=[foil_null], prior=fa,
                       supersession_targets={"FOIL_DEV:E0003": "FOIL_DEV:E0001"})
    check("F6 append-only: re-fold => v2 under v1, event sha8 stable",
          fa2.version == 2 and fa2.under is fa and A[0].sha8 == sha_before)

    # scope guard - refuse folding this-session output as source
    refused = False
    try:
        fold_session([Event("who_dat_runtime_assessment_v0_1:E1", ROOT, [], text="x")])
    except ValueError:
        refused = True
    check("scope: refuse folding this-session output as source", refused)

    # re-fold appends (append-only) and preserves v1 beneath -> exercises the under edge
    lam.laminate(fa2)
    check("F1 append-only re-fold: v1 still present after v2 laminated",
          "FOIL_DEV:E0001" in lam._all_fold_ids() and len(lam.folds) == 3)

    # emit graph sanity
    g = emit_graph(lam)
    check("emit: graph carries under + ROOT-supersedes edges",
          any(e["type"] == "under" for e in g["edges"])
          and any(e["type"] == "supersedes" and e["authority"] == "ROOT" for e in g["edges"]))

    print("-" * 66)
    print(f"{'ALL PASS' if fails == 0 else str(fails) + ' FAILED'}"
          f"  ({len(lam.folds)} folds laminated, {len(g['nodes'])} graph nodes)")
    return fails


if __name__ == "__main__":
    sys.exit(_selftest())
