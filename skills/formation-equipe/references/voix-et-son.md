# Voice and sound

## Voices (Cartesia, model sonic, French)

| Voice | Use | Voice ID |
|---|---|---|
| Salif (clone) | Staff training, default | `16dba105-0026-4ff7-bf90-12562786a97c` |
| Sandrine (house) | When the user prefers the house voice | `2435841c-fce7-4fd5-aed1-dc7008eb7d20` |

A voice ID is configuration, not permission: use a cloned voice only with its
owner's consent.

## Spelling for the voice

Write the script for reading, then respell only in the text sent to the voice:

- "Roogo" → "Rohgo"; "Burkina Faso" → "Bourkina Faso".
- Prices and numbers in words when the voice stumbles on digits.
- Respellings for one video only go on the command line, so the script stays
  as captioned: `narration.py script.md --respell "CNIB=C N I B"` (repeatable).
  Never keep a second copy of the script for the voice.
- Words a staff member must find on screen stay spelled as on screen in the
  captions; captions come from the approved script, never from the
  transcription.

Generate a 10 second test of any new spelling and confirm it by ear before the
full read.

## Pace

Staff follow the screen while they listen: target 130 to 160 words a minute,
with a pause at each step change. `scripts/narration.py` prints the measured
pace from the word timestamps after every read.

- `--speed`: Cartesia speed, 1.0 normal. Clones read fast (Salif's clone
  measured about 185 words a minute), so a clone (the default voice, or
  `--clone`) defaults to 0.9. Other voices default to 1.0.
- `--pause`: seconds of silence between script paragraphs (default 0.9; 0 for
  none). One paragraph is one step, so each step change gets a breath.
- Measured on Salif's clone: 138 words in 44.7 s with no pause at 1.0;
  52.8 s with 7 pauses at speed 0.9 and 0.9 s pauses.
- Word timestamps are taken from the final audio, pauses included, so captions
  still match the voice. The pauses are pure digital silence.
- Pauses alone must not push a video past 3 minutes; shorten the script instead.

## Cleaning a cloned voice

Cloned voices reproduce the hiss and rumble of the recording they were made
from. `scripts/nettoyer_voix.py in.wav out.wav 0.9`:

- takes the quietest 12% of 20 ms frames as the noise profile, leaving out
  frames of pure digital silence (below -120 dB, such as the pauses above),
- reduces it by the given proportion (0.9 is the tested default),
- prints speech level, background level and the gap, before and after.
- When nothing audible sits between the words, it says "already clean" and
  copies the file unchanged.

Aim for a gap above 18 dB. Above about 0.95 the voice turns metallic; listen to
the result. Keep the original file, and keep the cleaned one only if the gap
improved.

A clone's background changes from take to take: the same text with the same
settings measured 14.5 dB on one take and 31.7 dB on the next. Measure every
take; a take under 18 dB before cleaning is re-recorded, not cleaned harder.

## Music

- A licensed instrumental, credited on the closing card with the license and
  "extrait mixé" when cut.
- It plays from the first to the last frame: louder over the title card,
  ducked under the voice, rising again when the voice stops, faded out over
  the last 3 seconds.
- `scripts/mixer.py` does this with a sidechain duck and normalizes to
  -16 LUFS.
