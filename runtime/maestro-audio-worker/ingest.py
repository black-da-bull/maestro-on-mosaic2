from __future__ import annotations

import argparse
import json
import os

from worker_core import ArtifactStore

parser = argparse.ArgumentParser(description="Import an artifact into the immutable Maestro audio-worker store")
parser.add_argument("path")
parser.add_argument("--expected-sha256")
parser.add_argument("--root", default=os.getenv("MAESTRO_ARTIFACT_ROOT", "./data/artifacts"))
args = parser.parse_args()
print(json.dumps(ArtifactStore(args.root).import_file(args.path, args.expected_sha256), indent=2))
