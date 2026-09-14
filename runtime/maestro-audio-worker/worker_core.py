from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import uuid
from pathlib import Path
from typing import Any

SCHEMA = "maestro.audio.worker.v0.6"
REQUEST_SCHEMA = "maestro.audio.gateway.v0.5"
SHA_RE = re.compile(r"^[0-9a-f]{64}$")
JOB_RE = re.compile(r"^[A-Za-z0-9._:-]{1,200}$")
MAX_CONTEXT_BYTES = 16 * 1024

ADAPTER_META: dict[str, dict[str, str]] = {
    "beat_this": {"evidence_class": "model_inference", "role": "beat_downbeat_tempo"},
    "songformer": {"evidence_class": "model_inference", "role": "structure_sections"},
    "chordmini": {"evidence_class": "model_inference", "role": "harmony_chords"},
    "basic_pitch": {"evidence_class": "model_inference", "role": "lightweight_amt"},
    "advanced_amt": {"evidence_class": "model_inference", "role": "instrument_agnostic_amt"},
    "clap": {"evidence_class": "model_inference", "role": "text_audio_embedding"},
    "audio_language": {"evidence_class": "advisory_inference", "role": "evidence_reasoning"},
    "statistical_embedding": {"evidence_class": "derived_measurement", "role": "non_semantic_descriptor_baseline"},
}

AUTHORITY = {
    "technical_ust_mutation": False,
    "canon_promotion": False,
    "renderer_policy_promotion": False,
    "keeper_or_release_approval": False,
    "operator_decision_required": True,
}

class WorkerValidationError(ValueError):
    pass

class ArtifactUnavailable(FileNotFoundError):
    pass

class AdapterNotConfigured(RuntimeError):
    pass

class AdapterUnavailable(RuntimeError):
    pass


def utc_ts() -> str:
    from datetime import datetime, timezone
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path, chunk_size: int = 4 * 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def _json_size(value: Any) -> int:
    return len(json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def _logical_ref(value: Any, name: str, max_len: int) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > max_len:
        raise WorkerValidationError(f"{name}_invalid")
    if "://" in value.lower() or value.lower().startswith(("file:", "data:")) or ".." in value or "\\" in value or value.startswith("/"):
        raise WorkerValidationError(f"{name}_must_be_logical_artifact_reference")
    return value


def validate_job_request(payload: Any) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise WorkerValidationError("job_request_must_be_object")
    allowed = {"schema", "project_id", "source_ref", "source_sha256", "deterministic_analysis_id", "adapters", "context", "authority"}
    unknown = sorted(set(payload) - allowed)
    if unknown:
        raise WorkerValidationError("job_request_unknown_fields:" + ",".join(unknown))
    required = {"project_id", "source_ref", "source_sha256", "deterministic_analysis_id", "adapters"}
    missing = sorted(required - set(payload))
    if missing:
        raise WorkerValidationError("job_request_missing_fields:" + ",".join(missing))
    if payload.get("schema") not in (None, REQUEST_SCHEMA):
        raise WorkerValidationError("unsupported_request_schema")
    project_id = _logical_ref(payload["project_id"], "project_id", 300)
    source_ref = _logical_ref(payload["source_ref"], "source_ref", 1000)
    deterministic_id = _logical_ref(payload["deterministic_analysis_id"], "deterministic_analysis_id", 500)
    source_sha = payload["source_sha256"]
    if not isinstance(source_sha, str) or not SHA_RE.fullmatch(source_sha):
        raise WorkerValidationError("source_sha256_must_be_lowercase_sha256")
    adapters = payload["adapters"]
    if not isinstance(adapters, list) or not adapters:
        raise WorkerValidationError("adapters_must_be_nonempty_list")
    clean: list[str] = []
    for adapter in adapters:
        if not isinstance(adapter, str) or adapter not in ADAPTER_META:
            raise WorkerValidationError(f"unknown_adapter:{adapter}")
        if adapter not in clean:
            clean.append(adapter)
    context = payload.get("context") or {}
    if not isinstance(context, dict) or _json_size(context) > MAX_CONTEXT_BYTES:
        raise WorkerValidationError("context_invalid_or_too_large")
    incoming_authority = payload.get("authority")
    if incoming_authority is not None:
        if not isinstance(incoming_authority, dict):
            raise WorkerValidationError("authority_must_be_object")
        for key, expected in AUTHORITY.items():
            if key in incoming_authority and incoming_authority[key] != expected:
                raise WorkerValidationError(f"authority_violation:{key}")
    return {
        "schema": REQUEST_SCHEMA,
        "project_id": project_id,
        "source_ref": source_ref,
        "source_sha256": source_sha,
        "deterministic_analysis_id": deterministic_id,
        "adapters": clean,
        "context": context,
        "authority": dict(AUTHORITY),
    }


class ArtifactStore:
    """Content-addressed immutable local object store.

    A gateway submits a logical source_ref plus SHA-256. The worker never dereferences
    arbitrary network URLs. The artifact must already exist in the store under its hash.
    """
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()
        self.objects = self.root / "objects"
        self.objects.mkdir(parents=True, exist_ok=True)

    def object_path(self, sha256: str) -> Path:
        if not SHA_RE.fullmatch(sha256):
            raise WorkerValidationError("invalid_sha256")
        return self.objects / sha256[:2] / sha256

    def import_file(self, source: str | Path, expected_sha256: str | None = None) -> dict[str, Any]:
        src = Path(source).resolve()
        if not src.is_file():
            raise ArtifactUnavailable(str(src))
        actual = sha256_file(src)
        if expected_sha256 and actual != expected_sha256:
            raise WorkerValidationError("artifact_import_sha256_mismatch")
        dest = self.object_path(actual)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists():
            if sha256_file(dest) != actual:
                raise WorkerValidationError("artifact_store_corruption")
        else:
            fd, tmp_name = tempfile.mkstemp(prefix="artifact-", dir=str(dest.parent))
            os.close(fd)
            tmp = Path(tmp_name)
            try:
                shutil.copyfile(src, tmp)
                if sha256_file(tmp) != actual:
                    raise WorkerValidationError("artifact_copy_sha256_mismatch")
                os.chmod(tmp, 0o444)
                os.replace(tmp, dest)
            finally:
                tmp.unlink(missing_ok=True)
        return {"sha256": actual, "size_bytes": dest.stat().st_size, "path": str(dest), "immutable": True}

    def retrieve(self, sha256: str) -> Path:
        path = self.object_path(sha256)
        if not path.is_file():
            raise ArtifactUnavailable(f"artifact_not_present:{sha256}")
        actual = sha256_file(path)
        if actual != sha256:
            raise WorkerValidationError("artifact_store_source_identity_mismatch")
        return path


class JobStore:
    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()
        self.jobs = self.root / "jobs"
        self.jobs.mkdir(parents=True, exist_ok=True)
        self._lock = threading.RLock()

    def _path(self, job_id: str) -> Path:
        if not JOB_RE.fullmatch(job_id):
            raise WorkerValidationError("invalid_job_id")
        return self.jobs / f"{job_id}.json"

    def put(self, record: dict[str, Any]) -> None:
        path = self._path(record["job_id"])
        encoded = json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True).encode("utf-8")
        with self._lock:
            fd, tmp_name = tempfile.mkstemp(prefix="job-", dir=str(self.jobs))
            with os.fdopen(fd, "wb") as f:
                f.write(encoded)
                f.flush()
                os.fsync(f.fileno())
            os.replace(tmp_name, path)

    def get(self, job_id: str) -> dict[str, Any]:
        path = self._path(job_id)
        if not path.is_file():
            raise KeyError(job_id)
        with self._lock:
            return json.loads(path.read_text(encoding="utf-8"))

    def recoverable(self) -> list[dict[str, Any]]:
        out = []
        for path in sorted(self.jobs.glob("*.json")):
            try:
                record = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if record.get("status") in {"queued", "running"}:
                record["status"] = "queued"
                record["updated_at"] = utc_ts()
                record["error"] = None
                record["results"] = []
                self.put(record)
                out.append(record)
        return out


def _base_provenance(adapter_id: str, sha: str, implementation: str, version: str | None, **extra: Any) -> dict[str, Any]:
    value = {
        "source_sha256": sha,
        "implementation": implementation,
        "implementation_version": version or "unknown",
        "evidence_class": ADAPTER_META[adapter_id]["evidence_class"],
    }
    value.update({k: v for k, v in extra.items() if v is not None})
    return value


def _result(adapter_id: str, status: str, sha: str, schema: str, implementation: str, version: str | None = None,
            output: dict[str, Any] | None = None, error: str | None = None, warnings: list[str] | None = None,
            confidence: float | None = None, **prov: Any) -> dict[str, Any]:
    r: dict[str, Any] = {
        "adapter_id": adapter_id,
        "status": status,
        "schema": schema,
        "provenance": _base_provenance(adapter_id, sha, implementation, version, **prov),
        "warnings": warnings or [],
    }
    if output is not None:
        r["output"] = output
    if error is not None:
        r["error"] = error
    if confidence is not None:
        r["confidence"] = float(confidence)
    return r


def _package_version(name: str) -> str | None:
    try:
        import importlib.metadata
        return importlib.metadata.version(name)
    except Exception:
        return None


def _probe_command(executable: str) -> str | None:
    return shutil.which(executable)


def probe_capabilities() -> dict[str, Any]:
    try:
        import torch
        torch_info = {
            "installed": True,
            "version": getattr(torch, "__version__", None),
            "cuda_available": bool(torch.cuda.is_available()),
            "cuda_device_count": int(torch.cuda.device_count()),
            "mps_available": bool(getattr(getattr(torch, "backends", None), "mps", None) and torch.backends.mps.is_available()),
        }
    except Exception as exc:
        torch_info = {"installed": False, "error": exc.__class__.__name__}
    adapters: dict[str, Any] = {}
    adapters["beat_this"] = {"configured": _package_version("beat-this") is not None, "package_version": _package_version("beat-this")}
    adapters["songformer"] = {"configured": bool(os.getenv("SONGFORMER_ROOT") or os.getenv("MAESTRO_SONGFORMER_COMMAND_JSON"))}
    adapters["chordmini"] = {"configured": bool(os.getenv("CHORDMINI_ROOT") or os.getenv("MAESTRO_CHORDMINI_COMMAND_JSON"))}
    adapters["basic_pitch"] = {"configured": bool(_probe_command("basic-pitch")), "package_version": _package_version("basic-pitch")}
    adapters["advanced_amt"] = {"configured": bool(os.getenv("TSUMUGI_ROOT") or os.getenv("MAESTRO_ADVANCED_AMT_COMMAND_JSON"))}
    adapters["clap"] = {"configured": _package_version("laion-clap") is not None, "package_version": _package_version("laion-clap")}
    adapters["audio_language"] = {"configured": bool(os.getenv("MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON"))}
    adapters["statistical_embedding"] = {"configured": True, "implementation": "maestro_streaming_statistics"}
    return {"schema": SCHEMA, "python": sys.version.split()[0], "torch": torch_info, "adapters": adapters, "authority": dict(AUTHORITY)}


def _parse_command_env(name: str, input_path: Path, output_path: Path, context_path: Path) -> list[str]:
    raw = os.getenv(name, "").strip()
    if not raw:
        raise AdapterNotConfigured(f"{name}_not_configured")
    try:
        arr = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise AdapterNotConfigured(f"{name}_must_be_json_array") from exc
    if not isinstance(arr, list) or not arr or not all(isinstance(x, str) and x for x in arr):
        raise AdapterNotConfigured(f"{name}_must_be_nonempty_string_array")
    replacements = {"{input}": str(input_path), "{output}": str(output_path), "{context}": str(context_path)}
    return [replacements.get(x, x) for x in arr]


def _run_json_command(adapter_id: str, env_name: str, path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"maestro-{adapter_id}-") as td:
        out = Path(td) / "output.json"
        ctx = Path(td) / "context.json"
        ctx.write_text(json.dumps(context, indent=2, ensure_ascii=False), encoding="utf-8")
        cmd = _parse_command_env(env_name, path, out, ctx)
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=int(os.getenv("MAESTRO_ADAPTER_TIMEOUT_S", "3600")))
        if proc.returncode != 0:
            raise AdapterUnavailable(f"{adapter_id}_command_failed:{proc.returncode}:{proc.stderr[-1000:]}")
        if not out.is_file():
            raise AdapterUnavailable(f"{adapter_id}_command_produced_no_output")
        value = json.loads(out.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise AdapterUnavailable(f"{adapter_id}_command_output_must_be_object")
        return value


def run_beat_this(path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    try:
        from beat_this.inference import File2Beats
        import torch
        import statistics
    except Exception as exc:
        raise AdapterNotConfigured("beat_this_not_installed") from exc
    requested = str(context.get("beat_this_device") or "auto")
    if requested == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    else:
        device = requested
    if device == "cuda" and not torch.cuda.is_available():
        raise AdapterUnavailable("beat_this_cuda_requested_but_unavailable")
    checkpoint = str(context.get("beat_this_checkpoint") or os.getenv("BEAT_THIS_CHECKPOINT") or "final0")
    tracker = File2Beats(checkpoint_path=checkpoint, device=device, dbn=bool(context.get("beat_this_dbn", False)))
    beats, downbeats = tracker(str(path))
    beats = [float(x) for x in beats]
    downbeats = [float(x) for x in downbeats]
    intervals = [b - a for a, b in zip(beats, beats[1:]) if b > a]
    tempo = 60.0 / statistics.median(intervals) if intervals else None
    output: dict[str, Any] = {"beats_s": beats, "downbeats_s": downbeats, "tempo_bpm": tempo, "device": device, "checkpoint": checkpoint}
    evidence = context.get("tempo_evidence")
    if isinstance(evidence, dict) and tempo is not None:
        comparisons = {}
        studio = evidence.get("studio_project_bpm")
        if isinstance(studio, (int, float)):
            comparisons["studio_project_bpm_delta"] = float(tempo) - float(studio)
        midi_median = evidence.get("midi_tempo_median_bpm")
        if isinstance(midi_median, (int, float)):
            comparisons["midi_median_bpm_delta"] = float(tempo) - float(midi_median)
        low = evidence.get("midi_tempo_min_bpm")
        high = evidence.get("midi_tempo_max_bpm")
        if isinstance(low, (int, float)) and isinstance(high, (int, float)):
            comparisons["within_midi_observed_range"] = float(low) <= float(tempo) <= float(high)
        output["calibration_comparison"] = comparisons
    return _result("beat_this", "completed", sha, "maestro.adapter.beat_this.v0.6", "CPJKU/beat_this",
                   _package_version("beat-this"), output=output, checkpoint=checkpoint, device=device)


def run_statistical_embedding(path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    try:
        import numpy as np
        import soundfile as sf
    except Exception as exc:
        raise AdapterNotConfigured("numpy_soundfile_required_for_statistical_embedding") from exc
    block_frames = int(context.get("statistical_block_frames") or 65536)
    features: list[list[float]] = []
    with sf.SoundFile(str(path), "r") as f:
        sr = int(f.samplerate)
        channels = int(f.channels)
        frames = int(len(f))
        while True:
            block = f.read(block_frames, dtype="float32", always_2d=True)
            if block.size == 0:
                break
            mono = block.mean(axis=1)
            rms = float(np.sqrt(np.mean(mono * mono) + 1e-20))
            peak = float(np.max(np.abs(mono)))
            mean = float(np.mean(mono))
            std = float(np.std(mono))
            zcr = float(np.mean(np.not_equal(np.signbit(mono[1:]), np.signbit(mono[:-1])))) if len(mono) > 1 else 0.0
            crest = peak / max(rms, 1e-12)
            features.append([rms, peak, mean, std, zcr, crest])
    arr = np.asarray(features, dtype="float64")
    if arr.size == 0:
        raise AdapterUnavailable("empty_audio")
    vector = np.concatenate([arr.mean(axis=0), arr.std(axis=0), arr.min(axis=0), arr.max(axis=0)]).tolist()
    output = {
        "descriptor": "streaming_block_statistics_v0.6",
        "vector": [float(x) for x in vector],
        "dimensions": len(vector),
        "sample_rate": sr,
        "channels": channels,
        "frames": frames,
        "duration_s": frames / sr if sr else None,
        "blocks": len(features),
        "semantic": False,
    }
    return _result("statistical_embedding", "completed", sha, "maestro.adapter.statistical_embedding.v0.6",
                   "maestro_streaming_statistics", "0.6", output=output,
                   warnings=["Descriptor is non-semantic and requires project-specific calibration before similarity interpretation."])


def run_basic_pitch(path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    exe = shutil.which("basic-pitch")
    if not exe:
        if os.getenv("MAESTRO_BASIC_PITCH_COMMAND_JSON"):
            output = _run_json_command("basic_pitch", "MAESTRO_BASIC_PITCH_COMMAND_JSON", path, sha, context)
            return _result("basic_pitch", "completed", sha, "maestro.adapter.amt.v0.6", "configured_basic_pitch_command", "external", output=output)
        raise AdapterNotConfigured("basic_pitch_not_installed")
    with tempfile.TemporaryDirectory(prefix="maestro-basic-pitch-") as td:
        proc = subprocess.run([exe, td, str(path)], capture_output=True, text=True, timeout=int(os.getenv("MAESTRO_ADAPTER_TIMEOUT_S", "3600")))
        if proc.returncode != 0:
            raise AdapterUnavailable(f"basic_pitch_failed:{proc.returncode}:{(proc.stderr or proc.stdout)[-1000:]}")
        midi = next(Path(td).glob("*.mid"), None) or next(Path(td).glob("*.midi"), None)
        if midi is None:
            raise AdapterUnavailable("basic_pitch_produced_no_midi")
        midi_sha = sha256_file(midi)
        output = {"midi_sha256": midi_sha, "midi_size_bytes": midi.stat().st_size, "artifact_persistence": "requires_worker_artifact_export"}
    return _result("basic_pitch", "completed", sha, "maestro.adapter.amt.v0.6", "spotify/basic-pitch", _package_version("basic-pitch"), output=output)


def run_command_adapter(adapter_id: str, env_name: str, path: Path, sha: str, context: dict[str, Any], schema: str, implementation: str) -> dict[str, Any]:
    output = _run_json_command(adapter_id, env_name, path, sha, context)
    return _result(adapter_id, "completed", sha, schema, implementation, str(output.pop("implementation_version", "external")), output=output)


def run_clap(path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    try:
        import laion_clap
    except Exception as exc:
        if os.getenv("MAESTRO_CLAP_COMMAND_JSON"):
            return run_command_adapter("clap", "MAESTRO_CLAP_COMMAND_JSON", path, sha, context, "maestro.adapter.embedding.v0.6", "configured_clap_command")
        raise AdapterNotConfigured("laion_clap_not_installed") from exc
    model_name = str(context.get("clap_model") or "HTSAT-base")
    model = laion_clap.CLAP_Module(enable_fusion=bool(context.get("clap_enable_fusion", False)), amodel=model_name)
    checkpoint = context.get("clap_checkpoint") or os.getenv("CLAP_CHECKPOINT")
    if checkpoint:
        model.load_ckpt(checkpoint)
    else:
        model.load_ckpt()
    audio = model.get_audio_embedding_from_filelist(x=[str(path)], use_tensor=False)[0].tolist()
    text_vec = None
    text = context.get("clap_text")
    if isinstance(text, str) and text.strip():
        text_vec = model.get_text_embedding([text], use_tensor=False)[0].tolist()
    return _result("clap", "completed", sha, "maestro.adapter.embedding.v0.6", "LAION-AI/CLAP", _package_version("laion-clap"),
                   output={"audio_embedding": audio, "text_embedding": text_vec, "dimensions": len(audio), "model": model_name}, checkpoint=str(checkpoint) if checkpoint else "default")


def run_audio_language(path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    evidence = context.get("evidence")
    if not isinstance(evidence, dict) or not evidence:
        raise AdapterUnavailable("audio_language_requires_evidence_context")
    output = _run_json_command("audio_language", "MAESTRO_AUDIO_LANGUAGE_COMMAND_JSON", path, sha, context)
    claims = output.get("claims")
    contradictions = output.get("contradictions", [])
    if not isinstance(claims, list) or not all(isinstance(x, dict) for x in claims):
        raise AdapterUnavailable("audio_language_claims_must_be_list_of_objects")
    if not isinstance(contradictions, list) or not all(isinstance(x, dict) for x in contradictions):
        raise AdapterUnavailable("audio_language_contradictions_must_be_list_of_objects")
    for claim in claims:
        refs = claim.get("evidence_refs")
        if not isinstance(refs, list) or not refs or not all(isinstance(x, str) and x for x in refs):
            raise AdapterUnavailable("audio_language_claim_requires_evidence_refs")
    output["advisory_only"] = True
    output["contradictions_preserved"] = True
    return _result("audio_language", "completed", sha, "maestro.adapter.audio_language.v0.6", "configured_audio_language_reasoner", "external", output=output)


def run_adapter(adapter_id: str, path: Path, sha: str, context: dict[str, Any]) -> dict[str, Any]:
    try:
        if adapter_id == "beat_this":
            return run_beat_this(path, sha, context)
        if adapter_id == "statistical_embedding":
            return run_statistical_embedding(path, sha, context)
        if adapter_id == "basic_pitch":
            return run_basic_pitch(path, sha, context)
        if adapter_id == "songformer":
            return run_command_adapter(adapter_id, "MAESTRO_SONGFORMER_COMMAND_JSON", path, sha, context, "maestro.adapter.songformer.v0.6", "ASLP-lab/SongFormer")
        if adapter_id == "chordmini":
            return run_command_adapter(adapter_id, "MAESTRO_CHORDMINI_COMMAND_JSON", path, sha, context, "maestro.adapter.harmony.v0.6", "ChordMini")
        if adapter_id == "advanced_amt":
            return run_command_adapter(adapter_id, "MAESTRO_ADVANCED_AMT_COMMAND_JSON", path, sha, context, "maestro.adapter.amt.v0.6", "anime-song/tsumugi")
        if adapter_id == "clap":
            return run_clap(path, sha, context)
        if adapter_id == "audio_language":
            return run_audio_language(path, sha, context)
        raise WorkerValidationError(f"unknown_adapter:{adapter_id}")
    except AdapterNotConfigured as exc:
        return _result(adapter_id, "not_configured", sha, f"maestro.adapter.{adapter_id}.v0.6", ADAPTER_META[adapter_id]["role"], "unavailable", error=str(exc))
    except AdapterUnavailable as exc:
        return _result(adapter_id, "unavailable", sha, f"maestro.adapter.{adapter_id}.v0.6", ADAPTER_META[adapter_id]["role"], "unavailable", error=str(exc))
    except Exception as exc:
        return _result(adapter_id, "failed", sha, f"maestro.adapter.{adapter_id}.v0.6", ADAPTER_META[adapter_id]["role"], "unknown", error=f"{exc.__class__.__name__}:{exc}")


def create_job(payload: Any, artifacts: ArtifactStore, jobs: JobStore) -> dict[str, Any]:
    request = validate_job_request(payload)
    artifacts.retrieve(request["source_sha256"])
    job_id = "job-" + uuid.uuid4().hex
    now = utc_ts()
    record = {
        "job_id": job_id,
        "status": "queued",
        "source_sha256": request["source_sha256"],
        "adapters": request["adapters"],
        "results": [],
        "created_at": now,
        "updated_at": now,
        "completed_at": None,
        "error": None,
        "request": request,
    }
    jobs.put(record)
    return record


def public_job(record: dict[str, Any]) -> dict[str, Any]:
    allowed = {"job_id", "status", "source_sha256", "adapters", "results", "error", "created_at", "updated_at", "completed_at"}
    return {k: record[k] for k in allowed if k in record and record[k] is not None}


def execute_job(job_id: str, artifacts: ArtifactStore, jobs: JobStore) -> dict[str, Any]:
    record = jobs.get(job_id)
    request = record["request"]
    now = utc_ts()
    record.update({"status": "running", "updated_at": now, "results": [], "error": None})
    jobs.put(record)
    try:
        source = artifacts.retrieve(request["source_sha256"])
        pre_hash = sha256_file(source)
        results = [run_adapter(adapter_id, source, request["source_sha256"], request["context"]) for adapter_id in request["adapters"]]
        post_hash = sha256_file(source)
        if pre_hash != request["source_sha256"] or post_hash != request["source_sha256"]:
            raise WorkerValidationError("source_hash_changed_during_analysis")
        record.update({"status": "completed", "results": results, "updated_at": utc_ts(), "completed_at": utc_ts(), "error": None})
    except Exception as exc:
        record.update({"status": "failed", "results": [], "updated_at": utc_ts(), "completed_at": utc_ts(), "error": f"{exc.__class__.__name__}:{exc}"})
    jobs.put(record)
    return record
