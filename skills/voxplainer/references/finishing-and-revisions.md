# Finishing and revision workflow

Read this reference when revising an existing cut, adding music or effects, designing its ending, or rendering a release candidate.

## Turn feedback into a change contract

Translate every note into four fields before editing: the exact scene or time range, the visible or audible defect, the requested change, and what must remain unchanged. When a screenshot contains arrows or numbered annotations, use them only to locate the feedback; do not reproduce the marks in the video.

Preserve the previous master. Render revisions to a versioned filename until the user explicitly chooses a replacement. Do not deploy, publish or overwrite a live asset unless the user asks.

When a defect is isolated, replace the smallest stable unit: one narration segment, one scene, one sound cue, or one outro. Preserve the unaffected remainder and the previous master. Re-render the whole encoded deliverable only to assemble and validate the corrected units.

## Music and effects

- Treat a relative request literally. For “increase the music by 8%,” multiply the existing music gain by `1.08`; do not add eight percentage points or change narration gain to simulate the result. Keep this multiplier visible in configuration or code.
- Measure and audition the complete encoded mix after any gain change. Check integrated LUFS and true peak; `mean_volume` is not a loudness substitute. A safe peak does not prove that speech remains intelligible.
- Duck music under speech when necessary. If the ending is music-only, a modest lift may begin after the final spoken phrase, followed by a deliberate fade.
- Effects are optional. Keep only effects whose timing and character clearly reinforce the pictured action. Remove them when they feel ornamental, mismatched, repetitive or compete with narration. A clean narration-and-music mix is preferable to forcing prepared assets into the edit.
- When a spoken pause is requested, encode it in narration or the timeline as an explicit duration and verify it by listening; punctuation alone is not deterministic across TTS engines. Preserve a natural vocal tail and let the underlying bed or room tone continue so the pause does not resemble an abrupt mute.
- If a provider supports SSML pauses, keep the punctuation before the break tag and generate the two spoken clauses in one scene-sized request. Avoid hand-splicing independent TTS files unless the provider-native result is unusable; hard joins can create resonance, duplicated room tone, or mute-like dropouts.
- Before generation, identify statement-to-question, framing-to-list, and premise-to-new-scene boundaries. Give these one deliberate provider-native break when comprehension needs it, then verify the final word before the break and first word after it are complete.

## Pronunciation continuity

Maintain two forms for names that need help: the display spelling used on screen and a tested spoken form used only in the TTS transcript or pronunciation dictionary. Record both in the narration manifest. Test the name in a representative sample and at least one sentence join. Do not change on-screen brand spelling to force pronunciation.

## Language, overlays, and caption integrity

- Proofread spoken copy, captions, and interface text as natural language. A grammatically possible literal translation can still be wrong in context; review verbs, idioms, local usage, and product terminology explicitly.
- Keep the canonical on-screen spelling separate from any phonetic TTS spelling. Captions use the canonical form.
- Time narration-named labels and lists to the words that introduce them. Items should not all exist before they are spoken, and they should retain subtle life after landing rather than becoming inert stickers.
- Treat faces and emotionally important gestures as protected visual zones. Reposition, simplify, or stagger overlays instead of covering the character's eyes, mouth, or expression.
- Put captions in a control-safe mid-lower band, not against the bottom edge. Test the encoded deliverable at its actual display size with native playback controls visible.
- Segment captions into complete, readable phrases rather than rapidly replacing
  tiny word fragments. Use word timing to place phrase boundaries, not to force every
  word into a separate visual event. Give each phrase a stable reading hold, avoid
  back-to-back flashes, and merge very short adjacent cues when meaning and timing
  permit. Review at normal speed and at the target viewing size.
- Treat caption collision, mistranslation, and a wrong brand pronunciation as release-blocking defects even when the render is technically valid.

## Review-render contract

A silent render is an internal visual preflight only. Label it `silent`, keep it out
of user-facing approval indexes unless the review is explicitly visual-only, and do
not treat it as a rough cut or release candidate. When the production contract names
a narrator, every user-facing rough cut and master must contain the approved voice,
unless the user explicitly asks to review picture without sound.

## Ending architecture

A reliable explainer ending has two distinct beats:

1. The final narrated card completes the argument. Its main illustration, message and any CTA settle fully. Disable automatic outgoing wipes or exit transforms on this scene unless the transition into the outro has been intentionally designed and reviewed.
2. Reserve roughly 3–5 seconds for a music-only brand outro. Use a centered, enlarged logo and the full destination URL. Avoid new narration, dense copy or new ideas. Hold the complete composition through the final video frame while fading the music over roughly the final 2–3 seconds.

If the user removes a CTA from the final narrated card, do not silently reintroduce it in the outro. A URL may remain as destination context unless the user also removes that.

Removal QA must inspect a settled frame and the encoded tail. Remove the label, background, hit area, entrance/exit animation, and any duplicate brand token—not just the most visible rectangle.

## Narrative sound effects

Treat sound effects as brief evidence of an on-screen action, not as a second soundtrack. Preserve the supplied source and create a derived, clearly named production clip. Trim to the shortest recognizable burst, add short edge fades, lower it beneath narration, and synchronize its entrance with the visual action and spoken verb. For repeating source audio such as ringing or vibration, use one clean burst unless repetition is part of the story. Review the effect in the full mix; a technically quiet effect can still distract if it arrives early or continues after the action has resolved.

## Visual substitutions

When replacing an abstract monogram or placeholder with meaning-bearing imagery, express the requested idea as a simple visual relationship rather than another label. For collaboration, for example, show multiple people connected to shared work, evidence or an outcome. For skills, use recognizable pictograms plus short labels and animate them with restrained orbital or staged motion around the subject. Keep the subject as the focal point.

Prefer a user-provided, locally accurate asset when it already communicates the requested place or symbol. If the requested operation is background removal, isolation, cleanup, or reframing, edit that asset rather than regenerating a look-alike. Preserve the source and record the derived asset. Use meaningful local imagery or a brand-specific quiet texture instead of generic filler dots.

Use semantic icons from one coherent system. Evaluate the icon without its label; if it could plausibly mean something else, replace it. Do not preserve a weak placeholder simply because it is already animated.

## Transition continuity

For every full-frame wipe or carried color, record the outgoing scene, transition color, and incoming background. Default the terminal transition color to the incoming background so the wipe completes into the next scene. Review at least one frame before the wipe, its full-coverage frame, and the first settled incoming frame. A mismatched flash is a defect unless it expresses a deliberate narrative rupture.

Keep transitions between similar interface states short enough that old and new text
do not coexist as a distracting double image. Inspect the transition at full speed
for ghosting, rippling, warped edges, and illegible intermediate states; a transition
that makes authentic UI look synthetic fails even when both endpoint frames are good.

When revising repeated objects without extending duration, preserve the scene boundary and compress the choreography: use shorter individual entrances, overlapping stagger, and faster settling. Verify the last item finishes before the handoff.

## Evidence before the full render

Render stills before spending time on the complete export:

- the revised dense or annotated scene;
- the final narrated card after all elements have settled;
- the middle of the music-only outro;
- the intended final frame.

For a meaningful landmark outro, also render an alpha/color proof showing the asset at full opacity over the exact brand background. Prefer a clean three-layer stack—background, landmark, text—before introducing decorative patterns or full-frame tints.

For an outro that continues a narrative location, render a proof against the complete approved scene. A floating isolated character, missing table, clipped room, or other incomplete environment is a release-blocking defect even if the brand lockup itself is correct.

After the full render:

1. Decode the entire master with FFmpeg or an equivalent decoder.
2. Probe duration, dimensions, frame rate, codecs, sample rate and channel count.
3. Measure integrated loudness and true peak.
4. Extract a frame from the encoded file within roughly the final 100 ms and inspect it. A source-code still is insufficient because duration, transition and encoding defects can appear only in the master.
5. Watch and listen across the last narrated phrase, the cut into the outro and the final fade. Confirm that no old transition briefly exposes fragments or blank color.
6. Run the selected visual mode's encoded review passes and answer its acceptance question with observed evidence, not intent.
7. Watch once at target phone or desktop size with player controls visible, verifying caption placement, URL legibility, and safe areas.

Record the revised filename, runtime, mix measurements and review evidence in the delivery report.
