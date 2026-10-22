import importlib.util
import io
import json
import os
import py_compile
import shutil
import stat
import subprocess
import sys
import tempfile
import unittest
import wave
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1] / "skills" / "formation-equipe"
SCRIPTS = ROOT / "scripts"
HAS_FFMPEG = shutil.which("ffmpeg") is not None
HAS_NUMPY = importlib.util.find_spec("numpy") is not None
HAS_PIL = importlib.util.find_spec("PIL") is not None
FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "C:/Windows/Fonts/arial.ttf",
]
FONT = next((f for f in FONT_CANDIDATES if Path(f).is_file()), None)
NBSP = "\u00a0"


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
        for key in ("captures", "script", "words", "narration", "font_title", "font_text", "logo", "out", "intro", "outro", "shots",
                    "size", "caption_y", "badge"):
            self.assertIn(key, plan)
        self.assertIn(plan["size"], ([1920, 1080], [1080, 1920]))
        self.assertLessEqual(plan["caption_y"], 0.85)
        times = [s[0] for s in plan["shots"]]
        self.assertEqual(times, sorted(times))


FAKE_KEY = "fake-test-key-not-real"
FAKE_SECURITY = """#!/bin/sh
# Stand-in for macOS `security`: logs its arguments, knows one synthetic item.
printf '%s\\n' "$*" >> "$FAKE_SECURITY_LOG"
[ "$1" = find-generic-password ] || exit 1
shift
service=""; account=""; print=0
while [ $# -gt 0 ]; do
  case "$1" in
    -s) service="$2"; shift 2;;
    -a) account="$2"; shift 2;;
    -w) print=1; shift;;
    *) echo "unexpected argument $1" >&2; exit 2;;
  esac
done
[ "$service" = "$FAKE_SERVICE" ] || { echo "item not found" >&2; exit 44; }
if [ -n "$account" ] && [ "$account" != "$FAKE_ACCOUNT" ]; then echo "item not found" >&2; exit 44; fi
[ "$print" = 1 ] && echo "$FAKE_KEY_VALUE"
exit 0
"""


class KeychainTests(unittest.TestCase):
    """PRD 1: the key is read from the Keychain, with or without an account name, never shown."""

    def setUp(self):
        self.nar = load("narration")
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        fake = self.tmp / "security"
        fake.write_text(FAKE_SECURITY)
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        self.log = self.tmp / "calls.log"
        env = {k: v for k, v in os.environ.items() if k != "TEST_VOICE_KEY"}
        env.update(PATH=f"{self.tmp}{os.pathsep}{os.environ.get('PATH', '')}", FAKE_SECURITY_LOG=str(self.log),
                   FAKE_SERVICE="test.voice.api-key", FAKE_ACCOUNT="", FAKE_KEY_VALUE=FAKE_KEY)
        self.env = env

    def lookup(self, account=None, **env):
        out, err = io.StringIO(), io.StringIO()
        with mock.patch.dict(os.environ, {**self.env, **env}, clear=True), redirect_stdout(out), redirect_stderr(err):
            try:
                key = self.nar.secret("TEST_VOICE_KEY", "test.voice.api-key", account)
            except SystemExit as e:
                key = e
        return key, out.getvalue() + err.getvalue()

    def test_service_comes_right_after_s_and_account_after_a(self):
        key, shown = self.lookup("default", FAKE_ACCOUNT="default")
        self.assertEqual(key, FAKE_KEY)
        self.assertNotIn(FAKE_KEY, shown)
        self.assertEqual(self.log.read_text().splitlines()[0],
                         "find-generic-password -s test.voice.api-key -a default -w")

    def test_works_without_an_account_name(self):
        key, _ = self.lookup(None)
        self.assertEqual(key, FAKE_KEY)
        self.assertEqual(self.log.read_text().splitlines(), ["find-generic-password -s test.voice.api-key -w"])

    def test_item_saved_without_the_expected_account_is_still_found(self):
        key, _ = self.lookup("default", FAKE_ACCOUNT="someone-else")
        self.assertEqual(key, FAKE_KEY)

    def test_environment_wins_and_keychain_is_not_called(self):
        key, _ = self.lookup("default", TEST_VOICE_KEY="from-env")
        self.assertEqual(key, "from-env")
        self.assertFalse(self.log.exists())

    def test_missing_key_names_variable_and_service_never_a_value(self):
        err, shown = self.lookup("default", FAKE_SERVICE="another.item")
        self.assertIsInstance(err, SystemExit)
        self.assertIn("TEST_VOICE_KEY", str(err.code))
        self.assertIn("test.voice.api-key", str(err.code))
        self.assertNotIn(FAKE_KEY, str(err.code) + shown)

    def test_the_real_cartesia_lookup_uses_the_fixed_order(self):
        with mock.patch.dict(os.environ, {**self.env, "FAKE_SERVICE": "ai.cartesia.api-key", "FAKE_ACCOUNT": "default"},
                             clear=True), mock.patch.object(self.nar.urllib.request, "urlopen") as urlopen:
            urlopen.return_value.read.return_value = b"RIFF"
            with redirect_stdout(io.StringIO()):
                self.nar.speak("Bonjour", "voice-id", str(self.tmp / "a.wav"))
        self.assertEqual(urlopen.call_args[0][0].get_header("X-api-key"), FAKE_KEY)
        self.assertIn("-s ai.cartesia.api-key -a default -w", self.log.read_text())


def write_wav(path, seconds=1.0, sr=16000):
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes(b"\x00\x00" * int(seconds * sr))


class NarrationPaceTests(unittest.TestCase):
    """PRD 2: speed and pauses per run, clone defaults, timestamps still match. No network."""

    def setUp(self):
        self.nar = load("narration")
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        self.script = self.tmp / "script.md"
        self.script.write_text("# Titre\n\n1. Ouvrez Roogo.\n2. Cliquez sur Postuler.\n3. Envoyez.\n", encoding="utf-8")

    def run_main(self, *args, fal_words=None):
        bodies = []

        def fake_urlopen(req, timeout=None):
            bodies.append((req.full_url, json.loads(req.data)))
            resp = mock.MagicMock()
            if "cartesia" in req.full_url:
                resp.read.return_value = b"RIFF-fake-audio"
                return resp
            return io.StringIO(json.dumps({"text": "", "words": fal_words or []}))

        out = self.tmp / "audio" / "n.wav"
        argv = ["narration.py", str(self.script), "--out", str(out), *args]
        with mock.patch.object(sys, "argv", argv), mock.patch.object(self.nar.urllib.request, "urlopen", fake_urlopen), \
                mock.patch.object(self.nar, "duration", return_value=10.0), \
                mock.patch.dict(os.environ, {"CARTESIA_API_KEY": "k", "FAL_KEY": "k"}), redirect_stdout(io.StringIO()) as log:
            self.nar.main()
        return bodies, log.getvalue(), out

    def test_clone_defaults_slow_down_and_pause_between_paragraphs(self):
        bodies, log, _ = self.run_main()
        body = bodies[0][1]
        self.assertEqual(body["voice"]["id"], self.nar.SALIF_FR)
        self.assertEqual(body["generation_config"], {"speed": 0.9})
        self.assertEqual(body["transcript"],
                         'Ouvrez Rohgo. <break time="0.9s"/> Cliquez sur Postuler. <break time="0.9s"/> Envoyez.')
        self.assertIn("speed 0.9, pause 0.9 s", log)

    def test_speed_and_pause_are_set_per_run(self):
        body = self.run_main("--speed", "0.85", "--pause", "1.2")[0][0][1]
        self.assertEqual(body["generation_config"], {"speed": 0.85})
        self.assertEqual(body["transcript"].count('<break time="1.2s"/>'), 2)

    def test_other_voices_keep_normal_speed_unless_marked_as_clone(self):
        body = self.run_main("--voice", "house-voice", "--pause", "0")[0][0][1]
        self.assertNotIn("generation_config", body)
        self.assertNotIn("<break", body["transcript"])
        body = self.run_main("--voice", "another-clone", "--clone")[0][0][1]
        self.assertEqual(body["generation_config"], {"speed": 0.9})

    def test_word_timestamps_come_from_the_audio_with_pauses_and_report_pace(self):
        heard = [{"type": "word", "text": w, "start": s, "end": s + 0.3} for w, s in
                 [("Ouvrez", 0.2), ("Rogo.", 0.6), ("Cliquez", 1.9), ("sur", 2.3), ("Postuler.", 2.6), ("Envoyez.", 3.9)]]
        heard.insert(2, {"type": "spacing", "text": " ", "start": 0.9, "end": 1.9})
        bodies, log, out = self.run_main(fal_words=heard)
        self.assertTrue(bodies[1][0].startswith("https://fal.run/"))
        saved = json.loads(out.with_suffix(".words.json").read_text(encoding="utf-8"))
        self.assertEqual([w["s"] for w in saved], [0.2, 0.6, 1.9, 2.3, 2.6, 3.9])
        self.assertIn("2 pauses", log)
        self.assertNotIn("WARNING", log)

    def test_pace_flags_bad_timestamps_and_measures_words_a_minute(self):
        ws = [{"w": "a", "s": i * 0.4, "e": i * 0.4 + 0.3} for i in range(100)]
        rep = self.nar.pace(ws, 40.0)
        self.assertAlmostEqual(rep["wpm"], 150)
        self.assertEqual(rep["problems"], [])
        bad = self.nar.pace([{"w": "a", "s": 1.0, "e": 1.2}, {"w": "b", "s": 0.5, "e": 12.0}], 10.0)
        self.assertEqual(len(bad["problems"]), 2)


@unittest.skipUnless(HAS_NUMPY, "numpy not installed")
class VoiceCleaningTests(unittest.TestCase):
    """PRD 3: digital-silence pauses never break the noise profile or the measurement."""

    def setUp(self):
        import numpy as np
        self.np = np
        self.nv = load("nettoyer_voix")
        self.sr = 16000

    def speech_with_breaks(self, hiss_db=None, seed=0):
        """Tone bursts (speech), 0.1 s word gaps, and two 0.9 s breaks of pure digital silence."""
        np, sr = self.np, self.sr
        rng = np.random.default_rng(seed)
        t = np.arange(int(0.4 * sr)) / sr
        word = 0.3 * np.sin(2 * np.pi * 220 * t) * (1 + 0.3 * np.sin(2 * np.pi * 3 * t))
        gap = np.zeros(int(0.1 * sr))
        para = np.concatenate([np.concatenate([word, gap]) for _ in range(6)])
        if hiss_db is not None:
            para = para + rng.normal(0, 10 ** (hiss_db / 20), len(para))
        brk = np.zeros(int(0.9 * sr))
        return np.concatenate([para, brk, para, brk, para])

    def test_profile_ignores_digital_silence(self):
        x = self.speech_with_breaks(hiss_db=-45)
        d = self.nv.frame_db(x, int(0.02 * self.sr))
        self.assertGreater((d < -120).mean(), 0.12)      # the old "quietest 12%" was pure silence
        noise, cut, has_background = self.nv.noise_profile(x, self.sr)
        self.assertTrue(has_background)
        self.assertGreater(len(noise), 0)
        self.assertGreater(cut, -120)
        s, b = self.nv.speech_and_background(x, self.sr, cut)
        self.assertTrue(self.np.isfinite(b))
        self.assertGreater(s - b, 20)

    def test_silence_and_speech_only_is_already_clean(self):
        x = self.speech_with_breaks()
        noise, cut, has_background = self.nv.noise_profile(x, self.sr)
        self.assertFalse(has_background)
        self.assertIn("background silent", self.nv.gap_line("original", x, self.sr, cut, has_background))

    def test_all_silence_does_not_crash(self):
        x = self.np.zeros(self.sr)
        self.assertFalse(self.nv.noise_profile(x, self.sr)[2])
        self.assertEqual(self.nv.speech_and_background(x, self.sr), (float("-inf"), float("-inf")))

    @unittest.skipUnless(importlib.util.find_spec("soundfile"), "soundfile not installed")
    def test_command_copies_a_clean_file_and_says_so(self):
        import soundfile as sf
        tmp = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, tmp)
        sf.write(tmp / "in.wav", self.speech_with_breaks(), self.sr, subtype="PCM_16")
        r = subprocess.run([sys.executable, str(SCRIPTS / "nettoyer_voix.py"), str(tmp / "in.wav"), str(tmp / "out.wav")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertIn("already clean", r.stdout)
        self.assertTrue((tmp / "out.wav").is_file())

    @unittest.skipUnless(importlib.util.find_spec("soundfile") and importlib.util.find_spec("noisereduce"),
                         "soundfile or noisereduce not installed")
    def test_command_cleans_hiss_around_silent_breaks_and_the_gap_improves(self):
        import re
        import soundfile as sf
        tmp = Path(tempfile.mkdtemp()); self.addCleanup(shutil.rmtree, tmp)
        sf.write(tmp / "in.wav", self.speech_with_breaks(hiss_db=-40), self.sr, subtype="PCM_16")
        r = subprocess.run([sys.executable, str(SCRIPTS / "nettoyer_voix.py"), str(tmp / "in.wav"), str(tmp / "out.wav")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr)
        gaps = [float(g) for g in re.findall(r"gap\s+(-?[\d.]+) dB", r.stdout)]
        self.assertEqual(len(gaps), 2, r.stdout)
        self.assertGreater(gaps[1], gaps[0])


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
        self.assertEqual([c[0].replace(NBSP, " ") for c in caps],
                         ["Cliquez sur Nouveau.", "Roogo écrit le script.", "Vérifiez le prix ?"])
        self.assertAlmostEqual(caps[1][1], 1.5)

    def test_long_sentences_are_split(self):
        text = "1. " + " ".join(["mot"] * 40) + "."
        words = [{"w": "mot", "s": i * 0.3, "e": i * 0.3 + 0.25} for i in range(40)]
        caps = self.al.phrases(text, words)
        self.assertGreater(len(caps), 1)
        self.assertTrue(all(len(c[0]) <= 70 for c in caps))

    # PRD 5: the two sentences from the 22 October run.
    QUOTES = ("# Titre\n\n1. Remplissez le formulaire avec votre nom et votre numéro, puis « Envoyer ma candidature ».\n"
              "2. Pour chaque candidat, ajoutez une note. « Retenu » pour la présélection.\n")

    def heard_for(self, text):
        spoken = [w for w in self.al.script_words(text)]
        heard, t = [], 0.0
        for w in spoken:
            core = self.al.norm(w)
            heard.append({"w": core, "s": round(t, 2), "e": round(t + 0.3, 2)}); t += 0.35
        return heard

    def test_opening_quote_goes_with_the_next_word(self):
        words = [w.replace(NBSP, " ") for w in self.al.script_words(self.QUOTES)]
        self.assertIn("« Envoyer", words)
        self.assertIn("puis", words)
        self.assertIn("« Retenu »", words)
        self.assertIn("note.", words)
        self.assertNotIn("«", words)
        nb = self.al.script_words("1. Cliquez sur «\u00a0Envoyer\u00a0» maintenant.")
        self.assertEqual([w.replace(NBSP, " ") for w in nb], ["Cliquez", "sur", "« Envoyer »", "maintenant."])

    def test_closing_marks_stay_with_the_word_before(self):
        words = self.al.script_words("1. Ouvrez « Mes candidatures » : est-ce prêt ? Oui !")
        self.assertEqual([w.replace(NBSP, " ") for w in words],
                         ["Ouvrez", "« Mes", "candidatures » :", "est-ce", "prêt ?", "Oui !"])

    def test_captions_never_start_or_end_on_a_lone_quote_and_the_sentence_breaks(self):
        caps = self.al.phrases(self.QUOTES, self.heard_for(self.QUOTES), max_seconds=2.7, max_chars=40)
        texts = [c[0].replace(NBSP, " ") for c in caps]
        for c in texts:
            self.assertFalse(c.endswith("«"), texts)
            self.assertFalse(c.startswith("»"), texts)
        self.assertTrue(any(c.startswith("« Envoyer ma candidature »") or c.endswith("« Envoyer ma candidature ».")
                            for c in texts), texts)
        self.assertTrue(any(c.endswith("une note.") for c in texts), texts)
        self.assertTrue(any(c.startswith("« Retenu » pour la présélection") for c in texts), texts)

    def test_timing_of_every_spoken_word_is_unchanged(self):
        heard = self.heard_for(self.QUOTES)
        for (txt, s, e), h in zip(self.al.aligned(self.QUOTES, heard), heard):
            self.assertEqual((s, e), (h["s"], h["e"]), txt)


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


def contrast(a, b):
    def lum(c):
        ch = [(v / 255) / 12.92 if v / 255 <= 0.03928 else ((v / 255 + 0.055) / 1.055) ** 2.4 for v in c[:3]]
        return 0.2126 * ch[0] + 0.7152 * ch[1] + 0.0722 * ch[2]
    hi, lo = sorted((lum(a), lum(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


@unittest.skipUnless(HAS_FFMPEG and HAS_PIL and FONT, "ffmpeg, Pillow or a TrueType font missing")
class MontageLayoutTests(unittest.TestCase):
    """PRD 4: size, centred readable captions and the badge, from the plan alone."""

    LOGO = (232, 106, 23)

    def setUp(self):
        from PIL import Image, ImageDraw
        self.Image = Image
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        (self.tmp / "captures").mkdir()
        # synthetic phone captures: a white screen and a cream screen, gray band at the top
        for name, colour in (("s01-blanc", (255, 255, 255)), ("s02-creme", (255, 250, 245))):
            im = Image.new("RGB", (1170, 2532), colour)
            ImageDraw.Draw(im).rectangle([0, 0, 1170, 500], fill=(128, 128, 128))
            im.save(self.tmp / "captures" / f"{name}.png")
        Image.new("RGBA", (200, 200), self.LOGO + (255,)).save(self.tmp / "logo.png")
        (self.tmp / "script.md").write_text(
            "# T\n\n1. Ouvrez la page Carrières sur votre téléphone, puis « Postuler ».\n", encoding="utf-8")
        words = ["Ouvrez", "la", "page", "Carrières", "sur", "votre", "téléphone,", "puis", "Postuler."]
        (self.tmp / "words.json").write_text(json.dumps(
            [{"w": w, "s": 2.0 + i * 0.15, "e": 2.1 + i * 0.15} for i, w in enumerate(words)]), encoding="utf-8")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=16000:cl=mono", "-t", "4",
                        str(self.tmp / "n.wav")], check=True)
        self.mt = load("montage")

    def plan(self, **extra):
        p = {"captures": "captures", "script": "script.md", "words": "words.json", "narration": "n.wav",
             "font_title": FONT, "font_text": FONT, "logo": "logo.png", "out": "out/silent.mp4",
             "size": [1080, 1920], "caption_y": 0.7, "badge": True, "fps": 5,
             "intro": {"title": "Comment postuler\nchez Roogo", "subtitle": "Sur votre téléphone"},
             "outro": {"title": "À vous", "subtitle": "Une ligne\nDeux lignes", "credit": ["Musique : test"]},
             "shots": [[0.0, "s01-blanc", [0.5, 0.5, 1.0]], [3.0, "s02-creme", [0.5, 0.6, 1.1]]]}
        p.update(extra)
        path = self.tmp / "plan.json"
        path.write_text(json.dumps(p, ensure_ascii=False), encoding="utf-8")
        return self.mt.Film(path)

    def test_vertical_render_has_the_right_size(self):
        film = self.plan()
        with redirect_stdout(io.StringIO()):
            film.render()
        info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                          "stream=width,height", "-of", "json", str(film.out)],
                                         capture_output=True, text=True, check=True).stdout)["streams"][0]
        self.assertEqual((info["width"], info["height"]), (1080, 1920))

    def check_caption(self, film, t):
        from PIL import ImageDraw
        im, _ = film.frame(t)
        self.assertEqual(im.size, (film.W, film.H))
        cap = film.caption(t - self.mt.T0)
        self.assertTrue(cap)
        lines, _, (x0, y0, x1, y1) = film.caption_box(ImageDraw.Draw(im), cap)
        self.assertAlmostEqual((y0 + y1) / 2, film.H * film.caption_y, delta=2)
        self.assertLess(y1, film.H * 0.9)                    # never at the bottom edge
        self.assertGreaterEqual(x0, 0); self.assertLessEqual(x1, film.W)
        box = im.getpixel((x0 + 6, (y0 + y1) // 2))
        self.assertGreaterEqual(contrast(box, self.mt.CAPTION_INK), 4.5)
        text_pixels = [im.getpixel((x, y)) for x in range(x0, x1, 2) for y in range(y0 + 22, y1 - 22, 2)]
        self.assertTrue(any(contrast(p, box) >= 4.5 for p in text_pixels))
        return im, lines

    def test_captions_centred_readable_on_white_and_cream(self):
        film = self.plan()
        self.check_caption(film, self.mt.T0 + 2.3)        # white screen
        self.check_caption(film, self.mt.T0 + 3.4)        # cream screen

    def test_long_captions_wrap_inside_the_frame(self):
        film = self.plan(caption_size=70)
        _, lines = self.check_caption(film, self.mt.T0 + 2.3)
        self.assertGreater(len(lines), 1)
        self.assertFalse(any(l.endswith("«") for l in lines))

    def test_badge_on_screen_shots_not_on_cards(self):
        film = self.plan()
        x0, y0, x1, y1 = film.badge_box
        self.assertGreater(x0, film.W * 0.7); self.assertLess(y1, film.H * 0.15)
        centre = ((x0 + x1) // 2, (y0 + y1) // 2)
        ring = (x0 + 6, (y0 + y1) // 2)
        screen = film.frame(self.mt.T0 + 2.3)[0]
        self.assertEqual(screen.getpixel(centre), self.LOGO)
        self.assertTrue(all(v > 240 for v in screen.getpixel(ring)))    # white circle over the gray screen
        for t in (0.5, film.total - 0.5):                                 # title and closing cards
            card = film.frame(t)[0]
            self.assertEqual(card.getpixel(centre), self.mt.CREAM)

    def test_landscape_and_no_badge(self):
        film = self.plan(size=[1920, 1080], badge=False)
        im, _ = self.check_caption(film, self.mt.T0 + 2.3)
        self.assertIsNone(film.badge)
        self.assertEqual(im.size, (1920, 1080))

    def test_captions_cannot_sit_at_the_bottom_edge(self):
        with self.assertRaises(SystemExit):
            self.plan(caption_y=0.95)

    def test_cards_accept_a_manual_line_break(self):
        from PIL import ImageDraw, ImageFont
        d = ImageDraw.Draw(self.Image.new("RGB", (10, 10)))
        self.assertEqual(self.mt.wrap(d, "Une ligne\nDeux lignes", ImageFont.truetype(FONT, 40), 2000),
                         ["Une ligne", "Deux lignes"])


if __name__ == "__main__":
    unittest.main()
