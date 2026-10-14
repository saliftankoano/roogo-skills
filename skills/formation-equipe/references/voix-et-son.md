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
- Words a staff member must find on screen stay spelled as on screen in the
  captions; captions come from the approved script, never from the
  transcription.

Generate a 10 second test of any new spelling and confirm it by ear before the
full read.

## Cleaning a cloned voice

Cloned voices reproduce the hiss and rumble of the recording they were made
from. `scripts/nettoyer_voix.py in.wav out.wav 0.9`:

- takes the quietest 12% of 20 ms frames as the noise profile,
- reduces it by the given proportion (0.9 is the tested default),
- prints speech level, background level and the gap, before and after.

Aim for a gap above 18 dB. Above about 0.95 the voice turns metallic; listen to
the result. Keep the original file.

## Music

- A licensed instrumental, credited on the closing card with the license and
  "extrait mixé" when cut.
- It plays from the first to the last frame: louder over the title card,
  ducked under the voice, rising again when the voice stops, faded out over
  the last 3 seconds.
- `scripts/mixer.py` does this with a sidechain duck and normalizes to
  -16 LUFS.
