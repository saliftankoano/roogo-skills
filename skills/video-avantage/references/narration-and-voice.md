# Narration and character voice

Provider-independent workflow. Follow it whatever provider is selected, then
read **only** the selected provider reference:
[elevenlabs.md](elevenlabs.md) or [cartesia.md](cartesia.md).

Getting voice wrong is the single most likely reason a finished video is
rejected, and it is the most expensive thing to discover late.

## Two roles

This format has two distinct speaking roles, and they are directed differently
on every provider:

- **The narrator** carries the argument. One voice, stable across the whole
  video, delivering the cold open, the rewind cue, the explanation, and the
  callback.
- **Named characters** play the story. Each gets its own voice and keeps it for
  the whole film. A character voice never narrates and the narrator never plays
  a character.

Declare each voice's role before generating, and switch voices only at scene
boundaries. Loudness-match the handoffs so a role change does not read as a
level jump.

## Select the provider

ElevenLabs with the narrator voice **Alimata** is the default for this format.
Cartesia is approved when the requester asks for it, when a needed voice is
unavailable, or when the cast is better served by its approved voices.

Record the provider, every voice ID, the model, and all delivery settings in the
build's manifest. Publishing a voice ID is configuration, not permission:
confirm access and usage rights before generating, and if a voice is
unavailable, stop and ask for an authorized alternative rather than
substituting one silently.

## Confirm by ear before spending

For anything sound-dependent, never guess and then rebuild a slow, costly video
around the guess. Generate a short, cheap standalone clip of just the disputed
line or word and have the requester confirm by ear first. A successful
generation, a valid voice ID, and a clean transcript all pass while the video
still sounds wrong to the person who has to publish it.

This applies to the voice itself, to any delivery control, and to the brand
name's pronunciation.

## Brand name pronunciation

No provider reads the brand name correctly in French by default. The correction
is provider-specific and lives in each provider reference. Whichever is used, it
belongs in the transcript or in a pronunciation dictionary, never on screen.

When captions are later built from real word timestamps, the transcript renders
the spoken word inconsistently across takes. Substitute those variants back to
the correct on-screen spelling before captions are rendered.

## Lip sync: never reuse dialogue footage under swapped audio

If a clip was generated with native dialogue, its mouth is animated to specific
words. If the line later changes, even slightly, reusing that footage under a
new voice track reads as broken lip sync. Changing provider or voice counts as
changing the line.

The fix is to regenerate that shot as a non-verbal reaction clip, prompting
explicitly for listening, reacting, mouth mostly closed, not speaking, no
dialogue. Narration can then be laid over it freely, because no mouth movement
is baked in. Apply this proactively to any character shot whose line might
change across revisions, not only to shots that were silent from the start.

## Transcription is a separate choice

Word timestamps for captions come from transcribing the finished narration
track. The transcription provider is independent of the text-to-speech
provider: narration generated on one service can be timed with whichever
speech-to-text the toolchain offers. Do not switch narration provider merely to
match the transcriber.
