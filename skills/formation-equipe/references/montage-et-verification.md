# Building and checking

## Layout (30 fps)

All set in the plan file ([montage.example.json](../scripts/montage.example.json));
no project wrapper is needed.

- `size`: 1920x1080 for the desktop app, 1080x1920 for a phone. The capture
  fills the whole frame.
- Captions in a dark brown box with cream text (contrast far above 4.5:1, so
  they read on white and cream screens), wrapped to the frame width, centred
  at `caption_y` (default 0.72 of the height; the script refuses more than
  0.85). Never at the bottom edge. Choose a height where the box does not hide
  the button the narration names.
- The Roogo badge (white circle with the logo) top-right on every screen shot,
  never on the title and closing cards, which already show the full logo.
  `badge_logo` takes another image; `badge: false` only for a non-Roogo video.
- Title card (logo, title, subtitle) for about 4 seconds; narration starts
  2 seconds in. Closing card with the two or three rules and the music credit,
  about 4.5 seconds. Card texts wrap on their own and take "\n" for a line
  break.
- `caption_layout: "band"` with `badge: false` rebuilds the former layout
  (captions in a band under the screen) exactly, for an old video only.

## Camera

- Each shot: a capture, the narration time it starts, and a target framing
  (center x, center y as fractions of the capture, zoom). The camera eases
  from slightly wider than the target to the target while the shot lasts.
- Zoom 1.0 is the full width; 1.5 to 2.2 for a button or a field. Never zoom
  past the capture's sharpness (2.2 on 2x captures).
- Change shot on the narration word that names the next thing. Cross-fade
  8 frames between shots.
- Cards get a slow 3% push-in: no frame may stay still for more than 3 seconds.

## Captions

- From the approved script, aligned to the word timestamps
  (`scripts/aligner.py`), one sentence or part of a sentence at a time, at most
  about 60 characters and 2.7 seconds.
- An opening « stays with the word after it, a closing », colon, question or
  exclamation mark with the word before, so no caption starts or ends on a lone
  quote mark. Check with `montage.py plan.json --captions`.

## Checks before delivery

- `scripts/verifier.py final.mp4`: still-frame scan (fails on any freeze over
  3 s), integrated loudness, duration of audio and video, contact sheet.
- Transcribe the final audio; every word of the script must be there.
- Look at a frame in the middle of every shot: right screen, nothing private,
  caption readable.
- Compress for delivery (H.264, CRF about 23) when the file is over about
  100 MB.
