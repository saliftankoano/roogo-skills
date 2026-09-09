---
name: milestone
description: >-
  Turn an existing static Roogo milestone or celebration graphic, a follower
  count, an anniversary, a download milestone, an award, into a 9:16 video post
  with music. Use for requests such as "we hit [N] followers", "milestone
  post", "animate this celebration graphic", or "turn this poster into a
  video". Always ask the requester to choose the cheap path, a simple zoom that
  costs nothing, or the premium path, generated motion that costs real money
  per clip, before building. Do not use for feature or benefit explainer videos
  or for owner call-out ads.
---

# Milestone

One static milestone graphic in, one scored 9:16 video out. There is no script
to write and no character to cast; the job is bringing one existing image to
life without damaging its typography.

## Always ask first: cheap or premium

The cost gap is roughly forty to fifty times, so the requester chooses
deliberately every time. Never assume.

| | Cheap, zoom | Premium, generated motion |
| --- | --- | --- |
| Technique | Ken Burns zoom on the composited still | Image-to-video, the decorative elements actually move |
| Cost | effectively nothing, ffmpeg only | real money per clip, in the low single dollars for 15 seconds |
| Duration | any length, trivially | chained in 15 second increments |
| When it is worth it | quick turnaround, tight budget, frequent milestone posts | one big milestone worth the spend and the wait |

## Route the work

1. Composite the graphic to fill the vertical canvas. Read
   [references/composite.md](references/composite.md) and use
   [scripts/composite_9x16.py](scripts/composite_9x16.py).
2. For the cheap path, read [references/cheap-zoom.md](references/cheap-zoom.md).
3. For the premium path, read
   [references/premium-motion.md](references/premium-motion.md) and follow it
   step by step, checking frames between generations.
4. For music, the final mix, verification, and archiving, read
   [references/music-and-delivery.md](references/music-and-delivery.md).

## Non-negotiable conventions

- **Never crop real content** to reach 9:16. Extend the canvas behind the
  untouched original instead.
- **Never run a zoom directly on a 1080 pixel source.** Upscale roughly six
  times first, or the motion jitters.
- **Check frames from every generated clip** before chaining the next one or
  committing to a final render. Typography distortion is the main failure mode
  of image-to-video on a graphic with text.
- **State the actual spend to the requester** in the final summary whenever the
  premium path was used. It is real money, not a rounding error.
- French real-title filenames, for example `Roogo - <hook>.mp4`. No em dashes,
  no emoji.
- When revising an existing milestone video, keep the previous version
  alongside with a suffix rather than overwriting it. The cheap version is
  often still wanted elsewhere after a premium one ships.

## Completion checks

Before delivering, verify:

- the composited still contains all of the original graphic, uncropped;
- the output is exactly 1080x1920;
- frames were spot-checked at the start, at every crossfade seam, and at the
  very end, not only at the first frame;
- typography and the logo are sharp and unwarped in every checked frame;
- music fades are present and the final mix passed a loudness pass;
- any shared source asset that was modified in place was backed up first;
- the spend, the technique used, and any gotchas are reported.
