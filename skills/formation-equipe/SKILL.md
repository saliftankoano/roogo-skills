---
name: formation-equipe
description: >-
  Make a Roogo staff training video for a feature of the Roogo web app: real
  screen captures from a signed-in browser, a French narration in a cloned or
  house voice cleaned of background hiss, slow camera moves over each capture,
  captions from the approved script, title and closing cards, a credited music
  bed ducked under the voice, and checks before delivery. Ends every run with
  improvement candidates for this skill, each tied to a gap and evidence. Use
  for requests such as "vidéo de formation", "training video for the team",
  "explique le Studio à l'équipe", "refais la vidéo de formation avec la
  nouvelle version", or "tutoriel pour Ablassé". Do not use for marketing
  videos aimed at owners, renters or buyers (`vsl`, `video-avantage`,
  `appel-proprietaires`, `visite-pov`, `milestone`).
---

# Formation équipe

A training video shows staff how to use one part of the Roogo app, using the
real screens they will see. It is internal: plain, accurate, calm. About 1 to 3
minutes. Read [README.md](README.md) for the plain explanation.

This skill stands on its own. Do not hand the work to a general product-demo
or video skill: follow this workflow, and improve it (step 9) when it falls
short.

## Boundaries

- Audience is Roogo staff. Anything for owners, renters, buyers or social media
  belongs to the marketing skills listed in the description.
- Show the product as it is in production now. Never film a local build,
  a mock-up, or a feature that is not deployed, unless the user asks for it
  and the video says so.
- Never show real customers' personal data on screen. Pick test or public
  listings, and hide emails and phone numbers that are not Roogo's own.

## Workflow

1. **Brief.** Which feature, which staff, what they must be able to do after
   watching. List the steps in the order a staff member does them. Check the
   feature in production first; if it changed since the last video, list what
   changed.
2. **Script.** One short paragraph per step, spoken French, second person
   ("Cliquez sur…"), words that match the buttons on screen exactly. Name
   prices and limits only as the app shows them. End with the two or three
   rules to remember. Get the script approved before recording anything.
   See [references/voix-et-son.md](references/voix-et-son.md) for spelling
   words for the voice.
3. **Capture.** Drive the user's own signed-in browser over the DevTools
   protocol, in a dedicated tab, at 1600x825 CSS pixels and 2x scale. The user
   signs in; the agent never types credentials. Hide private details before
   every shot. Follow [references/capture.md](references/capture.md) and start
   from [scripts/capture.example.mjs](scripts/capture.example.mjs).
4. **Narration.** `scripts/narration.py` reads the approved script with the
   chosen voice, then writes word timestamps. Listen to a short sample before
   the full read when the voice or a spelling is new.
5. **Clean the voice.** Cloned voices carry hiss and low rumble.
   `scripts/nettoyer_voix.py` reduces it and prints the speech-to-background
   gap before and after. Use the cleaned file only if the gap improved and the
   voice still sounds natural.
6. **Build.** Write the shot list (time in the narration, capture, framing) in
   a copy of [scripts/montage.example.json](scripts/montage.example.json), then
   run `scripts/montage.py`. Camera moves, cards and captions follow
   [references/montage-et-verification.md](references/montage-et-verification.md).
   Then `scripts/mixer.py` lays the music under the narration.
7. **Verify.** `scripts/verifier.py` on the final file: no still image longer
   than 3 seconds, loudness near -16 LUFS, audio and video the same length, a
   contact sheet. Transcribe the final audio and compare it to the script.
   Look at frames at every shot change. Say plainly what you did not watch or
   hear in full.
8. **Deliver.** A French title as the file name ("Roogo | Équipe - <sujet>"),
   saved where the team keeps training videos (Roogo: the vault, under
   `06 Product and technology/Videos/`). Keep the previous version under a
   dated name instead of overwriting it. Offer a lighter copy for WhatsApp.
9. **Improve this skill.** Mandatory, every run, even a short one. Follow
   [references/ameliorations.md](references/ameliorations.md): bring
   improvement candidates, each with the gap it closes and the evidence from
   this run. Never edit an installed copy of this skill; accepted changes go
   to the skill repository through a pull request.

## Defaults

- Voice: the user's choice. Roogo defaults: Salif's French clone for staff
  training, Sandrine (house voice) otherwise. Voice IDs are in
  [references/voix-et-son.md](references/voix-et-son.md).
- Music: a licensed instrumental the user supplies, credited on the closing
  card. Roogo uses "Carefree" by Kevin MacLeod (CC BY 4.0). No music file is
  shipped.
- Light Roogo look: cream background, dark brown text, orange accent. Logo and
  fonts are supplied by the user; none are shipped.
- No em dashes and no emoji in on-screen text or captions.

## Requirements

Node with Playwright (capture), Python 3 with Pillow, numpy, soundfile and
noisereduce, ffmpeg and ffprobe. A Cartesia key in `CARTESIA_API_KEY` or the
macOS Keychain item `ai.cartesia.api-key`; a fal key in `FAL_KEY` or the
Keychain item `roogo-content-key` for word timestamps. Never print keys.
