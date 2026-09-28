# Visite POV

Turn the real photos of one live Roogo listing into a narrated 9:16
walkthrough video, for when no one filmed a visit. The camera drifts slowly
across each photo as if you were walking the property, one narrator tells the
story, and the video ends on an outro with the price and a number to call or
WhatsApp. The package also writes the French caption staff paste when posting.

## What it is for

A listing is live and all you have is photos, often 360-camera shots. Use a
different package when a renter or buyer demand should make owners call
(`appel-proprietaires`), when a feature needs explaining without listing photos
(`video-avantage`), or for a celebration graphic (`milestone`).

## Requirements

- Python 3 with Pillow, and `ffmpeg`/`ffprobe`.
- Node, for `npx hyperframes@0.8.81` (the outro).
- A Cartesia API key in `CARTESIA_API_KEY` (or the macOS Keychain item
  `ai.cartesia.api-key`) for the narrator.
- A large Whisper model for the transcription check, for example `mlx_whisper`
  with `whisper-large-v3-turbo`.
- Your own copies of the Roogo logo and the Urbanist font (not shipped here),
  and a music bed you have the rights to.

## How a build runs

1. Read the facts from the live listing.
2. Blur faces with `scripts/flouter_visages.py faces.json`.
3. Write the script in simple spoken French, generate Sandrine's voiceover,
   transcribe it back and check the numbers and names.
4. Render the outro from `scripts/outro-hyperframes/` with the listing's values
   and one listing photo.
5. Write `plan.json` (one shot per phrase, cut on the word timestamps) and run
   `python3 scripts/build_pov.py plan.json`.
6. Check frames at the cuts and in the outro.
7. Write the French caption.

The plan format is documented at the top of `scripts/build_pov.py`.

## Example prompt

```text
$visite-pov Make a POV video for https://www.roogobf.com/proprietes/<listing>
using these 8 photos. Also make a diaspora variant.
```

## Deliverables

- One MP4 per variant, 1080x1920, about 35 to 45 seconds, named like a French title.
- One French caption per variant with hashtags.

## Cost

Near zero: Cartesia narration is billed to your own account, everything else
runs locally. The agent states the estimate before generating.

## Limits

- Face boxes are found by eye; the script blurs the boxes you give it.
- The outro is 5.5 seconds and then holds; very long service and contact lines
  just extend the hold.
- The camera drift works on stills only; it does not stabilize video footage.
