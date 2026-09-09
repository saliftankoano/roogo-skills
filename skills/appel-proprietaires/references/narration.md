# Narration

## Voice

Use the Roogo narrator voice **Alimata**, ElevenLabs voice ID
`4SFJvuIUvxaPLgk8FoK3`, through the plain text-to-speech endpoint. Do not add
bracketed emotion tags and do not switch her to the dialogue endpoint; both
have been rejected by ear as sounding like a different person. Take delivery
and tone from punctuation instead.

Publishing a voice ID is configuration, not permission. Confirm the account has
access and the right to use the voice before generating. If it is unavailable,
ask for an authorized alternative rather than silently substituting one.

## Spoken numbers

Write the phone number out as French number pairs, for example "soixante-sept,
zero zero, soixante et un, seize". Never spell digits individually; a
digit-by-digit reading is mispronounced and sounds like a different number.

Verify rather than assume: re-transcribe the generated audio and confirm the
digits come back grouped as pairs. Transcribe the phone-number segment in
isolation, because a long pass regularly mishears numbers and names.

## Brand name pronunciation

The French model reads the brand name incorrectly by default. Spell it
`Rôogo` in narration prompt text only, never on screen. This spelling was
confirmed by ear on short test clips. Do not invent a new spelling and rebuild
a full video around it; generate a short test clip and have the requester
confirm by ear first.

## Reusable closing clip

The closing block, from "do not leave your house empty" through the phone
number, never references the specific zone, criteria, or budget. Treat it as a
fixed, already-verified audio clip stored with the team's reusable assets, and
splice it onto a freshly generated hook, criteria, and budget section. This
saves a generation on every build and guarantees the number is always
pronounced correctly.

Keep the known-good word or segment timestamps for that clip alongside it, so
caption timing for the closing section does not need to be recomputed.

## Verification

- Probe the generated narration and confirm its duration before building any
  video timeline against it.
- Correct transcription spellings against the approved script before they reach
  the screen. The brand name, place names, and singular or plural forms are the
  usual offenders.
