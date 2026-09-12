# Composite the graphic to 9:16

Milestone graphics are almost never native 9:16; they are usually 4:5 or
square. Cropping to fit loses the graphic's own top and bottom elements.

Instead, extend the canvas: a blurred, slightly darkened, edge-to-edge copy of
the same image sits behind the untouched original, centred.

```text
[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
     gblur=sigma=45,eq=brightness=-0.06[bg];
[0:v]scale=1080:-1:force_original_aspect_ratio=decrease,setsar=1[fg];
[bg][fg]overlay=x=(W-w)/2:y=(H-h)/2[outv]
```

This is the same contain-and-blur technique used for landscape property photos
elsewhere; it works for any aspect-ratio mismatch, not only landscape sources.

Save the result as a still PNG. Both paths build from that same file, so a
graphic composited once can be rendered cheaply now and premium later without
redoing this step.

[scripts/composite_9x16.py](../scripts/composite_9x16.py) runs it.
