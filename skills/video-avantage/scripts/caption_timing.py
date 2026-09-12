#!/usr/bin/env python3
"""Frame-exact timing for a flattened caption overlay track.

Caption states are rendered as short clips and concatenated into one
transparent track that is overlaid on the video in a single pass. Giving each
clip a duration in seconds makes every clip round independently, and the error
accumulates: one build landed the caption track three seconds out of sync with
a 46 second video after about 114 clips.

The fix is to derive each clip's frame count from successive ROUNDED CUMULATIVE
target frames, so the track's total length always matches the video exactly.

Usage:
    python3 caption_timing.py --fps 30 --boundaries 0.8 1.6 2.45 3.0
    python3 caption_timing.py --fps 30 --boundaries 0.8 1.6 --json
"""

import argparse
import json


def chunk_words(words, max_words=4, breaking=".?!,:;"):
    """Group timed words into caption chunks.

    `words` is a sequence of (start, end, text). A chunk closes at
    sentence-ending punctuation or after `max_words` words, whichever is first.
    """
    chunks, current = [], []
    for word in words:
        current.append(word)
        text = word[2].strip()
        if len(current) >= max_words or (text and text[-1] in breaking):
            chunks.append(current)
            current = []
    if current:
        chunks.append(current)
    return chunks


def clip_frames(boundaries, fps):
    """Frame count per clip from cumulative end times, in seconds.

    `boundaries` are the cumulative end time of each clip, the last one being
    the total track length. The returned counts always sum to
    round(boundaries[-1] * fps), so the flattened track matches the video.
    """
    frames, used = [], 0
    for index, boundary in enumerate(boundaries):
        if index and boundary <= boundaries[index - 1]:
            raise ValueError(f"boundaries must increase: {boundary} at {index}")
        target = round(boundary * fps)
        count = target - used
        if count < 1:
            raise ValueError(
                f"clip {index} would render {count} frames; chunks are too short "
                f"for {fps} fps")
        frames.append(count)
        used = target
    return frames


def total_frames(boundaries, fps):
    """Total frames the flattened track must contain."""
    return round(boundaries[-1] * fps) if boundaries else 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--boundaries", type=float, nargs="+", required=True,
                        help="cumulative end time of each caption clip")
    parser.add_argument("--fps", type=float, default=30.0)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    frames = clip_frames(args.boundaries, args.fps)
    report = {
        "fps": args.fps,
        "clips": len(frames),
        "frames": frames,
        "total_frames": total_frames(args.boundaries, args.fps),
    }
    if args.json:
        print(json.dumps(report, indent=2))
        return
    for index, count in enumerate(frames):
        print(f"  clip {index:<3} {count:>4} frames")
    print(f"total {report['total_frames']} frames over {report['clips']} clips")


if __name__ == "__main__":
    main()
