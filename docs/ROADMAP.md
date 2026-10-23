# Roadmap

This document tracks accepted work that the team still intends to build. It is
not a history of shipped work; see [CHANGELOG.md](CHANGELOG.md) for that.
See [DECISIONS.md](DECISIONS.md) for reasons, [SYSTEM.md](SYSTEM.md) for current
mechanisms, and [DOMAIN.md](DOMAIN.md) for terminology.

## Now

- [ ] **Apply the October 2026 training-video lessons to `formation-equipe`** — Keychain lookup fix, narration pace and pauses, voice cleaning that survives silent pauses, plan-driven vertical or landscape editing with centred captions and the badge, quote-aware captions, and phone capture of public pages with a list of test data created.
  - Done when: package validation and tests pass and the PR is merged to `main`; then the installed copy is refreshed from `main` and the next delivery is checked against the PRD metrics (pace 130 to 160 words a minute, no editing wrapper, no unreported test uploads).
  - Delivery branch: `feat/formation-equipe-improvements`. Spec: [PRDs 1 to 6](prd/formation-equipe-improvements-2026-10.md). [Decision](DECISIONS.md#training-videos-meet-the-house-rules-by-default--2026-10-22). PRD 7 (a « Carrières » entry in the roogo-web phone menu) belongs to roogo-web, not this repository.

- [ ] **Publish the cleanup skill** — add `nettoyage`: trace, sort into one Downloads folder per conversation, Trash the rest.
  - Done when: package validation and tests pass and the package is merged to `main`; then the local installs are refreshed from `main`.
  - Delivery branch: `feat/nettoyage`. [Decision](DECISIONS.md).

- [ ] **Publish Salif's language-specific Cartesia choices** — keep his French and English voices discoverable in all three narrated packages without changing narrator defaults.
  - Done when: package validation passes and the voice configuration is merged to `main`.
  - Delivery branch: `feat/roogo-video-skills`. [Decision](DECISIONS.md#name-salifs-reusable-cartesia-voices-by-language--2026-09-09).

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

- [x] **Publish the staff training video skill** — merged 2026-10-14 in [PR #8](https://github.com/saliftankoano/roogo-skills/pull/8); recorded in [CHANGELOG.md](CHANGELOG.md).
- [x] **Publish the VSL skill** — merged 2026-10-06 in [PR #6](https://github.com/saliftankoano/roogo-skills/pull/6); recorded in [CHANGELOG.md](CHANGELOG.md).
- [x] **Make the published skill understandable to human repository visitors** — merged 2026-09-09 in [PR #2](https://github.com/saliftankoano/roogo-skills/pull/2); recorded in [CHANGELOG.md](CHANGELOG.md).
- [x] **Publish the improved Voxplainer package and validation** — merged 2026-09-09 in [PR #1](https://github.com/saliftankoano/roogo-skills/pull/1); recorded in [CHANGELOG.md](CHANGELOG.md).
