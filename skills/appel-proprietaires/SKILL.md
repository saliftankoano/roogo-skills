---
name: appel-proprietaires
description: >-
  Build a Roogo owner call-out ad bundle when one specific renter or buyer
  demand exists and matching property owners should call. Use for requests
  such as "appel a proprietaires", "a client is looking for a house, a shop,
  or a commercial space in [zone], budget [amount], it is urgent", or "make an
  ad for this search". Produces a 1080x1920 narrated carousel video with
  burned-in French captions plus a French social-caption document; the 4:5
  static poster is a separate on-request format. Do not use for general brand
  promotion, app feature explainers, testimonial edits, or showcase videos of
  an already published listing.
---

# Appel a proprietaires

One renter or buyer demand in, one ready-to-post owner call-out bundle out.
One ad states one demand. Never combine several demands in a single creative.

## Route the work

1. Collect the demand brief and get the script approved before generating
   anything. Read [references/brief-and-script.md](references/brief-and-script.md).
2. Read [references/brand-system.md](references/brand-system.md) before drawing
   any frame, card, or poster.
3. Whenever generating, splicing, or verifying narration, read
   [references/narration.md](references/narration.md), then read only the
   selected provider reference:
   [references/elevenlabs.md](references/elevenlabs.md) or
   [references/cartesia.md](references/cartesia.md). ElevenLabs with the
   narrator voice Alimata is the default; Cartesia is approved when the
   requester asks for it or the default voice is unavailable.
4. For the default deliverable, the vertical carousel video, read
   [references/carousel-video.md](references/carousel-video.md).
5. For the social caption document, publishing tracking, and file naming, read
   [references/captions-and-publishing.md](references/captions-and-publishing.md).
6. Only when the requester explicitly asks for a static image, read
   [references/static-poster.md](references/static-poster.md).

Preserve any duration, aspect ratio, language, phone number, brand asset, or
delivery specification the requester supplies. Otherwise use the reference
defaults and state them briefly.

## Default bundle

Produce these in order, pausing for approval where noted:

1. **Script**, approved by the requester before any paid generation.
2. **Music selection** from a rights-cleared library, approved with the script.
3. **Narration**, generated only after the script is approved.
4. **Carousel video**, 1080x1920, roughly 35 to 40 seconds.
5. **Caption document** in French, covering every platform the team posts to.

## Non-negotiable conventions

- The video is **1080x1920, true 9:16**. The 4:5 ratio belongs to the static
  poster only; a 4:5 video letterboxes on vertical surfaces. This was shipped
  wrong once and three videos had to be rebuilt.
- Every video carries the white-circle Roogo badge in the top-right corner,
  excluded only over spans that already show the full centered logo. Build it
  with [scripts/watermark_badge.py](scripts/watermark_badge.py).
- Never let an image model render text. Every word on screen is drawn with PIL
  in the brand font so spelling and accents are exact.
- Never reuse furnished listing photography for an unfurnished or modest ask.
- Never promise a guarantee. State how the rent reaches the owner instead.
- Confirm the spelling of every place name with the requester before posting.
  Do not guess a neighborhood name.
- No em dashes and no emoji in ad copy. The social caption document is the one
  exception where emoji are allowed, because staff paste it directly.
- The contact phone number is a supplied input, always shown large. Visible
  contact details read as credibility for this audience, not as clutter.

## Completion checks

Before calling the bundle complete, verify:

- the demand, zone, budget, and contact details match the approved brief;
- the rendered video is exactly 1080x1920 and its video and audio durations
  agree when probed;
- the narration was auditioned by ear and approved before the paid batch, and
  the manifest records the provider, voice ID, model, and settings used;
- the narrated phone number was re-transcribed and reads back as grouped number
  pairs, not single digits;
- captions were width-checked in the real font and never overflow the frame;
- the watermark is present and is absent over full-logo cards;
- the audio mix was measured rather than guessed;
- the caption document names the site link and the phone number;
- no private path, credential, or unapproved claim appears in any deliverable.
