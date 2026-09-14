from __future__ import annotations

import json
import tempfile
import wave
from pathlib import Path

import numpy as np

from worker_core import ArtifactStore, JobStore, create_job, execute_job, probe_capabilities, public_job, sha256_file, validate_job_request


def wav(path: Path):
    sr = 8000
    t = np.arange(sr, dtype=np.float32) / sr
    x = (0.2 * np.sin(2 * np.pi * 440 * t) * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(x.tobytes())


def main():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source = root / 'source.wav'; wav(source)
        sha = sha256_file(source)
        artifacts = ArtifactStore(root / 'artifacts')
        imported = artifacts.import_file(source, sha)
        assert imported['immutable'] is True
        obj = Path(imported['path'])
        assert oct(obj.stat().st_mode & 0o777) == '0o444'
        assert sha256_file(artifacts.retrieve(sha)) == sha

        req = {
            'schema': 'maestro.audio.gateway.v0.5',
            'project_id': 'project:test',
            'source_ref': f'artifact:sha256:{sha}',
            'source_sha256': sha,
            'deterministic_analysis_id': 'analysis:test',
            'adapters': ['statistical_embedding', 'beat_this'],
            'context': {},
            'authority': {
                'technical_ust_mutation': False,
                'canon_promotion': False,
                'renderer_policy_promotion': False,
                'keeper_or_release_approval': False,
                'operator_decision_required': True,
            },
        }
        clean = validate_job_request(req)
        assert clean['adapters'] == ['statistical_embedding', 'beat_this']
        jobs = JobStore(root / 'state')
        record = create_job(req, artifacts, jobs)
        done = execute_job(record['job_id'], artifacts, jobs)
        pub = public_job(done)
        assert pub['status'] == 'completed'
        by_id = {r['adapter_id']: r for r in pub['results']}
        assert by_id['statistical_embedding']['status'] == 'completed'
        assert by_id['statistical_embedding']['provenance']['source_sha256'] == sha
        assert by_id['beat_this']['status'] in {'not_configured','completed','failed','unavailable'}
        assert set(public_job(record)) <= {'job_id','status','source_sha256','adapters','results','error','created_at','updated_at','completed_at'}
        caps = probe_capabilities()
        assert caps['authority']['canon_promotion'] is False
        assert 'beat_this' in caps['adapters']
        print(json.dumps({'passed': True, 'checks': 13, 'beat_this_status': by_id['beat_this']['status'], 'capabilities': caps}, indent=2))


if __name__ == '__main__':
    main()
