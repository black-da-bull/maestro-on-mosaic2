from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import unittest

from calibration_manifest import CalibrationManifestError, MANIFEST_AUTHORITY, validate_calibration_manifest

FOLDER = Path(__file__).resolve().parents[3] / '_PROVENANCE/experiments/2026-09-14'


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.manifest = json.loads((FOLDER / 'bitter-thank-you-calibration-run-v0.7.json').read_text())
        # Exact allowlist, not filesystem resolution of caller-supplied paths.
        ref = self.manifest['model_runs'][0]['result_ref']
        self.evidence = {ref: (FOLDER / ref).read_bytes()}

    def validate(self):
        return validate_calibration_manifest(self.manifest, evidence_loader=self.evidence.__getitem__)

    def reject(self, pattern):
        with self.assertRaisesRegex(CalibrationManifestError, pattern):
            self.validate()

    def replicated(self):
        refs = []
        for i in range(3):
            ref = f'experiment:{i}'
            analysis_ref = f'analysis:{i}'
            analysis = json.dumps({'status': 'completed', 'output': {'rms': 0.1},
                                   'provenance': {'source_sha256': str(i) * 64}}).encode()
            self.evidence[analysis_ref] = analysis
            record = {'experiment_artifact_id': ref, 'source_sha256': str(i) * 64,
                      'status': 'completed', 'analysis_records': [{'ref': analysis_ref, 'sha256': hashlib.sha256(analysis).hexdigest()}]}
            raw = json.dumps(record).encode()
            self.evidence[ref] = raw
            self.manifest['evidence_surfaces'].append({
                'id': ref, 'class': 'renderer_experiment', 'authority': 'experimental',
                'experiment_artifact_id': ref, 'source_sha256': str(i) * 64,
                'result_ref': ref, 'result_sha256': hashlib.sha256(raw).hexdigest()})
            refs.append(ref)
        self.manifest['replication'].update(completed_runs=3, evidence_refs=refs)
        self.manifest['operator_judgment'] = {'status': 'completed', 'decision': 'promote', 'evidence_refs': refs}
        self.manifest['promotion'].update(level='policy', operator_approved=True, reversible=True,
                                         model_version_scope='Suno v6 test scope', experiment_artifact_ids=refs)

    def test_staged_observation(self):
        value = self.validate()
        self.assertEqual(value['promotion']['level'], 'observation')
        self.assertEqual(value['source']['sha256'], 'bb0e6ed54ca37c636bd6d4d91888e02a4a8f59652e2c2e7dcbb9e30af0cab66e')
        self.assertEqual(len(value['contradictions']), 3)
        self.assertEqual([r['adapter_id'] for r in value['model_runs'] if r['status'] == 'completed'], ['beat_this'])

    def test_authority_required(self):
        del self.manifest['authority']
        self.reject('authority_fields')

    def test_each_authority_flag(self):
        for key, expected in MANIFEST_AUTHORITY.items():
            with self.subTest(key=key):
                self.manifest['authority'][key] = not expected
                self.reject('authority_boundary')
                self.manifest['authority'][key] = expected

    def test_authority_no_numeric_booleans(self):
        self.manifest['authority']['canon_promotion'] = 0
        self.reject('authority_boundary')

    def test_unknown_authority(self):
        self.manifest['authority']['grant_everything'] = True
        self.reject('authority_fields')

    def test_unknown_adapter(self):
        self.manifest['model_runs'][0]['adapter_id'] = 'invented_model'
        self.reject('unsupported_adapter')

    def test_duplicate_adapter(self):
        self.manifest['model_runs'].append(deepcopy(self.manifest['model_runs'][0]))
        self.reject('duplicate_model_run')

    def test_wrong_source(self):
        self.manifest['model_runs'][0]['source_sha256'] = 'a' * 64
        self.reject('source_identity_mismatch')

    def test_no_completion_refs(self):
        self.manifest['model_runs'][0]['evidence_refs'] = []
        self.reject('completed_requires_evidence')

    def test_unresolvable_completion_ref(self):
        self.manifest['model_runs'][0]['evidence_refs'] = ['imaginary']
        self.reject('unknown_evidence_ref')

    def test_no_model_asset(self):
        del self.manifest['model_runs'][0]['model_identity']['asset_sha256']
        self.reject('model_asset_identity')

    def test_no_loader(self):
        with self.assertRaisesRegex(CalibrationManifestError, 'loader_required'):
            validate_calibration_manifest(self.manifest)

    def test_missing_result(self):
        self.evidence.clear()
        self.reject('evidence_unavailable')

    def test_tampered_result(self):
        self.evidence[self.manifest['model_runs'][0]['result_ref']] = b'{}'
        self.reject('evidence_unavailable')

    def change_result(self, mutate):
        run = self.manifest['model_runs'][0]
        result = json.loads(self.evidence[run['result_ref']])
        mutate(result)
        raw = json.dumps(result).encode()
        self.evidence[run['result_ref']] = raw
        run['result_sha256'] = hashlib.sha256(raw).hexdigest()
        for surface in self.manifest['evidence_surfaces']:
            if surface.get('ref') == run['result_ref']:
                surface['result_sha256'] = run['result_sha256']

    def test_empty_inference(self):
        self.change_result(lambda r: r.update(output={}))
        self.reject('output_required')

    def test_envelope_source_mismatch(self):
        self.change_result(lambda r: r['provenance'].update(source_sha256='a' * 64))
        self.reject('identity_mismatch')

    def test_envelope_model_mismatch(self):
        self.change_result(lambda r: r['provenance'].update(asset_sha256='a' * 64))
        self.reject('identity_mismatch')

    def test_envelope_unknown_fields(self):
        self.change_result(lambda r: r.update(canon_promotion=True))
        self.reject('envelope_invalid')

    def test_diagnostics_for_failure_states(self):
        run = self.manifest['model_runs'][1]
        del run['blocking_reason']
        for status in ['blocked', 'failed', 'unavailable', 'not_configured']:
            with self.subTest(status=status):
                run['status'] = status
                self.reject('blocking_reason_invalid')
        run['error'] = 'checkpoint missing'
        self.validate()

    def test_contradiction_requires_evidence(self):
        self.manifest['contradictions'][0].update(resolution='resolved_with_evidence', evidence_refs=[])
        self.reject('resolved_requires_evidence')

    def test_contradiction_unknown_reference(self):
        self.manifest['contradictions'][0].update(resolution='resolved_with_evidence', evidence_refs=['typo'])
        self.reject('unknown_evidence_ref')

    def test_premature_candidate(self):
        self.manifest['promotion']['level'] = 'candidate'
        self.reject('requires_replication')

    def test_unsupported_replication_count(self):
        self.manifest['replication']['completed_runs'] = 3
        self.reject('evidence_count_mismatch')

    def test_boolean_counter(self):
        self.manifest['replication']['completed_runs'] = False
        self.reject('completed_runs_invalid')

    def test_duplicate_replication_refs(self):
        self.replicated()
        self.manifest['replication']['evidence_refs'] = ['experiment:0'] * 3
        self.reject('duplicates')

    def test_replication_source_identity(self):
        self.replicated()
        self.manifest['evidence_surfaces'][-1]['source_sha256'] = 'a' * 64
        self.reject('replication_identity')

    def test_candidate_explicit_approval(self):
        self.replicated()
        self.manifest['promotion'].update(level='candidate', operator_approved=False)
        self.manifest['operator_judgment']['decision'] = 'reject promotion'
        self.reject('explicit_operator_approval')

    def test_rejected_decision_cannot_promote(self):
        self.replicated()
        self.manifest['operator_judgment']['decision'] = 'reject promotion'
        self.reject('affirmative_decision')

    def test_missing_replication_analysis(self):
        self.replicated()
        del self.evidence['analysis:1']
        self.reject('evidence_unavailable')

    def test_operator_judgment_required(self):
        self.replicated()
        self.manifest['operator_judgment']['status'] = 'pending'
        self.reject('requires_operator_judgment')

    def test_policy_scope(self):
        self.replicated()
        del self.manifest['promotion']['model_version_scope']
        self.reject('model_version_scope')

    def test_policy_reversibility(self):
        self.replicated()
        self.manifest['promotion']['reversible'] = False
        self.reject('must_be_reversible')

    def test_policy_evidence(self):
        self.replicated()
        self.manifest['promotion']['experiment_artifact_ids'] = ['invented']
        self.reject('verified_experiments')

    def test_valid_policy_does_not_mutate_authority(self):
        self.replicated()
        self.assertEqual(self.validate()['authority'], MANIFEST_AUTHORITY)

    def test_no_automatic_promotion_or_score(self):
        for field in ['auto_promotion', 'universal_quality_score']:
            self.manifest['promotion'][field] = True
            self.reject('forbidden')
            self.manifest['promotion'][field] = False


if __name__ == '__main__':
    unittest.main()
