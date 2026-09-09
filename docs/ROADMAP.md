# Roadmap

This document tracks accepted work that the team still intends to build. It is
not a history of shipped work; see [CHANGELOG.md](CHANGELOG.md) for that.
See [DECISIONS.md](DECISIONS.md) for reasons, [SYSTEM.md](SYSTEM.md) for current
mechanisms, and [DOMAIN.md](DOMAIN.md) for terminology.

## Now

- [ ] **Publish audience-first video planning** — guide audience selection, message framing, campaign organization, and message-readiness review across Voxplainer modes.
  - Done when: agent guidance, human examples, and public behavioral review cases are validated and merged to `main`.
  - Delivery branch: `feat/voxplainer-audience-messaging`. [Decision](DECISIONS.md).

- [ ] **Publish the three Roogo ad-format skills** — migrate the owner call-out, feature explainer, and milestone video workflows as self-contained, public-safe packages with human guides and tested timing helpers.
  - Done when: the three packages, the catalog entries, the logbook updates, and the helper tests are validated and merged to `main`.
  - Delivery branch: `feat/roogo-video-skills`. [Decision](DECISIONS.md).

## Next

- [ ] **Adopt the reviewed skill locally and revisit the video campaign** — apply the accepted audience/message guidance before further campaign revisions.
  - Done when: after the PR is reviewed and merged, the installed skill is compared and updated, and campaign audience/message briefs are revisited with the user.
  - Dependency: audience-first planning PR. No local installation, campaign rewrite, narration purchase, or render is part of that PR.

## Later

Additional skill migration remains subject to selecting and reviewing each package;
no specific next package or delivery date is committed. Only Voxplainer is currently published.

## Recently completed

- [x] **Make the published skill understandable to human repository visitors** — merged 2026-09-09 in [PR #2](https://github.com/saliftankoano/roogo-skills/pull/2); recorded in [CHANGELOG.md](CHANGELOG.md).
- [x] **Publish the improved Voxplainer package and validation** — merged 2026-09-09 in [PR #1](https://github.com/saliftankoano/roogo-skills/pull/1); recorded in [CHANGELOG.md](CHANGELOG.md).
