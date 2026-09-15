# Calibration manifest validation

The v0.7 manifest is development evidence. Validation never promotes Technical UST,
Creative UST, canon, renderer policy, or keeper/release state.

`validate_calibration_manifest(payload, evidence_loader=loader)` requires the full
`MANIFEST_AUTHORITY` block with exact boolean values. Model IDs come from the worker
registry. Failed, blocked, unavailable and unconfigured runs require diagnostics.
Planned work can remain without a failure diagnostic.

The loader is supplied by trusted application code and returns persisted bytes for
an allowlisted logical reference. It must not open arbitrary paths or URLs from a
manifest. No filesystem or network retrieval is performed by this validator. Every
loaded record is limited to 2 MiB and verified against its SHA-256 before parsing.

Completed runs require a declared evidence surface, a result reference, a byte hash,
model/package identity, and model asset hashes (except the statistical baseline).
The persisted worker envelope must identify the same source, adapter, implementation,
version and assets, with completed status and nonempty output. This checks an
evidence contract; it does not independently rerun or prove the musical inference.

Replication evidence references must resolve to renderer-experiment surfaces with
distinct experiment IDs and artifact hashes. Each surface points to a hash-verified
completed experiment record containing `experiment_artifact_id`, `source_sha256`,
`status`, and nonempty `analysis_records` (`ref` and `sha256` for each persisted
analysis). Analysis contents must identify the same artifact and contain completed
output. Counters alone cannot satisfy replication. Required counts are experimental
policy, not a universal renderer fact.

Candidate and policy records require completed replication, completed operator
judgment with `decision: "promote"`, `operator_approved: true`, model/version scope,
and verified experiment IDs. Policies additionally require `reversible: true`.
These fields record an approval; callers remain responsible for authenticating the
operator. The validator grants no workflow mutation authority.

All contradiction references must identify declared evidence surfaces. Resolved
contradictions require at least one reference. Referencing a surface preserves its
evidence class; it does not upgrade provider text to measurement.

The Bitter Thank You worker envelope is a normalized copy of the prior private-run
receipt, which remains unchanged. Its reference/hash replace the old summary receipt
in the manifest. This repair does not represent a new Beat This execution.

Run: `PYTHONPATH=. python tests/test_calibration_manifest.py`.
