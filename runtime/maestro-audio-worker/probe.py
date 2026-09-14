from __future__ import annotations

import json

from worker_core import probe_capabilities

print(json.dumps(probe_capabilities(), indent=2, sort_keys=True))
