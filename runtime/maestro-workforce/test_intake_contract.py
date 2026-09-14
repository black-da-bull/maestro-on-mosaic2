"""Deterministic proposal boundary tests; no provider or audible-quality claim."""
import hashlib
import importlib.util
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import intake_compiler as compiler
import mvp_contract_fixture as fixture

class IntakeContract(unittest.TestCase):
    def test_owned_proposals_rejected_outputs_nulls_and_locked_source(self):
        descriptors = compiler._address_descriptors()
        first = descriptors[0]
        lyrics = "  Keep these words.\nAnd this spacing.\n"
        def model(prompt):
            return {"project_interpretation": "Preserve intimacy", "proposals": [
                {"address": first["address"], "owner_id": first["primary_owner"]["id"],
                 "status": "proposed", "value": "minor", "rationale": "Vision requests a lament", "confidence": .8},
                {"address": descriptors[1]["address"], "owner_id": "wrong", "status": "proposed", "value": "bad"},
                {"address": "UNAUTHORIZED", "owner_id": "wrong"}]}
        result = compiler.compile_technical_ust({"vision": "Intimate lament", "lyrics": lyrics}, model)
        rows = [r for axis in result["technical_ust"].values() for r in axis["addresses"]]
        self.assertEqual(len(rows), len(descriptors))
        self.assertEqual(sum(r["status"] == "proposed" for r in rows), 1)
        self.assertEqual(len(result["rejected_model_outputs"]), 2)
        self.assertTrue(all(r["rationale"] for r in rows))
        self.assertEqual(result["intake_manifest"]["locked_lyrics"], lyrics)
        self.assertEqual(result["lyrics_preservation"]["source_sha256"], hashlib.sha256(lyrics.encode()).hexdigest())
        self.assertEqual(result["canonical_status"], "proposed_not_locked")

    def test_both_entrypoints_compile_and_fail_closed(self):
        root = Path(__file__).resolve().parents[2]
        spec = importlib.util.spec_from_file_location("root_mvp_test", root / "app.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        original = fixture.mvp
        try:
            for entry in [original, module]:
                fixture.mvp = entry
                with patch.object(compiler, "call_gateway", return_value={"proposals": []}):
                    status, result = fixture.call("POST", "/api/compile", {"vision": "Slow soul", "lyrics": "Original words"})
                self.assertEqual(status, 200)
                self.assertEqual(result["canonical_status"], "proposed_not_locked")
                self.assertFalse(result["lyrics_preservation"]["source_text_mutated"])
                with patch.dict(os.environ, {}, clear=True):
                    status, result = fixture.call("POST", "/api/compile", {"vision": "Slow soul"})
                self.assertEqual(status, 503)
                with patch.object(compiler, "call_gateway", return_value=[]):
                    status, result = fixture.call("POST", "/api/compile", {"vision": "Slow soul"})
                self.assertEqual(status, 502)
                status, result = fixture.call("POST", "/api/compile", {})
                self.assertEqual(status, 400)
        finally:
            fixture.mvp = original

if __name__ == "__main__":
    unittest.main()
