"""
Unit tests for ems_engine — run with: python3 -m pytest ems_engine/tests/
or, if pytest is not installed in the environment: python3 ems_engine/tests/test_core.py

These cover the parts of the package that are genuinely new (router) and
the parts that were relocated and must continue to match previously
validated behaviour exactly (gates checker).

Does NOT make live API calls — no test here requires NIM_API_KEY,
ANTHROPIC_API_KEY, or network access. Live-call validation is a separate,
explicit step (see IMPLEMENTATION_STATUS.md — "v2 chain has never been
run end-to-end... recommend a dry run").
"""

import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from ems_engine.providers.base import ProviderError
from ems_engine.providers.router import get_provider, list_registered_providers, resolve_provider_name
from ems_engine.gates.checker import check_readiness


class TestProviderRouter(unittest.TestCase):
    def setUp(self):
        # Ensure a clean env for each test — no leftover provider config
        for key in ("EMS_DEFAULT_PROVIDER", "NIM_API_KEY", "ANTHROPIC_API_KEY", "OPENAI_API_KEY"):
            os.environ.pop(key, None)

    def test_explicit_provider_wins(self):
        self.assertEqual(resolve_provider_name(explicit="claude"), "claude")

    def test_fallback_default_is_nim(self):
        self.assertEqual(resolve_provider_name(), "nim")

    def test_env_var_default_respected(self):
        os.environ["EMS_DEFAULT_PROVIDER"] = "claude"
        self.assertEqual(resolve_provider_name(), "claude")

    def test_explicit_beats_env_var(self):
        os.environ["EMS_DEFAULT_PROVIDER"] = "claude"
        self.assertEqual(resolve_provider_name(explicit="openai"), "openai")

    def test_unknown_provider_raises(self):
        with self.assertRaises(ProviderError):
            get_provider(explicit="not-a-real-provider")

    def test_unconfigured_provider_raises_not_silently_falls_back(self):
        # No API keys set in this test environment by design (see setUp)
        with self.assertRaises(ProviderError):
            get_provider(explicit="nim")

    def test_all_three_providers_registered(self):
        registered = list_registered_providers()
        for expected in ("nim", "claude", "openai"):
            self.assertIn(expected, registered)


class TestReadinessGatesUnchangedBehaviour(unittest.TestCase):
    """
    Confirms the relocated gates checker (ems_engine.gates.checker) produces
    identical results to the originally validated version in
    .github/scripts/check_readiness_gates.py for the same fixture cases.
    """

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmpdir, ignore_errors=True)

    def test_empty_platform_dir_fails_all_gates(self):
        result = check_readiness(self.tmpdir, "TEST_EMPTY", reduced_scope=True)
        self.assertFalse(result["all_gates_pass"])
        self.assertTrue(result["overall_status"].startswith("BLOCKED"))
        self.assertEqual(len(result["failing_gates"]), 10)

    def test_populated_platform_dir_passes_most_gates(self):
        spine_dir = os.path.join(self.tmpdir, "spine")
        os.makedirs(spine_dir, exist_ok=True)

        filler = "x" * 300  # over the MIN_CONTENT_CHARS threshold

        for fname in (
            "USE_CASE_REGISTER.md",
            "ARCHITECTURE_DOCUMENT.md",
            "KNOWLEDGE_GRAPH.md",
            "MASTER_TECHNICAL_SPECIFICATION.md",
        ):
            with open(os.path.join(self.tmpdir, fname), "w") as f:
                f.write(filler)

        with open(os.path.join(self.tmpdir, "SCAN_RESULT.json"), "w") as f:
            f.write('{"scan_status": "SUCCESS"}' + (" " * 280))  # padded over threshold

        with open(os.path.join(spine_dir, "test.md"), "w") as f:
            f.write("spine content")

        with open(os.path.join(self.tmpdir, "INTAKE_RUN_LOG.md"), "w") as f:
            f.write('"pass": true\n"pass": true\n' + filler)

        result = check_readiness(self.tmpdir, "TEST_FULL", reduced_scope=True)

        # RG-008 (Founder Questions) is always N/A by design — never PASS
        # RG-002/RG-004 depend on SCAN_RESULT.json content size in this fixture
        self.assertNotIn("RG-001", result["failing_gates"])
        self.assertNotIn("RG-005", result["failing_gates"])
        self.assertNotIn("RG-006", result["failing_gates"])
        self.assertNotIn("RG-007", result["failing_gates"])
        self.assertNotIn("RG-009", result["failing_gates"])
        self.assertIn("RG-008", result["failing_gates"])  # always N/A currently


    def test_genesis_origin_platform_can_reach_same_ceiling_as_brownfield(self):
        """
        Regression test for a real bug found during a brownfield/greenfield
        simulation exercise: the gate checker originally only recognised
        INTAKE_RUN_LOG.md and SCAN_RESULT.json as evidence for RG-001/002/004,
        which meant a greenfield (MISSION-000 Genesis) platform could NEVER
        pass those gates regardless of how complete its genesis run was —
        genesis has no repo to scan, so SCAN_RESULT.json never exists for it.

        This test builds a genesis-origin fixture (GENESIS_RUN_LOG.md instead
        of INTAKE_RUN_LOG.md, no SCAN_RESULT.json, architecture doc serving
        as the tech-stack evidence) and confirms it reaches the same honest
        ceiling as the brownfield case: only RG-008 (Founder Questions,
        not yet implemented for either origin) blocks it.
        """
        spine_dir = os.path.join(self.tmpdir, "spine")
        os.makedirs(spine_dir, exist_ok=True)
        filler = "x" * 300

        for fname in (
            "USE_CASE_REGISTER.md",
            "ARCHITECTURE_DOCUMENT.md",
            "KNOWLEDGE_GRAPH.md",
            "MASTER_TECHNICAL_SPECIFICATION.md",
        ):
            with open(os.path.join(self.tmpdir, fname), "w") as f:
                f.write(filler)

        with open(os.path.join(spine_dir, "test.md"), "w") as f:
            f.write("spine content")

        # GENESIS_RUN_LOG.md instead of INTAKE_RUN_LOG.md — no SCAN_RESULT.json
        # at all, since genesis has no repo to scan, by design.
        with open(os.path.join(self.tmpdir, "GENESIS_RUN_LOG.md"), "w") as f:
            f.write('"pass": true\n"pass": true\n' + filler)

        result = check_readiness(self.tmpdir, "TEST_GENESIS", reduced_scope=True)

        self.assertNotIn("RG-001", result["failing_gates"])
        self.assertNotIn("RG-002", result["failing_gates"])
        self.assertNotIn("RG-003", result["failing_gates"])
        self.assertNotIn("RG-004", result["failing_gates"])
        self.assertNotIn("RG-005", result["failing_gates"])
        self.assertNotIn("RG-006", result["failing_gates"])
        self.assertNotIn("RG-007", result["failing_gates"])
        self.assertNotIn("RG-009", result["failing_gates"])
        self.assertNotIn("STANDARDS_ENGINEER_GATE", result["failing_gates"])
        self.assertIn("RG-008", result["failing_gates"])  # always N/A currently, both origins
        self.assertEqual(len(result["failing_gates"]), 1)  # ONLY RG-008 should block genesis, same as brownfield


if __name__ == "__main__":
    unittest.main()
