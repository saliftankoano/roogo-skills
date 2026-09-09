# Cartesia narration

Use this reference when Cartesia is the selected narration provider. Also follow the provider-independent approval, timing and audio-finishing workflow in [narration.md](narration.md).

Rapoko remains the primary ElevenLabs narrative voice for editorial and story-led
work. Cartesia is approved when the explanatory or multi-voice structure benefits
from one of these roles. For product demos, Salif is the default. An installed
Product Video / `product-demo-video` skill can assist with walkthrough capture; when
unavailable, use [horizontal-product-explainer.md](horizontal-product-explainer.md)
for safe capture and evidence framing while preserving the requested format.

## Approved reusable voices

- **Salif** — voice ID `16dba105-0026-4ff7-bf90-12562786a97c`; provider catalog
  name `Salif voice`; host and product presenter.
- **Sandrine** — voice ID `2435841c-fce7-4fd5-aed1-dc7008eb7d20`; provider catalog
  name `Sandrine rtb`; approachable tutorial instructor.
- **Wendata Nathalie Kaoré** — voice ID
  `fe4cf239-7292-499d-95a1-59c03e9caf2f`; slower, careful explanation of complex
  material.

Treat these name and ID mappings as user-provided voice-catalog metadata. Choose by
narrative function and audition every selected voice in the target language before
a paid batch. In a multi-voice film, keep each voice on complete scene-sized
segments, declare its role, and loudness-match the handoffs.

## Production defaults

- Read credentials from `CARTESIA_API_KEY`; never expose or commit the value. On macOS, a reusable alternative is a generic login-Keychain item with service `ai.cartesia.api-key` and account `default`. Retrieve only the password with `/usr/bin/security find-generic-password -s ai.cartesia.api-key -a default -w`, without printing or logging it.
- For offline scene narration, prefer the bytes endpoint or official SDK file-generation method. WebSocket and SSE add no value when the full scene transcript is already known.
- Use French language guidance (`fr`) for French narration.
- Prefer `sonic-3.5` for current development. Pin a dated stable snapshot in a release contract when reproducibility matters; do not use `sonic-latest` for a release master.
- Generate a lossless WAV source at 44.1 or 48 kHz, then normalize and encode the project delivery format. Do not use raw PCM unless the caller also records and applies its encoding metadata.
- Preserve the exact voice ID supplied by the user and audition it in the target language. Model-level language support does not prove that an individual voice is a good language or brand fit.

## API shape

Use the current official Cartesia SDK or `POST /tts/bytes` with the required API version header. A typical file-generation request contains:

- `model_id`: the chosen stable Sonic model or pinned snapshot;
- `transcript`: one complete scene-sized utterance;
- `voice`: ID mode with the approved voice ID;
- `language`: `fr` for French;
- `output_format`: WAV, `pcm_s16le`, 44.1 kHz.

Avoid optional speed, emotion and volume controls until the unmodified sample has been auditioned. When controls are used, record them in the manifest and regenerate the approval sample because they can materially change delivery.

For precise semantic pauses, use Cartesia's supported break syntax inside the transcript, for example `Phrase terminée.<break time="650ms"/>Question suivante ?`. Keep the punctuation before the tag and do not require whitespace around it. Punctuation remains the primary pacing tool; reserve `break` for a specific silence before a question, list, new premise, or other deliberate boundary. Avoid chains of break tags because they split linguistic context and can produce unnatural delivery.

Pronunciation dictionaries are available on current Sonic models. Use one only after a plain-transcript sample proves a name or domain term needs correction, and store the dictionary ID in the voice contract.
