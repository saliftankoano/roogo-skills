"""Run the workflow's actual whitespace step against disposable Git histories."""

import os
from pathlib import Path
import subprocess
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = yaml.safe_load((ROOT / ".github/workflows/validate.yml").read_text())
CHECK = next(step["run"] for step in WORKFLOW["jobs"]["validate"]["steps"]
             if step.get("name") == "Check changed-line whitespace")


class WhitespaceWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="roogo-whitespace-tests-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.git("init", "-q")
        self.git("config", "user.name", "Fixture Reviewer")
        self.git("config", "user.email", "review@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.whitespace", "blank-at-eol,blank-at-eof,space-before-tab")
        self.base = self.commit("Clean baseline\n")

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True,
                              capture_output=True, text=True).stdout.strip()

    def commit(self, text):
        (self.root / "example.md").write_text(text)
        self.git("add", "example.md")
        self.git("commit", "-qm", "Fixture commit")
        return self.git("rev-parse", "HEAD")

    def check(self, base, head, event="push"):
        env = dict(os.environ, DIFF_BASE=base, DIFF_HEAD=head, GITHUB_EVENT_NAME=event)
        return subprocess.run(["bash", "-e", "-o", "pipefail", "-c", CHECK],
                              cwd=self.root, env=env, capture_output=True, text=True)

    def test_committed_whitespace_fails_with_clean_worktree(self):
        head = self.commit("Introduced trailing space   \n")
        self.assertEqual(self.git("status", "--porcelain"), "")
        for event in ("push", "pull_request"):
            with self.subTest(event=event):
                result = self.check(self.base, head, event)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("trailing whitespace", result.stdout)

    def test_clean_changes_pass(self):
        head = self.commit("Clean new content\n")
        self.assertEqual(self.check(self.base, head).returncode, 0)

    def test_first_push_checks_against_empty_tree(self):
        head = self.commit("Trailing space   \n")
        self.assertNotEqual(self.check("0" * 40, head).returncode, 0)
        self.assertEqual(self.check("0" * 40, self.base).returncode, 0)

    def test_pr_ignores_base_branch_only_changes(self):
        # The common ancestor has legacy whitespace. Only main fixes it; the PR
        # adds a clean new file. A direct base-tip/head comparison would wrongly
        # blame the PR for reintroducing the legacy whitespace.
        common = self.commit("Legacy trailing space   \n")
        self.git("checkout", "-qb", "feature", common)
        (self.root / "feature.md").write_text("Feature\n")
        self.git("add", "feature.md")
        self.git("commit", "-qm", "Feature")
        head = self.git("rev-parse", "HEAD")
        self.git("checkout", "--detach", common)
        base_tip = self.commit("Legacy trailing space\n")
        direct = subprocess.run(["git", "diff", "--check", base_tip, head],
                                cwd=self.root, capture_output=True, text=True)
        self.assertNotEqual(direct.returncode, 0)
        self.assertEqual(self.check(base_tip, head, "pull_request").returncode, 0)

    def test_missing_revision_fails(self):
        self.assertNotEqual(self.check("", self.base).returncode, 0)


if __name__ == "__main__":
    unittest.main()
