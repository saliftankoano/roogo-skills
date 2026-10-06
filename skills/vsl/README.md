# VSL

**VSL means "video sales letter".** It is a sales pitch turned into a video. A
good one does five things in order: it makes a **promise**, shows the viewer
**the pains they already recognize**, explains **how the product removes them**,
**answers the objections** (usually the price), and then **asks for one action**.
A well-made VSL delivers the same strong pitch every time, to everyone, without
anyone having to present it.

For Roogo this is the video a property owner watches to understand why to list
with us, on the website or as a social ad. It is not an explainer for a feature
and not a video about one listing.

## What it is for

- A website page that sells (for example a page for property owners), with a
  16:9 video.
- The same pitch as a 9:16 video for social platforms.

Use a different package when one live listing needs a video (`visite-pov`), a
renter or buyer demand should make owners call (`appel-proprietaires`), a
feature needs explaining with no photography (`video-avantage`), or you have a
celebration graphic to animate (`milestone`).

## What you get

- A French script that follows the five-part pitch, about 80 seconds.
- A 16:9 and a 9:16 video built in HyperFrames, with a Sandrine narrator,
  house-style captions, music, quiet sound effects and an outro with App Store
  and Google Play badges and the phone number highlighted pair by pair as it is
  spoken.
- A French social caption.

## Requirements

- Node (for `npx hyperframes`), Python 3 with Pillow, `ffmpeg` and `ffprobe`.
- A Cartesia API key in `CARTESIA_API_KEY` (or the macOS Keychain item
  `ai.cartesia.api-key`) for the narrator.
- A speech-to-text helper that writes word timestamps (`FAL_TOOL` points to it).
- An image and image-to-video provider for the few generated shots.
- Your own Roogo logo, the Nunito ExtraBold font, a music track you have the
  rights to, and sound effects you have the rights to. None are shipped.

## How a build runs

1. Choose the audience, the single promise and the one action.
2. Write and approve the script.
3. Collect real listing photos; list the few shots that must be generated.
4. `python3 scripts/build_vo.py scenes.json` for voice, timeline and word
   timestamps.
5. Scaffold two HyperFrames projects (horizontal and vertical), copy the
   assets, run `scripts/gen_horizontal.py` and `scripts/gen_vertical.py`.
6. Check, review stills and levels, render, compress.

## Example prompts

```text
$vsl Make a VSL for property owners in Ouagadougou. Promise: your house let
and your rent collected without chasing anyone. Fees: 0 FCFA today, 50% of one
month's rent once if Roogo finds the tenant and collects the first rent, then
7% of each rent collected through Roogo. Use real listing photos from the
site. Start with the script and the asset plan; do not generate anything yet.
```

```text
$vsl Make the 9:16 version of the owner VSL for social, with captions and an
outro showing both stores.
```

## Limits

- The two generators are a reference build of the owner VSL. A new VSL means
  editing the photo picks, scene copy and timing blocks, not filling a form.
- Sound effects, fonts, the logo and music are not included.
- Fee wording is a summary of what the user supplied; legal terms need review.
- Do not publish or deploy without the user's go-ahead.

The store icons in `scripts/apple.svg` and `scripts/play.svg` come from
[Phosphor Icons](https://phosphoricons.com) (MIT).
