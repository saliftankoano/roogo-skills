# Decisions

Why we made non-obvious choices. See [SYSTEM.md](SYSTEM.md) for mechanisms,
[DOMAIN.md](DOMAIN.md) for terminology, [CHANGELOG.md](CHANGELOG.md) for shipped
changes, and [ROADMAP.md](ROADMAP.md) for unfinished commitments.

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
