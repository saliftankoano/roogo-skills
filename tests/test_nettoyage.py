import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills" / "nettoyage"
SCRIPT = ROOT / "scripts" / "rangement.py"


class RangementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp()).resolve()
        self.env = {**os.environ, "RANGEMENT_DIR": str(self.tmp / "Agent"),
                    "RANGEMENT_CORBEILLE": str(self.tmp / "Trash")}
        self.env.pop("RANGEMENT_DOSSIER", None)
        self.folder = Path(self.run_ok("ouvrir", "Vidéo test").strip())
        self.work = self.tmp / "work"; self.work.mkdir()

    def run_cmd(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], env=self.env, capture_output=True, text=True)

    def run_ok(self, *args):
        r = self.run_cmd(*args)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout

    def test_folder_layout(self):
        self.assertTrue(self.folder.name.startswith("Vidéo test "))
        self.assertTrue((self.folder / "final").is_dir())
        self.assertTrue((self.folder / "a-reprendre").is_dir())
        self.assertTrue((self.folder / "LISEZMOI.md").is_file())

    def test_full_cycle(self):
        final = self.work / "video.mp4"; final.write_bytes(b"x")
        plan = self.work / "plan.json"; plan.write_text("{}")
        junk = self.work / "frames"; junk.mkdir(); (junk / "f1.png").write_bytes(b"y")
        for p in (final, plan, junk):
            self.run_ok("trace", str(p))
        self.assertIn("3 item(s)", self.run_ok("bilan"))
        self.run_ok("final", str(final))
        self.run_ok("garder", str(plan), "--pourquoi", "plan de montage")
        self.run_ok("jeter", str(junk))
        self.assertTrue(final.exists())                      # final is a copy
        self.assertTrue((self.folder / "final" / "video.mp4").exists())
        self.assertFalse(plan.exists())                      # kept items move
        self.assertTrue((self.folder / "a-reprendre" / "plan.json").exists())
        self.assertFalse(junk.exists())
        self.assertTrue((self.tmp / "Trash" / "frames" / "f1.png").exists())  # recoverable
        self.assertIn("0 item(s)", self.run_ok("bilan"))
        readme = (self.folder / "LISEZMOI.md").read_text(encoding="utf-8")
        self.assertIn("plan de montage", readme)
        self.assertIn("frames", readme)

    def test_refuses_broad_and_conversation_paths(self):
        for p in (Path.home(), self.folder, self.tmp / "Agent"):
            r = self.run_cmd("jeter", str(p), "--confirme")
            self.assertNotEqual(r.returncode, 0, p)
            self.assertTrue(p.exists())

    def test_refuses_a_repository_root(self):
        repo = self.tmp / "repo"; repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        r = self.run_cmd("jeter", str(repo))
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("root of a git repository", r.stderr)

    def test_refuses_git_tracked_files(self):
        repo = self.tmp / "repo2"; repo.mkdir()
        subprocess.run(["git", "init", "-q", str(repo)], check=True)
        f = repo / "a.txt"; f.write_text("a")
        subprocess.run(["git", "-C", str(repo), "add", "a.txt"], check=True)
        r = self.run_cmd("jeter", str(f), "--confirme")
        self.assertIn("tracked by git", r.stderr)
        self.assertTrue(f.exists())

    def test_trace_process_and_note(self):
        self.run_ok("trace", "--process", str(os.getpid()), "--quoi", "test server")
        self.assertIn("PROCESS", self.run_ok("bilan"))
        self.run_ok("note", "Pour reprendre : relancer montage.py plan.json")
        self.assertIn("relancer montage.py", (self.folder / "LISEZMOI.md").read_text(encoding="utf-8"))
        lines = (self.folder / ".traces.jsonl").read_text(encoding="utf-8").splitlines()
        self.assertTrue(all(json.loads(l)["t"] for l in lines))

    def test_skill_text_states_the_safety_rules(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for phrase in ("Only clean what **you** created", "Trash", "ask before removing", "~/Downloads/Agent/"):
            self.assertIn(phrase, skill)


if __name__ == "__main__":
    unittest.main()
