from __future__ import annotations

from copy import deepcopy

from calibration_manifest import CalibrationManifestError, SCHEMA, validate_calibration_manifest

SHA = 'b' * 64


def base_manifest():
    return {
        'schema': SCHEMA,
        'run_id': 'calibration:test:001',
        'project_id': 'project:test',
        'source': {
            'artifact_ref': 'artifact:test:source',
            'sha256': SHA,
            'artifact_role': 'original_reference',
            'content_verified': True,
        },
        'evidence_surfaces': [
            {'id': 'studio-header', 'class': 'provider_project_state', 'authority': 'observed_evidence', 'value': 103.0},
            {'id': 'midi-map', 'class': 'artifact_measurement', 'authority': 'derived_measurement', 'value': 100.65},
        ],
        'model_runs': [
            {
                'adapter_id': 'beat_this',
                'status': 'blocked',
                'source_sha256': SHA,
                'blocking_reason': 'worker_not_provisioned',
                'evidence_refs': [],
            },
            {
                'adapter_id': 'clap',
                'status': 'completed',
                'source_sha256': SHA,
                'model_identity': {
                    'implementation': 'LAION-AI/CLAP',
                    'version': '1.1.7',
                    'asset_sha256': 'c' * 64,
                },
                'evidence_refs': ['evidence:clap:001'],
            },
        ],
        'contradictions': [
            {
                'id': 'tempo-surface-disagreement',
                'a': 'Studio header 103 BPM',
                'b': 'MIDI map median 100.65 BPM',
                'resolution': 'preserve_both',
                'evidence_refs': ['studio-header', 'midi-map'],
            }
        ],
        'operator_judgment': {'status': 'pending'},
        'replication': {'required_runs': 3, 'completed_runs': 0},
        'promotion': {
            'level': 'observation',
            'operator_approved': False,
            'universal_quality_score': False,
            'auto_promotion': False,
        },
    }


def expect_error(payload, text):
    try:
        validate_calibration_manifest(payload)
    except CalibrationManifestError as exc:
        assert text in str(exc), (text, str(exc))
    else:
        raise AssertionError(f'expected {text}')


def main():
    manifest = base_manifest()
    validated = validate_calibration_manifest(manifest)
    assert validated['promotion']['level'] == 'observation'

    wrong_source = deepcopy(manifest)
    wrong_source['model_runs'][0]['source_sha256'] = 'a' * 64
    expect_error(wrong_source, 'source_identity_mismatch')

    premature_candidate = deepcopy(manifest)
    premature_candidate['promotion']['level'] = 'candidate'
    expect_error(premature_candidate, 'requires_replication')

    no_operator = deepcopy(manifest)
    no_operator['replication']['completed_runs'] = 3
    no_operator['promotion']['level'] = 'candidate'
    expect_error(no_operator, 'requires_operator_judgment')

    forbidden_score = deepcopy(manifest)
    forbidden_score['promotion']['universal_quality_score'] = True
    expect_error(forbidden_score, 'universal_quality_score_forbidden')

    lost_contradiction = deepcopy(manifest)
    lost_contradiction['contradictions'][0]['resolution'] = 'resolved_with_evidence'
    lost_contradiction['contradictions'][0]['evidence_refs'] = []
    expect_error(lost_contradiction, 'resolved_requires_evidence')

    policy = deepcopy(manifest)
    policy['operator_judgment'] = {'status': 'completed', 'decision': 'promote', 'evidence_refs': ['operator:listen:001']}
    policy['replication']['completed_runs'] = 3
    policy['promotion']['level'] = 'policy'
    expect_error(policy, 'explicit_operator_approval')
    policy['promotion']['operator_approved'] = True
    validated_policy = validate_calibration_manifest(policy)
    assert validated_policy['promotion']['level'] == 'policy'

    print({'passed': True, 'checks': 8, 'schema': SCHEMA})


if __name__ == '__main__':
    main()
