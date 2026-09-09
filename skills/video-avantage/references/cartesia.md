# Cartesia narration and dialogue

Use this reference when Cartesia is the selected provider. Also follow the
provider-independent workflow in
[narration-and-voice.md](narration-and-voice.md).

ElevenLabs remains the default for this format. Cartesia is approved when the
requester asks for it, when a needed voice is unavailable, or when the cast is
better served by its approved voices.

## Approved cast

- **Sandrine**, voice ID `2435841c-fce7-4fd5-aed1-dc7008eb7d20`; provider
  catalog name `Sandrine rtb`. Approachable instructor register; the narrator
  role for this format on Cartesia.
- **Salif**, voice ID `16dba105-0026-4ff7-bf90-12562786a97c`; provider catalog
  name `Salif voice`. Host and presenter; a named character or an on-camera
  presenter beat.
- **Wendata Nathalie Kaoré**, voice ID
  `fe4cf239-7292-499d-95a1-59c03e9caf2f`. Slower, careful delivery for complex
  material; use when a comparison card needs the numbers landed deliberately.

Treat these names and ID mappings as user-provided voice-catalog metadata.
Choose by narrative function, not by novelty, and audition every selected voice
in French before a paid batch. Model level language support does not prove that
an individual voice is a good language or brand fit.

In a multi-voice film, keep each voice on complete scene-sized segments, declare
its role, and loudness-match the handoffs.

## Direction without emotion tags

Cartesia has no bracketed emotion-tag convention, and pasting ElevenLabs-style
tags into a transcript risks having them spoken aloud. Direct delivery instead
through, in order of preference:

1. **Casting.** Pick the voice whose native register already matches the beat.
   A resigned line and a confident line are usually two different voices in this
   format anyway, because they are two different characters.
2. **Punctuation.** Question marks, ellipses, and sentence length carry most of
   the delivery.
3. **Break tags**, for a deliberate silence before a question, a list, or a new
   premise, for example
   `Et le résultat ?<break time="600ms"/>Deux fois plus.` Keep the punctuation
   before the tag and do not chain tags; chains split linguistic context and
   produce unnatural delivery.
4. **The optional speed, emotion, and volume controls**, last. Do not touch them
   until the unmodified sample has been auditioned. When one is used, record it
   in the manifest and regenerate the approval sample, because it can materially
   change delivery.

Verify by transcribing a sample that no markup was spoken aloud, exactly as was
done when the tag convention was validated on the other provider.

## Production defaults

- Read credentials from `CARTESIA_API_KEY`; never expose or commit the value.
  On macOS, a reusable alternative is a generic login-Keychain item with service
  `ai.cartesia.api-key` and account `default`. Retrieve only the password with
  `/usr/bin/security find-generic-password -s ai.cartesia.api-key -a default -w`,
  without printing or logging it.
- For a known script, prefer the bytes endpoint or the official SDK's
  file-generation method. WebSocket and SSE add nothing when the transcript is
  already written and approved.
- Set the language to `fr`.
- Prefer `sonic-3.5`. Pin a dated stable snapshot when a build must be
  reproducible; do not use a floating latest alias for a delivered video.
- Generate a lossless WAV source at 44.1 or 48 kHz, then normalize and encode
  the delivery format. Do not use raw PCM unless the caller also records and
  applies its encoding metadata.

## API shape

Use the current official SDK or `POST /tts/bytes` with the required API version
header. A typical request contains:

- `model_id`: the chosen stable Sonic model or pinned snapshot;
- `transcript`: one complete scene-sized utterance;
- `voice`: ID mode with the approved voice ID;
- `language`: `fr`;
- `output_format`: WAV, `pcm_s16le`, 44.1 kHz.

## Brand name pronunciation

Generate a plain-transcript sample first. Only if the brand name is wrong,
correct it with a Cartesia pronunciation dictionary on a current Sonic model and
store the dictionary ID in the voice contract. Do not carry the ElevenLabs
respelling across providers; it is a workaround for a different model and can
make this one worse.

Confirm the corrected pronunciation by ear before building the full video.

## Lip sync

A character line generated here cannot be laid under footage whose mouth was
animated to a take from another voice or another provider. Regenerate that shot
as a non-verbal reaction clip instead; see
[narration-and-voice.md](narration-and-voice.md).
