#!/usr/bin/env python3
"""Vision + lyrics -> governed proposed Technical UST compiler.

This is the missing Phase 0/1 bridge for the creator-facing MVP.
The controller never invents musical values. It prepares the intake packet and
lawful address assignments; model execution acts as bounded specialist labor and
returned values are accepted only for addresses owned by the declared worker.
Unreturned/invalid addresses remain explicit nulls.
"""
from __future__ import annotations

import hashlib
import json
import os
import urllib.error
import urllib.request
from typing import Any, Callable, Dict, List, Optional

import technical_ust_runtime as technical_ust
import workforce_runtime as workforce

GATEWAY_URL = "https://ai-gateway.vercel.sh/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-5.6-sol"
AXIS_ORDER = ["THY", "VOC", "STY", "TIM", "PER", "POST", "MAP", "LYR"]


class ModelExecutionUnavailable(RuntimeError):
    pass


class ModelResponseInvalid(RuntimeError):
    pass


def _worker_view(worker_id: str) -> Dict[str, str]:
    worker = workforce.resolve(worker_id)
    if not worker:
        return {"id": worker_id, "name": worker_id, "role": worker_id}
    identity = worker.get("identity") or {}
    return {
        "id": worker_id,
        "name": identity.get("role_name") or worker_id,
        "role": identity.get("role_name") or worker_id,
    }


def _address_descriptors() -> List[Dict[str, Any]]:
    overlay = technical_ust.load_overlay()
    out: List[Dict[str, Any]] = []
    seen = set()
    for axis in AXIS_ORDER:
        axis_binding = (overlay.get("axis_bindings") or {}).get(axis) or {}
        for key, key_binding in (axis_binding.get("key_bindings") or {}).items():
            candidates = []
            if key_binding.get("primary_owner"):
                candidates.append(key)
            candidates.extend((key_binding.get("subkey_bindings") or {}).keys())
            for address in candidates:
                if address in seen:
                    continue
                seen.add(address)
                binding = technical_ust.binding_for(address, overlay)
                worker = _worker_view(binding["primary_owner"])
                sub = binding.get("subkey_binding") or {}
                keyb = binding.get("key_binding") or {}
                axb = binding.get("axis_binding") or {}
                out.append({
                    "address": address,
                    "axis": axis,
                    "primary_owner": worker,
                    "required_reviewers": [_worker_view(ref) for ref in binding["required_reviewers"]],
                    "semantic_role": sub.get("role") or keyb.get("scope") or axb.get("primary_scope") or axb.get("primary_scope_limit") or axb.get("rule") or "address-specific musical state",
                    "status": sub.get("status") or keyb.get("status") or axb.get("status") or "bound",
                })
    return out


def build_intake(payload: Dict[str, Any]) -> Dict[str, Any]:
    project_name = str(payload.get("project_name") or "").strip()
    song_title = str(payload.get("song_title") or "").strip()
    vision = str(payload.get("vision") or "").strip()
    lyrics = str(payload.get("lyrics") or "")
    instrumental = bool(payload.get("instrumental"))
    if not vision and not lyrics.strip():
        raise ValueError("artist vision or lyrics/source text is required")
    if not song_title:
        song_title = project_name or "Untitled Maestro Project"
    lyrics_status = "instrumental" if instrumental else ("locked_source" if lyrics.strip() else "absent")
    return {
        "project_title_or_working_name": project_name or song_title,
        "song_title": song_title,
        "artist_vision_statement": vision,
        "target_outcome": str(payload.get("target_outcome") or "develop the artist vision into an executable song state").strip(),
        "request_mode": "vision_lyrics_to_technical_ust",
        "hard_constraints": payload.get("hard_constraints") or [],
        "soft_preferences": payload.get("soft_preferences") or [],
        "references": payload.get("references") or [],
        "lyrics_status": lyrics_status,
        "lyrics_locked": bool(lyrics.strip()) and not instrumental,
        "locked_lyrics": lyrics if lyrics.strip() and not instrumental else "",
        "lyrics_sha256": hashlib.sha256(lyrics.encode("utf-8")).hexdigest() if lyrics else None,
        "persona_performance_intent": payload.get("persona_performance_intent") or None,
    }


def _prompt(intake: Dict[str, Any], descriptors: List[Dict[str, Any]]) -> str:
    assignments = [
        {
            "address": item["address"],
            "axis": item["axis"],
            "owner_id": item["primary_owner"]["id"],
            "owner_name": item["primary_owner"]["name"],
            "semantic_role": item["semantic_role"],
            "reviewers": [reviewer["name"] for reviewer in item["required_reviewers"]],
        }
        for item in descriptors
    ]
    return f"""You are executing the bounded specialist drafting pass inside Maestro v5-c.

GOVERNING RULES
- Artist vision and supplied lyrics/source are authoritative inputs.
- Produce proposed Technical UST state, not Creative UST and not renderer prompts.
- Technical UST has eight axes in this runtime: THY, VOC, STY, TIM, PER, POST, MAP, LYR.
- Each address has a lawful owner. Treat owner_name as the specialist whose judgment creates that proposal.
- Do not write any address not listed below.
- Infer musically when evidence and domain expertise support a useful proposal; do not merely restate the vision.
- If a responsible specialist cannot justify a value, return status=justified_null and explain why.
- Never silently rewrite, improve, paraphrase, or replace supplied lyrics. LYR proposals may describe structure, prosody, assignments, cadence, delivery, or preservation constraints, but the source lyric text remains immutable.
- Preserve contradictions and uncertainty in rationale rather than smoothing them away.
- Output JSON only.

INTAKE
{json.dumps(intake, ensure_ascii=False)}

LAWFUL ADDRESS ASSIGNMENTS
{json.dumps(assignments, ensure_ascii=False)}

Return exactly this shape:
{{
  "project_interpretation": "one concise producer-level reading of what the artist is trying to make the listener feel and what must be protected",
  "proposals": [
    {{
      "address": "one listed address",
      "owner_id": "the listed owner_id",
      "status": "proposed" | "justified_null",
      "value": <JSON scalar/object/list or null>,
      "rationale": "musical reasoning tied to vision/lyrics/domain expertise",
      "provenance": ["vision" | "lyrics" | "constraint" | "specialist_inference"],
      "confidence": 0.0
    }}
  ]
}}

Return one proposal for every listed address. Confidence must be between 0 and 1.
"""


def call_gateway(prompt: str) -> Dict[str, Any]:
    token = os.getenv("AI_GATEWAY_API_KEY") or os.getenv("VERCEL_OIDC_TOKEN")
    if not token:
        raise ModelExecutionUnavailable("Vercel AI Gateway authentication is unavailable")
    model = os.getenv("MAESTRO_INTERPRETATION_MODEL") or DEFAULT_MODEL
    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": "Return strict JSON. Do not include markdown fences."},
            {"role": "user", "content": prompt},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0.35,
    }).encode("utf-8")
    request = urllib.request.Request(
        GATEWAY_URL,
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "maestro-v5c-browser-mvp/1.0",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=90) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", "replace")[:1200]
        raise ModelExecutionUnavailable(f"AI Gateway HTTP {exc.code}: {detail}") from exc
    except (urllib.error.URLError, TimeoutError) as exc:
        raise ModelExecutionUnavailable(f"AI Gateway request failed: {exc}") from exc
    try:
        content = payload["choices"][0]["message"]["content"]
        parsed = json.loads(content)
    except (KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        raise ModelResponseInvalid("AI Gateway returned a non-JSON specialist result") from exc
    if not isinstance(parsed, dict):
        raise ModelResponseInvalid("specialist result must be a JSON object")
    return parsed


def compile_technical_ust(payload: Dict[str, Any], model_caller: Optional[Callable[[str], Dict[str, Any]]] = None) -> Dict[str, Any]:
    intake = build_intake(payload)
    descriptors = _address_descriptors()
    allowed = {item["address"]: item for item in descriptors}
    raw = (model_caller or call_gateway)(_prompt(intake, descriptors))
    proposals = raw.get("proposals") or []
    if not isinstance(proposals, list):
        raise ModelResponseInvalid("proposals must be a list")

    accepted: Dict[str, Dict[str, Any]] = {}
    rejected: List[Dict[str, Any]] = []
    for proposal in proposals:
        if not isinstance(proposal, dict):
            rejected.append({"reason": "proposal_not_object"})
            continue
        address = str(proposal.get("address") or "")
        descriptor = allowed.get(address)
        if not descriptor:
            rejected.append({"address": address, "reason": "address_not_authorized"})
            continue
        expected_owner = descriptor["primary_owner"]["id"]
        if proposal.get("owner_id") != expected_owner:
            rejected.append({"address": address, "reason": "owner_mismatch", "expected_owner": expected_owner})
            continue
        status = proposal.get("status")
        if status not in {"proposed", "justified_null"}:
            rejected.append({"address": address, "reason": "invalid_status"})
            continue
        confidence = proposal.get("confidence")
        try:
            confidence = max(0.0, min(1.0, float(confidence)))
        except (TypeError, ValueError):
            confidence = 0.0
        value = proposal.get("value") if status == "proposed" else None
        if status == "proposed" and value is None:
            status = "justified_null"
        accepted[address] = {
            "address": address,
            "axis": descriptor["axis"],
            "owner": descriptor["primary_owner"],
            "required_reviewers": descriptor["required_reviewers"],
            "semantic_role": descriptor["semantic_role"],
            "status": status,
            "value": value if status == "proposed" else None,
            "rationale": str(proposal.get("rationale") or "").strip(),
            "provenance": proposal.get("provenance") if isinstance(proposal.get("provenance"), list) else [],
            "confidence": confidence,
        }

    # No skipped leaves: every routable runtime address is represented explicitly.
    for address, descriptor in allowed.items():
        if address not in accepted:
            accepted[address] = {
                "address": address,
                "axis": descriptor["axis"],
                "owner": descriptor["primary_owner"],
                "required_reviewers": descriptor["required_reviewers"],
                "semantic_role": descriptor["semantic_role"],
                "status": "justified_null",
                "value": None,
                "rationale": "specialist result did not lawfully disposition this address; preserved as explicit null",
                "provenance": [],
                "confidence": 0.0,
            }

    ordered = sorted(accepted.values(), key=lambda item: (AXIS_ORDER.index(item["axis"]), item["address"]))
    by_axis = {}
    for axis in AXIS_ORDER:
        items = [item for item in ordered if item["axis"] == axis]
        if not items:
            continue
        by_axis[axis] = {
            "status": "proposed",
            "proposed": sum(1 for item in items if item["status"] == "proposed"),
            "justified_null": sum(1 for item in items if item["status"] == "justified_null"),
            "addresses": items,
        }

    return {
        "phase": "sequential_technical_ust_drafting",
        "canonical_status": "proposed_not_locked",
        "intake_manifest": intake,
        "project_interpretation": str(raw.get("project_interpretation") or "").strip(),
        "technical_ust": by_axis,
        "open_question_list": [
            {"address": item["address"], "reason": item["rationale"], "owner": item["owner"]}
            for item in ordered if item["status"] == "justified_null"
        ],
        "rejected_model_outputs": rejected,
        "lyrics_preservation": {
            "locked": intake["lyrics_locked"],
            "source_sha256": intake["lyrics_sha256"],
            "source_text_mutated": False,
        },
        "next_gate": "draft.technical.ust freeze only after all required addresses are dispositioned; round-robin follows",
        "execution_topology": "single-model bounded-specialist simulation for MVP; controller validates address ownership and preserves explicit nulls",
    }
