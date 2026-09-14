from __future__ import annotations

import json
import os

from worker_core import probe_capabilities

BRIDGE_ENV = {
    'songformer': 'MAESTRO_SONGFORMER_COMMAND_JSON',
    'chordmini': 'MAESTRO_CHORDMINI_COMMAND_JSON',
    'basic_pitch': 'MAESTRO_BASIC_PITCH_COMMAND_JSON',
    'advanced_amt': 'MAESTRO_ADVANCED_AMT_COMMAND_JSON',
    'clap': 'MAESTRO_CLAP_COMMAND_JSON',
    'audio_language': 'MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON',
}

caps = probe_capabilities()
for adapter_id, env_name in BRIDGE_ENV.items():
    if os.getenv(env_name, '').strip():
        entry = caps['adapters'].setdefault(adapter_id, {})
        entry['configured'] = True
        entry['execution'] = 'isolated_json_command_bridge'
        entry['bridge_env'] = env_name

caps['artifact_fetch'] = {
    'configured': bool(os.getenv('MAESTRO_ARTIFACT_FETCH_BASE_URL', '').strip()),
    'source_identity': 'sha256_derived_object_path_only',
    'arbitrary_source_urls_allowed': False,
    'redirects_allowed': False,
}

print(json.dumps(caps, indent=2, sort_keys=True))
