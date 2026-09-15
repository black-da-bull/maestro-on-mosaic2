from __future__ import annotations

import re
import hashlib
import json
from collections.abc import Callable

from worker_core import ADAPTER_META, AUTHORITY
from typing import Any

SCHEMA = 'maestro.audio.calibration-run.v0.7'
SHA_RE = re.compile(r'^[0-9a-f]{64}$')
MODEL_STATUSES = {'planned', 'blocked', 'not_configured', 'unavailable', 'failed', 'completed'}
PROMOTION_LEVELS = {'none', 'observation', 'candidate', 'policy'}
MANIFEST_AUTHORITY = {**AUTHORITY, 'creative_ust_mutation': False, 'auto_promotion': False}
CONTRADICTION_RESOLUTIONS = {'preserve_both', 'unresolved', 'resolved_with_evidence'}


class CalibrationManifestError(ValueError):
    pass


def _require_string(value: Any, name: str, *, max_len: int = 1000) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > max_len:
        raise CalibrationManifestError(f'{name}_invalid')
    return value


def _require_sha(value: Any, name: str) -> str:
    if not isinstance(value, str) or not SHA_RE.fullmatch(value):
        raise CalibrationManifestError(f'{name}_must_be_lowercase_sha256')
    return value


def _validate_evidence_refs(value: Any, name: str) -> list[str]:
    if not isinstance(value, list):
        raise CalibrationManifestError(f'{name}_must_be_list')
    out: list[str] = []
    for ref in value:
        out.append(_require_string(ref, f'{name}_ref', max_len=500))
    if len(set(out)) != len(out):
        raise CalibrationManifestError(f'{name}_duplicates')
    return out


def validate_calibration_manifest(payload: Any, *, evidence_loader: Callable[[str], bytes] | None = None) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise CalibrationManifestError('manifest_must_be_object')
    if payload.get('schema') != SCHEMA:
        raise CalibrationManifestError('unsupported_manifest_schema')

    authority = payload.get('authority')
    if not isinstance(authority, dict) or set(authority) != set(MANIFEST_AUTHORITY):
        raise CalibrationManifestError('authority_fields_invalid')
    if any(authority[k] is not v for k, v in MANIFEST_AUTHORITY.items()):
        raise CalibrationManifestError('authority_boundary_violation')

    run_id = _require_string(payload.get('run_id'), 'run_id', max_len=300)
    project_id = _require_string(payload.get('project_id'), 'project_id', max_len=300)

    source = payload.get('source')
    if not isinstance(source, dict):
        raise CalibrationManifestError('source_must_be_object')
    source_ref = _require_string(source.get('artifact_ref'), 'source_artifact_ref', max_len=1000)
    source_sha = _require_sha(source.get('sha256'), 'source_sha256')
    artifact_role = _require_string(source.get('artifact_role'), 'source_artifact_role', max_len=200)
    if source.get('content_verified') is not True:
        raise CalibrationManifestError('source_content_must_be_verified')

    surfaces = payload.get('evidence_surfaces')
    if not isinstance(surfaces, list) or not surfaces:
        raise CalibrationManifestError('evidence_surfaces_must_be_nonempty_list')
    clean_surfaces: list[dict[str, Any]] = []
    surface_ids: set[str] = set()
    for index, surface in enumerate(surfaces):
        if not isinstance(surface, dict):
            raise CalibrationManifestError(f'evidence_surface_{index}_must_be_object')
        sid = _require_string(surface.get('id'), f'evidence_surface_{index}_id', max_len=300)
        if sid in surface_ids:
            raise CalibrationManifestError(f'duplicate_evidence_surface:{sid}')
        surface_ids.add(sid)
        clean = dict(surface)
        clean['id'] = sid
        clean['class'] = _require_string(surface.get('class'), f'evidence_surface_{index}_class', max_len=100)
        clean['authority'] = _require_string(surface.get('authority'), f'evidence_surface_{index}_authority', max_len=200)
        clean_surfaces.append(clean)

    runs = payload.get('model_runs')
    if not isinstance(runs, list) or not runs:
        raise CalibrationManifestError('model_runs_must_be_nonempty_list')
    clean_runs: list[dict[str, Any]] = []
    adapter_ids: set[str] = set()
    for index, run in enumerate(runs):
        if not isinstance(run, dict):
            raise CalibrationManifestError(f'model_run_{index}_must_be_object')
        adapter_id = _require_string(run.get('adapter_id'), f'model_run_{index}_adapter_id', max_len=100)
        if adapter_id not in ADAPTER_META:
            raise CalibrationManifestError('unsupported_adapter_id')
        if adapter_id in adapter_ids:
            raise CalibrationManifestError(f'duplicate_model_run:{adapter_id}')
        adapter_ids.add(adapter_id)
        status = run.get('status')
        if not isinstance(status, str) or status not in MODEL_STATUSES:
            raise CalibrationManifestError(f'model_run_{adapter_id}_invalid_status')
        if _require_sha(run.get('source_sha256'), f'model_run_{adapter_id}_source_sha256') != source_sha:
            raise CalibrationManifestError(f'model_run_{adapter_id}_source_identity_mismatch')
        clean = dict(run)
        clean['adapter_id'] = adapter_id
        clean['status'] = status
        clean['evidence_refs'] = _validate_evidence_refs(run.get('evidence_refs', []), f'model_run_{adapter_id}_evidence_refs')
        if any(ref not in surface_ids for ref in clean['evidence_refs']):
            raise CalibrationManifestError('model_run_unknown_evidence_ref')
        if status == 'completed':
            if not clean['evidence_refs']:
                raise CalibrationManifestError('completed_requires_evidence_refs')
            identity = run.get('model_identity')
            if not isinstance(identity, dict):
                raise CalibrationManifestError(f'model_run_{adapter_id}_completed_requires_model_identity')
            _require_string(identity.get('implementation'), f'model_run_{adapter_id}_implementation', max_len=300)
            _require_string(identity.get('version'), f'model_run_{adapter_id}_version', max_len=300)
            hashes = identity.get('asset_sha256')
            if adapter_id != 'statistical_embedding' and hashes is None:
                raise CalibrationManifestError('completed_requires_model_asset_identity')
            if hashes is not None:
                if isinstance(hashes, str):
                    _require_sha(hashes, f'model_run_{adapter_id}_asset_sha256')
                elif isinstance(hashes, dict):
                    if not hashes:
                        raise CalibrationManifestError(f'model_run_{adapter_id}_asset_sha256_empty')
                    for key, value in hashes.items():
                        _require_string(key, f'model_run_{adapter_id}_asset_name', max_len=200)
                        _require_sha(value, f'model_run_{adapter_id}_{key}_sha256')
                else:
                    raise CalibrationManifestError(f'model_run_{adapter_id}_asset_sha256_invalid')
            _validate_completed_result(run, clean_surfaces, evidence_loader)
        elif status != 'planned':
            _require_string(run.get('blocking_reason') or run.get('error'), f'model_run_{adapter_id}_blocking_reason', max_len=2000)
        clean_runs.append(clean)

    contradictions = payload.get('contradictions')
    if not isinstance(contradictions, list):
        raise CalibrationManifestError('contradictions_must_be_list')
    clean_contradictions: list[dict[str, Any]] = []
    contradiction_ids: set[str] = set()
    for index, item in enumerate(contradictions):
        if not isinstance(item, dict):
            raise CalibrationManifestError(f'contradiction_{index}_must_be_object')
        cid = _require_string(item.get('id'), f'contradiction_{index}_id', max_len=300)
        if cid in contradiction_ids:
            raise CalibrationManifestError(f'duplicate_contradiction:{cid}')
        contradiction_ids.add(cid)
        resolution = item.get('resolution')
        if not isinstance(resolution, str) or resolution not in CONTRADICTION_RESOLUTIONS:
            raise CalibrationManifestError(f'contradiction_{cid}_invalid_resolution')
        clean = dict(item)
        clean['id'] = cid
        clean['a'] = _require_string(item.get('a'), f'contradiction_{cid}_a', max_len=2000)
        clean['b'] = _require_string(item.get('b'), f'contradiction_{cid}_b', max_len=2000)
        clean['resolution'] = resolution
        clean['evidence_refs'] = _validate_evidence_refs(item.get('evidence_refs', []), f'contradiction_{cid}_evidence_refs')
        if resolution == 'resolved_with_evidence' and not clean['evidence_refs']:
            raise CalibrationManifestError(f'contradiction_{cid}_resolved_requires_evidence')
        if any(ref not in surface_ids for ref in clean['evidence_refs']):
            raise CalibrationManifestError('contradiction_unknown_evidence_ref')
        clean_contradictions.append(clean)

    operator = payload.get('operator_judgment')
    if not isinstance(operator, dict):
        raise CalibrationManifestError('operator_judgment_must_be_object')
    operator_status = operator.get('status')
    if not isinstance(operator_status, str) or operator_status not in {'pending', 'completed'}:
        raise CalibrationManifestError('operator_judgment_invalid_status')
    if operator_status == 'completed':
        _require_string(operator.get('decision'), 'operator_judgment_decision', max_len=300)
        operator_refs = _validate_evidence_refs(operator.get('evidence_refs', []), 'operator_judgment_evidence_refs')
        if any(ref not in surface_ids for ref in operator_refs):
            raise CalibrationManifestError('operator_judgment_unknown_evidence_ref')

    replication = payload.get('replication')
    if not isinstance(replication, dict):
        raise CalibrationManifestError('replication_must_be_object')
    required = replication.get('required_runs')
    completed = replication.get('completed_runs')
    if type(required) is not int or required < 1:
        raise CalibrationManifestError('replication_required_runs_invalid')
    if type(completed) is not int or completed < 0 or completed > required:
        raise CalibrationManifestError('replication_completed_runs_invalid')

    refs = _validate_evidence_refs(replication.get('evidence_refs', []), 'replication_evidence_refs')
    if len(refs) != completed:
        raise CalibrationManifestError('replication_evidence_count_mismatch')
    identities = set()
    artifact_identities = set()
    for ref in refs:
        surface = next((x for x in clean_surfaces if x['id'] == ref), None)
        if surface is None or surface['class'] != 'renderer_experiment':
            raise CalibrationManifestError('replication_requires_experiment_evidence')
        experiment_id = _require_string(surface.get('experiment_artifact_id'), 'experiment_artifact_id')
        artifact_sha = _require_sha(surface.get('source_sha256'), 'replication_source_sha256')
        result_ref = _require_string(surface.get('result_ref'), 'replication_result_ref')
        result_sha = _require_sha(surface.get('result_sha256'), 'replication_result_sha256')
        record = _load_evidence(result_ref, result_sha, evidence_loader)
        if record.get('experiment_artifact_id') != experiment_id or record.get('source_sha256') != artifact_sha:
            raise CalibrationManifestError('replication_identity_mismatch')
        if record.get('status') != 'completed' or not isinstance(record.get('analysis_records'), list) or not record['analysis_records']:
            raise CalibrationManifestError('replication_requires_completed_analysis')
        for analysis in record['analysis_records']:
            if not isinstance(analysis, dict):
                raise CalibrationManifestError('replication_analysis_reference_invalid')
            analysis_ref = _require_string(analysis.get('ref'), 'replication_analysis_ref')
            analysis_sha = _require_sha(analysis.get('sha256'), 'replication_analysis_sha256')
            result = _load_evidence(analysis_ref, analysis_sha, evidence_loader)
            provenance = result.get('provenance')
            if (result.get('status') != 'completed' or not isinstance(result.get('output'), dict)
                    or not result['output'] or not isinstance(provenance, dict)
                    or provenance.get('source_sha256') != artifact_sha):
                raise CalibrationManifestError('replication_analysis_invalid')
        if artifact_sha in artifact_identities:
            raise CalibrationManifestError('duplicate_replication_artifact')
        artifact_identities.add(artifact_sha)
        if experiment_id in identities:
            raise CalibrationManifestError('duplicate_replication_identity')
        identities.add(experiment_id)

    promotion = payload.get('promotion')
    if not isinstance(promotion, dict):
        raise CalibrationManifestError('promotion_must_be_object')
    level = promotion.get('level')
    if not isinstance(level, str) or level not in PROMOTION_LEVELS:
        raise CalibrationManifestError('promotion_level_invalid')
    operator_approved = promotion.get('operator_approved') is True
    if level in {'candidate', 'policy'}:
        if completed < required:
            raise CalibrationManifestError('promotion_candidate_requires_replication')
        if operator_status != 'completed':
            raise CalibrationManifestError('promotion_candidate_requires_operator_judgment')
    if level in {'candidate', 'policy'} and not operator_approved:
        raise CalibrationManifestError('policy_promotion_requires_explicit_operator_approval')
    if level in {'candidate', 'policy'}:
        if operator.get('decision') != 'promote':
            raise CalibrationManifestError('promotion_requires_affirmative_decision')
        _require_string(promotion.get('model_version_scope'), 'model_version_scope', max_len=500)
        experiments = _validate_evidence_refs(promotion.get('experiment_artifact_ids'), 'promotion_experiment_artifact_ids')
        if not experiments or any(x not in identities for x in experiments):
            raise CalibrationManifestError('promotion_requires_verified_experiments')
    if level == 'policy' and promotion.get('reversible') is not True:
        raise CalibrationManifestError('policy_must_be_reversible')
    if promotion.get('universal_quality_score') is not False:
        raise CalibrationManifestError('universal_quality_score_forbidden')
    if promotion.get('auto_promotion') is not False:
        raise CalibrationManifestError('auto_promotion_forbidden')

    return {
        **payload,
        'run_id': run_id,
        'project_id': project_id,
        'source': {**source, 'artifact_ref': source_ref, 'sha256': source_sha, 'artifact_role': artifact_role},
        'evidence_surfaces': clean_surfaces,
        'model_runs': clean_runs,
        'contradictions': clean_contradictions,
    }


def _load_evidence(ref, expected_sha, loader):
    # The caller supplies a trusted content store. Manifest URLs/paths are never opened here.
    if loader is None:
        raise CalibrationManifestError('evidence_loader_required')
    try:
        raw = loader(ref)
        if not isinstance(raw, bytes) or len(raw) > 2 * 1024 * 1024:
            raise ValueError('invalid_size_or_type')
        if hashlib.sha256(raw).hexdigest() != expected_sha:
            raise ValueError('hash_mismatch')
        record = json.loads(raw)
        if not isinstance(record, dict):
            raise ValueError('not_object')
        return record
    except (OSError, KeyError, ValueError, TypeError) as exc:
        raise CalibrationManifestError(f'evidence_unavailable_or_invalid:{ref}') from exc


def _validate_completed_result(run, surfaces, loader):
    ref = _require_string(run.get('result_ref'), 'completed_result_ref')
    sha = _require_sha(run.get('result_sha256'), 'completed_result_sha256')
    if not any(s['id'] in run['evidence_refs'] and s.get('ref') == ref and s.get('result_sha256') == sha for s in surfaces):
        raise CalibrationManifestError('completed_result_surface_missing')
    result = _load_evidence(ref, sha, loader)
    # Use the strict worker result envelope, not provider traces or summary-only receipts.
    allowed = {'adapter_id', 'status', 'schema', 'output', 'confidence', 'provenance', 'warnings', 'error'}
    if set(result) - allowed or result.get('status') != 'completed' or result.get('adapter_id') != run['adapter_id']:
        raise CalibrationManifestError('completed_result_envelope_invalid')
    _require_string(result.get('schema'), 'completed_result_schema')
    if not isinstance(result.get('output'), dict) or not result['output']:
        raise CalibrationManifestError('completed_result_output_required')
    provenance = result.get('provenance')
    if not isinstance(provenance, dict):
        raise CalibrationManifestError('completed_result_provenance_required')
    identity = run['model_identity']
    expected = {'source_sha256': run['source_sha256'], 'implementation': identity['implementation'],
                'implementation_version': identity['version'], 'asset_sha256': identity.get('asset_sha256'),
                'evidence_class': ADAPTER_META[run['adapter_id']]['evidence_class']}
    if any(provenance.get(k) != v for k, v in expected.items()):
        raise CalibrationManifestError('completed_result_identity_mismatch')
    if not isinstance(result.get('warnings', []), list) or not all(isinstance(x, str) for x in result.get('warnings', [])):
        raise CalibrationManifestError('completed_result_warnings_invalid')
