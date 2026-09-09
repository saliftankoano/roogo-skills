# Video avantage

Turn one Roogo feature, differentiator, or business-model benefit into a
narrated vertical explainer video, built entirely from generated actors,
comparison cards, and text cards. No property photography required.

The name is the French phrase the team uses for this format, a benefit video.

## What it is for

Roogo has something to explain or dramatise, a commission model, voice notes,
3D tours, and **no real listing photography or footage exists to build from**.
The video is carried by generated actors, narration, and on-screen data.

Use a different tool when:

- a specific renter or buyer demand exists and the ad should make owners call;
- real photographs of a published listing exist and the goal is to showcase
  that property;
- an existing celebration graphic simply needs to be animated.

## Install

Copy this directory into your configured Codex user skills directory, commonly
`~/.codex/skills/video-avantage`. If it is already there, compare and back up
the existing copy before replacing it.

## Requirements

- A media generation, text-to-speech, dialogue, and transcription toolchain the
  agent can call, already authenticated, with balance headroom for character
  clips. Voices run on ElevenLabs by default, or on Cartesia when you ask for
  it; the package documents directing both.
- `ffmpeg` and `ffprobe`.
- Python with `Pillow`.
- Your own brand assets: the brand fonts, the transparent logo, and a
  rights-cleared instrumental library. None are bundled here, and this package
  grants no rights to them.

No local transcription tool is needed for this format; word timestamps come
from transcribing the synthetic narration track.

## Example prompt

```text
$video-avantage Make a 45 second French vertical video explaining why our
commission is transparent compared with a classic broker. Use the approved
numbers I gave you, do not derive new ones. Write the script first and stop
there; I want to approve it and the music before any clip is generated. Tell me
the expected spend before you start generating.
```

## What you get

1. A script in the cold-open structure, approved before any generation.
2. Narration in the Roogo narrator voice, on your chosen provider, with
   character lines in their own voices where the story needs them.
3. Generated character clips, comparison cards, and text cards.
4. Hand-rolled captions positioned per segment, clear of on-screen graphics.
5. A mixed, loudness-normalised, watermarked vertical video with a real French
   filename, plus a statement of the actual generation spend.

## Review checkpoints

You approve the script, the numbers, and the music before anything is
generated. For anything that depends on how it sounds, the agent sends a short
test clip for you to confirm by ear before building the full video. The agent
verifies the render itself: no silent beat, no caption collision, no
lip-sync mismatch, matching audio and video durations, and a frame-exact
caption track.

## Limits

- This package is instructions and helpers, not a rendering service. It
  provisions no credentials, fonts, logos, music, or footage.
- The voice IDs it names are configuration, not permission to use those voices.
- A change of voice or provider invalidates any footage whose mouth was animated
  to the old take; that shot is regenerated as a reaction clip.
- Character clips cost real money per generation. Revisions that change only
  audio, text, or captions reuse existing footage instead of regenerating it.
- Numbers on screen come from the approved reference model, never re-derived
  for a new creative.

## How it is organised

- [SKILL.md](SKILL.md) is the agent-facing contract.
- [Brief and story structure](references/brief-and-structure.md)
- [Brand system](references/brand-system.md)
- [Narration and character voice](references/narration-and-voice.md), and the
  provider references for [ElevenLabs](references/elevenlabs.md) and
  [Cartesia](references/cartesia.md)
- [Comparison and explainer cards](references/comparison-cards.md)
- [Captions](references/captions.md)
- [Audio mixing, cost, and revisions](references/audio-and-revisions.md)
- Helpers: [watermark_badge.py](scripts/watermark_badge.py) and
  [caption_timing.py](scripts/caption_timing.py)
