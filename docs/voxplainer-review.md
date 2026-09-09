# Voxplainer review corrections

## Audience/message planning review — 2026-09-09

Reviewed cases I–M in the [public fixtures](../tests/fixtures/voxplainer-review.md)
by walking through the new [planning reference](../skills/voxplainer/references/audience-and-messaging.md)
and its entrypoint routing. This is a maintainer instruction review, not an
independent agent run, generated-film evaluation, or real audience study.

| Case | Decision reached in the walkthrough | Review outcome |
| --- | --- | --- |
| Mixed six-film inventory | Propose viewers and communication jobs before scripts; identify split/merge options while retaining the commissioned count until accepted. | Covered; no paid production authorized. |
| Organizer film with three actors | Keep one organizer-facing story; traveler and hotel actions explain the organizer's outcome without assigning staff-only controls to the viewer. | Covered; no forced three-film split. |
| General education | Explain nightly availability to non-specialists and resolve the question without a sales action or invented demographic profile. | Covered; no mandatory commercial CTA. |
| Subtitle-only repair | Preserve script, voice, runtime, and lineup; report any audience concern separately. | Covered; no strategy rewrite or repeated approval gate. |
| Valid encoding, mixed addressees | Flag traveler → staff reviewer → owner shifts as a messaging defect despite technical success; ask for a primary-viewer decision before script lock. | Covered; actual viewer comprehension remains untested. |

Package validation, the Codex skill validator, all 19 executable regression tests,
and changed-line whitespace checks passed locally. The five new scenarios are
judgment-based fixtures, not five new automatic tests. No installed skill or
campaign media was changed by this review.

## Initial production-guidance review

The initial package review identified six issues. The PR now:

- reports silent or unmeasurable audio as a failure with strict JSON `null`
  measurements, and rejects invalid numeric limits;
- allows unbranded scenes and limits duplicate identity treatments where used;
- checks SDR pixel format, color range and BT.709 metadata, audio format, exact
  promoted filenames and SHA-256 hashes, with explicit delivery overrides;
- accepts private supplied assets through a local source and rights record;
- includes an outro URL only when requested or approved;
- offers a bundled capture reference when the optional Product Video skill is absent.

The repository includes MIT licensing for original code and instructions, CI package
checks and audio regression tests. Named voice IDs remain deliberate configuration;
the license grants no voice, media or trademark rights.

## Behavioral decision review

Reviewed the eight synthetic cases in `tests/fixtures/voxplainer-review.md` against
the revised instructions. These are manual instruction walkthroughs, not paid
generation tests or independent rendered-video evaluations.

| Case | Observed decision from the revised instructions | Result |
| --- | --- | --- |
| Private photo | Local filename and permission record satisfy supplied-asset provenance; no public URL required. | Pass |
| Unbranded tutorial | Unbranded scenes and the requested ending are explicitly allowed; the contract controls duration and audio. | Pass |
| Standalone skill | Optional Product Video handoff has a bundled fallback and preserves the requested format. | Pass |
| Stale UI | The capture-freshness rule requires recapture before claiming current UI proof. | Pass |
| Ordinary SDR master | Finishing checks explicitly include color and audio defaults, missing metadata, promoted filenames and hashes. | Pass |
| HDR override | Explicit delivery requirements override the SDR defaults and must be checked against the contract. | Pass |
| Static beat and flashing captions | Meaningful visual changes and phrase holds follow processed narration; an isolated repair preserves accepted audio and runtime. | Pass |
| Unavailable voice | Voice access stays unresolved while script work continues; no silent substitution. | Pass |

## Executable coverage

The audio suite uses real generated WAV files for the normal, silent and threshold
failure paths, plus missing/corrupt files and invalid limits. JSON is parsed with a
strict non-finite-number rejection. The package suite checks a valid minimal skill
and malformed package inputs. CI does not claim to prove visual quality, voice
naturalness, license validity, or compliance of a future rendered master; those
remain evidence-based production reviews.

The follow-up validation review corrected two blind spots: references are now
traversed from `SKILL.md` rather than counted as linked anywhere, and CI checks
committed changes rather than a clean working tree. Pull requests use the merge
base; pushes use the before/after revisions, with the empty tree for a first push.
Tests execute the workflow's actual whitespace shell step in disposable Git
repositories and cover disconnected reference cycles and nested reachable chains.
The full suite now has 19 tests. Checkout and Python setup use pinned Node 24 action
releases to remove the deprecated runtime warning.
