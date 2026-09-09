---
name: voxplainer
description: Create research-led editorial explainer videos as vertical social shorts, horizontal YouTube long-form, or horizontal product explainers, including scripting, visual beat planning, production TTS narration, Remotion production, and render review. Use when a user wants a polished visual explainer rather than a talking-head edit, generic slideshow, or literal screen-recording walkthrough.
---

# Voxplainer

Create clear, energetic editorial explainers in a distinctive system derived from the user's subject and brand. The name describes the format; do not copy Vox branding, logos, proprietary artwork, or a particular published video shot-for-shot.

## Route the format

- For a 9:16 YouTube Short, TikTok, Reel, or other social video, read [references/shorts.md](references/shorts.md).
- For a 16:9 YouTube long-form video, read [references/long-form.md](references/long-form.md).
- For a 16:9 product or feature explainer that should feel editorial rather than like
  a screen recording, read both [references/long-form.md](references/long-form.md)
  and [references/horizontal-product-explainer.md](references/horizontal-product-explainer.md).
- Before creating visual beats, select one of the three production grammars in [references/visual-modes.md](references/visual-modes.md): **Editorial Motion**, **Cinematic Parallax**, or **Layered 2.5D**. Treat them as complementary options, not quality tiers or replacements.
- When selecting **Editorial Motion**, read [references/editorial-motion.md](references/editorial-motion.md) before designing graphics or choreography.
- When selecting **Cinematic Parallax**, read [references/cinematic-parallax.md](references/cinematic-parallax.md) before selecting or generating imagery.
- When a person-centered story, emotional attachment, or narrative product film is requested, read [references/story-first.md](references/story-first.md).
- When selecting **Layered 2.5D**, read [references/layered-2-5d.md](references/layered-2-5d.md) before generating images or implementing scenes.
- Whenever generating, revising, or timing narration, read [references/narration.md](references/narration.md). Then read only the selected provider reference: [Cartesia](references/cartesia.md) or [ElevenLabs](references/elevenlabs.md).
- Whenever sourcing, downloading, editing, or redistributing third-party icons,
  photography, footage, music, or sound effects, read
  [references/asset-provenance.md](references/asset-provenance.md). An asset being
  free to download does not establish its commercial-use or redistribution rights.
- Default editorial explainers, Editorial Motion films, Layered 2.5D films,
  Cinematic Parallax films, and story-first productions to ElevenLabs using the
  Roogo character voice **Rapoko** (`4SFJvuIUvxaPLgk8FoK3`; provider catalog name
  `Ropako-voice`). For complex teaching-led explainers, Cartesia **Wendata Nathalie
  Kaoré** (`fe4cf239-7292-499d-95a1-59c03e9caf2f`) is an approved slower-paced
  alternative. Multi-voice films may also use Cartesia **Salif**
  (`16dba105-0026-4ff7-bf90-12562786a97c`) as host and **Sandrine**
  (`2435841c-fce7-4fd5-aed1-dc7008eb7d20`) as tutorial instructor. Give every
  voice a stable story role and switch only at scene boundaries. Literal step-by-step screen
  demonstrations belong to `$product-demo-video`; editorial product explainers may
  remain in Voxplainer and use interface captures as evidence inside the story.
- Whenever revising a rendered video, mixing music or effects, designing the final card, or producing a release master, read [references/finishing-and-revisions.md](references/finishing-and-revisions.md).
- When the user wants the explainer to feel cinematic, like an animated movie, or asks for richer staging and full-element animation, read [references/animated-film.md](references/animated-film.md).
- If the user requests both formats, establish one research and story core, then create two independently composed edits. Do not produce the short by mechanically cropping the long-form render.

Preserve any duration, aspect ratio, frame rate, language, brand system, toolchain, or delivery specification supplied by the user. Otherwise use the relevant reference defaults and state them briefly.

## Establish the production contract

Before implementation, resolve from the request and available files:

- audience, desired takeaway, platform, duration, call to action, and tone;
- factual claims requiring research or citations;
- brand assets, footage, illustrations, data, maps, and usage constraints;
- narration provider, voice or voice ID, pronunciation needs, and narration language;
- delivery scope: concept, script, storyboard, preview, or final rendered video.

Make reasonable reversible assumptions when inputs are absent. Ask only when a missing choice would materially change the story or incur an external cost the user has not authorized.

## Build from story to frames

1. **Research the claim.** Separate verified facts from hypotheses. For factual or current topics, use authoritative sources, retain a source ledger, and make dates and units explicit. Never invent statistics or citations.
2. **Write for listening.** Create a spoken script with a clear premise, causal progression, concrete language, and no unsupported rhetorical inflation. Read it aloud or estimate the actual spoken duration before locking it.
3. **Choose a visual grammar.** Select Editorial Motion, Cinematic Parallax, Layered 2.5D, or a deliberate hybrid according to the story's needs, revision cost, available assets, and desired emotional immediacy. Load the selected mode reference, record why the mode serves the argument, and write its mode-specific acceptance question into the storyboard review notes.
4. **Create visual beats.** Give every line a visual job. Prefer evidence, diagrams, maps, comparisons, timelines, and purposeful typography over decorative motion.
5. **Define scenes.** For each scene record its narration, intended duration, start frame, end frame, layers, motion, transition, transition color, assets, and factual source. Mark semantic narration boundaries before generation—especially setup-to-question, framing-to-list, and premise-to-new-scene—and assign explicit provider-native breaks only where comprehension needs them. Also record what changes emotionally, which element causes that change, which face or gesture zones must remain unobstructed, and which visual action hands the story into the next scene. Treat reference screenshots as composition and motion evidence, not assets to copy blindly. When a wipe or color field introduces the next scene, derive its color from the incoming scene unless a deliberate contrast has been justified.
6. **Approve and finish narration before timing.** Generate a representative sample with the requested provider and voice, then audition it before a paid batch. Generate scene-sized clips only after the voice is accepted, validate and normalize the clips, then probe the processed files again. The final processed audio—not the raw provider download or a placeholder voice—is the timing backbone for scene boundaries and captions.
7. **Implement reproducibly.** Prefer Remotion for programmable scenes unless the user chose another stack. Keep content, timing, design tokens, assets, and scene components separable enough to revise without rebuilding the entire edit.
8. **Review rendered evidence.** Apply the selected mode's review passes to representative stills and an encoded preview. Include the final narrated card, the first outro frame, both sides of every important transition, and a frame extracted from the encoded master near its actual end. Review audio across deliberate pauses and joins rather than only measuring silence. Revise concrete defects such as crowding, weak contrast, abrupt easing, dead time, incorrect map geometry, caption collisions, claims appearing without evidence, layer seams, edge halos, semantic icon errors, insufficient motion, mismatched transition color, abrupt sonic muting, or half-completed closing transitions.
9. **Deliver clearly.** Provide the requested render and, when in scope, the editable project, narration file, caption file, asset/source ledger, and exact preview/render commands.

## Editorial visual language

Create a coherent system before polishing individual scenes:

- a compact type scale with one dominant message at a time;
- an intentional palette with one highlight color and sufficient contrast;
- consistent strokes, arrows, labels, textures, and image treatment;
- staged motion with readable entrances, holds, emphasis, and exits;
- camera movement motivated by a change in scale, location, or argument;
- transitions that connect ideas rather than merely decorate cuts.

Use recognizable, meaning-bearing icons. Prefer a coherent established icon set such as Phosphor when code-native icons are appropriate. Reject placeholder geometry whose meaning depends on the nearby label.

Avoid accidental stillness. An active scene should have a clear primary action, supporting reactions, and subtle environmental life. Elements may hold still only when the pause is deliberate and helps the viewer feel or understand a beat.

Use kinetic text selectively for the words that carry the argument. Keep important content inside platform-safe areas. When maps are needed, use accurate vector or GeoJSON boundaries rather than guessed polygons. When an illustration generator produces a weak or inconsistent asset, replace it with a curated, editable asset instead of hiding the defect with more animation.

## Make feedback operational

Avoid prompts such as “make it better” or “more polished.” Diagnose and specify the change:

- what is wrong;
- where and when it occurs;
- the desired visible behavior;
- what must remain unchanged;
- the evidence used to accept the revision.

Render key frames early: opening composition, major transition frames, densest information frame, and end card. Then review the full preview for pacing, audio sync, caption timing, transition continuity, and encoding artifacts.

## Completion checks

Before calling a video complete, verify:

- the hook and final takeaway are immediately understandable;
- every important claim is accurate and traceable;
- visuals advance the explanation instead of echoing narration generically;
- the selected visual mode passes its own acceptance question and review passes;
- every active element enters, acts or reacts, and exits or transforms with a visible narrative purpose;
- the edit has no unintended frozen tableau, lifeless background, or transition that resets the world without a story reason;
- the last narrated scene resolves fully before a deliberate end hold or music-only outro, and the final encoded frame contains no partial wipe, clipped logo or departing element;
- narration, scenes, captions, music, and sound effects are synchronized;
- narrative sound effects use only the shortest recognizable action cue, are faded at their edges, sit below narration, and preserve the supplied source as a separate asset;
- deliberate spoken pauses preserve sonic continuity through natural vocal tails, room tone, or continuing music rather than sounding like the entire mix was abruptly muted;
- every question, list, and new-premise boundary has been audited for understandable spacing, and the final word before each break is fully pronounced;
- each scene uses one approved brand mark unless intentional repetition has been reviewed, and requested removals are absent from settled frames and the encoded tail;
- the narration manifest matches the user-approved provider and voice ID and no placeholder or system voice is presented as final;
- any user-facing review or release render that promises narration contains the approved voice; silent renders are labeled and used only as internal visual preflights;
- the voice was audibly reviewed for naturalness, pronunciations and joins; technical success or a valid voice ID alone does not satisfy this check;
- processed narration and the encoded master pass the project’s documented loudness and true-peak targets;
- relative mix requests such as “music +8%” are implemented as explicit, reproducible gain changes and rechecked on the encoded master;
- text is legible at the target viewing size and avoids UI/caption collisions;
- captions were checked on the encoded target player with playback controls visible, not only in a source preview;
- captions remain readable long enough to scan and do not flash through fragmented phrases merely to mirror word-level timing;
- no settled or moving overlay blocks a main character's eyes, mouth, expression, or essential gesture;
- every decomposed scene and narrative outro preserves the approved full scene without missing furniture, transparent surfaces, floating cutouts, or damaged context;
- spoken and visible copy use natural, contextually correct language, and narration-named overlays enter on the corresponding spoken words;
- repeated items such as documents, cards, tags, or labels enter in an authored sequence and settle within the allotted beat instead of arriving simultaneously or extending the scene unintentionally;
- transition fields, wipes, and carried colors resolve into the incoming scene without a visually unrelated flash;
- every icon communicates the intended object or action at target size without relying on its label;
- every third-party asset has an exact source and license record, an untouched source copy, and a documented derived working copy when modified;
- every product capture reflects the approved fixture and current interface state; stale placeholders or pre-update screens are not presented as current product proof;
- maps, charts, numbers, units, dates, and labels are correct;
- no API key or secret appears in prompts, code, logs, or committed files;
- the final file matches the requested dimensions, frame rate, duration, codec, and audio configuration.
