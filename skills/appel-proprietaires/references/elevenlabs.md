# ElevenLabs narration

Use this reference when ElevenLabs is the selected provider. Also follow the
provider-independent workflow in [narration.md](narration.md).

## Voice

- **Alimata**, voice ID `4SFJvuIUvxaPLgk8FoK3`. The default narrator for this
  ad format. Other packages in this repository label the same ID `Rapoko`, with
  the provider catalog name `Ropako-voice`; keep the exact ID and catalog name
  in manifests whichever label the copy uses.

Treat the name and ID mapping as user-provided voice-catalog metadata. Audition
the voice in French before a paid batch.

## Endpoint and delivery

Generate through the **plain text-to-speech endpoint**, with no bracketed
emotion tags. Moving this voice to the dialogue endpoint with stacked emotion
tags at low stability has been rejected by ear: it does not sound like the same
person, even with an identical voice ID. Take delivery and tone from
**punctuation** instead, using exclamation marks, ellipses, and question marks.

- Read credentials from `ELEVENLABS_API_KEY`; never expose or commit the value.
- Preserve the exact approved voice ID, model, output format, stability,
  similarity, style, speaker boost, and speed settings in the manifest.
- Prefer a stable multilingual model for French, and test the brand name, place
  names, and the phone number in the approval sample.
- Generate into isolated temporary storage, validate, then normalize and
  replace the stable paths.

## Brand name pronunciation

Spell the brand name `Rôogo` in the prompt text only, never on screen. This
spelling was confirmed by ear on short test clips. An intermediate attempt,
`Rougo`, overshot into a full French vowel and was rejected.

Transcripts of the result render the spoken word inconsistently across takes.
Substitute any of those variants back to the correct on-screen spelling before
captions are rendered.
