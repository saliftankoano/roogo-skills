# ElevenLabs narration and dialogue

Use this reference when ElevenLabs is the selected provider. Also follow the
provider-independent workflow in
[narration-and-voice.md](narration-and-voice.md).

## Cast

- **Alimata**, voice ID `4SFJvuIUvxaPLgk8FoK3`. The default narrator. Other
  packages in this repository label the same ID `Rapoko`, with the provider
  catalog name `Ropako-voice`; keep the exact ID and catalog name in manifests
  whichever label the copy uses.
- **Jerome**, voice ID `YwEKgPNrswweXodAZi29`. A male African-accented voice,
  identified by the user as Cameroonian. Used for named characters.
- **Isac**, voice ID `SomyDQQmnE7TsltdiDgp`. A second male character voice.

Treat these names and ID mappings as user-provided voice-catalog metadata.
Reuse a character voice when the requester asks for it by name or by exact ID;
do not substitute one for another without approval.

## The narrator uses the plain endpoint

Generate the narrator through the **plain text-to-speech endpoint**, with no
bracketed emotion tags.

An attempt to move her to the dialogue endpoint with stacked emotion tags at low
stability was rejected outright: it does not sound like the same person, even
with an identical voice ID. Take delivery and tone from **punctuation** instead:
exclamation marks, ellipses, question marks.

## Named characters use the dialogue endpoint

Characters playing a role use the **dialogue endpoint**, with one entry in the
speaker list and one or two bracketed emotion tags prefixed to the line, for
example `[resigned, quietly disappointed]` or `[pleased, confident, warm]`, at
stability around 0.45.

The endpoint reads bracketed tags as delivery direction and never speaks them
aloud, confirmed by transcribing the result. Three or more tags, or stability
below about 0.35, reads as overacted and robotic rather than expressive.

## Credentials and settings

- Read credentials from `ELEVENLABS_API_KEY`; never expose or commit the value.
- Preserve the exact approved voice IDs, model, output format, stability,
  similarity, style, speaker boost, and speed settings in the manifest.
- Prefer a stable multilingual model for French, and test the brand name and any
  numeric claim in the approval sample.
- Generate scene-sized files into isolated temporary storage, validate them,
  then normalize and replace the stable paths.

## Brand name pronunciation

Spell the brand name `Rôogo` in narration and dialogue prompt text only, never
on screen. This was confirmed correct by ear on short test clips. An
intermediate attempt, `Rougo`, overshot into a full French vowel and was
rejected as well.
