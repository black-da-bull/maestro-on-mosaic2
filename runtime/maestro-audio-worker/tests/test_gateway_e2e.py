from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
import wave
from pathlib import Path
from urllib.request import Request, urlopen

import numpy as np

WORKER_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WORKER_ROOT))
from worker_core import ArtifactStore, sha256_file  # noqa: E402


def make_wav(path: Path) -> None:
    sr = 16000
    t = np.arange(sr * 2, dtype=np.float32) / sr
    x = (0.15 * np.sin(2 * np.pi * 220 * t) * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr); w.writeframes(x.tobytes())


def request_json(method: str, url: str, token: str, payload=None):
    body = None if payload is None else json.dumps(payload).encode('utf-8')
    headers = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    if body is not None:
        headers['Content-Type'] = 'application/json'
    req = Request(url, data=body, headers=headers, method=method)
    with urlopen(req, timeout=10) as r:
        return r.status, json.loads(r.read().decode('utf-8'))


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source = root / 'source.wav'; make_wav(source)
        sha = sha256_file(source)
        artifact_root = root / 'artifacts'; state_root = root / 'state'
        ArtifactStore(artifact_root).import_file(source, sha)
        token = 'integration-secret'
        env = os.environ.copy()
        env.update({
            'PYTHONPATH': str(WORKER_ROOT),
            'MAESTRO_ARTIFACT_ROOT': str(artifact_root),
            'MAESTRO_AUDIO_WORKER_STATE': str(state_root),
            'MAESTRO_AUDIO_WORKER_TOKEN': token,
            'MAESTRO_AUDIO_WORKER_CONCURRENCY': '1',
        })
        proc = subprocess.Popen(
            [sys.executable, '-m', 'uvicorn', 'service:app', '--host', '127.0.0.1', '--port', '8099'],
            cwd=WORKER_ROOT, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
        )
        try:
            deadline = time.time() + 20
            while True:
                if proc.poll() is not None:
                    raise RuntimeError('worker_exited:' + (proc.stdout.read() if proc.stdout else ''))
                try:
                    with urlopen('http://127.0.0.1:8099/health', timeout=1) as r:
                        if r.status == 200: break
                except Exception: pass
                if time.time() >= deadline: raise RuntimeError('worker_health_timeout')
                time.sleep(0.1)
            status, caps = request_json('GET', 'http://127.0.0.1:8099/v1/capabilities', token)
            assert status == 200 and caps['authority']['canon_promotion'] is False
            payload = {
                'schema': 'maestro.audio.gateway.v0.5',
                'project_id': 'project:gateway-e2e',
                'source_ref': f'artifact:sha256:{sha}',
                'source_sha256': sha,
                'deterministic_analysis_id': 'analysis:gateway-e2e',
                'adapters': ['statistical_embedding'],
                'context': {},
                'authority': {
                    'technical_ust_mutation': False,
                    'canon_promotion': False,
                    'renderer_policy_promotion': False,
                    'keeper_or_release_approval': False,
                    'operator_decision_required': True,
                },
            }
            status, submitted = request_json('POST', 'http://127.0.0.1:8099/v1/jobs', token, payload)
            assert status == 202 and submitted['job_id'].startswith('job-')
            deadline = time.time() + 30
            while True:
                status, result = request_json('GET', f"http://127.0.0.1:8099/v1/jobs/{submitted['job_id']}", token)
                assert status == 200
                if result['status'] in {'completed', 'failed'}: break
                if time.time() >= deadline: raise RuntimeError('job_timeout')
                time.sleep(0.1)
            assert result['status'] == 'completed', result
            adapter = result['results'][0]
            assert adapter['adapter_id'] == 'statistical_embedding'
            assert adapter['status'] == 'completed'
            assert adapter['provenance']['source_sha256'] == sha
            assert adapter['provenance']['evidence_class'] == 'derived_measurement'
            print(json.dumps({'passed': True, 'checks': 9, 'job_id': submitted['job_id'], 'source_sha256': sha}, indent=2))
        finally:
            proc.terminate()
            try: proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill(); proc.wait(timeout=5)


if __name__ == '__main__': main()
