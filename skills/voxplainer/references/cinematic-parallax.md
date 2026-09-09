# Cinematic Parallax production method

Use this method for image-led scenes that need human emotion, place, or documentary texture without the preparation cost of true independent RGBA planes. The source may be a generated image, licensed photograph, user-provided photograph, or rich illustration.

## Select an image that can move

Approve the source only when it has:

- a clear focal subject and emotional beat;
- visible foreground, subject-plane, and background cues;
- useful negative space for code-native overlays;
- enough overscan for the intended delivery aspect ratio;
- locally credible clothing, architecture, objects, and environment;
- consistent identity, wardrobe, lighting, props, and screen direction across related shots.

Reject imagery with weak anatomy, unexplained edge artifacts, no readable depth, or a composition whose critical content touches the crop boundary. If the user provides a suitable local asset, preserve and adapt it rather than regenerating an imitation.

## Create perceived depth honestly

Use a restrained combination of:

- whole-image dolly, pan, or pullback;
- region masks with small differential movement;
- selective focus or depth blur;
- controlled light, shadow, haze, or reflection changes;
- code-native labels, evidence, and typography.

Maintain one camera intention per shot. Do not rotate around a flat subject, reveal geometry that does not exist, or distort anatomy to simulate depth. A slow zoom alone is not a parallax scene.

Keep at least two visual systems subtly alive during an active scene—for example camera drift plus changing window light, or a restrained subject-region move plus an evidence overlay. Their motion should support the same emotional or explanatory beat.

## Make the image tell a story

For each shot, define what the subject wants, notices, fears, decides, or changes. Reveal a meaningful detail, introduce the relevant evidence, and use that object, gaze, color, or movement to hand off into the next scene.

Vary shot function across the sequence: establishment, human reaction, evidence detail, decision, and resolution. Preserve identity and object continuity so the film feels like one story rather than a collection of attractive images.

## Integrate overlays

Render exact text and data as code-native layers. Place overlays in negative space or near the photographed object they explain. Introduce narration-named items on the corresponding words and keep a small residual motion after each item settles.

Keep overlays sparse enough that the image retains emotional authority. Put captions in a control-safe mid-lower band with generous side margins and verify them on the encoded target player with controls visible.

## Transitions and continuity

Prefer motivated transitions:

- a foreground object crossing the frame;
- movement following a gaze or hand;
- a line, object, or color continuing into the next shot;
- a detail becoming a code-native diagram or card.

Avoid default wipes, blank-color interruptions, and transitions that expose partial frames or clipped imagery. Let the final composition settle before a stable outro.

When a color wipe is appropriate, use the incoming shot's dominant background color as the wipe destination. Extract frames immediately before, during, and after the boundary; a polished wipe should feel as though the next world has expanded into the frame, not as though an unrelated color card briefly interrupted the edit.

## Review passes

Review the encoded motion:

1. **Image-integrity pass:** inspect faces, hands, text-like artifacts, and local details.
2. **Continuity pass:** compare identity, wardrobe, lighting, props, and screen direction across shots.
3. **Depth-plausibility pass:** confirm the motion does not expose the flat image as false geometry.
4. **Overscan pass:** inspect every corner at the beginning and end of movement.
5. **Stagnation pass:** flag shots that are only slow zooms with no meaningful secondary behavior.
6. **Overlay-sync pass:** verify labels and evidence enter with narration rather than appearing as static decoration.
7. **Caption-and-outro pass:** test playback controls and inspect the final encoded frame.

If the desired movement requires clean independent occlusion, substantial subject travel, or a foreground object crossing the subject, switch the shot to Layered 2.5D instead of forcing a flat image beyond its geometry.
