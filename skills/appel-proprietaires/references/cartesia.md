# Cartesia narration

Use this reference when Cartesia is the selected provider. Also follow the
provider-independent workflow in [narration.md](narration.md).

ElevenLabs remains the default narrator for this ad format. Cartesia is
approved when the requester asks for it, when the default voice is
unavailable, or when the ad wants a warmer, more instructional register.

## Approved voices

- **Sandrine**, voice ID `2435841c-fce7-4fd5-aed1-dc7008eb7d20`; provider
  catalog name `Sandrine rtb`. Approachable instructor register; the narrator
  role for this ad format on Cartesia.
- **Salif French**, voice ID `16dba105-0026-4ff7-bf90-12562786a97c`;
  French (`fr`) host/presenter when the requester selects Salif's own voice.
- **Salif English**, voice ID `c84975e2-dba8-45ae-9fd7-53f2590ea7d2`;
  English (`en`) host/presenter for an explicitly approved English adaptation.

Salif supplied his two own-voice mappings for reuse on 2026-09-09. Match his
selected voice to the approved narration language; ask if ambiguous. These options
do not change the format's French-language default or Sandrine's narrator role,
replace an approved voice, authorize paid generation, grant other users voice
rights, or overwrite saved provider profiles.

Treat the name and ID mapping as user-provided voice-catalog metadata. Choose by
narrative function, and audition the voice in the approved language before a paid batch. Model
level language support does not prove that an individual voice is a good
language or brand fit, and this format's audience judges the voice immediately.

Keep one voice for the whole ad. This format is a single narrator speaking to
owners; a mid-ad voice change reads as two different advertisers.

## Production defaults

- Read credentials from `CARTESIA_API_KEY`; never expose or commit the value.
  On macOS, a reusable alternative is a generic login-Keychain item with service
  `ai.cartesia.api-key` and account `default`. Retrieve only the password with
  `/usr/bin/security find-generic-password -s ai.cartesia.api-key -a default -w`,
  without printing or logging it.
- For a known script, prefer the bytes endpoint or the official SDK's
  file-generation method. WebSocket and SSE add nothing when the full transcript
  is already written and approved.
- Set the language to `fr`, or `en` for an explicitly approved English adaptation.
- Prefer `sonic-3.5`. Pin a dated stable snapshot when a build must be
  reproducible; do not use a floating latest alias for a delivered ad.
- Generate a lossless WAV source at 44.1 or 48 kHz, then normalize and encode
  the delivery format. Do not use raw PCM unless the caller also records and
  applies its encoding metadata.

## API shape

Use the current official SDK or `POST /tts/bytes` with the required API version
header. A typical request contains:

- `model_id`: the chosen stable Sonic model or pinned snapshot;
- `transcript`: one complete section of the approved script;
- `voice`: ID mode with the approved voice ID;
- `language`: `fr`, or `en` for an approved English adaptation;
- `output_format`: WAV, `pcm_s16le`, 44.1 kHz.

Avoid the optional speed, emotion, and volume controls until the unmodified
sample has been auditioned. When a control is used, record it in the manifest
and regenerate the approval sample, because it can materially change delivery.

## Pacing and the phone number

Punctuation remains the primary pacing tool. For a deliberate silence before the
call to action or before the phone number, use the supported break syntax inside
the transcript, for example
`Votre maison correspond ?<break time="650ms"/>Appelez maintenant.` Keep the
punctuation before the tag, and do not chain break tags: chains split
linguistic context and produce unnatural delivery.

Still write the number as French number pairs in the transcript, and still
re-transcribe the generated segment in isolation to confirm the digits come back
grouped. The pairing rule is about how the number is written, not about which
provider reads it.

## Brand name pronunciation

Generate a plain-transcript sample first. Only if the brand name is wrong,
correct it with a Cartesia pronunciation dictionary on a current Sonic model and
store the dictionary ID in the voice contract. Do not carry the ElevenLabs
respelling across providers; it is a workaround for a different model and can
make this one worse.

Confirm the corrected pronunciation by ear before building the full ad.
