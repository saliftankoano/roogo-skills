# ElevenLabs narration

Use this reference when ElevenLabs is the selected narration provider. Also follow the provider-independent approval, timing and audio-finishing workflow in [narration.md](narration.md).

## Named reusable voice

- **Rapoko** — voice ID `4SFJvuIUvxaPLgk8FoK3`; provider catalog name
  `Ropako-voice`. This is the default for Roogo editorial explainers, motion
  explainers, Layered 2.5D films, Cinematic Parallax films, and story-first work.
  Use “Rapoko” in public-facing labels while retaining the exact provider catalog
  name and ID in manifests.
- **Jérôme** — voice ID `YwEKgPNrswweXodAZi29`. The user identifies this as a male African-accented voice from Cameroon.

Treat these names, identity descriptions, and ID mappings as user-provided
voice-catalog metadata. Rapoko is the Voxplainer default. Reuse Jérôme when the user
asks for Jérôme or selects his exact ID; do not substitute Jérôme for Rapoko without
approval. Audition the selected voice in the target language and context before a
paid batch.

- Read credentials from `ELEVENLABS_API_KEY`; never expose or commit the value.
- Preserve the exact user-approved voice ID, model, output format, stability, similarity, style, speaker-boost and speed settings in the manifest.
- Use the current supported SDK or API and consult official documentation before choosing a model or parameter set.
- Prefer a stable multilingual model for French narration and test acronyms, names and numeric claims in the approval sample.
- Generate scene-sized files into isolated temporary storage, validate them, then normalize and atomically replace the stable paths.
