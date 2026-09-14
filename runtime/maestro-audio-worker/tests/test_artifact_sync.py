from __future__ import annotations

import hashlib
import threading
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from artifact_sync import object_url, sync_artifact, validate_base_url
from worker_core import ArtifactStore, sha256_file


class Handler(BaseHTTPRequestHandler):
    token = 'sync-secret'
    blobs: dict[str, bytes] = {}
    redirects: dict[str, str] = {}

    def do_GET(self):
        if self.headers.get('Authorization') != f'Bearer {self.token}':
            self.send_response(401)
            self.end_headers()
            return
        redirect = self.redirects.get(self.path)
        if redirect is not None:
            self.send_response(302)
            self.send_header('Location', redirect)
            self.end_headers()
            return
        data = self.blobs.get(self.path)
        if data is None:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header('Content-Type', 'application/octet-stream')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *args):
        return


def expect_error(fn, text):
    try:
        fn()
    except Exception as exc:
        assert text in str(exc), (text, str(exc))
    else:
        raise AssertionError(f'expected error containing {text}')


def main():
    with tempfile.TemporaryDirectory() as td:
        payload = b'Maestro immutable artifact\n' * 2048
        sha = hashlib.sha256(payload).hexdigest()
        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        base = f'http://127.0.0.1:{server.server_port}'
        path = f'/objects/{sha[:2]}/{sha}'
        Handler.blobs = {path: payload}
        Handler.redirects = {}
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            store = ArtifactStore(Path(td) / 'store')
            result = sync_artifact(sha, store, base_url=base, token=Handler.token, max_bytes=len(payload) + 1)
            assert result['fetched'] is True
            assert result['source'] == 'trusted_sha_derived_object_url'
            assert sha256_file(store.retrieve(sha)) == sha

            again = sync_artifact(sha, store, base_url=base, token=Handler.token)
            assert again['fetched'] is False

            mismatch_store = ArtifactStore(Path(td) / 'mismatch')
            Handler.blobs = {path: b'wrong bytes'}
            expect_error(lambda: sync_artifact(sha, mismatch_store, base_url=base, token=Handler.token), 'sha256_mismatch')

            redirect_store = ArtifactStore(Path(td) / 'redirect')
            Handler.blobs = {}
            Handler.redirects = {path: f'{base}/elsewhere'}
            expect_error(lambda: sync_artifact(sha, redirect_store, base_url=base, token=Handler.token), 'redirect_refused')

            expect_error(lambda: validate_base_url('http://example.com'), 'requires_https_or_localhost')
            expect_error(lambda: validate_base_url('https://user:secret@example.com'), 'must_not_contain_credentials')
            expect_error(lambda: validate_base_url('https://example.com/object?token=secret'), 'must_not_contain_credentials')
            expect_error(lambda: object_url(base, 'bad'), 'invalid_sha256')
            expect_error(lambda: sync_artifact(sha, ArtifactStore(Path(td) / 'zero'), base_url=base, token=Handler.token, max_bytes=0), 'max_bytes_must_be_positive')
            print({'passed': True, 'checks': 13, 'sha256': sha})
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)


if __name__ == '__main__':
    main()
