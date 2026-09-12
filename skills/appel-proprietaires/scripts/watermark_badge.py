#!/usr/bin/env python3
"""Build the Roogo signature watermark badge: a white circle with the logo,
placed in the top-right corner of a transparent overlay the size of the video.

Every Roogo video carries this badge. Exclude it from any span that already
shows the full centered logo, otherwise it reads as redundant double branding.

Usage:
    python3 watermark_badge.py --logo path/to/logo.png --out watermark.png
    python3 watermark_badge.py --logo logo.png --out wm.png --width 1080 \
        --height 1920 --logo-height 84 --margin 40

Composite in a single ffmpeg pass, excluding the full-logo card spans:

    ffmpeg -y -i in.mp4 -i wm.png -filter_complex \
      "[0:v][1:v]overlay=0:0:enable='lt(t,A)+between(t,B,C)'[v]" \
      -map "[v]" -map 0:a -c:a copy out.mp4

Compute A, B, and C from the real post-transition timeline when the video is an
xfade chain; see xfade_timeline.py.
"""

import argparse

from PIL import Image, ImageDraw

CIRCLE_FILL = (255, 255, 255, 235)


def build_badge(logo_path, out_path, width=1080, height=1920, logo_height=84,
                margin=40, top=90, right_inset=28):
    """Render the transparent badge overlay and return its centre coordinates."""
    radius = logo_height // 2 + 16
    centre_x = width - margin - right_inset - radius
    centre_y = top + radius

    canvas = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)
    draw.ellipse(
        [centre_x - radius, centre_y - radius, centre_x + radius, centre_y + radius],
        fill=CIRCLE_FILL,
    )

    logo = Image.open(logo_path).convert("RGBA")
    logo_width = max(1, round(logo.width * logo_height / logo.height))
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)
    canvas.paste(logo, (centre_x - logo_width // 2, centre_y - logo_height // 2), logo)
    canvas.save(out_path)
    return centre_x, centre_y


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--logo", required=True, help="path to the transparent logo")
    parser.add_argument("--out", required=True, help="output PNG path")
    parser.add_argument("--width", type=int, default=1080)
    parser.add_argument("--height", type=int, default=1920)
    parser.add_argument("--logo-height", type=int, default=84)
    parser.add_argument("--margin", type=int, default=40)
    args = parser.parse_args()

    build_badge(args.logo, args.out, args.width, args.height, args.logo_height,
                args.margin)
    print(f"saved {args.out}")


if __name__ == "__main__":
    main()
