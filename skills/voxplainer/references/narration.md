# Production narration workflow

Use the user-selected TTS provider and voice as the narration source while keeping the integration replaceable and secrets safe. Read the matching provider reference after this file.

## Voxplainer default

Use ElevenLabs voice **Rapoko** as the primary narrative voice for editorial and
story-led productions. Its exact provider voice ID is
`4SFJvuIUvxaPLgk8FoK3`; ElevenLabs currently labels it `Ropako-voice`. Preserve
“Rapoko” as the public-facing Roogo character name and preserve the provider's ID
and catalog name in production metadata. For a calm, slower explanation of complex
material, Cartesia **Wendata Nathalie Kaoré** is an approved primary or supporting
narrator. Multi-voice productions may use **Salif**
(`16dba105-0026-4ff7-bf90-12562786a97c`) as host and **Sandrine** as tutorial
instructor. For literal step-by-step screen demonstrations, use an installed
Product Video / `product-demo-video` skill when available. Otherwise follow
[horizontal-product-explainer.md](horizontal-product-explainer.md) for safe capture
and evidence framing while preserving the requested walkthrough format. Keep
editorial product explainers in Voxplainer when the interface serves as evidence
inside a broader visual argument.

When using multiple voices, assign one stable role to each voice in the production
contract and mark all narrator changes before generation. Change voices only at
complete scene boundaries, never within a sentence. Generate and approve each voice
independently, normalize them to a common loudness target, and audit every handoff
for tone, pacing, captions, and semantic continuity. Multi-voice is a storytelling
choice, not a default requirement.

## Voice contract

Record the provider, selected voice or voice ID, model or pinned snapshot, language, accent, tone, pacing, pronunciation overrides, source loudness target, true-peak ceiling, and approval state in project configuration. Preserve a user-selected provider and voice exactly. If none is supplied, create a short voice-direction note and request a choice only when selecting incorrectly would cause paid regeneration or conflict with brand identity.

Do not imitate a real person's voice without the rights and authorization to use it.

The included voice IDs are Roogo configuration, not credentials or a grant of voice
rights. Availability can differ by provider account. Confirm authorized access before
generation; if the selected voice is unavailable, prepare the script and cue plan
while requesting an authorized replacement. Do not substitute another voice silently.

## Voice approval gate

A valid voice ID proves only that the provider can synthesize audio. It does not prove that the result sounds natural, fits the brand, or pronounces the script correctly.

1. Generate one representative sample before the full batch. Include the opening tone plus at least one difficult name, abbreviation, number, or emotionally important sentence when the script contains them.
2. Audition the actual file through an available audio playback or review path. If the environment cannot play audio, give the sample to the user and leave voice approval explicitly pending. Do not infer naturalness from waveform, metadata, provider reputation, or a successful API response.
3. After approval, record the exact provider, voice ID and settings and use them for the complete batch. Check the finished manifest against the request.
4. Do not carry pronunciation spellings from a different engine into the selected provider without testing them. Punctuation inserted to make one engine spell an abbreviation may create unnatural pauses in another.

A system or placeholder voice is allowed only for a timing draft. Mark it in the manifest and filename, keep it out of release masters, and never describe the resulting video as final unless the user explicitly approves that voice.

## Generation workflow

1. Finalize a narration draft and estimate duration before a billable generation.
2. Normalize abbreviations, dates, units, names, and numbers for the selected model without changing their meaning, then use the voice approval gate above.
3. Split long narration at stable scene or chapter boundaries so a small revision does not require regenerating the whole program.
4. Use the supported SDK or API available in the project. Consult current official documentation when an endpoint, model, version header or parameter matters; do not hardcode instructions copied from an outdated tutorial.
5. Read provider credentials from an environment variable. Keep local environment files ignored and never paste secrets into prompts, source files, screenshots, logs or rendered metadata.
6. Generate into an isolated temporary directory. Confirm the provider’s actual output filename, decode the result successfully, and only then atomically replace the stable segment path. A failed or oddly named provider output must not destroy previously approved audio.
7. Save audio with stable segment identifiers and a manifest containing script text, exact provider and voice settings, generation date, raw and processed durations, loudness targets, file path, and whether human listening approval occurred. Reuse unchanged approved segments.
8. Listen to the hook, the densest line, the call to action and any joins that change tone. For a short batch, prefer reviewing every segment. Flag mispronunciations, clipped boundaries, robotic cadence, unnatural emphasis, pacing jumps and inconsistent tone before animation is locked.

If live provider access is unavailable, continue with the approved script, pronunciation guide, segment manifest and estimated timing. Clearly mark placeholder timing and do not claim that final narration was generated.

## Timing Remotion to narration

Convert the duration of the final processed audio to frames using the composition frame rate. Normalization or transcoding happens before this measurement because processing can change boundaries slightly. Derive scene boundaries from semantic pauses and segment timing, not from evenly divided durations. Allow intentional breathing room around major claims while avoiding silent dead space. Validate programmatically that every scene allocation is longer than its processed narration.

For captions, prefer real alignment data. If only segment timestamps exist, align phrases within each segment and flag them for review. Do not treat text-length estimates as final synchronization.

## Deliberate pauses without sonic dropouts

A pause that gives a sentence time to land is a vocal pause, not necessarily total digital silence. Preserve the breath of the edit:

- shape the outgoing word with a short natural tail or roughly `150–250 ms` fade when an edit would otherwise cut it hard;
- let approved music, room tone, or restrained ambience continue underneath;
- keep the requested pause duration explicit in the timeline rather than stretching the whole scene unpredictably;
- crossfade edited narration segments when needed, but do not smear consonants or shorten the semantic pause;
- audition the complete encoded mix across the join.

Silence detection can confirm that audio exists, but it cannot prove that a pause sounds intentional. Reject a pause that resembles a mute button, clipped file boundary, or missing asset even when its numeric duration is correct.

For providers that support SSML breaks, prefer a provider-native break inside one scene-sized utterance over cutting two independently generated clips together. End the preceding sentence with its real punctuation, then add one supported break tag such as `<break time="1s"/>`, and keep the following sentence in the same request. Regenerate only that narration segment, then retime its captions from the processed waveform. Because an SSML break can reduce linguistic context across the boundary, audition the result; it is a controlled pause, not an automatic guarantee of natural delivery.

## Semantic-boundary pause map

Before generating narration, mark the places where the listener must understand a change in discourse. Do this before visual timing so animation follows speech rather than guessing at it.

- **Statement → question:** end the setup with its real punctuation, add one explicit break, then ask the question. Start around `500–750ms`; the listener should feel the setup land without hearing a mute-like hole.
- **Framing sentence → list:** finish the framing sentence, add a shorter break around `350–500ms`, then deliver the list with natural comma pacing. Do not run the first item into the setup.
- **Completed idea → new scene or premise:** use punctuation first. Add a `350–600ms` break only when the next clause introduces a distinctly new time, place, instruction, or decision.
- **Setup → quoted challenge:** place the break before the question itself, not after its first words.

Do not add a break after every sentence mechanically. Cartesia notes that breaks reduce surrounding context and several tags in quick succession can sound unnatural. Use one tag per meaningful boundary, keep the surrounding text in the same scene-sized request, and let punctuation handle ordinary phrasing.

After synthesis, run a boundary-completeness review. For every explicit break and every scene join, verify that the final content word before the boundary is fully spoken—including its last syllable—and that the first word after it is not clipped. A correct amount of measured silence does not pass if a word such as “réelle” is swallowed. Regenerate the smallest affected narration segment and retime captions from the processed audio.

## Audio finishing and review

Provider audio can be natural yet unexpectedly quiet or inconsistent across clips. Use this order:

1. Decode and probe every generated source.
2. Normalize narration clips consistently before retiming. When the project has no target, −16 LUFS integrated with a −1.5 dBTP ceiling is a useful speech-first starting point, not a universal platform requirement. Prefer two-pass EBU R128 normalization for release assets when practical; verify short clips even when a one-pass workflow is used.
3. Re-probe the processed duration and use that value for scenes and captions.
4. Render the real mix, then measure the encoded master with an integrated-loudness meter. Do not use `mean_volume` as a substitute for LUFS.
5. Listen to the encoded master on ordinary speakers or headphones. Metrics can reveal clipping and level problems; they cannot identify robotic delivery, wrong emphasis or distracting joins.

Record both source and master targets in the production contract. Duck music and sound effects under speech, check for audible edits between generated segments, and revise gain or normalization when the master misses the documented target.

Run the bundled checker against processed clips and masters when `ffmpeg` and `ffprobe` are available:

```bash
python3 scripts/audio_quality_gate.py path/to/clip.mp3 path/to/master.mp4
```

It reports decoding metadata, integrated LUFS and true peak, and fails when the default acceptance window is missed. Override its bounds only to match a documented production contract—not merely to make a failing file pass.
