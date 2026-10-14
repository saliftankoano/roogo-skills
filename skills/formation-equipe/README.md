# Formation équipe

Training videos for the Roogo team: one feature of the Roogo app, shown on the
real screens, explained step by step in French.

## What you get

- A 1 to 3 minute 1920x1080 MP4 with a French title as its file name.
- Real captures of the app in production, with slow camera moves to the part
  that matters, captions under the screen, a title card and a closing card
  with the rules to remember.
- A narration in the voice you choose, cleaned of background hiss, over a
  credited music bed that drops under the voice.
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
   the screens from it.
4. The agent records the narration, cleans it, builds the video, mixes the
   music and runs the checks.
5. You watch it and approve; the agent saves it with the team's videos and
   lists what it created while filming, for you to keep or delete.
6. The agent presents its improvement candidates. You accept, change or reject
   each; accepted ones go into a pull request to this repository.

## Setup

- Node with Playwright; Python 3 with Pillow, numpy, soundfile, noisereduce;
  ffmpeg.
- Cartesia key (`CARTESIA_API_KEY` or Keychain item `ai.cartesia.api-key`) and
  fal key (`FAL_KEY` or Keychain item `roogo-content-key`).
- Your own logo, fonts and licensed music. None are shipped.

## Example prompts

- "Fais une vidéo de formation sur le Studio de contenu pour l'équipe."
- "Le Studio a changé, refais la vidéo de formation."
- "Training video for staff on adding a guest voice."

## Limits

- Staff training only; marketing videos use the other Roogo video skills.
- It films production as it is. A feature that is not deployed is not filmed
  unless you ask, and the video then says so.
- The agent never signs in for you.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
- [references/](references/): capture, voice and sound, building and checks,
  the improvement protocol and the lessons journal.
- [scripts/](scripts/): capture template, narration, voice cleaning, caption
  alignment, build, mix and checks.
