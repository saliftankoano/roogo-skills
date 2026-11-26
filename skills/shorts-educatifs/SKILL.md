---
name: shorts-educatifs
description: >-
  Make a Roogo educational comedy short in the Rasmané paper-cut series: a 9:16
  video of 40 to 68 seconds where Rasmané meets a housing or land situation, a
  narrator tells it, it is funny, and it ends on one useful lesson and a WhatsApp
  call to action. Covers the script (voice first, 10 rules), one paper-cut image
  per scene, ElevenLabs or Cartesia voices, the edit, loudness checks and the
  social captions. Use for "vidéo éducative", "nouvel épisode", "Rasmané",
  "edu-laugh", "short éducatif", "épisode S1-02 / S2-03 / S3-01", "version
  diaspora", or when an agent in HyperFrames must make the next episode of the
  series. Not for property listings (`visite-pov`), owner call-outs
  (`appel-proprietaires`), feature explainers with AI actors (`video-avantage`)
  or staff training (`formation-equipe`).
---

# Shorts éducatifs (série Rasmané)

Everything lives in the vault folder `/Users/salif/Desktop/Kazedra/Roogo/knowledge/roogo/Videos/Shorts éducatifs/` (the source of truth). Read, in this order:

1. `Series bible.md`: look, cast, voices, the 7-beat shape, how to make an episode.
2. `series.json`: machine-readable style blocks, voices, video and end-card settings.
3. `Episode checklist.md`: pick the next episode and its lane; tick it only when posted.
4. `04 Marketing/Playbooks/Educational shorts (paper cut).md`: the 10 scenario rules and open decisions.
5. `04 Marketing/Hashtag rules.md`: captions and tags.

## Workflow

1. **Source the facts first.** Any legal or customary claim gets a source in the episode folder before the script. Check `00 Start Here/Conflicts and confirmations.md`. No fee, price or percentage in a video while the owner fee model has two versions in the vault. Never promise a result.
2. **Script, voice first.** Plain spoken French, « tu », full sentences, no em dash, no emoji on screen, never « faux ». Humour mocks a habit, never a person or group. Brand: « Roogo » on screen, « Rohgo » in voice text. Diaspora episodes: say « aux États-Unis », « dishwasher », « delivery ». Write `Script.md` and `episode.json` (copy `Outils/episode.template.json`). **Salif approves every script**; drafts stay drafts.
3. **Images.** One prompt per scene in `prompts/<scene>.txt`: style block, scene (start « The same young man from the reference »), frame block, copied from `series.json`. Run `python3 Outils/studio.py images --yes` after reading the estimate (about $0.042 each, 5 at a time). Check each image against its sentence: no text, no blank band, right character, people with dark brown skin, only the scene that needs paper holds a paper.
4. **Voices.** `python3 Outils/studio.py voix`. Narrator Tony or Mathieu (not decided for the series), pushing characters Pumba. Whisper mishears « Rasmané »: Salif confirms by ear.
5. **Edit and measure.** `build`, then `mesure` (target -16 LUFS, true peak at most -1.5 dB). Hard cut per sentence, slow push-in, captions toward the centre, Roogo badge on every frame but the end card. Salif listens to anything sound-dependent before it ships.
6. **Captions.** One `Légendes réseaux sociaux.md` per episode: TikTok always `#burkinatiktok #ouagadougou #fyp` plus 2 targeted tags; IG/FB `#Roogo #Ouagadougou #ImmobilierBurkina` plus 2; `roogobf.com` on its own line. WhatsApp Status: no tags.
7. **Record.** Update `status` in `episode.json`, the checklist, and the vault; commit and push the vault. Videos and audio stay local (git ignores them).

The toolkit (`Outils/studio.py`: `doctor`, `images`, `voix`, `build`, `mesure`, `tout`) is described in `Outils/README.md`. Keys come from the macOS keychain and are never printed or saved. If a command is blocked, stop and report it. Ask before any single paid step above about $1.

## Close every run with improvement candidates

List 1 to 3 gaps you hit (a rule missing, a tool step that failed, a verdict from Salif not yet in the bible), each with the evidence, and propose the edit to this skill or to the series bible. Do not apply them unasked.
