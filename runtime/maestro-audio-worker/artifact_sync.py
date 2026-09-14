from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from worker_core import ArtifactStore, SHA_RE, WorkerValidationError

DEFAULT_MAX_BYTES = 4 * 1024 * 1024 * 1024


def validate_base_url(value: str) -> str:
    base = value.strip().rstrip('/')
    parsed = urlparse(base)
    if parsed.scheme == 'https' and parsed.netloc:
        return base
    if parsed.scheme == 'http' and parsed.hostname in {'127.0.0.1', 'localhost', '::1'}:
        return base
    raise WorkerValidationError('artifact_fetch_base_url_requires_https_or_localhost')


def object_url(base_url: str, sha256: str) -> str:
    if not SHA_RE.fullmatch(sha256):
        raise WorkerValidationError('invalid_sha256')
    base = validate_base_url(base_url)
    return f'{base}/objects/{sha256[:2]}/{sha256}'


def sync_artifact(
    sha256: str,
    store: ArtifactStore,
    *,
    base_url: str,
    token: str | None = None,
    max_bytes: int = DEFAULT_MAX_BYTES,
    timeout_s: int = 120,
) -> dict:
    try:
        existing = store.retrieve(sha256)
        return {
            'sha256': sha256,
            'size_bytes': existing.stat().st_size,
            'immutable': True,
            'fetched': False,
            'source': 'existing_content_addressed_object',
        }
    except FileNotFoundError:
        pass

    url = object_url(base_url, sha256)
    headers = {'Accept': 'application/octet-stream'}
    if token:
        headers['Authorization'] = f'Bearer {token}'
    request = Request(url, headers=headers, method='GET')

    fd, temp_name = tempfile.mkstemp(prefix='maestro-artifact-fetch-')
    os.close(fd)
    temp_path = Path(temp_name)
    digest = hashlib.sha256()
    total = 0
    try:
        with urlopen(request, timeout=timeout_s) as response, temp_path.open('wb') as out:
            content_length = response.headers.get('Content-Length')
            if content_length:
                declared = int(content_length)
                if declared < 0 or declared > max_bytes:
                    raise WorkerValidationError('artifact_fetch_declared_size_exceeds_limit')
            while True:
                chunk = response.read(4 * 1024 * 1024)
                if not chunk:
                    break
                total += len(chunk)
                if total > max_bytes:
                    raise WorkerValidationError('artifact_fetch_stream_exceeds_limit')
                digest.update(chunk)
                out.write(chunk)
        actual = digest.hexdigest()
        if actual != sha256:
            raise WorkerValidationError('artifact_fetch_sha256_mismatch')
        receipt = store.import_file(temp_path, expected_sha256=sha256)
        return {
            'sha256': sha256,
            'size_bytes': receipt['size_bytes'],
            'immutable': True,
            'fetched': True,
            'source': 'trusted_sha_derived_object_url',
        }
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description='Fetch one immutable Maestro artifact by SHA-derived trusted object URL')
    parser.add_argument('sha256')
    parser.add_argument('--root', default=os.getenv('MAESTRO_ARTIFACT_ROOT', './data/artifacts'))
    parser.add_argument('--base-url', default=os.getenv('MAESTRO_ARTIFACT_FETCH_BASE_URL', ''))
    parser.add_argument('--token', default=os.getenv('MAESTRO_ARTIFACT_FETCH_TOKEN'))
    parser.add_argument('--max-bytes', type=int, default=int(os.getenv('MAESTRO_ARTIFACT_FETCH_MAX_BYTES', str(DEFAULT_MAX_BYTES))))
    args = parser.parse_args()
    if not args.base_url:
        raise SystemExit('MAESTRO_ARTIFACT_FETCH_BASE_URL_or_--base-url_required')
    result = sync_artifact(args.sha256, ArtifactStore(args.root), base_url=args.base_url, token=args.token, max_bytes=args.max_bytes)
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
