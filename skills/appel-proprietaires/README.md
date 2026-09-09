# Appel a proprietaires

Turn one renter or buyer demand into a ready-to-post owner call-out ad bundle:
a narrated vertical carousel video with burned-in French captions, plus the
social copy the team pastes when publishing.

The name is the French phrase the team uses for this format, a call to property
owners. One ad states one demand.

## What it is for

A client is searching for a specific property, in a specific zone, at a
specific budget, and the goal is to make owners of matching properties call.
The ad calls owners in; it never advertises an available listing.

Use a different tool when:

- the request is about explaining an app feature, a differentiator, or a
  business-model benefit;
- the request is to animate an existing celebration graphic;
- real photographs of an already published listing exist and the goal is to
  showcase that property.

## Install

Copy this directory into your configured Codex user skills directory, commonly
`~/.codex/skills/appel-proprietaires`. If it is already there, compare and back
up the existing copy before replacing it.

## Requirements

- A media generation and text-to-speech toolchain the agent can call, already
  authenticated. Narration runs on ElevenLabs by default, or on Cartesia when
  you ask for it; the package documents both.
- `ffmpeg` and `ffprobe`.
- Python with `Pillow` for on-screen text and cards, and `python-docx` for the
  caption document.
- A local transcription tool for word timestamps.
- Your own brand assets: the variable brand font, the transparent logo, and a
  rights-cleared instrumental music library. None of these are bundled here,
  and this package grants no rights to them.

If narration authentication fails, or the configured voice is unavailable,
stop and ask. Do not substitute another voice or another image model silently.

## Example prompt

```text
$appel-proprietaires A client is looking for a shop on the Nora road, between
the grocery and the courthouse, to sell cosmetics, budget 50 000 FCFA a month,
urgent. Contact number in the ad: the campaign number I gave you. Start with
the script and the music pick only, no generation yet. Confirm the spelling of
every place name with me before anything is rendered.
```

## What you get

1. A script, approved by you before anything is generated.
2. A music selection from a rights-cleared library, approved with the script.
3. Narration in the Roogo narrator voice, on your chosen provider, with the
   phone number spoken as number pairs and verified by re-transcription.
4. A 1080x1920 carousel video, roughly 35 to 40 seconds, with burned-in
   captions, brand cards, a measured audio mix, and the corner watermark.
5. A French caption document covering the video title, the short-form caption,
   the page post, a group repost with a share ask, and publishing notes.

The 4:5 static poster is a separate format, produced only when you ask for it.

## Review checkpoints

You are asked to approve the script and the music before any paid generation,
and to confirm place-name spelling before anything is published. The agent
verifies the render itself: the canvas is exactly 1080x1920, video and audio
durations agree, the spoken number reads back as pairs, captions fit the frame
in the real font, and the watermark is absent over full-logo cards.

## Limits

- This package is instructions and helpers, not a rendering service. It
  provisions no credentials, fonts, logos, music, or footage.
- The voice IDs it names are configuration, not permission to use those voices.
- A reusable closing clip belongs to the voice that produced it. Changing
  provider mid-campaign means regenerating it, not mixing two voices in one ad.
- Generated housing imagery must match the stated budget and must never reuse
  furnished listing photography for a modest unfurnished ask.
- No guarantee of rental may be promised in the copy.

## How it is organised

- [SKILL.md](SKILL.md) is the agent-facing contract.
- [Demand brief and script](references/brief-and-script.md)
- [Brand system](references/brand-system.md)
- [Narration](references/narration.md), and the provider references for
  [ElevenLabs](references/elevenlabs.md) and [Cartesia](references/cartesia.md)
- [Carousel video](references/carousel-video.md)
- [Captions, tracking, and naming](references/captions-and-publishing.md)
- [Static poster, on request](references/static-poster.md)
- Helpers: [watermark_badge.py](scripts/watermark_badge.py) and
  [xfade_timeline.py](scripts/xfade_timeline.py)
