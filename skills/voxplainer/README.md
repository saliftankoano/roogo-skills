# Voxplainer: a guide for people

Voxplainer helps you turn a researched idea or verified product feature into a
narrated visual explanation. It helps organize the audience and message before
covering the script, visual beats, voices, assets,
Remotion implementation, revision, and release review. You can request just a
concept or storyboard; you do not have to commission a finished video.

This is an agent skill, not an application you launch or a one-command renderer.
Its [operating instructions](SKILL.md) tell the agent what to do and which focused
references to read. The name describes an editorial format, not an affiliation
with Vox or permission to copy its branding.

## Install and run

1. Get this repository, for example with
   `git clone https://github.com/saliftankoano/roogo-skills.git`.
2. Copy the **whole** `skills/voxplainer` folder into your configured Codex user
   skills directory, commonly `~/.codex/skills/voxplainer`. Do not copy only
   `SKILL.md`: its references and helper script are part of the package. Compare
   and back up an existing installation before replacing it.
3. Open a new Codex task in your intended production workspace. Check that
   Voxplainer is available and invoke it with `$voxplainer` in your prompt.
4. Supply the brief and assets below. Start with a script/storyboard if you want
   to approve the direction before production costs are incurred.

Updating the cloned repository does not update a separately copied installation.
After reviewing an upstream change, repeat the comparison/copy step and start a
new task so it loads the updated instructions.

### What you need

For planning, the agent needs your brief and readable evidence. Rendering adds a
Node.js/Remotion environment and its project dependencies; those are set up in the
production workspace, not shipped here as a ready-made video project. The audio
helper requires Python 3.10+ and FFmpeg/ffprobe. Browser or simulator access is
needed only when fresh product captures are in scope. Image-led modes may require
image-generation or editing tools, or suitable supplied assets.

For paid narration, configure the selected provider privately with
`CARTESIA_API_KEY` or `ELEVENLABS_API_KEY`. The [Cartesia reference](references/cartesia.md)
also describes optional macOS Keychain reuse. Do not paste credentials into the
brief, commit them, or print them in logs. Check voice access, usage rights, and
budget before generation; the public voice IDs do not grant those rights.

Production media, credentials, captures, and renders belong outside the skill
repository. The skill does not supply your official logo, licensed soundtrack,
private product evidence, provider credits, or a universal access entitlement to
the named voices.

## Start with the audience and message

You can use Voxplainer before you know which videos to make. Ask it to organize a
feature inventory into films with distinct viewers and purposes, or review an
existing cut for confusing audience shifts. This planning layer applies to every
mode; it is not an additional visual mode or a requirement to render anything.

The agent helps establish **who is watching, why they care, what they already
know, what this film should explain, and what happens next**. A promotional film
for a prospective customer, a tutorial for an existing user, and internal staff
training need different messages even when they show the same feature. General
editorial education can end with understanding rather than a sales CTA.

Expect a compact audience/message brief and, for a campaign, an inventory of
viewers, purposes, takeaways, proof, endings, and proposed keep/refocus/split/merge/
defer decisions. Proposed changes do not automatically change an approved lineup.
Review material audience choices before locking scripts or buying narration;
existing approval remains valid for unchanged decisions. See the
[audience and messaging workflow](references/audience-and-messaging.md) for the
operating criteria.

```text
$voxplainer Review this proposed video inventory for audience clarity. Distinguish
prospective hotel owners, current hotel administrators, reception staff, and
travelers. Recommend a primary viewer and communication purpose for each film;
flag overlaps and propose splits or merges with reasons. Preserve the commissioned
count until I approve changes. Deliver audience/message briefs and a proposed
campaign map only. Do not rewrite full scripts, generate narration, or render yet.
```

## Understand the modes

Choose three things separately: **delivery format**, **visual grammar**, and any
**storytelling treatment**. For example: “16:9 product explainer, Editorial Motion,
with a story-first opening.” They are not competing labels for the same setting.

### Delivery formats: where and how the film is watched

| Format | Default canvas and duration | What it is for |
| --- | --- | --- |
| [Vertical social short](references/shorts.md) | 9:16, 1080×1920; usually 20–60 seconds | One self-contained insight for a phone feed. |
| [Horizontal long-form](references/long-form.md) | 16:9, 1920×1080; duration follows the argument | More context, evidence, comparisons, and chapters when useful. |
| [Horizontal editorial product explainer](references/horizontal-product-explainer.md) | 16:9, 1920×1080; agree duration in the brief | User problem → mechanism → verified interface proof → practical outcome and limits. |

Unless you specify otherwise, delivery defaults to 30 fps, H.264 MP4, and AAC
audio. A short horizontal film is possible; “long-form” is not a minimum-duration
restriction. When requesting both 16:9 and 9:16, expect independently composed
edits sharing research, not a cropped horizontal master. Exact platform limits
must be checked when they matter to the delivery.

### Visual grammars: how the explanation is built

These are the skill's three production modes, not three quality tiers. See the
[mode-selection reference](references/visual-modes.md) for the complete rules.

| Mode | What you will see | Choose it when | What must pass review |
| --- | --- | --- | --- |
| [Editorial Motion](references/editorial-motion.md) | Authored typography, meaningful icons, diagrams, counters, charts, and UI evidence that build and transform. | The mechanism, comparison, or data needs precision and frequent revision. | Information changes in step with the explanation; completed slides merely fading in are insufficient. |
| [Cinematic Parallax](references/cinematic-parallax.md) | Rich photographs or illustrations with authored reframing, masks, regional motion, and depth cues. | People and place matter, without preparing independent transparent planes for every shot. | Depth and focus feel believable; it is not simply a long zoom or a warped photograph. |
| [Layered 2.5D](references/layered-2-5d.md) | Independently moving background, subject, and foreground layers from an approved master scene. | A hero story warrants deeper spatial staging and more asset preparation. | Layers recombine cleanly, with no halos, duplicate objects, missing surfaces, or sliding cutouts. |

A **hybrid** assigns these deliberately by scene: for example, Cinematic Parallax
for a traveler's situation, then Editorial Motion to explain the booking process.
Logos, exact text, captions, statistics, and diagrams stay code-native even in
image-led scenes. A UI screenshot is never locally warped to imitate depth.

### Optional storytelling treatments

- [Story-first](references/story-first.md) gives the film a person, desire,
  pressure, choice, and resolution. The product changes the situation instead of
  appearing as a list of features. It is a narrative treatment, not a fourth
  rendering mode.
- [Animated-film treatment](references/animated-film.md) adds cinematic staging,
  purposeful actions and reactions, continuity, and sound-led handoffs. It can be
  combined with the visual grammars; it does not automatically mean 3D animation.

Narration, asset sourcing, and finishing are workflows used across modes, not
additional visual modes. If uncertain, ask the agent to propose a mode and explain
its fit and revision cost before generating assets.

## Write a useful brief

Include the audience, intended takeaway, factual sources or verified captures,
platform/aspect ratio, target duration, language, visual mode, requested voice,
brand/logo files, music source, CTA, output folder, and current delivery scope.
State prohibited claims and whether paid narration or image generation is
authorized. Missing material choices should be resolved before cost or production.

### Horizontal product tutorial

```text
$voxplainer Make a 90-second French 16:9 editorial product explainer for hotel
administrators onboarding their hotel, using Editorial Motion and Sandrine as
tutorial instructor. Help them understand the setup tasks and end with the
verified next setup action. Keep receptionist task training out of this film.
Use only my supplied current
captures as product proof. Use the official logo once on the ending and music
from my supplied folder. No decorative background shapes. Deliver a script,
storyboard, and capture-gap list first; no paid generation yet.
```

### Short mechanism explanation

```text
$voxplainer Plan a 45-second 9:16 Editorial Motion explainer in French about
per-night room pledges for hotel managers evaluating an event commitment. Explain
how the rooms they offer relate to each night. Use Nathalie. Build the
inventory as the narration explains it, using my verified rules and numbers.
Show the capacity boundary without promising availability. Start with a script
and storyboard, then request a voice sample review before full narration.
```

### Image-led local story

```text
$voxplainer Plan a 75-second 16:9 story-first film in Cinematic Parallax with
Rapoko for first-time travelers considering the service. Follow a traveler
preparing for arrival, using my licensed location
photos. Use Editorial Motion only where the booking mechanism needs explaining.
Keep the approved product limits visible. Propose shots and missing assets before
any paid generation; do not invent a real customer's testimony.
```

### Multiplane hero film in two formats

```text
$voxplainer Develop a Layered 2.5D hero film with story-first and animated-film
treatments for event organizers evaluating accommodation coordination. Travelers
and hotel staff are supporting actors, not separate tutorial audiences. Resolve
the organizer's question about how commitments connect to traveler quotes.
Language: French; voice: Rapoko; target: 105 seconds. Compose both
16:9 and 9:16 natively. Start with the story and master-scene proposals; wait for
their review before decomposition or narration batches. Keep exact product text
and branding separate from the image assets.
```

### Longer researched explanation

```text
$voxplainer Outline a four-minute 16:9 editorial explanation of hotel-event
coordination for organizers. Use Editorial Motion, Rapoko, and my supplied
sources. Separate verified facts, examples, and unresolved claims. Propose
chapters only where the question changes. Deliver the outline and evidence ledger
first, not a rendered video.
```

### Revise an existing cut

```text
$voxplainer Revise the supplied cut at 00:18–00:32: the narration explains three
actions while the graphic stays still. Stage one meaningful change per spoken
action, using the current captures. Preserve voice, duration, approved claims,
brand palette, and music. Remove literal escape tokens and use stable phrase
captions. Deliver the revised excerpt plus comparison frames before the full cut.
```

## Voices and narration

| Voice | Provider | Intended role |
| --- | --- | --- |
| Rapoko | ElevenLabs | Default editorial, story-led, and hero-film narrator. |
| Salif | Cartesia | Product presenter or host; default for direct product demos. |
| Sandrine | Cartesia | Approachable tutorial instruction. |
| Wendata Nathalie Kaoré | Cartesia | Slower, complex teaching-led explanation. |
| Jérôme | ElevenLabs | Alternate only when explicitly selected; not an automatic substitute. |

The canonical IDs and provider settings live in [Cartesia](references/cartesia.md)
and [ElevenLabs](references/elevenlabs.md); follow [narration](references/narration.md)
for the sample, timing, and review process. An explicitly requested authorized
voice takes precedence over defaults. In a multi-voice film, each speaker needs a
stable role and switches occur at scene boundaries.

Review a representative sample for **every voice used** before paid batch
narration. After processing, the actual audio duration controls scene timing and
captions. A successful API call or numeric loudness check is not a listening
review. A narrated review cut must have narration; silent preflights must be
clearly labeled and cannot stand in for the requested narrated delivery.

## What you review and receive

Agree the checkpoints in the brief. A practical sequence is:

1. Audience/message brief and claims: who the film serves, its purpose and ending,
   what can be said, what remains blocked, and capture gaps.
2. Script, storyboard, selected modes, and representative voice samples.
3. Narrated rough cuts, comparison frames, pacing, captions, and music.
4. Encoded masters and release QA, including the complete ending.

For a final-video commission, request the MP4 plus editable project, exact render
commands, narration and caption files, source/license ledger, capture-freshness
manifest where applicable, and validation report. Concept-only requests stop at
the agreed planning artifacts. Review samples and rough cuts are acceptance
checkpoints, not permission to publish the film or exceed the authorized budget.

Important checks learned from production:

- The opening, scene sequence, language, and ending must serve the same primary
  viewer. A beautiful, technically valid video can still fail this message check.
  Agent review is not a measured audience-comprehension or retention study.
- Visuals must advance with the spoken explanation; motion is meaningful, not
  decorative churn. Backgrounds must respect the approved brand and removals.
- Use the actual approved logo without redundant typed branding. Inspect supplied
  music before sourcing something else; avoid an ominous bed for an enabling story.
- Use coherent semantic icons. [Asset provenance](references/asset-provenance.md)
  explains SVG Repo sourcing, exact asset/license records, and source preservation.
  A free download is not blanket permission to redistribute it.
- Product captures must be fresh, including uploaded cover photos. Show complete
  focal controls and enough screen context; never paste a photo into an old
  screenshot and label it current UI proof.
- Avoid overlapping labels, clipped captures, squished type, literal `\n` text,
  and flashing subtitle fragments. Check the encoded video with player controls.
- Watch and listen through joins, pauses, and the full outro. Check duration,
  dimensions, codec, loudness, true peak, and the actual final encoded frame.

The [finishing and revisions guide](references/finishing-and-revisions.md) is the
full checklist. The [audio quality helper](scripts/audio_quality_gate.py) supports
technical checks (`python3 scripts/audio_quality_gate.py --help` from this skill
folder); it cannot judge pacing, voice naturalness, factual truth, or visual taste.

## Limits and related workflows

Voxplainer must not invent statistics, successful payments, current UI states,
endorsements, or evidence. Generative scenes illustrate a story; they do not prove
a product works. Missing tools, permissions, licensed assets, or verified evidence
may limit delivery until supplied.

A literal click-by-click screen demonstration may use an independently installed
Product Video / `product-demo-video` skill. It is optional and is **not included**
in this repository. Without it, Voxplainer preserves the requested walkthrough and
uses its own capture/proof guidance. Horizontal editorial product explainers remain
in Voxplainer; their interface is evidence inside an explanation, not the entire
visual language.
