"""Exercise the visite-pov helpers with synthetic media; no credentials or real listings."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

from PIL import Image, ImageDraw, ImageStat


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skills/visite-pov/scripts"
sys.path.insert(0, str(SCRIPTS))
import build_pov  # noqa: E402


def probe(path, stream):
    out = subprocess.check_output([
        "ffprobe", "-v", "error", "-select_streams", stream, "-show_entries",
        "stream=duration", "-of", "csv=p=0", str(path),
    ])
    return float(out)


class DriftTests(unittest.TestCase):
    def test_drift_box_stays_inside_the_photo(self):
        shot = {"start": 0.0, "end": 4.0, "zoom": [1.0, 1.2], "pan": [0.0, 1.0], "y": 1.0}
        for t in (-0.2, 0.0, 2.0, 4.0, 4.2):
            left, top, s = build_pov.drift_box((1920, 1080), shot, t)
            self.assertGreaterEqual(left, -1e-6)
            self.assertGreaterEqual(top, -1e-6)
            self.assertLessEqual(left + build_pov.W / s, 1920 + 1e-6)
            self.assertLessEqual(top + build_pov.H / s, 1080 + 1e-6)

    def test_drift_moves_and_pushes_in(self):
        shot = {"start": 0.0, "end": 4.0, "zoom": [1.0, 1.2], "pan": [0.2, 0.8], "y": 0.5}
        left0, _, s0 = build_pov.drift_box((1920, 1080), shot, 0.0)
        left1, _, s1 = build_pov.drift_box((1920, 1080), shot, 4.0)
        self.assertGreater(s1, s0)
        self.assertGreater(left1, left0)


class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            raise RuntimeError("Tests require ffmpeg and ffprobe")
        cls.tmp = tempfile.TemporaryDirectory(prefix="roogo-pov-tests-")
        cls.root = Path(cls.tmp.name)

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_face_blur_only_touches_the_box(self):
        src = self.root / "src"
        src.mkdir()
        im = Image.new("RGB", (400, 300), "white")
        d = ImageDraw.Draw(im)
        for x in range(0, 400, 8):
            d.line([(x, 0), (x, 300)], fill="black", width=3)
        im.save(src / "a.jpg", quality=95)
        (self.root / "faces.json").write_text(json.dumps({
            "src": "src/", "out": "out/", "photos": ["a.jpg"],
            "faces": {"a.jpg": [[180, 130, 220, 170]]},
        }))
        subprocess.run([sys.executable, str(SCRIPTS / "flouter_visages.py"),
                        str(self.root / "faces.json")], check=True, capture_output=True)
        out = Image.open(self.root / "out/p1.png").convert("L")
        before = Image.open(src / "a.jpg").convert("L")
        inside = lambda img: ImageStat.Stat(img.crop((190, 140, 210, 160))).stddev[0]
        self.assertLess(inside(out), inside(before) / 2)
        self.assertEqual(out.crop((0, 0, 100, 100)).tobytes(), before.crop((0, 0, 100, 100)).tobytes())

    def test_build_matches_voiceover_length_and_watermarks_photos(self):
        work = self.root / "build"
        work.mkdir()
        for i, color in enumerate(("#8a5a2b", "#3d6b8f"), 1):
            Image.new("RGB", (1920, 1080), color).save(work / f"p{i}.png")
        logo = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(logo).rectangle([40, 40, 120, 120], fill=(201, 106, 46, 255))
        logo.save(work / "logo.png")
        for source, name, seconds in (
            ("sine=frequency=300", "vo.wav", 6),
            ("sine=frequency=500", "bed.wav", 12),
        ):
            subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", source, "-t", str(seconds),
                            str(work / name)], check=True)
        subprocess.run(["ffmpeg", "-v", "error", "-f", "lavfi", "-i", "color=c=0xcb7215:s=1080x1920:r=30",
                        "-t", "5.5", "-pix_fmt", "yuv420p", str(work / "outro.mp4")], check=True)
        plan = {
            "vo": "vo.wav", "music": "bed.wav", "outro": "outro.mp4", "endcard_from": 4.0,
            "out": "out.mp4", "logo": "logo.png",
            "shots": [
                {"photo": "p1.png", "start": 0.0, "end": 2.0, "zoom": [1.0, 1.1], "pan": [0.2, 0.4], "y": 0.5},
                {"photo": "p2.png", "start": 2.0, "end": 4.0, "zoom": [1.0, 1.1], "pan": [0.6, 0.4], "y": 0.8},
            ],
        }
        (work / "plan.json").write_text(json.dumps(plan))
        subprocess.run([sys.executable, str(SCRIPTS / "build_pov.py"), str(work / "plan.json")],
                       check=True, capture_output=True)
        out = work / "out.mp4"
        expected = build_pov.VO_DELAY + 6 + 1.4
        self.assertAlmostEqual(probe(out, "v:0"), expected, delta=0.1)
        self.assertAlmostEqual(probe(out, "a:0"), expected, delta=0.1)
        self.assertFalse(list(work.glob("*.tmp.mp4")))

        def frame(t):
            png = work / f"f{t}.png"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(out),
                            "-frames:v", "1", str(png)], check=True)
            return Image.open(png).convert("RGB")

        badge = (1080 - 40 - 28 - 58, 90 + 58 - 50)   # white ring above the logo, from build_pov.watermark
        self.assertGreater(sum(frame(1.0).getpixel(badge)), 600)       # white badge on photos
        self.assertLess(sum(frame(7.0).getpixel(badge)), 600)          # no badge over the outro


if __name__ == "__main__":
    unittest.main()
