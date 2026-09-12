#!/usr/bin/env python3
"""Fill a 9:16 canvas from a graphic that is not already 9:16.

Milestone graphics are usually 4:5 or square. Cropping them to fit loses real
content, so a blurred, slightly darkened, edge-to-edge copy of the same image
is placed behind the untouched original, centred.

Usage:
    python3 composite_9x16.py input.png output.png
    python3 composite_9x16.py input.png output.png --width 1080 --height 1920
"""

import argparse
import subprocess


def composite_filter(width, height, blur_sigma, darken):
    return (
        f"[0:v]scale={width}:{height}:force_original_aspect_ratio=increase,"
        f"crop={width}:{height},gblur=sigma={blur_sigma},eq=brightness={darken}[bg];"
        f"[0:v]scale={width}:-1:force_original_aspect_ratio=decrease,setsar=1[fg];"
        f"[bg][fg]overlay=x=(W-w)/2:y=(H-h)/2[outv]"
    )


def composite_9x16(src, out_path, width=1080, height=1920, blur_sigma=45,
                   darken=-0.06):
    subprocess.run(
        ["ffmpeg", "-y", "-i", src,
         "-filter_complex", composite_filter(width, height, blur_sigma, darken),
         "-map", "[outv]", "-frames:v", "1", out_path, "-loglevel", "error"],
        check=True,
    )
    return out_path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("src", help="the milestone graphic")
    parser.add_argument("out", help="output still PNG")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--blur-sigma", type=int, default=45)
    parser.add_argument("--darken", type=float, default=-0.06)
    args = parser.parse_args()

    composite_9x16(args.src, args.out, args.width, args.height, args.blur_sigma,
                   args.darken)
    print(f"saved {args.out}")


if __name__ == "__main__":
    main()
