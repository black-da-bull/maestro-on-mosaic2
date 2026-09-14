from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
import wave
from pathlib import Path

import numpy as np

WORKER_ROOT = Path(__file__).resolve().parents[1]
WORKFORCE_ROOT = WORKER_ROOT.parent / 'maestro-workforce'
sys.path.insert(0, str(WORKER_ROOT))
sys.path.insert(0, str(WORKFORCE_ROOT))

from worker_core import ArtifactStore, sha256_file  # noqa: E402
import audio_analysis_gateway as gateway  # noqa: E402


def make_wav(path: Path) -> None:
    sr = 16000
    t = np.arange(sr * 2, dtype=np.float32) / sr
    x = (0.12 * np.sin(2 * np.pi * 330 * t) * 32767).astype('<i2')
    with wave.open(str(path), 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes(x.tobytes())


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source = root / 'source.wav'
        make_wav(source)
        sha = sha256_file(source)
        artifact_root = root / 'artifacts'
        state_root = root / 'state'
        ArtifactStore(artifact_root).import_file(source, sha)

        token = 'maestro-gateway-worker-integration-secret'
        port = '8101'
        child_env = os.environ.copy()
        child_env.update({
            'PYTHONPATH': str(WORKER_ROOT),
            'MAESTRO_ARTIFACT_ROOT': str(artifact_root),
            'MAESTRO_AUDIO_WORKER_STATE': str(state_root),
            'MAESTRO_AUDIO_WORKER_TOKEN': token,
            'MAESTRO_AUDIO_WORKER_CONCURRENCY': '1',
        })
        proc = subprocess.Popen(
            [sys.executable, '-m', 'uvicorn', 'service:app', '--host', '127.0.0.1', '--port', port],
            cwd=WORKER_ROOT,
            env=child_env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        old_url = os.environ.get('MAESTRO_AUDIO_WORKER_URL')
        old_token = os.environ.get('MAESTRO_AUDIO_WORKER_TOKEN')
        try:
            deadline = time.time() + 20
            while True:
                if proc.poll() is not None:
                    raise RuntimeError('worker_exited:' + (proc.stdout.read() if proc.stdout else ''))
                try:
                    from urllib.request import urlopen
                    with urlopen(f'http://127.0.0.1:{port}/health', timeout=1) as response:
                        if response.status == 200:
                            break
                except Exception:
                    pass
                if time.time() >= deadline:
                    raise RuntimeError('worker_health_timeout')
                time.sleep(0.1)

            os.environ['MAESTRO_AUDIO_WORKER_URL'] = f'http://127.0.0.1:{port}'
            os.environ['MAESTRO_AUDIO_WORKER_TOKEN'] = token

            request = {
                'project_id': 'project:maestro-gateway-worker-e2e',
                'source_ref': f'artifact:sha256:{sha}',
                'source_sha256': sha,
                'deterministic_analysis_id': 'analysis:gateway-worker-e2e',
                'adapters': ['statistical_embedding'],
                'context': {'fixture': True},
            }
            submitted = gateway.submit_job(request)
            assert submitted['job_id'].startswith('job-')
            assert submitted['source_sha256'] == sha
            assert submitted['authority']['technical_ust_mutation'] is False

            deadline = time.time() + 30
            while True:
                result = gateway.get_job(submitted['job_id'])
                if result['status'] in {'completed', 'failed'}:
                    break
                if time.time() >= deadline:
                    raise RuntimeError('gateway_worker_job_timeout')
                time.sleep(0.1)

            assert result['status'] == 'completed', result
            adapter = result['results'][0]
            assert adapter['adapter_id'] == 'statistical_embedding'
            assert adapter['status'] == 'completed'
            assert adapter['provenance']['source_sha256'] == sha
            assert adapter['provenance']['evidence_class'] == 'derived_measurement'
            assert result['canon_promotion'] is False
            print(json.dumps({
                'passed': True,
                'checks': 10,
                'gateway_schema': gateway.SCHEMA_VERSION,
                'job_id': submitted['job_id'],
                'source_sha256': sha,
            }, indent=2))
        finally:
            if old_url is None:
                os.environ.pop('MAESTRO_AUDIO_WORKER_URL', None)
            else:
                os.environ['MAESTRO_AUDIO_WORKER_URL'] = old_url
            if old_token is None:
                os.environ.pop('MAESTRO_AUDIO_WORKER_TOKEN', None)
            else:
                os.environ['MAESTRO_AUDIO_WORKER_TOKEN'] = old_token
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait(timeout=5)


if __name__ == '__main__':
    main()
