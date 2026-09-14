from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PROFILES = {
    'basic-pitch': 'MAESTRO_BASIC_PITCH_COMMAND_JSON',
    'songformer': 'MAESTRO_SONGFORMER_COMMAND_JSON',
    'chordmini': 'MAESTRO_CHORDMINI_COMMAND_JSON',
    'tsumugi': 'MAESTRO_ADVANCED_AMT_COMMAND_JSON',
    'clap': 'MAESTRO_CLAP_COMMAND_JSON',
}

PROVENANCE_MARKERS = {
    'basic-pitch': 'model_artifact_sha256',
    'songformer': 'checkpoint_sha256',
    'chordmini': 'checkpoint_sha256',
    'tsumugi': 'checkpoint_sha256',
    'clap': 'checkpoint_sha256',
}


def main() -> None:
    checks = 0
    root_docker = (ROOT / 'Dockerfile').read_text(encoding='utf-8')
    assert 'artifact_sync.py' in root_docker
    assert 'service.py' in root_docker
    checks += 2

    for profile, bridge_env in PROFILES.items():
        profile_dir = ROOT / 'profiles' / profile
        docker = (profile_dir / 'Dockerfile').read_text(encoding='utf-8')
        bridge = (profile_dir / 'bridge.py').read_text(encoding='utf-8')

        assert 'service.py' in docker, profile
        assert 'artifact_sync.py' in docker, profile
        assert 'uvicorn' in docker, profile
        assert bridge_env in docker, profile
        assert PROVENANCE_MARKERS[profile] in bridge, profile
        assert 'canonical_' in bridge or 'renderer_policy_promoted' in bridge, profile
        checks += 6

    songformer = (ROOT / 'profiles' / 'songformer' / 'bridge.py').read_text(encoding='utf-8')
    assert 'songformer_cuda_required_by_upstream_inference_path' in songformer
    assert 'HF_HUB_OFFLINE' in songformer
    assert 'muq_cache_sha256' in songformer
    assert 'musicfm_checkpoint_sha256' in songformer
    assert "'device': 'cuda'" in songformer

    chordmini = (ROOT / 'profiles' / 'chordmini' / 'bridge.py').read_text(encoding='utf-8')
    assert "'device': device" in chordmini
    assert 'upstream_auto_cuda_then_mps_then_cpu' in chordmini

    tsumugi = (ROOT / 'profiles' / 'tsumugi' / 'bridge.py').read_text(encoding='utf-8')
    assert 'TSUMUGI_CHECKPOINT_must_reference_preprovisioned_local_file' in tsumugi
    assert "'device': device" in tsumugi

    clap = (ROOT / 'profiles' / 'clap' / 'bridge.py').read_text(encoding='utf-8')
    assert 'CLAP_CHECKPOINT_must_reference_preprovisioned_local_file' in clap
    assert 'clap_cuda_requested_but_unavailable' in clap
    assert "'device': device_name" in clap
    checks += 11

    print({'passed': True, 'checks': checks, 'profiles': sorted(PROFILES)})


if __name__ == '__main__':
    main()
