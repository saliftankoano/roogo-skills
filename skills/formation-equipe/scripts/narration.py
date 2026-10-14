#!/usr/bin/env python3
"""Read an approved training script aloud with Cartesia, then write word timestamps.

Usage:
  narration.py script.md --out audio/narration.wav [--voice <id>] [--test "short text"]
  narration.py --words-only audio/narration.wav --words audio/words.json

The script is Markdown: a "# Title" line, then numbered paragraphs ("1. ...").
The voice reads the paragraphs with the respellings in RESPELL applied; the
captions later come from the unchanged script. Word timestamps come from fal
(ElevenLabs Scribe v2), saved as [{"w", "s", "e"}].

Keys: CARTESIA_API_KEY or Keychain item ai.cartesia.api-key (account default);
FAL_KEY or Keychain item roogo-content-key. Keys are never printed.
"""
import argparse, base64, json, re, subprocess, sys, urllib.error, urllib.request
from pathlib import Path

SALIF_FR = "16dba105-0026-4ff7-bf90-12562786a97c"
RESPELL = {"Roogo": "Rohgo", "Burkina Faso": "Bourkina Faso"}
CARTESIA_VERSION = "2025-04-16"
MODEL = "sonic-3.5"
STT = "fal-ai/elevenlabs/speech-to-text/scribe-v2"
STT_USD_PER_MIN = 0.008


def secret(env, service, account=None):
    import os
    if os.environ.get(env):
        return os.environ[env]
    cmd = ["security", "find-generic-password", "-s", service, "-w"]
    if account:
        cmd[3:3] = ["-a", account]
    try:
        return subprocess.run(cmd, check=True, capture_output=True, text=True).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        sys.exit(f"Missing key: set {env} or add the Keychain item {service}.")


def paragraphs(script_text):
    body = [l for l in script_text.splitlines() if l.strip() and not l.startswith("#")]
    return [re.sub(r"^\d+b?\.\s*", "", l).strip() for l in body]


def for_voice(text):
    for word, spoken in RESPELL.items():
        text = re.sub(rf"\b{re.escape(word)}\b", spoken, text)
    return text


def speak(text, voice, out):
    body = json.dumps({
        "model_id": MODEL, "transcript": text, "language": "fr",
        "voice": {"mode": "id", "id": voice},
        "output_format": {"container": "wav", "encoding": "pcm_s16le", "sample_rate": 44100},
    }).encode()
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script", nargs="?")
    ap.add_argument("--out", default="audio/narration.wav")
    ap.add_argument("--voice", default=SALIF_FR)
    ap.add_argument("--test", help="read only this text, to check a voice or a spelling by ear")
    ap.add_argument("--words", help="where to write word timestamps (default: next to --out)")
    ap.add_argument("--words-only", help="skip the voice; timestamp this existing audio file")
    a = ap.parse_args()
    if a.words_only:
        return words(a.words_only, a.words or str(Path(a.words_only).with_suffix(".words.json")))
    if a.test:
        return speak(for_voice(a.test), a.voice, a.out)
    if not a.script:
        ap.error("give the script file, --test or --words-only")
    text = " ".join(for_voice(p) for p in paragraphs(Path(a.script).read_text(encoding="utf-8")))
    speak(text, a.voice, a.out)
    words(a.out, a.words or str(Path(a.out).with_suffix(".words.json")))


if __name__ == "__main__":
    main()
