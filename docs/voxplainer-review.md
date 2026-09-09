# Voxplainer review corrections

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
