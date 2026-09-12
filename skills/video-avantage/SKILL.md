---
name: video-avantage
description: >-
  Build a Roogo feature or benefit explainer video from AI-generated actors and
  narration when no real listing photography or footage exists. Use for
  requests such as "make a video about [feature]", "explain the commission
  model, voice notes, or 3D tours in a video", "we have no photos, use AI
  actors", or any request to promote an app feature, a differentiator, or a
  business-model benefit rather than a specific property. Produces a narrated,
  captioned, watermarked vertical video built from generated character clips,
  comparison cards, and text cards. Do not use for a specific renter or buyer
  demand call-out, or for showcasing an already published listing.
---

# Video avantage

One feature or benefit in, one narrated explainer video out, built entirely
from generated actors and on-screen data. No property photography is needed.

One feature equals one video. Get the script and any numbers approved before
generating anything expensive.

## Route the work

1. Confirm the brief and the script. Read
   [references/brief-and-structure.md](references/brief-and-structure.md)
   before writing a single line of script.
2. Read [references/brand-system.md](references/brand-system.md) before drawing
   any card or text frame.
3. Whenever generating, revising, or timing narration and character dialogue,
   read [references/narration-and-voice.md](references/narration-and-voice.md),
   then read only the selected provider reference:
   [references/elevenlabs.md](references/elevenlabs.md) or
   [references/cartesia.md](references/cartesia.md). ElevenLabs with the
   narrator voice Alimata is the default; Cartesia is approved when the
   requester asks for it or a needed voice is unavailable.
4. When the benefit needs a before-and-after or us-versus-them comparison, read
   [references/comparison-cards.md](references/comparison-cards.md).
5. Before building captions, read
   [references/captions.md](references/captions.md). The caption technique here
   is hand-rolled for a reason.
6. Before mixing audio or planning a revision round, read
   [references/audio-and-revisions.md](references/audio-and-revisions.md).

Preserve any duration, language, aspect ratio, voice, or delivery
specification the requester supplies. Otherwise use the reference defaults and
state them briefly.

## Non-negotiable conventions

- **Every beat has a voice over it.** No silent segments, ever. Even a pure
  reaction shot gets a short narrator line. Dead air reads as a mistake.
- **Watermark:** the white-circle Roogo badge, top-right, on every segment
  except spans already showing the full centred logo. Build it with
  [scripts/watermark_badge.py](scripts/watermark_badge.py).
- **Captions sit toward the centre**, positioned per segment against whatever
  is already on screen, never pinned to the bottom edge, never colliding with
  on-screen cards or labels.
- **Never reuse dialogue-lip-synced footage under a swapped audio line.**
  Regenerate that shot as a non-verbal reaction clip instead. Changing voice or
  provider counts as changing the line.
- **One voice per role, declared before generating**, switched only at scene
  boundaries and loudness-matched across the handoff.
- No em dashes and no emoji in on-screen or spoken copy. Final files carry real
  French titles, for example `Roogo - <hook>.mp4`, and contact details stay
  visible.
- Reuse rendered segments across revisions whenever only audio, text, or
  captions changed. Extract them from the prior render rather than paying to
  regenerate footage.

## Completion checks

Before calling the video complete, verify:

- the cold open states the payoff within the first few seconds;
- no segment is silent, and no caption collides with an on-screen graphic;
- the narrator was directed as its provider reference requires, and the manifest
  records the provider, every voice ID, the model, and the settings used;
- the brand name was confirmed by ear on a short test clip, not guessed;
- no shot with baked mouth movement plays under a different line, voice, or
  provider;
- no delivery markup was spoken aloud, confirmed by transcribing a sample;
- the audio mix used a longest-duration mix and a final loudness pass on the
  combined output, and the mixed duration matches the video;
- the caption track's total frame count equals the video's, computed from
  rounded cumulative frame targets rather than per-clip seconds;
- the watermark is present and absent over full-logo cards;
- every number on screen matches the approved reference model;
- the spend on generated clips is stated to the requester in the summary.
