#!/usr/bin/env python3
"""Build the silent training video: title card, slow camera moves over the
captures with captions, the Roogo badge on every screen shot, closing card.

Usage: montage.py plan.json [--stills 10.5,42] [--captions]
  --stills: save single frames to check; --captions: print the caption phrases.

The plan (see montage.example.json) gives the captures folder, the script and
word timestamps for captions, the narration audio, fonts, logo, card texts and
the shot list. Paths are relative to the plan file. Frames are piped to ffmpeg.

Layout settings (all optional):
  size            [1920, 1080] or [1080, 1920]; the screen fills the frame.
  caption_y       height of the caption box centre, as a fraction of the frame
                  (default 0.72; at most 0.85, never the bottom edge).
  caption_size    caption font size (default 44 landscape, 52 vertical).
  caption_max_chars  longest caption phrase (default 60).
  badge           true (default): the logo badge top-right on screen shots,
                  never on the title and closing cards. badge_logo: another image.
  capture_width   capture pixels shown at zoom 1 (default 2812, or the capture
                  width when smaller).
  fps             frames a second (default 30).
  caption_layout  "band": the former layout (screen above a cream caption band,
                  1920x1080 only). Kept to rebuild old videos; not house style.
Card titles and subtitles take a manual line break ("\\n").
"""
import argparse, json, subprocess, sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
from aligner import NBSP, load_words, phrases  # noqa: E402

CREAM, INK, SUB = (255, 250, 245), (37, 27, 22), (114, 88, 75)
CAPTION_BOX, CAPTION_INK = (37, 27, 22, 235), CREAM   # dark box, cream text: readable on white and cream screens
BADGE_FILL = (255, 255, 255, 235)
T0 = 2.0          # narration starts 2 s into the title card
INTRO_HOLD = 1.8  # title card stays this long after the narration starts
TAIL, OUTRO = 0.6, 4.5
BASE = (0.5, 0.56, 1.0)
MAX_CAPTION_Y = 0.85


def ease(p):
    p = min(max(p, 0.0), 1.0)
    return p * p * (3 - 2 * p)


def seconds(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0",
                                 str(path)], check=True, capture_output=True, text=True).stdout)


def wrap(draw, text, font, width):
    """Lines no wider than width. Splits on plain spaces only, so a quote mark
    joined by a non-breaking space stays with its word; no lone last word."""
    lines, cur = [], ""
    for w in text.replace("\n", " \n ").split(" "):
        if not w:
            continue
        if w == "\n":
            lines.append(cur); cur = ""; continue
        t = f"{cur} {w}".strip()
        if not cur or draw.textlength(t.replace(NBSP, " "), font=font) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    lines.append(cur)
    lines = [l for l in lines if l] or [""]
    if len(lines) >= 2 and " " not in lines[-1] and lines[-2].count(" ") >= 2:
        head, last = lines[-2].rsplit(" ", 1)
        if draw.textlength(f"{last} {lines[-1]}".replace(NBSP, " "), font=font) <= width:
            lines[-2:] = [head, f"{last} {lines[-1]}"]
    return [l.replace(NBSP, " ") for l in lines]


class Film:
    def __init__(self, plan_path):
        self.dir = Path(plan_path).resolve().parent
        p = json.loads(Path(plan_path).read_text(encoding="utf-8"))
        rel = lambda k: self.dir / p[k]
        self.W, self.H = p.get("size", [1920, 1080])
        self.fps = p.get("fps", 30)
        self.vertical = self.H > self.W
        self.band = p.get("caption_layout") == "band"
        if self.band and (self.W, self.H) != (1920, 1080):
            raise SystemExit("caption_layout band is only for 1920x1080")
        self.screen_h = 990 if self.band else self.H
        self.caption_y = p.get("caption_y", 0.72)
        if not 0.3 <= self.caption_y <= MAX_CAPTION_Y:
            raise SystemExit(f"caption_y must be between 0.3 and {MAX_CAPTION_Y}: captions sit toward the centre")
        self.caption_size = p.get("caption_size", 52 if self.vertical else 44)
        self.captures = rel("captures")
        self.shots = [tuple(s) for s in p["shots"]]
        self.nar = seconds(rel("narration"))
        self.total = T0 + self.nar + TAIL + OUTRO
        self.out = rel("out")
        self.title_font, self.text_font = str(rel("font_title")), str(rel("font_text"))
        self.logo = Image.open(rel("logo")).convert("RGBA")
        self.caps = phrases(rel("script").read_text(encoding="utf-8"), load_words(rel("words")),
                            max_chars=p.get("caption_max_chars", 60))
        self.capture_width = p.get("capture_width", 2812)  # zoom 1: capture width shown (crops any side nav)
        self.badge = None
        if p.get("badge", True):
            self.badge = self.make_badge(Image.open(self.dir / p.get("badge_logo", p["logo"])).convert("RGBA"))
        self.intro = self.card(p["intro"]["title"], p["intro"]["subtitle"])
        self.outro = self.card(p["outro"]["title"], p["outro"]["subtitle"], p["outro"].get("credit", []))
        self.cache = {}

    def font(self, path, size):
        return ImageFont.truetype(path, size)

    def centered(self, d, txt, y, font, fill):
        b = d.textbbox((0, 0), txt, font=font)
        d.text(((self.W - (b[2] - b[0])) / 2 - b[0], y), txt, font=font, fill=fill)

    def make_badge(self, logo):
        """White circle with the logo, top-right, on a transparent layer the size of the frame."""
        logo_h, right, top = (84, 68, 60) if self.vertical else (72, 52, 28)
        r = logo_h // 2 + 16
        cx, cy = self.W - right - r, top + r
        layer = Image.new("RGBA", (self.W, self.H), (0, 0, 0, 0))
        ImageDraw.Draw(layer).ellipse([cx - r, cy - r, cx + r, cy + r], fill=BADGE_FILL)
        lg = logo.resize((max(1, round(logo.width * logo_h / logo.height)), logo_h), Image.LANCZOS)
        if lg.width > 2 * r - 12:
            lg.thumbnail((2 * r - 12, logo_h), Image.LANCZOS)
        layer.paste(lg, (cx - lg.width // 2, cy - lg.height // 2), lg)
        self.badge_box = (cx - r, cy - r, cx + r, cy + r)
        return layer

    def card(self, title, sub, credit=()):
        W, H = self.W, self.H
        im = Image.new("RGB", (W, H), CREAM)
        d = ImageDraw.Draw(im)
        if self.band:  # the former layout, unchanged
            lg = self.logo.copy(); lg.thumbnail((380, 380))
            im.paste(lg, ((W - lg.width) // 2, 170), lg)
            self.centered(d, title, 640, self.font(self.title_font, 76), INK)
            self.centered(d, sub, 755, self.font(self.text_font, 40), SUB)
            for i, line in enumerate(credit):
                self.centered(d, line, 935 + 40 * i, self.font(self.text_font, 28), SUB)
            return im
        v = self.vertical
        logo_box, logo_y, ts, ss, cs = (440, 430, 84, 46, 30) if v else (380, 150, 76, 40, 28)
        tf, sf, cf = self.font(self.title_font, ts), self.font(self.text_font, ss), self.font(self.text_font, cs)
        lg = self.logo.copy(); lg.thumbnail((logo_box, logo_box))
        im.paste(lg, ((W - lg.width) // 2, logo_y), lg)
        y = logo_y + lg.height + (60 if v else 50)
        for line in wrap(d, title, tf, W - (140 if v else 300)):
            self.centered(d, line, y, tf, INK); y += int(ts * 1.2)
        y += 30
        for line in wrap(d, sub, sf, W - (160 if v else 300)):
            self.centered(d, line, y, sf, SUB); y += int(ss * 1.3)
        lines = [l for c in credit for l in wrap(d, c, cf, W - 120)]
        y = H - (330 if v else 60 + 40 * len(lines))
        for line in lines:
            self.centered(d, line, y, cf, SUB); y += int(cs * 1.4)
        return im

    def capture(self, name):
        if name not in self.cache:
            self.cache[name] = Image.open(self.captures / f"{name}.png").convert("RGB")
        return self.cache[name]

    def view(self, img, cx, cy, z):
        iw, ih = img.size
        w = min(self.capture_width, iw) / z; h = w * self.screen_h / self.W
        x0 = min(max(cx * iw - w / 2, 0), iw - w); y0 = min(max(cy * ih - h / 2, 0), ih - h)
        s = w / self.W
        return img.transform((self.W, self.screen_h), Image.AFFINE, (s, 0, x0, 0, s, y0), resample=Image.BICUBIC)

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

    def caption_box(self, draw, text):
        """Wrapped lines and the box (x0, y0, x1, y1) centred at caption_y."""
        font = self.font(self.title_font, self.caption_size)
        pad_x, pad_y, lh = 34, 22, int(self.caption_size * 1.3)
        lines = wrap(draw, text, font, self.W - (200 if self.vertical else 360))
        bw = max(draw.textlength(l, font=font) for l in lines) + 2 * pad_x
        bh = lh * len(lines) + 2 * pad_y
        cy = self.H * self.caption_y
        return lines, font, (round((self.W - bw) / 2), round(cy - bh / 2), round((self.W + bw) / 2), round(cy + bh / 2))

    def draw_caption(self, im, text):
        layer = Image.new("RGBA", im.size, (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
        lines, font, (x0, y0, x1, y1) = self.caption_box(d, text)
        d.rounded_rectangle([x0, y0, x1, y1], radius=18, fill=CAPTION_BOX)
        lh = int(self.caption_size * 1.3)
        for i, line in enumerate(lines):
            w = d.textlength(line, font=font)
            d.text(((self.W - w) / 2, y0 + 22 + i * lh - 2), line, font=font, fill=CAPTION_INK)
        im.paste(layer, (0, 0), layer)

    def push_in(self, card, p):
        """Slow 3% push-in so a card is never a still frame."""
        W, H = self.W, self.H
        z = 1 + 0.03 * ease(p); w, h = W / z, H / z
        return card.transform((W, H), Image.AFFINE, (1 / z, 0, (W - w) / 2, 0, 1 / z, (H - h) / 2), resample=Image.BICUBIC)

    def frame(self, t):
        nt = t - T0
        if t < T0 + INTRO_HOLD:
            return self.push_in(self.intro, t / (T0 + INTRO_HOLD)), -1
        if nt >= self.nar + TAIL:
            return self.push_in(self.outro, (nt - self.nar - TAIL) / OUTRO), 10 ** 6
        im = Image.new("RGB", (self.W, self.H), CREAM)
        scr, idx = self.screen(nt); im.paste(scr, (0, 0))
        if self.badge is not None:
            im.paste(self.badge, (0, 0), self.badge)
        c = self.caption(nt)
        if c and self.band:
            d = ImageDraw.Draw(im)
            self.centered(d, c.replace(NBSP, " "), self.screen_h + 18, self.font(self.title_font, 40), INK)
        elif c:
            self.draw_caption(im, c)
        return im, idx

    def render(self):
        self.out.parent.mkdir(parents=True, exist_ok=True)
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
                               "-s", f"{self.W}x{self.H}", "-r", str(self.fps), "-i", "-", "-c:v", "libx264",
                               "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p", str(self.out)],
                              stdin=subprocess.PIPE)
        prev = prev_idx = last = None; fade = 0
        for k in range(int(round(self.total * self.fps))):
            im, idx = self.frame(k / self.fps)
            if prev is not None and idx != prev_idx:
                fade, last = 8, prev
            if fade > 0:                     # 8-frame cross-fade between shots
                im = Image.blend(last, im, 1 - fade / 9); fade -= 1
            ff.stdin.write(im.tobytes()); prev, prev_idx = im, idx
        ff.stdin.close(); ff.wait()
        print(f"saved {self.out} ({self.total:.2f} s, {self.W}x{self.H})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--stills", help="comma-separated times in seconds")
    ap.add_argument("--captions", action="store_true", help="print the caption phrases and exit")
    a = ap.parse_args()
    film = Film(a.plan)
    if a.captions:
        for t, s, e in film.caps:
            print(f"{s:6.2f} {e:6.2f} {t.replace(NBSP, ' ')}")
    elif a.stills:
        for t in (float(x) for x in a.stills.split(",")):
            path = film.out.parent / f"still-{t:06.2f}.jpg"
            film.frame(t)[0].save(path, quality=85); print("saved", path)
    else:
        film.render()
