#!/usr/bin/env python3
"""Check a finished training video before delivery.

Usage: verifier.py final.mp4 [--max-still 3] [--sheet contact.jpg]

Fails (exit 1) on any still image longer than --max-still seconds, or when the
audio and video lengths differ by more than 0.5 s. Prints integrated loudness
(target about -16 LUFS) and writes a contact sheet of 12 frames.
"""
import argparse, json, re, subprocess, sys


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)


def stream_seconds(path, kind):
    out = run(["ffprobe", "-v", "error", "-select_streams", kind, "-show_entries", "stream=duration",
               "-of", "json", path]).stdout
    streams = json.loads(out or "{}").get("streams", [])
    return float(streams[0]["duration"]) if streams and "duration" in streams[0] else None


def stills(path, max_still):
    """Spans where the picture does not change, from ffmpeg's freezedetect."""
    log = run(["ffmpeg", "-hide_banner", "-i", path, "-vf", f"freezedetect=n=0.0015:d={max_still}",
               "-map", "0:v", "-f", "null", "-"]).stderr
    starts = [float(x) for x in re.findall(r"freeze_start: ([\d.]+)", log)]
    ends = [float(x) for x in re.findall(r"freeze_end: ([\d.]+)", log)]
    ends += [None] * (len(starts) - len(ends))
    return list(zip(starts, ends))


def loudness(path):
    log = run(["ffmpeg", "-hide_banner", "-i", path, "-af", "ebur128", "-f", "null", "-"]).stderr
    m = re.findall(r"I:\s+(-?[\d.]+) LUFS", log)
    return float(m[-1]) if m else None


def sheet(path, out, total):
    step = max(total / 12, 0.1)
    run(["ffmpeg", "-y", "-loglevel", "error", "-i", path, "-vf", f"fps=1/{step:.3f},scale=480:-1,tile=4x3",
         "-frames:v", "1", out])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video")
    ap.add_argument("--max-still", type=float, default=3.0)
    ap.add_argument("--sheet", default=None)
    a = ap.parse_args()
    v, au = stream_seconds(a.video, "v:0"), stream_seconds(a.video, "a:0")
    problems = []
    print(f"video {v} s, audio {au} s")
    if au is None:
        problems.append("no audio track")
    elif v is not None and abs(v - au) > 0.5:
        problems.append(f"audio and video differ by {abs(v - au):.2f} s")
    for s, e in stills(a.video, a.max_still):
        problems.append(f"still image from {s:.2f} s to {e if e is not None else 'the end'}")
    lufs = loudness(a.video) if au else None
    if lufs is not None:
        print(f"loudness {lufs:.1f} LUFS (target about -16)")
    out = a.sheet or re.sub(r"\.[^.]+$", "", a.video) + "-planche.jpg"
    sheet(a.video, out, v or 1)
    print("contact sheet", out)
    for p in problems:
        print("FAIL", p)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
