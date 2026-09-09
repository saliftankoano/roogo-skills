# Narration and character voice

Two roles, two different techniques. Getting this wrong is the single most
likely reason a finished video is rejected.

## Narrator

Use the Roogo narrator voice **Alimata**, ElevenLabs voice ID
`4SFJvuIUvxaPLgk8FoK3`, always through the **plain text-to-speech endpoint**,
with no bracketed emotion tags.

An attempt to move her to the dialogue endpoint with stacked emotion tags at
low stability was rejected outright: it does not sound like the same person,
even with an identical voice ID. Take delivery and tone from **punctuation**
instead: exclamation marks, ellipses, question marks.

## Named characters

Characters playing a role use the **dialogue endpoint**, one entry in the
speaker list, with one or two bracketed emotion tags prefixed to the line, for
example `[resigned, quietly disappointed]` or `[pleased, confident, warm]`, and
stability around 0.45. The endpoint reads bracketed tags as delivery direction
and never speaks them aloud, confirmed by transcribing the result. Three or
more tags, or stability below about 0.35, reads as overacted and robotic.

Give every voice a stable story role and switch only at scene boundaries.

## Voice rights

Publishing a voice ID is configuration, not permission. Confirm the account has
access and the right to use each voice before generating. If one is
unavailable, ask for an authorized alternative rather than substituting one
silently.

## Brand name pronunciation

The French model does not read the brand name correctly by default. Spell it
`Rôogo` in narration and dialogue prompt text **only**, never on screen. This
was confirmed correct by ear on short test clips. An intermediate attempt,
`Rougo`, overshot into a full French vowel and was rejected as well.

When captions are later built from real word timestamps, the transcript renders
the spoken word inconsistently across takes. Substitute any of those variants
back to the correct on-screen spelling.

**General rule for anything sound-dependent:** never guess and rebuild a slow,
costly video around the choice. Generate a short, cheap standalone test clip of
just the disputed line or word and have the requester confirm by ear first.

## Lip sync: never reuse dialogue footage under swapped audio

If a clip was generated with native dialogue, its mouth is animated to specific
words. If the line later changes, even slightly, reusing that footage under a
new voice track reads as broken lip sync.

The fix is to regenerate that shot as a non-verbal reaction clip, prompting
explicitly for listening, reacting, mouth mostly closed, not speaking, no
dialogue. Narration can then be laid over it freely, because no mouth movement
is baked in. Apply this proactively to any character shot whose line might
change across revisions, not only to shots that were silent from the start.
