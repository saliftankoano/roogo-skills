"""Check the CI validator against valid and broken disposable packages."""

from pathlib import Path
import runpy
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
validate = runpy.run_path(str(ROOT / "scripts/validate_skills.py"))["validate"]


class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="roogo-package-tests-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.package = self.root / "skills/example"
        self.package.mkdir(parents=True)
        self.entry = self.package / "SKILL.md"
        self.entry.write_text("---\nname: example\ndescription: A sample skill\n---\n# Example\n")

    def test_valid_minimal_package(self):
        self.assertEqual(validate(self.root), [])

    def test_name_mismatch_rejected(self):
        self.entry.write_text("---\nname: different\ndescription: Example\n---\n")
        self.assertTrue(validate(self.root))

    def test_missing_link_and_unlinked_reference_rejected(self):
        self.entry.write_text(self.entry.read_text() + "[Missing](references/missing.md)\n")
        refs = self.package / "references"
        refs.mkdir()
        (refs / "unlinked.md").write_text("# Not linked\n")
        self.assertEqual(len(validate(self.root)), 2)

    def test_invalid_python_rejected(self):
        (self.package / "broken.py").write_text("def broken(:\n")
        self.assertTrue(validate(self.root))

    def test_unreachable_reference_cycle_rejected(self):
        refs = self.package / "references"
        refs.mkdir()
        (refs / "a.md").write_text("[B](b.md)\n")
        (refs / "b.md").write_text("[A](a.md)\n")
        errors = validate(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("not reachable from SKILL.md" in error for error in errors))

    def test_reachable_reference_cycle_and_nested_chain_pass(self):
        refs = self.package / "references"
        (refs / "nested").mkdir(parents=True)
        self.entry.write_text(self.entry.read_text() + "[A](references/a.md)\n")
        (refs / "a.md").write_text("[B](nested/b.md)\n")
        (refs / "nested/b.md").write_text("[A](../a.md)\n")
        self.assertEqual(validate(self.root), [])

    def test_unreachable_nested_reference_rejected(self):
        nested = self.package / "references/nested"
        nested.mkdir(parents=True)
        (nested / "orphan.md").write_text("# Orphan\n")
        self.assertEqual(len(validate(self.root)), 1)

    def test_invalid_ui_metadata_rejected(self):
        agents = self.package / "agents"
        agents.mkdir()
        (agents / "openai.yaml").write_text("interface: []\n")
        self.assertTrue(validate(self.root))


if __name__ == "__main__":
    unittest.main()
