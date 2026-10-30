"""Contract tests for release metadata and read-only installation comparisons."""

import contextlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import URLError

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_installation as checker
from validate_sources import validate_release_metadata


class ReleaseToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="super-pm-release-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "reference"
        self.root.mkdir()
        (self.root / "scripts").mkdir()
        self.skill = self.root / "SKILL.md"
        self.skill.write_text('---\nname: super-pm\nmetadata:\n  version: "1.0.0"\n  source: "https://github.com/Lohaslee/super-pm"\n---\nBody\n')
        self.installed = Path(self.temp.name) / "installed"
        shutil.copytree(self.root, self.installed)

    def run_check(self, upstream=False, checkout=None, response=None):
        args = ["check_installation.py", "--compare", str(self.installed)]
        if upstream:
            args.append("--upstream")
        output = io.StringIO()
        with contextlib.ExitStack() as stack:
            stack.enter_context(patch.object(checker, "__file__", str(self.root / "scripts/check_installation.py")))
            stack.enter_context(patch.object(sys, "argv", args))
            stack.enter_context(contextlib.redirect_stdout(output))
            stack.enter_context(patch.object(checker, "checkout_state", return_value=checkout or {"commit": None, "skill_dirty": None}))
            if isinstance(response, Exception):
                stack.enter_context(patch.object(checker, "urlopen", side_effect=response))
            elif response is not None:
                stack.enter_context(patch.object(checker, "urlopen", return_value=io.BytesIO(json.dumps(response).encode())))
            code = checker.main()
        return code, json.loads(output.getvalue())

    def test_equal_content_ignores_caches(self):
        (self.installed / ".DS_Store").write_bytes(b"finder")
        (self.installed / "__pycache__").mkdir()
        (self.installed / "__pycache__/cached.pyc").write_bytes(b"cache")
        code, report = self.run_check()
        self.assertEqual(code, 0)
        self.assertTrue(report["installations"][0]["matches_reference"])

    def test_same_version_different_content_is_detected(self):
        (self.installed / "SKILL.md").write_text(self.skill.read_text() + "Different behavior\n")
        code, report = self.run_check()
        self.assertEqual(code, 1)
        self.assertEqual(report["installations"][0]["version"], "1.0.0")
        self.assertEqual(report["installations"][0]["modified"], ["SKILL.md"])

    def test_missing_installation_is_not_current(self):
        shutil.rmtree(self.installed)
        code, report = self.run_check()
        self.assertEqual(code, 1)
        self.assertIn("SKILL.md", report["installations"][0]["missing"])

    def test_missing_and_malformed_versions_are_rejected(self):
        self.assertEqual(validate_release_metadata(self.root), [])
        for replacement in ["", '  version: "1.0"\n', '  version: "01.0.0"\n']:
            with self.subTest(replacement=replacement):
                original = self.skill.read_text()
                self.skill.write_text(original.replace('  version: "1.0.0"\n', replacement))
                self.assertTrue(validate_release_metadata(self.root))
                self.skill.write_text(original)

    def test_offline_upstream_is_unknown(self):
        code, report = self.run_check(True, response=URLError("offline"))
        self.assertEqual(code, 2)
        self.assertEqual(report["upstream"]["status"], "unknown")

    def test_dirty_matching_commit_is_not_a_clean_release(self):
        code, report = self.run_check(True, {"commit": "a" * 40, "skill_dirty": True}, {"sha": "a" * 40})
        self.assertEqual(code, 1)
        self.assertEqual(report["upstream"]["status"], "local_changes")

    def test_unknown_checkout_does_not_claim_a_different_version(self):
        code, report = self.run_check(True, response={"sha": "a" * 40})
        self.assertEqual(code, 2)
        self.assertEqual(report["upstream"]["status"], "unknown_checkout")


if __name__ == "__main__":
    unittest.main()
