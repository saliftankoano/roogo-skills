"""Exercise the CLI with real, disposable media; no provider credentials needed."""

import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/voxplainer/scripts/audio_quality_gate.py"


def reject_nonfinite(value):
    raise ValueError(f"Non-standard JSON number: {value}")


class AudioQualityGateTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
            raise RuntimeError("Tests require ffmpeg and ffprobe")
        cls.tmp = tempfile.TemporaryDirectory(prefix="roogo-audio-tests-")
        cls.root = Path(cls.tmp.name)
        cls.tone = cls.root / "tone.wav"
        cls.silence = cls.root / "silence.wav"
        for source, output in (
            ("sine=frequency=440:duration=1", cls.tone),
            ("anullsrc=r=48000:cl=stereo", cls.silence),
        ):
            subprocess.run([
                "ffmpeg", "-v", "error", "-f", "lavfi", "-i", source,
                "-t", "1", "-c:a", "pcm_s16le", str(output),
            ], check=True)
        cls.corrupt = cls.root / "corrupt.wav"
        cls.corrupt.write_bytes(b"Not a media file")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def run_gate(self, *args):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            capture_output=True, text=True,
        )
        return result, json.loads(result.stdout, parse_constant=reject_nonfinite)

    def test_audible_tone_passes_and_has_finite_measurements(self):
        result, report = self.run_gate(self.tone)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(report["files"][0]["passed"])
        self.assertIsInstance(report["files"][0]["integratedLufs"], float)

    def test_silence_fails_with_strict_json(self):
        result, report = self.run_gate(self.silence)
        self.assertEqual(result.returncode, 1)
        item = report["files"][0]
        self.assertFalse(item["passed"])
        self.assertIsNone(item["integratedLufs"])
        self.assertIsNone(item["truePeakDbtp"])
        self.assertTrue(item["issues"])

    def test_contract_loudness_limits_fail(self):
        result, report = self.run_gate("--min-lufs", "-10", "--max-lufs", "0", self.tone)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(report["files"][0]["passed"])

    def test_contract_peak_limit_fails(self):
        result, report = self.run_gate("--max-true-peak", "-30", self.tone)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(report["files"][0]["passed"])

    def test_batch_reports_failures_and_continues(self):
        result, report = self.run_gate(self.root / "missing.wav", self.corrupt, self.tone)
        self.assertEqual(result.returncode, 1)
        self.assertEqual([item["passed"] for item in report["files"]], [False, False, True])

    def test_invalid_contract_limits_rejected(self):
        for flags in (("--min-lufs", "nan"), ("--max-true-peak", "inf"),
                      ("--min-lufs", "0", "--max-lufs", "-10")):
            with self.subTest(flags=flags):
                result = subprocess.run(
                    [sys.executable, str(SCRIPT), *flags, str(self.tone)],
                    capture_output=True, text=True,
                )
                self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
