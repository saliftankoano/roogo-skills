# Building and checking

## Layout (1920x1080, 30 fps)

- Screen area on top (1920x990), a cream caption band under it. Captions never
  cover the app.
- Title card (logo, title, one-line subtitle) for about 4 seconds; narration
  starts 2 seconds in.
- Closing card with the two or three rules and the music credit, about 4.5
  seconds.

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

## Checks before delivery

- `scripts/verifier.py final.mp4`: still-frame scan (fails on any freeze over
  3 s), integrated loudness, duration of audio and video, contact sheet.
- Transcribe the final audio; every word of the script must be there.
- Look at a frame in the middle of every shot: right screen, nothing private,
  caption readable.
- Compress for delivery (H.264, CRF about 23) when the file is over about
  100 MB.
