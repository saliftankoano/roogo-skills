#!/usr/bin/env python3
"""Build the silent training video: title card, slow camera moves over the
captures with captions under the screen, closing card.

Usage: montage.py plan.json [--stills 10.5,42]   (stills: save single frames to check)

The plan (see montage.example.json) gives the captures folder, the script and
word timestamps for captions, the narration audio, fonts, logo, card texts and
the shot list. Paths are relative to the plan file. Frames are piped to ffmpeg.
"""
import argparse, json, subprocess, sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
from aligner import load_words, phrases  # noqa: E402

FPS, W, H, SCREEN_H = 30, 1920, 1080, 990
CREAM, INK, SUB = (255, 250, 245), (37, 27, 22), (114, 88, 75)
T0 = 2.0          # narration starts 2 s into the title card
INTRO_HOLD = 1.8  # title card stays this long after the narration starts
TAIL, OUTRO = 0.6, 4.5
BASE = (0.5, 0.56, 1.0)


def ease(p):
    p = min(max(p, 0.0), 1.0)
    return p * p * (3 - 2 * p)


def seconds(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(path)], check=True, capture_output=True, text=True).stdout)


class Film:
    def __init__(self, plan_path):
        self.dir = Path(plan_path).resolve().parent
        p = json.loads(Path(plan_path).read_text(encoding="utf-8"))
        rel = lambda k: self.dir / p[k]
        self.captures = rel("captures")
        self.shots = [tuple(s) for s in p["shots"]]
        self.nar = seconds(rel("narration"))
        self.total = T0 + self.nar + TAIL + OUTRO
        self.out = rel("out")
        self.title_font, self.text_font = str(rel("font_title")), str(rel("font_text"))
        self.logo = Image.open(rel("logo")).convert("RGBA")
        self.caps = phrases(rel("script").read_text(encoding="utf-8"), load_words(rel("words")))
        self.capture_width = p.get("capture_width", 2812)  # zoom 1: capture width shown (crops any side nav)
        self.intro = self.card(p["intro"]["title"], p["intro"]["subtitle"])
        self.outro = self.card(p["outro"]["title"], p["outro"]["subtitle"], p["outro"].get("credit", []))
        self.cache = {}

    def centered(self, d, txt, y, font, fill):
        b = d.textbbox((0, 0), txt, font=font)
        d.text(((W - (b[2] - b[0])) / 2 - b[0], y), txt, font=font, fill=fill)

    def card(self, title, sub, credit=()):
        im = Image.new("RGB", (W, H), CREAM)
        lg = self.logo.copy(); lg.thumbnail((380, 380))
        im.paste(lg, ((W - lg.width) // 2, 170), lg)
        d = ImageDraw.Draw(im)
        self.centered(d, title, 640, ImageFont.truetype(self.title_font, 76), INK)
        self.centered(d, sub, 755, ImageFont.truetype(self.text_font, 40), SUB)
        for i, line in enumerate(credit):
            self.centered(d, line, 935 + 40 * i, ImageFont.truetype(self.text_font, 28), SUB)
        return im

    def capture(self, name):
        if name not in self.cache:
            self.cache[name] = Image.open(self.captures / f"{name}.png").convert("RGB")
        return self.cache[name]

    def view(self, img, cx, cy, z):
        w = self.capture_width / z; h = w * SCREEN_H / W; iw, ih = img.size
        x0 = min(max(cx * iw - w / 2, 0), iw - w); y0 = min(max(cy * ih - h / 2, 0), ih - h)
        s = w / W
        return img.transform((W, SCREEN_H), Image.AFFINE, (s, 0, x0, 0, s, y0), resample=Image.BICUBIC)

    def screen(self, nt):
        idx = max([i for i, s in enumerate(self.shots) if s[0] <= nt] or [0])
        start, name, target = self.shots[idx]
        end = self.shots[idx + 1][0] if idx + 1 < len(self.shots) else self.nar + TAIL
        wide = tuple(b + (a - b) * 0.45 for a, b in zip(target, BASE))  # start a little wider
        p = ease((nt - start) / max(end - start, 0.01))
        return self.view(self.capture(name), *[a + (b - a) * p for a, b in zip(wide, target)]), idx

    def caption(self, nt):
        cur = None
        for i, (txt, s, e) in enumerate(self.caps):
            nxt = self.caps[i + 1][1] if i + 1 < len(self.caps) else e + 0.4
            if s - 0.05 <= nt < nxt:
                cur = txt
        return cur

    @staticmethod
    def push_in(card, p):
        """Slow 3% push-in so a card is never a still frame."""
        z = 1 + 0.03 * ease(p); w, h = W / z, H / z
        return card.transform((W, H), Image.AFFINE, (1 / z, 0, (W - w) / 2, 0, 1 / z, (H - h) / 2), resample=Image.BICUBIC)

    def frame(self, t):
        nt = t - T0
        if t < T0 + INTRO_HOLD:
            return self.push_in(self.intro, t / (T0 + INTRO_HOLD)), -1
        if nt >= self.nar + TAIL:
            return self.push_in(self.outro, (nt - self.nar - TAIL) / OUTRO), 10 ** 6
        im = Image.new("RGB", (W, H), CREAM)
        scr, idx = self.screen(nt); im.paste(scr, (0, 0))
        c = self.caption(nt)
        if c:
            self.centered(ImageDraw.Draw(im), c, SCREEN_H + 18, ImageFont.truetype(self.title_font, 40), INK)
        return im, idx

    def render(self):
        self.out.parent.mkdir(parents=True, exist_ok=True)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                               "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium",
                               "-crf", "18", "-pix_fmt", "yuv420p", str(self.out)], stdin=subprocess.PIPE)
        prev = prev_idx = last = None; fade = 0
        for k in range(int(round(self.total * FPS))):
            im, idx = self.frame(k / FPS)
            if prev is not None and idx != prev_idx:
                fade, last = 8, prev
            if fade > 0:                     # 8-frame cross-fade between shots
                im = Image.blend(last, im, 1 - fade / 9); fade -= 1
            ff.stdin.write(im.tobytes()); prev, prev_idx = im, idx
        ff.stdin.close(); ff.wait()
        print(f"saved {self.out} ({self.total:.2f} s)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--stills", help="comma-separated times in seconds")
    a = ap.parse_args()
    film = Film(a.plan)
    if a.stills:
        for t in (float(x) for x in a.stills.split(",")):
            path = film.out.parent / f"still-{t:06.2f}.jpg"
            film.frame(t)[0].save(path, quality=85); print("saved", path)
    else:
        film.render()
