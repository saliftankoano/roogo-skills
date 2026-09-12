# Domain

This document defines the project-specific language a teammate or agent needs
before interpreting requirements, product behavior, or implementation choices.
Use these terms consistently. See [SYSTEM.md](SYSTEM.md) for how the system works,
[DECISIONS.md](DECISIONS.md) for why trade-offs were made,
[ROADMAP.md](ROADMAP.md) for unfinished commitments, and
[CHANGELOG.md](CHANGELOG.md) for shipped changes.

## Domain map

- **What this product serves:** Reusable, public-safe Roogo agent workflows; the first published workflow is video explanation.
- **Primary actors:** The commissioning user, production agent, reviewer, and future skill maintainer.
- **Core workflow:** Audience/message brief and evidence → script and beats → approved assets/narration → production → message, visual, and technical review → delivery.
- **External standards:** Provider access and usage terms, per-asset licensing, and the agreed media delivery specifications; MIT applies only to this repository's original code and documentation.

## Core vocabulary

### Audience/message brief

**Meaning:** The part of the production contract that names the primary viewer,
their situation and knowledge, the communication purpose, supported takeaway,
and intended next action or learning resolution.

**Origin:** Audience-centered communication planning, formalized in this skill
after the 2026-09-09 campaign messaging review.

**Why it matters for building:** A protagonist or supporting actor is not
necessarily the intended viewer. A film's language, evidence, and ending must
serve that viewer; visual grammar alone cannot establish relevance.

**Evidence:** [Planning workflow](../skills/voxplainer/references/audience-and-messaging.md)
and [system explanation](SYSTEM.md#audience-and-message-planning).

### Production contract

**Meaning:** The agreed audience, claim boundaries, format, voice, budget authority,
and delivery scope for a film.

**Origin:** Production-brief practice, narrowed by Voxplainer's operating workflow.

**Why it matters for building:** A storyboard request does not authorize paid
batch generation or publication. Defaults cannot override explicit user choices.

**Evidence:** [Establish the production contract](../skills/voxplainer/SKILL.md#establish-the-production-contract).

### Visual grammar / production mode

**Meaning:** How scenes are constructed: Editorial Motion, Cinematic Parallax, or
Layered 2.5D. Not the aspect ratio or narrative treatment.

**Origin:** Motion-design vocabulary organized into the three local production choices.

**Why it matters for building:** Each choice has distinct asset requirements and
review criteria; more layers are not automatically better.

**Evidence:** [Mode definitions](../skills/voxplainer/references/visual-modes.md).

### Visual beat

**Meaning:** A narrated idea with a specific visible action or change that helps
the viewer understand it.

**Origin:** Film/editing beat terminology, applied here to explanation and evidence.

**Why it matters for building:** A long narration over an unchanged slide fails
even when the layout looks polished. Decorative motion does not replace explanation.

**Evidence:** [Build from story to frames](../skills/voxplainer/SKILL.md#build-from-story-to-frames).

### Interface proof and capture freshness

**Meaning:** A real captured product state supports only the claim it visibly
establishes. Freshness identifies the build, fixture, time, viewport, and expected media.

**Origin:** Product-demo QA practice, made explicit through Roogo video iterations.

**Why it matters for building:** Old placeholders, synthetic composites, or a visible
button cannot prove current photos, completed payments, or an untested downstream action.

**Evidence:** [Interface evidence](../skills/voxplainer/references/horizontal-product-explainer.md#interface-evidence).

### Acceptance checkpoint / gate

**Meaning:** A review of a specific artifact, such as claims, a voice sample, rough
cut, or final master, against the production contract.

**Origin:** Production review practice; numbered gates were used in the hotel campaign.

**Why it matters for building:** Approval applies to the reviewed scope. Gate numbers
are project-specific, not universal permission for all later spending or release.

**Evidence:** [Review and deliverables](../skills/voxplainer/README.md#what-you-review-and-receive).

### Source asset and derived working copy

**Meaning:** The preserved original asset and its separately identified edited version,
with source, license, and modification records.

**Origin:** Media asset-management and provenance practice.

**Why it matters for building:** Being downloadable from SVG Repo or another library
does not prove redistribution rights; revisions must not destroy the original.

**Evidence:** [Asset provenance](../skills/voxplainer/references/asset-provenance.md).

### Ad bundle

**Meaning:** Everything one publishable ad needs, delivered together: the approved
script, the narration, the rendered video, and the social copy for each surface it is
posted to.

**Origin:** Roogo marketing practice, where one person writes, renders, and publishes.

**Why it matters for building:** A rendered file alone is not deliverable work. The
bundle also carries its own posting state, so a file that has not been moved into the
published subfolder is still unposted.

**Evidence:** [Default bundle](../skills/appel-proprietaires/SKILL.md).

### Post-transition timeline

**Meaning:** The real on-screen time of every clip in a crossfade chain, after each
transition has consumed one crossfade of overlap.

**Origin:** Repeated ffmpeg timing errors on carousel builds.

**Why it matters for building:** The naive cumulative sum drifts further wrong with
every transition, which both overruns the narration and misplaces the watermark
exclusion windows over full-logo cards.

**Evidence:** [xfade_timeline.py](../skills/appel-proprietaires/scripts/xfade_timeline.py).

### Flattened caption track

**Meaning:** All caption states rendered as clips and concatenated into one
transparent video track, overlaid on the base video in a single pass.

**Origin:** A build that chained about a hundred individually timed overlays and ran
for over three hours before being killed.

**Why it matters for building:** Per-overlay chaining reprocesses the whole video at
every stage, and per-clip durations in seconds accumulate rounding drift. Frame-exact
counts from rounded cumulative targets keep the track aligned with the video.

**Evidence:** [caption_timing.py](../skills/video-avantage/scripts/caption_timing.py).

### Cheap path and premium path

**Meaning:** The two ways to animate a milestone graphic: a free zoom, or generated
motion costing real money per clip.

**Origin:** The first milestone build, produced both ways for comparison.

**Why it matters for building:** The cost gap is roughly forty to fifty times, so the
path is the requester's decision on every build, and actual spend is reported back
rather than buried in a log.

**Evidence:** [Cheap or premium](../skills/milestone/README.md).

### Confirmed by ear

**Meaning:** A sound-dependent choice accepted by a person listening to a short test
clip, not by a successful generation or a valid voice ID.

**Origin:** Rejected narration takes that were technically correct and audibly wrong.

**Why it matters for building:** Voice endpoint, emotion tags, and brand-name
spelling all change how a voice sounds while every automated check still passes.
Guessing and rebuilding the whole video around the guess is the expensive failure.

**Evidence:** [Narration and character voice](../skills/video-avantage/references/narration-and-voice.md).
