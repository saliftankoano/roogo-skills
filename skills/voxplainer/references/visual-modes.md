# Visual production modes

Choose the visual grammar before generating assets. These modes are complementary options, not successive replacements or quality levels. A strong film may use one mode consistently or combine them deliberately by scene.

## Editorial Motion

Code-native motion graphics built from typography, shapes, charts, icons, cards, maps, and interface-like compositions.

Use it when the idea is abstract, data-led, procedural, comparison-heavy, or best understood through graphic simplification. It is the easiest mode to retheme, translate, revise, and adapt across formats.

Its strength is precision and expressive graphic choreography. Do not let it become a slideshow of completed cards. Build, draw, count, connect, sort, cross out, transform, and hand elements between scenes. Keep the world alive through a primary action, a secondary response, and subtle environmental movement.

Read [editorial-motion.md](editorial-motion.md) before designing or implementing this mode.

## Cinematic Parallax

Generated documentary-style photographs or rich illustrations animated as dimensional images using reframing, masks, region-specific movement, camera drift, scale, selective focus, depth blur, and editorial overlays.

Use it when a human situation, place, or local context needs emotional immediacy but preparing genuine transparent planes for every shot would cost more than the production warrants.

Choose master images with a clear foreground, subject plane, background, and useful negative space. Move regions at different perceived rates without pretending a flat image has more geometric freedom than it does. Typography and diagrams should annotate the image rather than replace it.

Read [cinematic-parallax.md](cinematic-parallax.md) before selecting, generating, or animating imagery for this mode.

## Layered 2.5D

A true multiplane composition built from independently movable RGBA assets:

- background clean plate at depth `0`;
- midground subject or action at depth `5`;
- foreground occlusion or detail at depth `10`;
- code-native labels, captions, evidence, and brand elements above depth `20`.

Use it for hero stories where immersion, local specificity, spatial continuity, and emotional attachment justify the additional asset preparation and review. This is the highest-control image-led mode, but it is not automatically the right choice for statistics, rapid comparisons, or heavily revised explainers.

Read [layered-2-5d.md](layered-2-5d.md) before generating or animating this mode.

## Choosing deliberately

| Need | Prefer |
| --- | --- |
| Exact data, fast revision, localization | Editorial Motion |
| Human context with moderate production effort | Cinematic Parallax |
| Character-led cinematic story and real depth | Layered 2.5D |
| Product mechanism inside a human story | Image-led mode plus Editorial Motion overlays |

Record the selected mode per scene in the storyboard. A switch between modes must serve a narrative purpose—for example, moving from a lived human moment into a precise product mechanism—not merely add variety.

Keep logos, exact copy, statistics, sources, charts, captions, evaluation bars, URLs, and calls to action code-native in every mode.

## Mode-specific acceptance question

Ask the relevant question before approving any scene:

- **Editorial Motion:** Does the scene visibly transform information in the order the argument develops, or is it merely a completed layout receiving entrances?
- **Cinematic Parallax:** Does the image preserve believable depth and emotional focus, or is it only a slow zoom over a static picture?
- **Layered 2.5D:** Do independently owned planes recombine cleanly and move with real depth, or do duplicated mattes, halos, transparency, and sliding cutouts reveal the construction?

If the answer is the weaker alternative, repair the scene or switch modes. Do not hide a structural failure with blur, darkness, overlays, faster cuts, or more decoration.
