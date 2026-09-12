# Milestone

Turn an existing static celebration graphic into a scored 9:16 video post:
a follower count, an anniversary, a download milestone, an award, a press
mention.

This is a much smaller job than the other Roogo video skills. There is no
script to write and no character to cast. The whole craft is bringing one
existing image to life without damaging its typography.

## What it is for

A static milestone graphic already exists and the ask is to post it as a video,
usually with music.

Use a different tool when the video needs to explain a feature or a benefit, or
when a specific renter or buyer demand should make owners call.

## Cheap or premium: you choose, every time

| | Cheap, zoom | Premium, generated motion |
| --- | --- | --- |
| Technique | Ken Burns zoom on the composited still | image-to-video, the confetti and sparkles actually move |
| Cost | effectively nothing | real money per clip, low single dollars for 15 seconds |
| Duration | any length | chained in 15 second increments |
| Best for | quick turnaround, frequent posts | one big milestone worth the spend |

The gap is roughly forty to fifty times, so the agent always asks rather than
assuming. Say which path you want in the prompt to skip the question.

## Install

Copy this directory into your configured Codex user skills directory, commonly
`~/.codex/skills/milestone`. If it is already there, compare and back up the
existing copy before replacing it.

## Requirements

- `ffmpeg` and `ffprobe`. The cheap path needs nothing else.
- For the premium path, an authenticated image-to-video toolchain with balance
  headroom.
- Python 3 for the compositing helper.
- Your own graphic and a rights-cleared music track. Neither is bundled here.

## Example prompt

```text
$milestone We hit 1000 followers on Facebook. Here is the graphic. Cheap path
please, 30 seconds, use the track I am attaching and cut the first 6 seconds of
it. Tell me before you modify that file.
```

## What you get

1. The graphic composited to fill 1080x1920 with none of it cropped away.
2. A rendered video on the path you chose.
3. Music faded in and out, with a final loudness pass.
4. Frames spot-checked across the whole timeline, not just the first one.
5. The technique used and, on the premium path, the actual spend.

## Review checkpoints

You choose the path and, on the premium path, approve the spend before a second
clip is generated. The agent checks typography and logo sharpness on frames
from every generated clip, and checks the crossfade seam on every build rather
than assuming it is clean.

## Limits

- This package is instructions and helpers, not a rendering service.
- It does not design the graphic; it animates one that already exists.
- It adds music, not narration. A milestone that needs a spoken line is an
  explainer video and belongs to a different skill.
- Generated motion costs real money per clip and cannot exceed 15 seconds per
  generation; longer videos are chained from the previous clip's last frame.
- A shared music file is only ever modified in place on an explicit
  instruction, and is backed up first.
- A revision keeps the previous version alongside rather than overwriting it.

## How it is organised

- [SKILL.md](SKILL.md) is the agent-facing contract.
- [Composite the graphic to 9:16](references/composite.md)
- [Cheap path: Ken Burns zoom](references/cheap-zoom.md)
- [Premium path: generated motion](references/premium-motion.md)
- [Music, mix, verification, and delivery](references/music-and-delivery.md)
- Helper: [composite_9x16.py](scripts/composite_9x16.py)
