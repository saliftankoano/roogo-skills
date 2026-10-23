# Decisions

Why we made non-obvious choices. See [SYSTEM.md](SYSTEM.md) for mechanisms,
[DOMAIN.md](DOMAIN.md) for terminology, [CHANGELOG.md](CHANGELOG.md) for shipped
changes, and [ROADMAP.md](ROADMAP.md) for unfinished commitments.

### Training videos meet the house rules by default — 2026-10-22

**Decision:** `formation-equipe` editing now defaults to the house rules: the
capture fills the frame (1920x1080 or 1080x1920, set in the plan), captions sit
toward the centre in a dark brown box with cream text, and the Roogo badge is
drawn top right on screen shots and never on the title and closing cards. The
badge image is a plan setting (`badge_logo`, defaulting to the card logo) and
the badge is drawn inside the skill. Clones default to speed 0.9; every voice
gets a 0.9 s pause between paragraphs. Voice cleaning ignores digital silence
and copies a file with nothing audible between words as "already clean".

**Why:** The 22 October 2026 run needed a 150-line wrapper to get a compliant
vertical video, cream captions were unreadable on cream screens, the clone read
185 words a minute, and the pauses then crashed the cleaning step. See the
[PRDs](prd/formation-equipe-improvements-2026-10.md).

**Ruled out / alternatives:** Keeping the former bottom caption band as the
default for old plans (PRD 4.6): it breaks the house rule for every plan reused
without the new settings, so the old look is opt-in only (`caption_layout:
"band"`, `badge: false`, verified pixel-identical). Importing the badge helper
from `video-avantage` (keeps each skill self-contained). A shared config file
for the badge (one more file to set up for a single path). Speed 0.9 for the
house voice (not judged by ear yet; PRD 2 open question).

### Agents clean up after themselves into one folder per conversation — 2026-10-14

**Decision:** Add `nettoyage`. Agents trace what they create, then sort it at
the end: the final output is copied to `final/` and what is needed for later
changes goes to `a-reprendre/`, both in one folder per conversation under
`~/Downloads/Agent/`, with a `LISEZMOI.md` index. Everything else goes to the
system Trash, and processes and tabs the agent opened are closed.

**Why:** Long tasks leave test renders, caches, running servers, tabs and stray
branches behind. Salif wants no residue, one place per conversation, and a copy
of the final output in that place even when it is also delivered elsewhere.

**Ruled out / alternatives:** Permanent deletion (not recoverable); cleaning
anything the agent did not create; removing records outside the machine
without asking; a dated-first folder name (the house rule names by subject,
date last).
### Staff training videos get their own standalone skill that improves itself — 2026-10-14

**Decision:** Add `formation-equipe` for Roogo staff training videos: real
production captures from the user's signed-in browser, a cleaned cloned-voice
narration, slow camera moves, script-spelled captions, a credited music bed and
automated checks. The skill stands on its own and must end every run with
improvement candidates, each naming the gap it closes and the evidence from that
run; accepted candidates reach the skill only through a pull request here.

**Why:** The staff videos made in October 2026 were good, but the method lived
in a general product-demo skill owned by another organization, which cannot be
published here, and the Roogo lessons (voice cleaning, capture hygiene, music
behaviour) lived only in one project folder. Salif wants clearly separated skills
per job and a skill that gets better with each run.

**Ruled out / alternatives:** Copying the general product-demo skill (not ours to
publish); a Roogo skill that delegates to it (Salif wants each job defined by its
own skill); optional retrospectives (they get skipped, so the step is mandatory,
and "no candidate" must be justified with evidence).

**Status:** Settled; verified merged to `main` in [PR #8](https://github.com/saliftankoano/roogo-skills/pull/8).

### Publish the VSL as its own package, real assets first — 2026-10-06

**Decision:** Add `vsl` for sales videos (website 16:9, social 9:16) built in
HyperFrames with real listing photos, a few generated shots for people, Sandrine,
house captions and a staggered store-badge outro.

**Why:** The format was iterated with the founder: ffmpeg zoom shook on stills,
long single shots felt static, generated photos were used where real listing
photos existed, some sound effects (gate creak, key jingle, motorbike engine, a
loud phone buzz) were annoying, and the phone number was easier to read when each
pair was highlighted as spoken.

**Ruled out / alternatives:** Cropping the horizontal video for vertical (weaker
layout); shipping sound effects, logo, fonts or music (licenses not recorded);
using the stores' official badge artwork (not redistributed here).

**Status:** Settled; verified merged to `main` in [PR #6](https://github.com/saliftankoano/roogo-skills/pull/6). Later rule added the same day: choose photos separately for each format.

### Publish the POV listing walkthrough as its own package — 2026-09-28

**Decision:** Add `visite-pov` for live listings that only have photos: camera
drift on the real photos, Sandrine on Cartesia, a HyperFrames outro whose only
action is calling or messaging the Roogo number, and French captions for posting.

**Why:** The format was proven on a real listing with the founder's review: the
earlier outro had too much text and white, the ElevenLabs narrator sounded flat
and changed a year between takes, and an app-download button competed with the
contact action a listing video exists to produce.

**Ruled out / alternatives:** Folding it into `appel-proprietaires` (different
audience and direction of the call); AI presenters for property videos (banned
after frozen presenters and poor lip sync); shipping the logo, fonts or listing
photos (not public-safe; supplied per machine).

**Status:** Settled; verified merged to `main` in [PR #5](https://github.com/saliftankoano/roogo-skills/pull/5).
See [SYSTEM.md](SYSTEM.md#how-do-the-roogo-video-formats-divide-the-work).

### Name Salif's reusable Cartesia voices by language — 2026-09-09

**Decision:** Preserve Salif's French voice and add his distinct English voice to
each narrated package's self-contained Cartesia reference, at his explicit request.

**Why:** Future productions need a discoverable language-to-voice mapping without
guessing from unnamed profiles or assuming one voice suits both languages.

**Ruled out / alternatives:** No global provider switch, replacement of approved
casts or narrator defaults, implied spending consent, new voice cloning, or stored
credentials. The reusable IDs do not grant voice rights to repository readers.

**Status:** Settled; implemented on the video-skills branch, not yet verified on
main. See [voice configuration](SYSTEM.md#how-are-salifs-reusable-voices-selected).

### Plan audience and message before video production — 2026-09-09

**Decision:** Add an audience/message planning layer across all Voxplainer modes,
with campaign organization and a distinct message-readiness review. Deliver this
through a repository PR before updating installed copies or revising campaign media.

**Why:** Feature-led films can confuse prospective customers, business decision
makers, and operational users even when their facts, visuals, and encoding pass.

**Ruled out / alternatives:** Another visual mode would not solve audience mixing.
One film per feature and mandatory sales CTAs would force inappropriate messages.
Blanket script rewrites during technical fixes would exceed approved scope.

**Status:** Settled direction; PR delivery and later adoption remain tracked in
[ROADMAP.md](ROADMAP.md). See [SYSTEM.md](SYSTEM.md#audience-and-message-planning).

### Publish the three Roogo ad formats as separate self-contained packages — 2026-09-09

**Decision:** Migrate the owner call-out, feature explainer, and milestone video
workflows as three packages with explicit exclusions in each description, and let
them repeat shared Roogo video conventions and helpers instead of importing a common
module. Inline the private production playbooks into package references, replacing
machine paths, campaign folders, and customer specifics with supplied inputs.

**Why:** Choosing the wrong format wastes paid generation, so the boundary has to be
visible at invocation time rather than discovered mid-build. A package must also stay
portable when it is copied alone into a user skills directory, and the private
playbooks it grew from cannot be published as they were written.

**Ruled out / alternatives:** One combined video skill with internal branching, which
would load every format's rules on every invocation; a shared repository-level module
for the watermark and conventions, which would break a package copied on its own;
pointing at the private playbook paths, which are unreadable outside one machine.

**Status:** Settled direction; delivery tracked in [ROADMAP.md](ROADMAP.md).

### Separate the human guide from the agent contract — 2026-09-09

**Decision:** Put a human-facing README inside each published skill, linked from
the repository catalog. Keep detailed operational rules canonical in SKILL.md and
its references. Use the five-document logbook for repository memory.

**Why:** A visitor should understand installation, modes, scope, and review without
having to reconstruct the workflow from instructions addressed to an agent.

**Ruled out / alternatives:** Expanding SKILL.md into a user manual would burden
every invocation. A repository-only guide would be less visible when browsing or
copying an individual package. One combined diary would blur shipped and planned work.

**Status:** Settled direction; documentation delivery is tracked in [ROADMAP.md](ROADMAP.md).

### Preserve complementary visual modes and evidence boundaries — 2026-09-09

**Decision:** Retain Editorial Motion, Cinematic Parallax, and Layered 2.5D as
complementary grammars. Choose format independently; treat story-first and
animated-film as optional treatments. Product captures prove only verified states.

**Why:** Production feedback showed that a single presentation template, static
slides, and stale screenshots cannot serve every explanation or credible demo.

**Ruled out / alternatives:** No universal card layout, mandatory 2.5D upgrade,
cropped vertical derivative, or fabricated UI proof.

**Status:** Settled; published in [PR #1](https://github.com/saliftankoano/roogo-skills/pull/1).
See [SYSTEM.md](SYSTEM.md) for routing and the guide's mode comparison.

### Publish self-contained, public-safe packages — 2026-09-09

**Decision:** Keep reusable instructions, references, and helpers together; keep
private credentials and generated media outside the repository. Publish original
code and documentation under MIT without granting third-party media or voice rights.

**Why:** A public skill must be portable without exposing the campaign's private
data or implying that downloaded assets and named voices are freely reusable.

**Ruled out / alternatives:** Shipping the entire local production workspace,
depending on private machine paths, or treating voice IDs as usage permission.

**Status:** Settled; enforced by package conventions, review, and validation in
[PR #1](https://github.com/saliftankoano/roogo-skills/pull/1).
