import py_compile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "skills" / "vsl"


class VslPackageTests(unittest.TestCase):
    def test_scripts_compile(self):
        for name in ("build_vo.py", "gen_horizontal.py", "gen_vertical.py"):
            py_compile.compile(str(ROOT / "scripts" / name), doraise=True)

    def test_no_private_paths_or_media_shipped(self):
        for f in ROOT.rglob("*"):
            if f.is_file() and f.suffix in {".py", ".md", ".css", ".yaml", ".json"}:
                text = f.read_text(encoding="utf-8")
                self.assertNotIn("/Users/", text, f)
        banned = {".mp3", ".wav", ".mp4", ".ttf", ".png", ".jpg"}
        shipped = [f for f in ROOT.rglob("*") if f.suffix.lower() in banned]
        self.assertEqual(shipped, [])

    def test_example_scenes_have_ids_and_text(self):
        import json

        scenes = json.loads((ROOT / "scripts" / "scenes.example.json").read_text(encoding="utf-8"))
        self.assertTrue(all("id" in s and s["vo"] for s in scenes))


if __name__ == "__main__":
    unittest.main()
