# Carousel video

The default deliverable: roughly 35 to 40 seconds, **1080x1920, true 9:16**,
one image per spoken idea, cut on the narrator's words.

## Canvas

1080x1920 is mandatory. The static poster's 4:5 ratio letterboxes on vertical
video surfaces. Three videos were once built at 1080x1350 and had to be rebuilt.

Generate source photographs directly at a 9:16 aspect ratio. Because a
1024x1536 source is proportionally wider than a 1080x1920 target, scale by
**height** first (`scale=-1:1920`) and crop the width to 1080. This is the
opposite of the older 4:5 crop math. Larger height targets, `scale=-1:2400` and
beyond, give tighter push-in variants of the same photograph.

## Word timing

Get word timestamps from a local transcription of the narration. When the
transcriber mishears place names or numbers, which is common, do not fight it
word by word. Anchor on its **segment-level** timestamps, which stay reliable
even when the words are garbled, substitute the known-correct script text for
each segment, assert that the segment count and order match, and distribute
those words evenly across each segment window.

## Slides

One image per criterion: exterior, empty living room, kitchen, shower,
courtyard. All empty and modest. Add PIL cards on the flat terracotta field for
the budget and the call to action.

**Pacing:** no slide holds longer than about five seconds. A ten-second opening
kills retention. Cover a long hook with two or three cuts of the same subject,
wide, then another angle, then a tight push-in, which reads as three shots.

**Anti-shake:** `zoompan` jitters when the input canvas is small. Upscale to
roughly six times the output first, `scale=6480:11520` for 1080x1920, so
rounding is sub-pixel. Never run `zoompan` directly on a 1080-pixel source.

## Chaining and timing math

Clips are chained with `xfade`, fade duration around 0.4 seconds, each offset
placed about 0.2 seconds before the word boundary it cuts on.

Chaining N clips shrinks the output by `XFADE * (N - 1)` seconds below the sum
of the intended clip durations, because every transition consumes one overlap.
Do not pad the end with a guessed extra second. Extend the **last** clip's own
render duration by exactly that amount plus the narration's lead-in delay, so
the video ends when the audio does. Probe the finished file and confirm the
video and audio stream durations agree.

The same shrinkage moves every card's real on-screen window. A card's true
start is `sum(durations[:k]) - XFADE * (k - 1)`, not the naive cumulative sum,
which drifts further wrong with every prior transition.

[scripts/xfade_timeline.py](../scripts/xfade_timeline.py) computes both: the
real start and end of every clip, the natural chain length, and the extension
the last clip needs to match a target audio duration.

## Burned-in captions

Burned-in captions are mandatory for vertical social video.

- Build an ASS track from the corrected word timings.
- Break chunks at punctuation, and **width-check each chunk in the real font**
  against the usable canvas width rather than capping at a blind word count.
  Long place names overflow a four-word cap.
- Urbanist Bold near 78 pixels on a 1920-tall canvas, white fill with a navy
  outline, bottom-center with a bottom margin around 220 to 360 so the
  platform's own interface stays clear.
- The `[Events]` format header must list all ten fields, including `Name`:
  `Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text`.
  Dropping `Name` leaks a leading comma into every rendered caption line, which
  is easy to miss when checking a single frame.

## Audio mix

Measure, do not guess. Run a volume detection pass on the raw narration and on
the music. Target a narration peak near -3 dB, boosting the generated track as
needed, and place the music roughly 10 dB under the narration mean. Fade the
music in about 1.5 seconds before speech starts and out at the end. Verify the
mixed file with a second volume detection pass.

Choose music from a rights-cleared instrumental library. Any commercial track
needs a rights check before it reaches a published ad.

## Watermark

Composite the white-circle badge in one overlay pass and exclude the spans that
already show a full centered logo, using an `enable` expression built from the
**real post-transition** card windows. See
[scripts/watermark_badge.py](../scripts/watermark_badge.py).

## Before delivery

Spot-check frames at the start, at each transition, over each card, and at the
very end. One checked frame is not evidence that a chained render is correct.
