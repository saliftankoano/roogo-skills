"""POV listing walkthrough renderer (Roogo, 1080x1920, 30 fps).

Real listing photos with a sub-pixel camera drift (push-in + pan), 0.4 s
crossfades, the white-circle Roogo watermark on every photo shot, optional fact
chips, then the pre-rendered HyperFrames outro (crossfaded in and held on its
last frame until the audio ends). Voiceover + music bed, loudness -14 LUFS.
No captions: home tours are captionless by default.

Usage: python3 build_pov.py plan.json

Plan JSON (paths are relative to the plan file):
{
  "vo": "vo.mp3", "music": "bed.mp3", "music_vol": 0.09,
  "outro": "outro.mp4", "endcard_from": 28.6,
  "out": "Roogo - Parcelle 336 m² à vendre Tanghin (POV, 40 millions).mp4",
  "logo": "logo.png", "font": "urbanist.ttf",
  "shots": [{"photo": "p5.png", "start": 0.0, "end": 3.0, "zoom": [1.0, 1.1],
             "pan": [0.2, 0.45], "y": 0.5, "chip": null}, ...]
}
`zoom` is the push-in (start, end); `pan` and `y` are 0..1 positions inside the
available pan range (lower `y` shows more ground; use ~0.8 on sky-heavy fisheye
shots). `chip` is an optional short fact shown as a pill. `endcard_from` is when
the outro starts (usually the start of "Avec Rohgo..."). `logo`/`font` may also
come from ROOGO_LOGO / ROOGO_FONT; `font` is only needed when a shot has a chip.
"""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, XF = 1080, 1920, 30, 0.4
ORANGE, WHITE = (201, 106, 46), (255, 255, 255)
VO_DELAY = 0.4


def font(path, size, weight="Bold"):
    f = ImageFont.truetype(path, size)
    try:
        f.set_variation_by_name(weight)
    except Exception:
        pass
    return f


def watermark(logo_path):
    """White-circle badge with the Roogo logo, top-right (standing rule on every video)."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    logo_h, margin = 84, 40
    r = logo_h // 2 + 16
    cx, cy = W - margin - 28 - r, 90 + r
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 235))
    logo = Image.open(logo_path).convert("RGBA").resize((logo_h, logo_h), Image.LANCZOS)
    img.paste(logo, (cx - logo_h // 2, cy - logo_h // 2), logo)
    return img


def chip(text, font_path):
    """Soft rounded pill with a light shadow, sitting in the vertical center band."""
    f = font(font_path, 58)
    tw = ImageDraw.Draw(Image.new("RGBA", (1, 1))).textlength(text, font=f)
    pw, ph = int(tw + 96), 112
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x, y = (W - pw) // 2, 1180
    d.rounded_rectangle([x + 4, y + 8, x + pw + 4, y + ph + 8], radius=ph // 2, fill=(0, 0, 0, 70))
    d.rounded_rectangle([x, y, x + pw, y + ph], radius=ph // 2, fill=ORANGE + (245,))
    d.text((x + 48, y + 22), text, font=f, fill=WHITE)
    return img


def ease(p):
    return 0.5 - 0.5 * math.cos(math.pi * max(0.0, min(1.0, p)))


def drift_box(src_size, shot, t):
    """Visible source rectangle (left, top, scale) for a shot at time t."""
    p = ease((t - (shot["start"] - XF / 2)) / ((shot["end"] - shot["start"]) + XF))
    sw, sh = src_size
    z0, z1 = shot.get("zoom", [1.0, 1.1])
    x0, x1 = shot.get("pan", [0.5, 0.5])
    s = max(W / sw, H / sh) * (z0 + (z1 - z0) * p)
    vw, vh = W / s, H / s
    cx = vw / 2 + (sw - vw) * (x0 + (x1 - x0) * p)
    cy = vh / 2 + (sh - vh) * shot.get("y", 0.5)
    return cx - vw / 2, cy - vh / 2, s


def drift_frame(src, shot, t):
    left, top, s = drift_box(src.size, shot, t)
    return src.transform((W, H), Image.AFFINE, (1 / s, 0, left, 0, 1 / s, top), Image.BICUBIC)


def duration(path):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                          "-of", "csv=p=0", path]))


def main(plan_path):
    base = os.path.dirname(os.path.abspath(plan_path))
    plan = json.load(open(plan_path))
    rel = lambda p: p if os.path.isabs(p) else os.path.join(base, p)
    logo = rel(plan.get("logo") or os.environ.get("ROOGO_LOGO", "logo.png"))
    font_path = rel(plan.get("font") or os.environ.get("ROOGO_FONT", "urbanist.ttf"))
    vo, outro, music = rel(plan["vo"]), rel(plan["outro"]), rel(plan["music"])
    shots, ec = plan["shots"], plan["endcard_from"]
    total = round(VO_DELAY + duration(vo) + 1.4, 2)

    photos = {s["photo"]: Image.open(rel(s["photo"])).convert("RGB") for s in shots}
    wm = watermark(logo)
    chips = {s["chip"]: chip(s["chip"], font_path) for s in shots if s.get("chip")}

    def render(shot, t):
        f = drift_frame(photos[shot["photo"]], shot, t).convert("RGBA")
        if shot.get("chip"):
            a = min(1.0, max(0.0, (t - shot["start"] - 0.15) / 0.3))   # chip fades in just after the cut
            c = chips[shot["chip"]]
            if a < 1:
                c = c.copy(); c.putalpha(c.getchannel("A").point(lambda v: int(v * a)))
            f.alpha_composite(c)
        f.alpha_composite(wm)
        return f.convert("RGB")

    stem = os.path.splitext(rel(plan["out"]))[0]
    photos_mp4, joined = stem + ".photos.tmp.mp4", stem + ".joined.tmp.mp4"
    enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                            "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
                            "-pix_fmt", "yuv420p", photos_mp4], stdin=subprocess.PIPE)
    for i in range(int((ec + XF / 2) * FPS)):   # photos run until the outro crossfade is complete
        t = i / FPS
        k = next(j for j, s in enumerate(shots) if t < s["end"] or j == len(shots) - 1)
        s = shots[k]
        frame = render(s, t)
        if k + 1 < len(shots) and t > s["end"] - XF / 2:        # crossfade into the next shot
            frame = Image.blend(frame, render(shots[k + 1], t), (t - (s["end"] - XF / 2)) / XF)
        elif k > 0 and t < s["start"] + XF / 2:                  # finish the crossfade from the previous one
            frame = Image.blend(render(shots[k - 1], t), frame, (t - (s["start"] - XF / 2)) / XF)
        enc.stdin.write(frame.tobytes())
    enc.stdin.close(); enc.wait()

    # HyperFrames outro: 5.5 s animation, then held on its final frame until the audio ends.
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", photos_mp4, "-i", outro, "-filter_complex",
                    f"[1:v]fps={FPS},format=yuv420p,tpad=stop_mode=clone:stop_duration={total},setpts=PTS-STARTPTS[o];"
                    f"[0:v]fps={FPS},format=yuv420p[p];"
                    f"[p][o]xfade=transition=fade:duration={XF}:offset={ec - XF / 2},trim=0:{total}[v]",
                    "-map", "[v]", "-c:v", "libx264", "-crf", "18", "-preset", "medium", "-pix_fmt", "yuv420p", joined],
                   check=True)

    out, ms, mv = rel(plan["out"]), int(VO_DELAY * 1000), plan.get("music_vol", 0.09)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", joined, "-i", vo, "-i", music,
                    "-filter_complex",
                    f"[1:a]adelay={ms}|{ms},apad[vo];"
                    f"[2:a]volume={mv},afade=t=in:st=0:d=1.2,afade=t=out:st={total - 1.6}:d=1.6[m];"
                    f"[vo][m]amix=inputs=2:duration=longest:normalize=0,atrim=0:{total},loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                    "-map", "0:v", "-map", "[a]", "-t", str(total), "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-ar", "48000", "-movflags", "+faststart", out], check=True)
    for tmp in (photos_mp4, joined):
        os.remove(tmp)
    print("FINAL", out, total)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
