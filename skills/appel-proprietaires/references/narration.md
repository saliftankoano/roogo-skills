# Narration

Provider-independent workflow. Follow it whatever provider is selected, then
read **only** the selected provider reference:
[elevenlabs.md](elevenlabs.md) or [cartesia.md](cartesia.md).

## Select the provider and voice

ElevenLabs with the Roogo narrator voice **Alimata** is the default for this
format. Cartesia is an approved alternative when the requester asks for it, when
the ElevenLabs voice is unavailable, or when the ad needs the slower, more
deliberate register Cartesia's approved voices provide.

Record the provider, the voice ID, the model, and every delivery setting in the
build's manifest. Never substitute a voice silently: if the approved one is
unavailable, stop and ask for an authorized alternative.

Publishing a voice ID is configuration, not permission. Confirm the account has
access and the right to use the voice before generating.

## Approve the voice before a paid batch

Generate one short representative sample, including the phone-number line, and
have the requester confirm it **by ear**. A successful generation and a valid
voice ID prove nothing about how the ad sounds. Only after the sample is
accepted do you generate the full narration.

## Spoken numbers

Write the phone number out as French number pairs, for example "soixante-sept,
zero zero, soixante et un, seize". Never spell digits individually; a
digit-by-digit reading is mispronounced and sounds like a different number.

Verify rather than assume: re-transcribe the generated audio and confirm the
digits come back grouped as pairs. Transcribe the phone-number segment in
isolation, because a long pass regularly mishears numbers and names.

## Brand name pronunciation

No provider reads the brand name correctly by default in French. The correction
is provider-specific and is described in each provider reference. Whichever
correction is used, it belongs in the narration prompt or in a pronunciation
dictionary, never on screen.

Confirm the fix by ear on a short test clip before building a full video around
it. Do not invent a new spelling and rebuild the whole ad on the guess.

## Reusable closing clip

The closing block, from "do not leave your house empty" through the phone
number, never references the specific zone, criteria, or budget. Treat it as a
fixed, already-verified audio clip stored with the team's reusable assets, and
splice it onto a freshly generated hook, criteria, and budget section. This
saves a generation on every build and guarantees the number is always
pronounced correctly.

Keep the known-good word or segment timestamps for that clip alongside it, so
caption timing for the closing section does not need to be recomputed.

A reusable clip belongs to the provider and voice that produced it. Switching
provider mid-campaign means regenerating the closing clip in the new voice and
re-verifying the number, not splicing two voices into one ad.

## Timing and delivery

- The final processed narration, not the raw provider download, is the timing
  backbone for slide boundaries and captions.
- Probe the generated narration and confirm its duration before building any
  video timeline against it.
- Correct transcription spellings against the approved script before they reach
  the screen. The brand name, place names, and singular or plural forms are the
  usual offenders.
