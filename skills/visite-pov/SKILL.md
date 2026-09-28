---
name: visite-pov
description: >-
  Build a Roogo POV listing walkthrough: a narrated 9:16 video for one live
  property listing (sale or rental) made from its real photos when no one filmed
  a visit, with slow camera drift, one narrator, an outro showing the price and
  a call/WhatsApp number, and French social captions with hashtags. Use for
  requests such as "make a video using these images for this property", "fais
  une vidéo avec ces photos pour ce bien", "visite POV", or a listing link sent
  with photos. Do not use for a renter or buyer demand calling owners in, for a
  feature or benefit explainer with no listing photos, for a celebration
  graphic, or for real footage of a presenter walking a property.
---

# Visite POV

One live listing plus its photos in; one narrated 9:16 walkthrough and its
French captions out. No AI actor, no captions on the video, near-zero cost.

## Boundaries

- A specific renter or buyer demand calling owners in is `appel-proprietaires`.
- A feature or benefit with no listing photos is `video-avantage`.
- An existing celebration graphic is `milestone`.
- Never generate an AI presenter or lip-synced actor for a property video.

## Workflow

1. **Facts.** Read the live listing: type, area, neighborhood, price, features,
   paperwork wording. Script only what it states. Do not repeat absolute claims
   such as guaranteed land security. If the listing's type or address
   contradicts its description, describe the real property and flag the listing.
2. **Privacy.** Blur residents' faces, always children, with
   `scripts/flouter_visages.py` before animating.
3. **Order.** Arrange photos as a walk: street and access, gate, courtyard, back.
4. **Script and voice.** Simple spoken French, 30 to 45 seconds, narrated by
   Sandrine on Cartesia. Read [references/script-and-voice.md](references/script-and-voice.md)
   for the structure, the punctuation that carries emotion, respellings and
   the transcription check. State the cost before generating.
5. **Outro.** Render the HyperFrames outro with the listing's values and one
   listing photo as the background: [references/outro.md](references/outro.md).
6. **Build.** Write a plan JSON with one shot per phrase, cut on the
   voiceover's word timestamps, and run `python3 scripts/build_pov.py plan.json`.
   The script adds the drift, crossfades, watermark, optional fact chips, the
   outro, the music bed and loudness normalization.
7. **Check.** Look at a frame at every cut and in the outro, and confirm video
   and audio durations match. Lower `y` on sky-heavy fisheye shots.
8. **Captions.** Write the French post text for staff to paste with the video:
   [references/captions.md](references/captions.md).

## Deliverables

- One 1080x1920 MP4 per variant, named like a French title, for example
  `Roogo - Parcelle 336 m² à vendre Tanghin (POV, 40 millions).mp4`.
- One French caption per variant, ready to paste.
- Optional A/B: the same photos with a second, targeted script (for example the
  diaspora) and a different music bed.

## Fixed rules

- One action on the outro: call or WhatsApp the Roogo number. No app-download
  button on property videos.
- Roogo watermark on every photo shot; the outro carries the full logo.
- No burned-in captions on home tours.
- No em dashes in any copy.
