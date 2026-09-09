#!/usr/bin/env python3
"""Measure narration or master audio and enforce explicit loudness bounds."""

from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path
from typing import Any


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=False, capture_output=True, text=True)


def probe(path: Path) -> dict[str, Any]:
    result = run([
        "ffprobe",
        "-v", "error",
        "-select_streams", "a:0",
        "-show_entries", "stream=codec_name,sample_rate,channels:format=duration",
        "-of", "json",
        str(path),
    ])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffprobe failed")

    payload = json.loads(result.stdout)
    streams = payload.get("streams", [])
    if not streams:
        raise RuntimeError("no audio stream")

    duration = float(payload.get("format", {}).get("duration", 0))
    if not math.isfinite(duration) or duration <= 0:
        raise RuntimeError("audio duration is not positive")

    stream = streams[0]
    return {
        "codec": stream.get("codec_name"),
        "sampleRate": int(stream["sample_rate"]) if stream.get("sample_rate") else None,
        "channels": stream.get("channels"),
        "durationSeconds": round(duration, 3),
    }


def loudness(path: Path) -> dict[str, float | str]:
    result = run([
        "ffmpeg",
        "-hide_banner",
        "-nostats",
        "-i", str(path),
        "-map", "0:a:0",
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null",
        "-",
    ])
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffmpeg loudness analysis failed")

    matches = re.findall(r"\{\s*\"input_i\".*?\}", result.stderr, flags=re.DOTALL)
    if not matches:
        raise RuntimeError("ffmpeg did not return loudness measurements")

    payload = json.loads(matches[-1])
    return {
        "integratedLufs": float(payload["input_i"]),
        "truePeakDbtp": float(payload["input_tp"]),
        "loudnessRangeLu": float(payload["input_lra"]),
        "normalizationType": payload["normalization_type"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Probe audio and fail files outside an explicit LUFS/true-peak window."
    )
    parser.add_argument("files", nargs="+", type=Path)
    parser.add_argument("--min-lufs", type=float, default=-24.0)
    parser.add_argument("--max-lufs", type=float, default=-12.0)
    parser.add_argument("--max-true-peak", type=float, default=-1.0)
    args = parser.parse_args()
    if not all(math.isfinite(value) for value in
               (args.min_lufs, args.max_lufs, args.max_true_peak)):
        parser.error("loudness limits must be finite")
    if args.min_lufs > args.max_lufs:
        parser.error("min-lufs must not exceed max-lufs")

    reports: list[dict[str, Any]] = []
    failed = False

    for path in args.files:
        report: dict[str, Any] = {"file": str(path), "passed": False, "issues": []}
        try:
            if not path.is_file():
                raise RuntimeError("file does not exist")

            report.update(probe(path))
            report.update(loudness(path))

            # Silence commonly measures -inf. Reject undefined measurements while
            # preserving a strict JSON report for downstream release tooling.
            for field in ("integratedLufs", "truePeakDbtp", "loudnessRangeLu"):
                if not math.isfinite(report[field]):
                    report[field] = None
                    report["issues"].append(f"{field} is not finite; audio may be silent or unmeasurable")

            integrated = report["integratedLufs"]
            peak = report["truePeakDbtp"]
            if integrated is not None and (integrated < args.min_lufs or integrated > args.max_lufs):
                report["issues"].append(
                    f"integrated loudness {integrated:.2f} LUFS is outside "
                    f"[{args.min_lufs:.2f}, {args.max_lufs:.2f}]"
                )
            if peak is not None and peak > args.max_true_peak:
                report["issues"].append(
                    f"true peak {peak:.2f} dBTP exceeds {args.max_true_peak:.2f} dBTP"
                )

            report["passed"] = not report["issues"]
        except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as error:
            report["issues"].append(str(error))

        failed = failed or not report["passed"]
        reports.append(report)

    print(json.dumps({"files": reports}, indent=2, allow_nan=False))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
