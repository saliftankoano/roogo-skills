# Editorial Motion production method

Use this method for explainers built primarily from code-native typography, geometry, icons, charts, cards, diagrams, maps, and interface-like illustrations. Its quality comes from choreography and transformation, not from the number of objects on screen.

## Build a visual vocabulary before scenes

Define a compact, reusable system:

- one dominant headline treatment and one supporting text treatment;
- a restrained palette with a single emphasis color per beat;
- consistent strokes, shadows, corner treatments, arrows, labels, and textures;
- recognizable icons with strong silhouettes at phone size;
- repeatable timing curves for entrances, fills, counts, handoffs, and exits.

Keep exact copy, numbers, logos, charts, captions, URLs, and calls to action code-native. Store content separately from animation so translation, retiming, and reuse do not require rebuilding the scene.

Normalize display copy at the content boundary. A newline escape belongs to data
serialization, never to the final glyph stream: scan for visible `\\n`, `\\r`, HTML
entities, template delimiters, and markup fragments in source copy and extracted
rendered frames. For intentional multiline text, author semantic lines or blocks and
verify line width, line-height, orphan words, and font scaling at the target player
size. Never solve overflow by squeezing tracking, collapsing leading, or forcing one
word onto every line.

Assign an explicit semantic layer order whenever elements overlap: environment/background, supporting repeated objects, emphasis or question card, captions, then persistent interface or branding. A positive `z-index` on every object is insufficient if the emphasis card still sits below a later object group. Inspect the actual overlap frame, not only isolated component stills.

Choose icons by semantic recognition, not geometric convenience. A speaking person should read as speech, a phone as a smartphone, a CV as a document, and reasoning as a question or thought—not as arbitrary split circles or rectangles. Prefer one coherent library such as Phosphor, Lucide, or an existing brand set. Inspect icons without labels at target size; replace any icon that cannot be understood on its own.

Use one approved brand mark per scene. A typed brand name, decorative initial, eyebrow label, and imported wordmark all count as separate marks when they repeat the same identity. Keep the official asset and remove accidental duplicates unless repetition is an intentional, reviewed composition.

## Compose states, then animate the change

Define five states for each active scene:

1. **Initial state:** what the viewer understands before the line begins.
2. **Narrated change:** the primary action introduced by the spoken line.
3. **Supporting response:** a secondary element reacts, confirms, or contrasts.
4. **Resolved state:** the idea is visually complete and briefly readable.
5. **Handoff:** an existing element motivates the next scene.

Do not fade in an already-completed card and call it motion. Build, draw, count, sort, connect, stamp, cross out, compare, transform, or pass information between elements. The visible change should carry the argument even with the audio muted.

For piles or repeated objects, choreograph a compact cascade: stagger each entrance, vary position or rotation slightly, and give every object a readable settling action. When duration must remain fixed, shorten each object's fall and overlap the stagger rather than adding time or dropping the entire group at once.

## Synchronize meaning to narration

When narration names a sequence such as “accueillir, négocier, relancer,” introduce each item on its own spoken word or phrase. Do not show the full list early. Give every named element a purposeful entrance and a small residual behavior after it lands.

Use kinetic text only for words that carry the reasoning or emotional turn. Numbers may count, bars may fill, and labels may rise or fade, but only while their evidence is being introduced. Timing should make cause and effect legible, not merely energetic.

Plan a meaningful visual pickup whenever the narration advances to a new idea. As a
starting heuristic, an explanatory passage should rarely hold the same completed
composition for more than roughly 3–5 seconds. The pickup may be a new semantic
object, state change, evidence crop, count, connection, or camera move that reveals
new information. Do not manufacture constant motion: the requirement is renewed
meaning, not decorative activity. If several clauses play over an unchanged finished
list, split the beat or progressively build and transform the list in speech order.

## Preserve hierarchy under motion

Each active beat should contain:

- one primary action that attracts attention;
- one secondary reaction that explains or reinforces it;
- subtle ambient life that prevents deadness without competing for focus.

Keep at least one anchor stable while other elements move. Avoid making every object float, pulse, or rotate independently. Use shared directional logic and staggered timing so the scene feels authored rather than procedural.

Transitions should transform or hand off an existing element whenever possible. Do not let a generic outgoing transform dismantle the final card, reveal a blank canvas, or leave partial fragments in the encoded frame.

Treat a full-frame wipe as the first visual layer of the incoming scene. Its terminal color should normally equal the next scene's background color so the boundary resolves continuously. If the colors differ, the mismatch must express an intentional rupture and be reviewed in motion.

## Illustration and character scenes

Give a character a clear silhouette, emotional role, and relationship to the surrounding graphics. Stage supporting skill icons, evidence cards, messages, or tools around the character one by one as the narration introduces them. Keep at least two supporting elements subtly alive, while preserving the character as the focal point.

Replace abstract initials or monograms with meaning-bearing imagery when the story calls for collaboration, skill, or human progress. Do not add decorative symbols solely to fill space.

## Reusable implementation shape

Model editorial beats as data rather than embedding copy and timing inside components:

```ts
type EditorialCue = {
  id: string;
  startFrame: number;
  role: "primary" | "secondary" | "ambient";
  enter: "draw" | "rise" | "count" | "fill" | "stamp" | "connect";
  exit?: "handoff" | "resolve" | "fade";
};
```

Create reusable primitives for staged labels, count-ups, bar fills, line drawing, card assembly, path movement, captions, scene handoffs, and stable outros. Keep design tokens, copy, cue timing, and scene composition independently editable.

## Review passes

Review the encoded motion, not only source stills:

1. **Hierarchy pass:** identify the intended focal point at every moment.
2. **Narration-sync pass:** verify named elements enter on their spoken phrase, in order.
3. **Muted-causality pass:** confirm the argument develops visually without narration.
4. **Stagnation pass:** flag any active beat that is only a static layout with camera drift.
5. **Clutter pass:** remove elements that do not change the viewer’s understanding.
6. **Transition pass:** inspect scene boundaries for resets, fragments, and half-built states.
7. **Icon pass:** hide labels temporarily and confirm every pictogram still communicates the intended meaning.
8. **Cascade pass:** inspect repeated objects frame by frame for authored order, overlap, weight, and complete settling inside the original beat.
9. **Final-frame pass:** extract and inspect the last encoded frame.
10. **Typography pass:** scan source and rendered copy for literal escape tokens,
    overflow, compressed leading, orphan words, and unintended one-word stacks.
11. **Attention-cadence pass:** mark long stretches without a meaningful visual
    pickup and confirm that any deliberate hold supports comprehension or emotion.

Editorial Motion fails when it reads as an animated slideshow. Repair the causal transformation and staging rather than adding more floating decoration.
