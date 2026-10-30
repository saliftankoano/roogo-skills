# Formation équipe

Training videos for the Roogo team: one feature of the Roogo app, shown on the
real screens, explained step by step in French.

## What you get

- A 1 to 3 minute MP4 with a French title as its file name: 1920x1080 for
  the desktop app, or 1080x1920 for public pages filmed on a phone.
- Real captures of the app in production, with slow camera moves to the part
  that matters, captions toward the centre in a dark box that reads on any
  screen, the Roogo badge top right, a title card and a closing card with the
  rules to remember.
- A narration in the voice you choose, at a pace staff can follow (130 to 160
  words a minute, a short pause at each step), cleaned of background hiss, over
  a credited music bed that drops under the voice.
- A contact sheet and the results of the checks.
- **Improvement candidates for this skill.** Every run ends with a short list:
  what the skill got wrong or left out, the evidence from that run, and the
  exact change proposed. Accepted ones are merged into this repository, so the
  skill improves with each video.

## How a run goes

1. You name the feature and who the video is for.
2. The agent checks the feature in production and writes the script. You
   approve it.
3. You sign in to roogobf.com in a separate Chrome window; the agent captures
   the screens from it. Public pages (careers, a listing) are filmed in a fresh
   signed-out browser at phone size instead.
4. The agent records the narration, cleans it, builds the video, mixes the
   music and runs the checks.
5. You watch it and approve; the agent saves it with the team's videos and
   lists every test row and uploaded file it created while filming, with where
   each lives, for you to keep or delete.
6. The agent presents its improvement candidates. You accept, change or reject
   each; accepted ones go into a pull request to this repository.

## Setup

- Node with Playwright; Python 3 with Pillow, numpy, soundfile, noisereduce;
  ffmpeg. If noisereduce is missing, a virtual environment in the working
  folder is enough: `python3 -m venv .venv && .venv/bin/pip install
  noisereduce soundfile numpy Pillow`.
- Keep the installed skill in step with this repository: an old copy brings
  back fixed bugs.
- Cartesia key (`CARTESIA_API_KEY` or Keychain item `ai.cartesia.api-key`,
  with or without an account name) and fal key (`FAL_KEY` or Keychain item
  `roogo-content-key`). Keys are never printed.
- Your own logo, fonts and licensed music. None are shipped.

## Example prompts

- "Fais une vidéo de formation sur le Studio de contenu pour l'équipe."
- "Le Studio a changé, refais la vidéo de formation."
- "Training video for staff on adding a guest voice."

## Limits

- Staff training only; marketing videos use the other Roogo video skills.
- It films production as it is. A feature that is not deployed is not filmed
  unless you ask, and the video then says so.
- The agent never signs in for you, and never deletes the test data it
  created; it lists it for you.
- The cleaned voice and the pace are measured, not judged by ear: listen
  before you approve.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
- [references/](references/): capture, voice and sound, building and checks,
  the improvement protocol and the lessons journal.
- [scripts/](scripts/): capture template, narration, voice cleaning, caption
  alignment, build, mix and checks.
