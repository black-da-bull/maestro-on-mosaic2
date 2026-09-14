from __future__ import annotations

import re
from typing import Any

SCHEMA = 'maestro.audio.calibration-run.v0.7'
SHA_RE = re.compile(r'^[0-9a-f]{64}$')
MODEL_STATUSES = {'planned', 'blocked', 'not_configured', 'unavailable', 'failed', 'completed'}
PROMOTION_LEVELS = {'none', 'observation', 'candidate', 'policy'}
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
    return out


def validate_calibration_manifest(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise CalibrationManifestError('manifest_must_be_object')
    if payload.get('schema') != SCHEMA:
        raise CalibrationManifestError('unsupported_manifest_schema')

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
        if adapter_id in adapter_ids:
            raise CalibrationManifestError(f'duplicate_model_run:{adapter_id}')
        adapter_ids.add(adapter_id)
        status = run.get('status')
        if status not in MODEL_STATUSES:
            raise CalibrationManifestError(f'model_run_{adapter_id}_invalid_status')
        if _require_sha(run.get('source_sha256'), f'model_run_{adapter_id}_source_sha256') != source_sha:
            raise CalibrationManifestError(f'model_run_{adapter_id}_source_identity_mismatch')
        clean = dict(run)
        clean['adapter_id'] = adapter_id
        clean['status'] = status
        clean['evidence_refs'] = _validate_evidence_refs(run.get('evidence_refs', []), f'model_run_{adapter_id}_evidence_refs')
        if status == 'completed':
            identity = run.get('model_identity')
            if not isinstance(identity, dict):
                raise CalibrationManifestError(f'model_run_{adapter_id}_completed_requires_model_identity')
            _require_string(identity.get('implementation'), f'model_run_{adapter_id}_implementation', max_len=300)
            _require_string(identity.get('version'), f'model_run_{adapter_id}_version', max_len=300)
            hashes = identity.get('asset_sha256')
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
        else:
            _require_string(run.get('blocking_reason') or run.get('error') or 'not_completed', f'model_run_{adapter_id}_blocking_reason', max_len=2000)
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
        if resolution not in CONTRADICTION_RESOLUTIONS:
            raise CalibrationManifestError(f'contradiction_{cid}_invalid_resolution')
        clean = dict(item)
        clean['id'] = cid
        clean['a'] = _require_string(item.get('a'), f'contradiction_{cid}_a', max_len=2000)
        clean['b'] = _require_string(item.get('b'), f'contradiction_{cid}_b', max_len=2000)
        clean['resolution'] = resolution
        clean['evidence_refs'] = _validate_evidence_refs(item.get('evidence_refs', []), f'contradiction_{cid}_evidence_refs')
        if resolution == 'resolved_with_evidence' and not clean['evidence_refs']:
            raise CalibrationManifestError(f'contradiction_{cid}_resolved_requires_evidence')
        clean_contradictions.append(clean)

    operator = payload.get('operator_judgment')
    if not isinstance(operator, dict):
        raise CalibrationManifestError('operator_judgment_must_be_object')
    operator_status = operator.get('status')
    if operator_status not in {'pending', 'completed'}:
        raise CalibrationManifestError('operator_judgment_invalid_status')
    if operator_status == 'completed':
        _require_string(operator.get('decision'), 'operator_judgment_decision', max_len=300)
        _validate_evidence_refs(operator.get('evidence_refs', []), 'operator_judgment_evidence_refs')

    replication = payload.get('replication')
    if not isinstance(replication, dict):
        raise CalibrationManifestError('replication_must_be_object')
    required = replication.get('required_runs')
    completed = replication.get('completed_runs')
    if not isinstance(required, int) or required < 1:
        raise CalibrationManifestError('replication_required_runs_invalid')
    if not isinstance(completed, int) or completed < 0 or completed > required:
        raise CalibrationManifestError('replication_completed_runs_invalid')

    promotion = payload.get('promotion')
    if not isinstance(promotion, dict):
        raise CalibrationManifestError('promotion_must_be_object')
    level = promotion.get('level')
    if level not in PROMOTION_LEVELS:
        raise CalibrationManifestError('promotion_level_invalid')
    operator_approved = promotion.get('operator_approved') is True
    if level in {'candidate', 'policy'}:
        if completed < required:
            raise CalibrationManifestError('promotion_candidate_requires_replication')
        if operator_status != 'completed':
            raise CalibrationManifestError('promotion_candidate_requires_operator_judgment')
    if level == 'policy' and not operator_approved:
        raise CalibrationManifestError('policy_promotion_requires_explicit_operator_approval')
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
