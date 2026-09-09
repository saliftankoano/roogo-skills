# Decisions

Why we made non-obvious choices. See [SYSTEM.md](SYSTEM.md) for mechanisms,
[DOMAIN.md](DOMAIN.md) for terminology, [CHANGELOG.md](CHANGELOG.md) for shipped
changes, and [ROADMAP.md](ROADMAP.md) for unfinished commitments.

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
