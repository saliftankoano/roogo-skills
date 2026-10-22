#!/usr/bin/env python3
"""Read an approved training script aloud with Cartesia, then write word timestamps.

Usage:
  narration.py script.md --out audio/narration.wav [--voice <id>] [--speed 0.9] [--pause 0.9]
               [--clone] [--test "short text"]
  narration.py --words-only audio/narration.wav --words audio/words.json

The script is Markdown: a "# Title" line, then numbered paragraphs ("1. ...").
The voice reads the paragraphs with the respellings in RESPELL applied; the
captions later come from the unchanged script. Word timestamps come from fal
(ElevenLabs Scribe v2) on the final audio, pauses included, saved as
[{"w", "s", "e"}]; the pace (words a minute, pauses) is printed after.

Pace: --speed is Cartesia's speed (1.0 normal); --pause puts a break of that
many seconds between paragraphs (0 for none). Cloned voices read fast, so a
clone (the default voice, or --clone) defaults to speed 0.9; every voice
defaults to a 0.9 s pause. Target: 130 to 160 words a minute.

Keys: CARTESIA_API_KEY or Keychain item ai.cartesia.api-key (account default);
FAL_KEY or Keychain item roogo-content-key. Keys are never printed.
"""
import argparse, base64, json, os, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

SALIF_FR = "16dba105-0026-4ff7-bf90-12562786a97c"
RESPELL = {"Roogo": "Rohgo", "Burkina Faso": "Bourkina Faso"}
CARTESIA_VERSION = "2025-04-16"
MODEL = "sonic-3.5"
STT = "fal-ai/elevenlabs/speech-to-text/scribe-v2"
STT_USD_PER_MIN = 0.008
CLONES = {SALIF_FR}          # cloned voices read fast: slower default speed
CLONE_SPEED, PAUSE = 0.9, 0.9
TARGET_WPM = (130, 160)


def secret(env, service, account=None):
    """The key from the environment, else the macOS Keychain. Never printed or logged.

    With an account, the item saved under that account is tried first, then any
    item with that service name, so it works whether or not the item has one.
    """
    if os.environ.get(env):
        return os.environ[env]
    tries = ([["-a", account]] if account else []) + [[]]
    for extra in tries:
        cmd = ["security", "find-generic-password", "-s", service, *extra, "-w"]
        try:
            found = subprocess.run(cmd, capture_output=True, text=True).stdout.strip()
        except FileNotFoundError:
            break
        if found:
            return found
    sys.exit(f"Missing key: set {env} or add the Keychain item {service}"
             + (f" (account {account})" if account else "") + ".")


def paragraphs(script_text):
    body = [l for l in script_text.splitlines() if l.strip() and not l.startswith("#")]
    return [re.sub(r"^\d+b?\.\s*", "", l).strip() for l in body]


def for_voice(text):
    for word, spoken in RESPELL.items():
        text = re.sub(rf"\b{re.escape(word)}\b", spoken, text)
    return text


def transcript(paras, pause=PAUSE):
    """Paragraphs as the voice reads them, with a break between paragraphs."""
    gap = f' <break time="{pause:g}s"/> ' if pause and pause > 0 else " "
    return gap.join(for_voice(p) for p in paras)


def request_body(text, voice, speed=1.0):
    body = {
        "model_id": MODEL, "transcript": text, "language": "fr",
        "voice": {"mode": "id", "id": voice},
        "output_format": {"container": "wav", "encoding": "pcm_s16le", "sample_rate": 44100},
    }
    if speed != 1.0:
        body["generation_config"] = {"speed": speed}
    return body


def speak(text, voice, out, speed=1.0):
    body = json.dumps(request_body(text, voice, speed)).encode()
    req = urllib.request.Request("https://api.cartesia.ai/tts/bytes", body, {
        "Cartesia-Version": CARTESIA_VERSION, "Content-Type": "application/json",
        "X-API-Key": secret("CARTESIA_API_KEY", "ai.cartesia.api-key", "default")})
    try:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
        Path(out).write_bytes(urllib.request.urlopen(req, timeout=300).read())
    except urllib.error.HTTPError as e:
        sys.exit(f"Cartesia error {e.code}: {e.read().decode()[:300]}")
    print("saved", out)


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", str(path)], check=True, capture_output=True, text=True).stdout)


def words(audio, out):
    print(f"word timestamps: about ${duration(audio) / 60 * STT_USD_PER_MIN:.3f}")
    uri = "data:audio/wav;base64," + base64.b64encode(Path(audio).read_bytes()).decode()
    req = urllib.request.Request(f"https://fal.run/{STT}", json.dumps({"audio_url": uri, "language_code": "fra"}).encode(),
                                 {"Authorization": f"Key {secret('FAL_KEY', 'roogo-content-key')}", "Content-Type": "application/json"})
    try:
        res = json.load(urllib.request.urlopen(req, timeout=600))
    except urllib.error.HTTPError as e:
        sys.exit(f"fal error {e.code}: {e.read().decode()[:300]}")
    ws = [{"w": w["text"], "s": w["start"], "e": w["end"]} for w in res.get("words", []) if w.get("type") == "word"]
    Path(out).write_text(json.dumps(ws, ensure_ascii=False), encoding="utf-8")
    print(f"saved {out} ({len(ws)} words)\nheard: {res.get('text', '')}")
    print(pace(ws, duration(audio))["report"])
    return ws


def pace(ws, total, min_pause=0.6):
    """Words a minute while speaking, pauses, and timestamp sanity (in order, inside the audio)."""
    problems = []
    if any(w["e"] < w["s"] for w in ws) or any(b["s"] < a["s"] for a, b in zip(ws, ws[1:])):
        problems.append("timestamps out of order")
    if ws and ws[-1]["e"] > total + 0.05:
        problems.append(f"timestamps end at {ws[-1]['e']:.2f} s, after the audio ({total:.2f} s)")
    pauses = [b["s"] - a["e"] for a, b in zip(ws, ws[1:]) if b["s"] - a["e"] >= min_pause]
    wpm = len(ws) / total * 60 if total else 0.0
    lo, hi = TARGET_WPM
    report = (f"pace {wpm:.0f} words a minute over {total:.1f} s, {len(pauses)} pauses of {min_pause} s or more"
              + ("" if lo <= wpm <= hi else f" (target {lo} to {hi})"))
    report += "".join(f"\nWARNING {p}" for p in problems)
    return {"wpm": wpm, "pauses": pauses, "problems": problems, "report": report}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script", nargs="?")
    ap.add_argument("--out", default="audio/narration.wav")
    ap.add_argument("--voice", default=SALIF_FR)
    ap.add_argument("--clone", action="store_true", help="the voice is a clone (slower default speed)")
    ap.add_argument("--speed", type=float, help=f"voice speed, 1.0 normal (default {CLONE_SPEED} for clones, else 1.0)")
    ap.add_argument("--pause", type=float, default=PAUSE, help="seconds of silence between paragraphs (0: none)")
    ap.add_argument("--test", help="read only this text, to check a voice or a spelling by ear")
    ap.add_argument("--words", help="where to write word timestamps (default: next to --out)")
    ap.add_argument("--words-only", help="skip the voice; timestamp this existing audio file")
    a = ap.parse_args()
    if a.speed is None:
        a.speed = CLONE_SPEED if (a.clone or a.voice in CLONES) else 1.0
    if a.words_only:
        return words(a.words_only, a.words or str(Path(a.words_only).with_suffix(".words.json")))
    if a.test:
        return speak(for_voice(a.test), a.voice, a.out, a.speed)
    if not a.script:
        ap.error("give the script file, --test or --words-only")
    print(f"speed {a.speed:g}, pause {a.pause:g} s between paragraphs")
    speak(transcript(paragraphs(Path(a.script).read_text(encoding="utf-8")), a.pause), a.voice, a.out, a.speed)
    words(a.out, a.words or str(Path(a.out).with_suffix(".words.json")))


if __name__ == "__main__":
    main()
