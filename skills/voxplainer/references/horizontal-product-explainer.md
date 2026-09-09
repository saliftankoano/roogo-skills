# Horizontal editorial product explainers

Use this route when a product or feature must be explained in 16:9 without adopting
the visual language of a conventional screen-recording walkthrough.

## Story contract

Apply the [audience/message brief](audience-and-messaging.md) before choosing which
product mechanics to show. Distinguish promotion, evaluation, onboarding, and
internal training. Cross-role handoffs should answer the primary viewer's question;
they are not a reason to teach every actor's interface in the same film.

Start with the user problem, coordination failure, or decision the feature resolves.
Explain the mechanism causally, then show the product interface as evidence that the
mechanism exists. End with the practical outcome and its boundary. Do not narrate a
tour of tabs merely because captures are available.

For an unfamiliar feature, answer these questions in order:

1. Who has the problem?
2. What breaks without coordination?
3. What does the feature connect or change?
4. What remains separate, private, or outside the feature?
5. Why is the result useful in practice?

## Visual grammar

Default to 1920×1080 at 30 fps. Use Editorial Motion as the base grammar, with
interface captures embedded as proof panels, detail crops, or moving evidence cards.
The product UI should normally occupy only the portion of the canvas needed to prove
the current line. Build relationships with diagrams, maps, timelines, role cards,
inventory counters, arrows, and purposeful kinetic type.

Avoid long full-screen holds, generic device mockups, completed dashboards that only
fade in, and decorative title cards that repeat the narration. Every scene must
transform information in the order the explanation develops.

Do not default role comparisons or process explanations to rounded white cards with
colored top borders, a boxed central icon, and connector lines. That pattern reads as
a generic presentation template unless the cards themselves are the evidence. Prefer
spatial staging across a real environment, full-bleed photography, typographic
contrast, masked brand-color fields, semantic objects, and transformations that show
how responsibility or state moves through the system. Use borders only when they
encode a real boundary the viewer must understand.

Reject generic dark navy canvases, dotted presentation grids, soft radial blobs,
water-ripple gradients, ornamental diagonal bands, and long decorative rules when
they do not encode the product or the argument. A quiet background must still belong
to the brand: use its approved colors, restrained material texture, supplied imagery,
or a semantic environment. Do not try to make an empty scene feel authored by adding
background effects.

Graphic paths, arrows, cards, masks, texture fields, and transition elements must
have protected lanes that never cross headlines, labels, captions, controls, or the
focal evidence at entrance, settled hold, or exit. When a process diagram competes
with its explanatory headline, reduce and relocate the diagram instead of layering
it over the text.

Treat copy serialization and typography as separate concerns. Decode intended line
breaks before rendering and fail the build or review if literal escape tokens such as
`\\n`, `\\r`, escaped HTML entities, or markup fragments appear on screen. Do not
use a narrow column to turn a short list into a one-word-per-line stack. Deliberate
multiline copy needs a readable measure, natural phrase grouping, sufficient
line-height, and balanced line lengths; switch to a row, grid, staged sequence, or
smaller type scale before compressing words into an awkward vertical block.

## Brand and music

Use the user's official logo asset. If the logo already contains the product name,
do not add a second typed product name beside or below it. The final outro should use
one approved brand mark, plus a URL only when requested or already approved.

Inspect user-supplied music before creating a procedural bed. Choose a track whose
emotional direction matches the story, preserve the source, record the selected file
and derived edit, duck it beneath narration, and measure the final mix. Reject music
that makes an enabling or optimistic product story feel ominous, mournful, or tense.

## Interface evidence

Use only verified captures and preserve claim boundaries. Crop or reframe to direct
attention, but never conceal an error or invent a successful result. When a control
is verified but its downstream action is not, describe and show the control without
claiming the result.

Before editing, create a capture-freshness manifest that records the app build or
commit, fixture identity, capture timestamp, viewport, expected media, and the exact
state each source proves. Re-capture after any visible product, copy, navigation,
fixture, or uploaded-media change. A photograph added editorially beside an old
screenshot does not make the screenshot current. If an approved cover image or hotel
photo should appear in the product, the interface capture itself must show it before
the film labels that state as product proof.

Treat every interface crop as an authored evidence frame, not as a generic image
placed into a fixed viewport. Record the source coordinates or transform, target
aspect ratio, focal control or result, and the meaningful context anchors that must
remain visible above and below it. Preserve enough top context for the viewer to know
which screen or task they are seeing, while removing unused bottom space that does
not contribute evidence. The first and last meaningful visible controls must be
fully framed; a partially clipped title, field, action, or result fails review.

Do not reuse one `object-fit` or vertical offset for unrelated screenshots. Compose
each capture around its own information hierarchy. Prefer a clean editorial crop
over a decorative phone shell, faux browser chrome, or bordered card when those
elements consume space without adding proof. Review the crop at its entrance,
settled hold, and exit, then inspect the encoded video with player controls visible
to ensure critical content remains legible in the real review context.

If the evidence requires understanding a long page or complete workflow state, do
not enlarge a narrow viewport until its top and bottom become unreadable. Reduce or
remove the enclosing frame, allocate a wider evidence region, and scale the source
with contain-style geometry so the complete required context fits. A smaller complete
screen is preferable to a larger crop that hides the item, code, action, or result the
scene claims to prove. Remove unused frame padding before removing meaningful source
content.

Capture the real responsive viewport required by the story. Do not simulate mobile
responsiveness by shrinking a desktop page or by cropping a larger layout until it
resembles a phone. Preserve the page header or task title, the focal action, and the
resulting state whenever those three anchors are necessary to understand the proof.

Use a static screenshot as a static source. Do not add local warping, ripple,
stretching, or pseudo-parallax inside a UI capture. A deliberate whole-frame pan or
scale is acceptable only when it reveals meaningful context and keeps text readable.
Between near-identical screens, prefer a short cut, masked handoff, or brief dissolve;
long dissolves create ghost labels and make the interface look broken.

When the user supplies genuine location or product photography, preserve it as a
source asset and use an authored crop instead of an empty media placeholder. Do not
composite the photo into a product screenshot and call it a verified app state. Until
the live product is recaptured with that media, identify the image as editorial or
demonstration evidence and keep it visually distinct from captured interface proof.

## Acceptance question

Does the film make the feature's practical value understandable before asking the
viewer to interpret its interface, with every capture functioning as evidence rather
than as the visual style itself? Does every interface crop retain its orientation
context and complete focal action without dead space or accidental clipping?
