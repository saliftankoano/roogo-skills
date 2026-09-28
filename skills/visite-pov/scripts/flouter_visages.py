"""Blur faces in listing photos before animating them (privacy; always blur children).

Usage: python3 flouter_visages.py faces.json

faces.json (paths relative to the file):
{
  "src": "photos/", "out": "work/",
  "photos": ["1.jpg", "2.jpg", ...],
  "faces": {"7.jpg": [[1026, 850, 1082, 912]], "1.jpg": [[1050, 554, 1068, 572]]}
}
Each box is [x0, y0, x1, y1] in source pixels around one face; find them by
cropping and zooming the photo. Output: p1.png, p2.png, ... in the order of
`photos`, ready for build_pov.py. Large faces get a stronger blur.
"""
import json, os, sys
from PIL import Image, ImageDraw, ImageFilter


def blur_faces(im, boxes):
    for x0, y0, x1, y1 in boxes:
        p = max(8, (x1 - x0) // 3)
        box = (x0 - p, y0 - p, x1 + p, y1 + p)
        radius = 12 if (x1 - x0) > 40 else 6
        region = im.crop(box).filter(ImageFilter.GaussianBlur(radius))
        mask = Image.new("L", region.size, 0)
        ImageDraw.Draw(mask).ellipse([0, 0, *region.size], fill=255)
        im.paste(region, box[:2], mask.filter(ImageFilter.GaussianBlur(3)))
    return im


def main(cfg_path):
    base = os.path.dirname(os.path.abspath(cfg_path))
    cfg = json.load(open(cfg_path))
    src, out = os.path.join(base, cfg["src"]), os.path.join(base, cfg["out"])
    os.makedirs(out, exist_ok=True)
    for i, name in enumerate(cfg["photos"], 1):
        im = Image.open(os.path.join(src, name)).convert("RGB")
        blur_faces(im, cfg.get("faces", {}).get(name, [])).save(os.path.join(out, f"p{i}.png"))
    print(f"saved p1..p{len(cfg['photos'])}.png in {out}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
