import importlib.util
import json
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills" / "formation-equipe"
SCRIPTS = ROOT / "scripts"
HAS_FFMPEG = shutil.which("ffmpeg") is not None


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(SCRIPTS))
    spec.loader.exec_module(mod)
    return mod


class FormationEquipePackageTests(unittest.TestCase):
    def test_scripts_compile(self):
        for f in SCRIPTS.glob("*.py"):
            py_compile.compile(str(f), doraise=True)

    def test_no_private_paths_or_media_shipped(self):
        for f in ROOT.rglob("*"):
            if f.is_file() and f.suffix in {".py", ".md", ".mjs", ".yaml", ".json"}:
                self.assertNotIn("/Users/", f.read_text(encoding="utf-8"), f)
        banned = {".mp3", ".wav", ".mp4", ".ttf", ".png", ".jpg"}
        self.assertEqual([f for f in ROOT.rglob("*") if f.suffix.lower() in banned], [])

    def test_improvement_step_is_mandatory_and_structured(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Improve this skill", skill)
        self.assertIn("Mandatory", skill)
        protocol = (ROOT / "references" / "ameliorations.md").read_text(encoding="utf-8")
        for field in ("**Gap:**", "**Evidence:**", "**Proposed change:**", "**Expected effect:**", "**Confidence:**"):
            self.assertIn(field, protocol)

    def test_skill_does_not_delegate_to_another_video_skill(self):
        self.assertNotIn("product-video", (ROOT / "SKILL.md").read_text(encoding="utf-8"))

    def test_example_plan_is_complete(self):
        plan = json.loads((SCRIPTS / "montage.example.json").read_text(encoding="utf-8"))
        for key in ("captures", "script", "words", "narration", "font_title", "font_text", "logo", "out", "intro", "outro", "shots"):
            self.assertIn(key, plan)
        times = [s[0] for s in plan["shots"]]
        self.assertEqual(times, sorted(times))


class AlignerTests(unittest.TestCase):
    def setUp(self):
        self.al = load("aligner")
        self.script = "# Titre\n\n1. Cliquez sur Nouveau. Roogo écrit le script.\n2. Vérifiez le prix ?\n"

    def test_captions_keep_script_spelling_with_heard_timing(self):
        heard = [{"word": w, "start": i * 0.5, "end": i * 0.5 + 0.4}
                 for i, w in enumerate("Cliquez sur Nouveau. Rogo écrit le script. Vérifiez le prix".split())]
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(heard, f)
        caps = self.al.phrases(self.script, self.al.load_words(f.name))
        self.assertEqual([c[0] for c in caps], ["Cliquez sur Nouveau.", "Roogo écrit le script.", "Vérifiez le prix ?"])
        self.assertAlmostEqual(caps[1][1], 1.5)

    def test_long_sentences_are_split(self):
        text = "1. " + " ".join(["mot"] * 40) + "."
        words = [{"w": "mot", "s": i * 0.3, "e": i * 0.3 + 0.25} for i in range(40)]
        caps = self.al.phrases(text, words)
        self.assertGreater(len(caps), 1)
        self.assertTrue(all(len(c[0]) <= 70 for c in caps))


@unittest.skipUnless(HAS_FFMPEG, "ffmpeg not installed")
class MediaTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def ff(self, *args):
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", *args], check=True)

    def test_verifier_fails_on_a_long_still_and_passes_on_motion(self):
        still = self.tmp / "still.mp4"
        self.ff("-f", "lavfi", "-i", "color=c=white:s=320x180:d=5", "-f", "lavfi", "-i", "sine=d=5", "-shortest", str(still))
        moving = self.tmp / "moving.mp4"
        self.ff("-f", "lavfi", "-i", "testsrc2=s=320x180:d=5", "-f", "lavfi", "-i", "sine=d=5", "-shortest", str(moving))
        verify = [sys.executable, str(SCRIPTS / "verifier.py")]
        self.assertEqual(subprocess.run(verify + [str(still)], capture_output=True).returncode, 1)
        self.assertEqual(subprocess.run(verify + [str(moving)], capture_output=True).returncode, 0)

    def test_mixer_keeps_the_video_length(self):
        video = self.tmp / "v.mp4"
        self.ff("-f", "lavfi", "-i", "testsrc2=s=320x180:d=6", str(video))
        voice = self.tmp / "n.wav"
        self.ff("-f", "lavfi", "-i", "sine=f=300:d=3", str(voice))
        music = self.tmp / "m.wav"
        self.ff("-f", "lavfi", "-i", "sine=f=500:d=10", str(music))
        out = self.tmp / "final.mp4"
        mixer = load("mixer")
        subprocess.run(mixer.build_command(str(video), str(voice), str(music), str(out), delay=1.0), check=True)
        self.assertAlmostEqual(mixer.seconds(str(out)), 6.0, delta=0.15)


if __name__ == "__main__":
    unittest.main()
