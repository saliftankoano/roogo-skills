#!/usr/bin/env python3
"""Real timing for an ffmpeg xfade chain.

Chaining N clips with xfade produces a video XFADE * (N - 1) seconds SHORTER
than the sum of the per-clip durations, because every transition consumes one
overlap. Two things depend on that shrinkage and are wrong if computed from the
naive cumulative sum:

* the natural end of the video, which must line up with the narration;
* the on-screen window of any card, used to exclude the watermark over spans
  that already show the full centred logo.

Usage:
    python3 xfade_timeline.py --xfade 0.4 --durations 5.6 3.8 2.6 2.7
    python3 xfade_timeline.py --xfade 0.4 --durations 5.6 3.8 --target 36.2
    python3 xfade_timeline.py --xfade 0.4 --durations 5.6 3.8 --json

Feed --target the exact audio duration, narration lead-in delay included. The
reported extension goes onto the LAST clip's own render duration; never pad the
end of the render with a guessed extra second.
"""

import argparse
import json


def chain_length(durations, xfade):
    """Total length of the rendered chain."""
    if not durations:
        return 0.0
    return sum(durations) - xfade * (len(durations) - 1)


def clip_windows(durations, xfade):
    """Return (visible_from, visible_to) for each clip on the real timeline.

    visible_from is when the clip first appears, the moment its incoming
    transition starts. visible_to is when it has fully left the frame. A clip is
    alone on screen between visible_from + xfade and visible_to - xfade.
    """
    windows = []
    elapsed = 0.0
    total = chain_length(durations, xfade)
    for index, duration in enumerate(durations):
        start = max(0.0, elapsed - xfade * index)
        end = min(total, elapsed + duration - xfade * index)
        windows.append((start, end))
        elapsed += duration
    return windows


def last_clip_extension(durations, xfade, target):
    """Seconds to add to the last clip so the chain ends exactly at target."""
    return target - chain_length(durations, xfade)


def enable_expression(durations, xfade, exclude):
    """ffmpeg overlay `enable` expression that hides the badge over `exclude`.

    `exclude` is the list of clip indices showing a full centred logo.
    """
    total = chain_length(durations, xfade)
    windows = clip_windows(durations, xfade)
    hidden = sorted(windows[index] for index in exclude)
    spans, cursor = [], 0.0
    for start, end in hidden:
        if start > cursor:
            spans.append((cursor, start))
        cursor = max(cursor, end)
    if cursor < total:
        spans.append((cursor, total))
    if not spans:
        return "0"
    terms = []
    for start, end in spans:
        if start <= 0.0:
            terms.append(f"lt(t,{end:.3f})")
        elif end >= total:
            terms.append(f"gte(t,{start:.3f})")
        else:
            terms.append(f"between(t,{start:.3f},{end:.3f})")
    return "+".join(terms)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--durations", type=float, nargs="+", required=True)
    parser.add_argument("--xfade", type=float, default=0.4)
    parser.add_argument("--target", type=float,
                        help="audio duration the chain must match")
    parser.add_argument("--exclude", type=int, nargs="*", default=[],
                        help="clip indices showing a full centred logo")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    windows = clip_windows(args.durations, args.xfade)
    report = {
        "chain_length": round(chain_length(args.durations, args.xfade), 3),
        "naive_sum": round(sum(args.durations), 3),
        "offsets": [round(start, 3) for start, _ in windows[1:]],
        "windows": [[round(start, 3), round(end, 3)] for start, end in windows],
    }
    if args.target is not None:
        report["last_clip_extension"] = round(
            last_clip_extension(args.durations, args.xfade, args.target), 3)
    if args.exclude:
        report["watermark_enable"] = enable_expression(
            args.durations, args.xfade, args.exclude)

    if args.json:
        print(json.dumps(report, indent=2))
        return
    print(f"naive sum      {report['naive_sum']}s")
    print(f"chain length   {report['chain_length']}s")
    for index, (start, end) in enumerate(report["windows"]):
        print(f"  clip {index:<2} visible {start:>7.3f} to {end:>7.3f}")
    if "last_clip_extension" in report:
        print(f"extend last clip by {report['last_clip_extension']}s")
    if "watermark_enable" in report:
        print(f"watermark enable: {report['watermark_enable']}")


if __name__ == "__main__":
    main()
