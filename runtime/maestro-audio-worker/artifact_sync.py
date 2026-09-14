from __future__ import annotations

import argparse
import hashlib
import json
import os
import tempfile
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener

from worker_core import ArtifactStore, SHA_RE, WorkerValidationError

DEFAULT_MAX_BYTES = 4 * 1024 * 1024 * 1024


class ArtifactFetchUnavailable(RuntimeError):
    pass


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: ANN001
        return None


def validate_base_url(value: str) -> str:
    base = value.strip().rstrip('/')
    parsed = urlparse(base)
    if parsed.username or parsed.password or parsed.query or parsed.fragment or parsed.params:
        raise WorkerValidationError('artifact_fetch_base_url_must_not_contain_credentials_query_or_fragment')
    if not parsed.hostname:
        raise WorkerValidationError('artifact_fetch_base_url_requires_host')
    if parsed.scheme == 'https':
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
    if max_bytes <= 0:
        raise WorkerValidationError('artifact_fetch_max_bytes_must_be_positive')
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
    opener = build_opener(_NoRedirect())

    fd, temp_name = tempfile.mkstemp(prefix='maestro-artifact-fetch-')
    os.close(fd)
    temp_path = Path(temp_name)
    digest = hashlib.sha256()
    total = 0
    try:
        try:
            response = opener.open(request, timeout=timeout_s)
        except HTTPError as exc:
            # Redirects are intentionally refused so configured trust cannot be
            # delegated by a remote 3xx response to an arbitrary host.
            if 300 <= exc.code < 400:
                raise ArtifactFetchUnavailable('artifact_fetch_redirect_refused') from exc
            raise ArtifactFetchUnavailable(f'artifact_fetch_http_error:{exc.code}') from exc
        except (URLError, TimeoutError) as exc:
            raise ArtifactFetchUnavailable(f'artifact_fetch_failed:{exc.__class__.__name__}') from exc

        with response, temp_path.open('wb') as out:
            content_length = response.headers.get('Content-Length')
            if content_length:
                try:
                    declared = int(content_length)
                except ValueError as exc:
                    raise WorkerValidationError('artifact_fetch_invalid_content_length') from exc
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
