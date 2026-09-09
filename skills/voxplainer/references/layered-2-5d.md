# Layered 2.5D production method

Use this method for true multiplane image-led scenes. Preserve the high-quality Awa approach while treating its remaining layer imperfections and occasional stillness as review targets, not a finished standard.

## Start with an approved master

Generate or select one complete composition that establishes subject identity, action, camera framing, lens, lighting, palette, local specificity, depth relationships, and negative space.

The image must contain readable foreground, midground, and background planes with useful overlaps. Avoid a subject pasted against an empty wall or a composition where all important objects share one focal plane.

Generate natively for the delivery aspect ratio. Keep faces, hands, key artifacts, captions, and overlays inside platform-safe areas.

## Derive sibling planes from the master

Do not regenerate the planes independently. Edit from the approved master so identity, perspective, coordinates, clothing, lighting, and depth blur remain consistent.

Create:

1. **Background clean plate:** remove nearer subjects and reconstruct everything they concealed.
2. **Midground RGBA plane:** isolate the principal person or action on genuine transparency.
3. **Foreground RGBA plane:** isolate the near-camera occlusion or transition object on genuine transparency.
4. **Optional atmosphere plane:** dust, light, shadow, reflection, or particles only when narratively useful.

Assign every visible pixel to one intentional owner. A nearer plane must not contain a faint duplicate of the complete master, furniture that belongs to the clean plate, or shadows that are also baked into the background. Decide explicitly whether contact shadows travel with the subject or remain on the surface behind it. An honest two-plane scene is better than inventing a contaminated foreground solely to satisfy a three-plane template.

Keep the original master. Use stable suffixes such as `-master`, `-background`, `-midground`, `-foreground`, and `-atmosphere`.

## Layer contract

Every plane must:

- use the same aspect ratio, pixel dimensions, camera framing, and subject coordinates;
- remain on the full shared canvas rather than being tightly cropped;
- preserve natural feathering, occlusion boundaries, and original depth blur;
- contain no checkerboard baked into pixels, matte color, captions, logos, or watermarks;
- pass an alpha-channel check when transparency is required;
- recombine into a static alignment proof that closely matches the approved master.

Inspect transparent edges over white, black, and a saturated diagnostic color. Reject halos, leftover fragments, double edges, holes in hair or fingers, mismatched shadows, and visibly invented background patches.

When extracting from an RGBA source, do not blindly preserve or multiply an inherited alpha channel. Background-removal tools can compound the old matte and leave the visible subject semi-transparent. Rebuild the extraction from the source RGB pixels, then verify that the resulting alpha reaches full opacity (`255`) in solid subject regions. Preview the recomposition over the final background before animating it.

For every transparent plane, record an alpha proof: minimum and maximum alpha, whether solid subject regions reach `255`, and previews over white, black, and saturated backgrounds. Compare the static recomposition directly against the approved master before writing motion code. Tables, walls, clothing, and other broad solid surfaces must never look ghosted or double-exposed.

Treat the approved full scene as the integrity reference. If a clean plate or isolated subject removes table edges, furniture, hands, shadows, or other visible context, do not animate the damaged decomposition. Repair the missing plane, reduce the scene to an honest full-master camera move plus code-native overlays, or regenerate the layers. Preserving the complete scene is more important than forcing nominal parallax.

## Character connection and protected zones

For every scene with a person, record face and gesture bounds in the storyboard. Reserve the eyes, nose, mouth, and the hand or object carrying the emotional action as protected zones. Titles, cards, captions, labels, and foreground wipes must not fully cover these zones. Brief edge occlusion may add depth, but a settled overlay across a face is a blocking defect because it weakens the viewer's connection to the character.

Place dense evidence below the face, beside the body, or in intentionally empty negative space. Test the first frame, settled frame, and maximum-motion frame because a safe starting position can drift across the face later. If there is no safe area, simplify the overlay, split it across beats, or change the crop.

## Depth and motion hierarchy

Use the stable conceptual order:

- background: `z-index 0`, least translation and scale;
- midground: `z-index 5`, moderate motion and primary focus;
- foreground: `z-index 10`, greatest translation and scale, optionally slight optical blur;
- overlays: `z-index 20+`.

Starting ranges for a slow push:

| Plane | Scale | Travel |
| --- | ---: | ---: |
| Background | `1.02 → 1.05` | `8–18 px` |
| Midground | `1.04 → 1.10` | `20–45 px` |
| Foreground | `1.10 → 1.20` | `45–90 px` |

These are calibration ranges, not fixed values. Use overscan so no move reveals empty edges. Maintain a single eased camera intention per shot—a push, pan, pullback, or restrained arc—rather than arbitrary independent drifting.

## Make the scene perform

Parallax alone is insufficient. Each active scene needs:

- one primary story action;
- one secondary reaction or editorial annotation;
- subtle environmental life;
- a motivated visual handoff to the next scene.

Keep at least two depth systems in subtle continuous motion during an active shot—for example, a slow background push plus a restrained subject drift, or a subject drift plus a foreground occlusion. The movements should share one camera intention but differ enough to preserve depth. A perfectly static cutout over a moving plate reads as a slideshow.

Examples include a phone lighting, a page slipping, fabric crossing the lens, a hand entering, evidence bars assembling, light changing, or a foreground object becoming a wipe. If the only change is a slow camera drift, treat the scene as too stagnant unless a deliberate emotional hold requires stillness.

Narration-named overlays must enter on the word or phrase that introduces them, not several beats earlier or after the sentence has moved on. Stagger lists item by item, give each item a purposeful entrance, and keep a small amount of residual motion after it lands. Use count-ups, fills, fades, and short rises only when they clarify the narrated evidence.

The foreground should do more than create depth. Use it to reveal, briefly occlude, direct attention, or transition. Preserve spatial continuity and screen direction across cuts.

## Keep exact information code-native

Render captions, exact copy, statistics, citations, scores, charts, waveforms, arrows, logos, URLs, and calls to action as editable code layers. Generated imagery supplies world and emotion; it must not become the source of truth for text or data.

Keep captions inside a platform-safe mid-lower band rather than against the bottom edge, where native player controls and mobile UI can cover them. Test the encoded portrait video with controls visible. A useful default is to keep the caption block around the lower third, with generous side margins and enough contrast to remain readable over every scene.

Separate spoken pronunciation from canonical on-screen spelling. When a brand name is mispronounced, preserve its normal written form in titles and captions while using a phonetic rendering only in the narration input. Store the approved spoken form in the project manifest so later regeneration does not reintroduce the error.

## Remotion implementation shape

Model planes as data rather than hard-coding each scene:

```ts
type DepthPlane = {
  src: string;
  zIndex: 0 | 5 | 10;
  x: [number, number];
  y: [number, number];
  scale: [number, number];
  filter?: string;
};
```

Place each full-canvas asset inside an overscanned, overflow-hidden scene. Derive movement from one normalized, eased scene progress value. Keep overlays above the photo planes and separate from camera transforms unless they are meant to inhabit the photographed space.

## The Awa storytelling pattern

The Awa film demonstrates the method through:

- a returning location that bookends the story;
- a phone whose meaning evolves from opportunity to exercise to invitation;
- foreground fabrics, CVs, and furniture that establish depth and provide handoffs;
- opposite camera direction at the resolution to make the world feel more open;
- a credible resolution—an interview rather than a guaranteed job;
- a complete music-only outro with a clean visual and audio fade.

Reuse these principles, not Awa's literal scenes.

## Review passes

Review the encoded motion, not only stills:

1. **Static reconstruction:** confirm the three planes align with the master.
2. **Ownership and alpha pass:** confirm each plane contains only its intended pixels, solid regions reach full opacity, and no furniture, shadow, or complete-frame duplicate appears twice.
3. **Edge pass:** inspect hair, hands, clothing, shadows, and foreground occlusions in motion.
4. **Depth pass:** mute overlays and verify visibly different but believable plane rates.
5. **Stagnation pass:** identify any active scene with only camera drift and add a meaningful action or reaction.
6. **Overscan pass:** inspect every corner at the beginning and end of movement.
7. **Muted story pass:** verify the story remains understandable through action and image.
8. **Outro pass:** inspect the first outro frame and final encoded frame for partial wipes, clipped layers, or unfinished transitions.
9. **Character pass:** inspect every settled overlay and maximum-motion frame for face, eye, mouth, hand, or story-object obstruction.
10. **Scene-integrity pass:** compare every composited shot and the outro against the approved full master; reject missing furniture, transparent surfaces, floating cutouts, or incomplete environmental context.

The final frame must remain fully composed through the last encoded frame. Fade the music, atmosphere, or camera energy without visually dismantling the lockup. Prefer a meaningful local landmark or quiet brand texture over generic filler dots, and verify the closing URL remains readable while playback controls are visible.

## Landmark outro contract

When the outro uses an isolated local landmark or other meaning-bearing image, prefer a strict, inspectable stack:

1. solid brand background at `z-index 0`;
2. landmark at `z-index 5`, with solid regions fully opaque and its natural color preserved;
3. code-native logo, message, and URL at `z-index 20+`.

Do not place generic patterns behind a landmark merely to fill space. Do not solve text contrast by reducing the landmark to a dark translucent ghost or covering it with a heavy full-frame veil. First adjust scale, crop, text position, local text shadow, or a small text-backed treatment. Use a tint only when it is deliberate and still preserves the visual identity and color of the landmark.

The transparent canvas around an isolated PNG is allowed; the landmark itself must not be semi-transparent. Verify interior alpha reaches `255`, then inspect the encoded outro over the actual brand background. The image, typography, and URL should read as three balanced planes rather than one flattened poster.

Do not hide poor extraction, inconsistent anatomy, or alignment defects behind blur, darkness, captions, or fast motion. Repair or regenerate the asset.

When an outro is meant to preserve the final narrative location, use the complete approved scene as its base layer. Do not replace the environment with isolated people floating over a brand field. Apply only restrained grading or a local contrast treatment, then place the brand message above it as a separate code-native layer.
