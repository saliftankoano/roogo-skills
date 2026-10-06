---
name: vsl
description: >-
  Build a Roogo VSL (video sales letter): one video that does the selling, with
  a promise, the pains the viewer recognizes, how it works, objections answered
  (fees), then the ask. Made in HyperFrames from real listing photos plus a few
  generated clips for people, a Sandrine narrator, house captions, quiet sound
  effects and an outro with App Store and Google Play badges. Produces a 16:9
  version for the website and a 9:16 version for social. Use for requests such
  as "VSL", "video sales letter", "vidéo de vente", "fais un VSL pour les
  propriétaires", or "version verticale du VSL". Do not use for one live
  listing (`visite-pov`), one renter or buyer demand calling owners in
  (`appel-proprietaires`), a feature explainer with no photography
  (`video-avantage`), or a celebration graphic (`milestone`).
---

# VSL

A VSL (video sales letter) is a sales pitch as a video: it states a promise,
shows the viewer their own problems, explains the mechanism, answers the
objections, then asks for one action. Read [README.md](README.md) for the plain
explanation. About 80 seconds for the website; cut a 20 to 30 second version
separately for paid ads.

## Boundaries

- One live listing from its photos is `visite-pov`.
- A specific renter or buyer demand calling owners in is `appel-proprietaires`.
- A feature with no photography is `video-avantage`; a celebration graphic is `milestone`.
- Never use seedance-2, lip-synced AI presenters, or invented traction and fee claims.

## Workflow

1. **Audience and offer.** Owners, renters or agents; one promise; one action.
   Quote fees and terms only from a source the user confirms. Never claim
   performance numbers that have no defined source.
2. **Script.** Promise, three pains, mechanism, price objection, alternative,
   ask. Simple spoken French, emotion by punctuation. Read
   [references/structure-and-script.md](references/structure-and-script.md).
   Get approval before paying for anything.
3. **Assets: look first, generate last.** Use real listing photos and existing
   footage wherever they exist. Generate only what does not exist (a person, a
   phone in a hand). Drop photos that show business names, addresses or
   phone-brand watermarks. State the plan and cost before generating. Confirm
   with the user that listing photos may be used in advertising.
4. **Generated shots.** Still image, then image-to-video (about 5 seconds per
   shot). For the same character in a second shot, pass the first still as a
   reference and change the action; check the face. Never leave one clip on
   screen for more than about 4 seconds.
5. **Voice.** `scripts/build_vo.py scenes.json` writes Sandrine's narration per
   scene, a normalized mix, `timeline.json` and `words.json`. Respell for TTS and
   read the transcription back. See
   [references/structure-and-script.md](references/structure-and-script.md).
6. **Build.** Scaffold a HyperFrames project, copy the assets, run
   `scripts/gen_horizontal.py`, then a separate project with
   `scripts/gen_vertical.py`; edit the picks and timings blocks for the new
   script. Rules for captions, outro, music, watermark and cuts:
   [references/house-rules.md](references/house-rules.md). Sound effects:
   [references/sound-effects.md](references/sound-effects.md).
7. **Verify.** `npx hyperframes check`, frames at the midpoint of every scene
   and at the cards and outro in both formats, level checks on the mix. Say
   plainly if you did not listen to or watch the whole video.
8. **Deliver.** Compress for delivery, write the French social caption, and
   never publish or deploy without asking.

## Defaults and limits

- HyperFrames for videos over about 30 seconds; ffmpeg only for quick vertical ads.
- No captions on the outro; watermark everywhere except the outro.
- Provide your own logo, font and music; none are shipped. Sound effects are
  described, not shipped, because their licenses must be checked per file.
- The generators are a reference build of the owner VSL: change the hard-coded
  photo picks, scene copy and timings; keep the structure.
