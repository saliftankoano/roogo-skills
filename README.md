# Roogo Skills

Reusable Codex skills for Roogo product, operations, marketing, and engineering workflows.

Skills are reviewed, improved, sanitized for public use, and migrated here one at a
time. Each skill keeps its operating instructions, focused references, helper scripts,
and public-safe metadata together.

## Repository layout

```text
roogo-skills/
├── skills/          Self-contained skill packages
├── docs/            Repository-level standards and decisions
├── scripts/         Repository validation and maintenance tools
├── tests/
│   └── fixtures/    Public-safe behavioral test inputs
└── .github/
    └── workflows/   Package validation and executable regression tests
```

Each skill belongs in `skills/<skill-name>/` and must contain a `SKILL.md`. A skill may also include `agents/`, `references/`, `scripts/`, and `assets/` when those resources have a concrete purpose.

## Skills

- [Voxplainer — human guide](skills/voxplainer/README.md) — research-led editorial explainers in vertical, long-form, and
  horizontal product formats, with audience/message planning, campaign organization,
  narration, Remotion production, asset provenance,
  and release QA guidance.
- [Appel a proprietaires — human guide](skills/appel-proprietaires/README.md) — owner call-out ad bundles
  built from one renter or buyer demand: a narrated 9:16 carousel video with burned-in
  French captions, plus the social copy for publishing.
- [Video avantage — human guide](skills/video-avantage/README.md) — feature and benefit
  explainer videos built entirely from generated actors, narration, and comparison
  cards, for when no listing photography exists.
- [Milestone — human guide](skills/milestone/README.md) — an existing celebration
  graphic turned into a scored 9:16 video post, on a cheap zoom path or a paid
  generated-motion path.

A skill is a set of instructions and supporting resources for an agent, not a
standalone video app. Start with each human guide for installation, requirements,
modes, example prompts, and review checkpoints; its `SKILL.md` is the agent-facing
operating contract.

The three Roogo ad formats are deliberately separate packages with explicit
boundaries, because choosing the wrong one wastes paid generation. One renter or
buyer demand calling owners in is `appel-proprietaires`; a feature or benefit with no
photography to build from is `video-avantage`; an existing celebration graphic to
animate is `milestone`.

## Quick start

Copy the package directory you want, for example `skills/voxplainer`, into your
configured Codex user skills directory, commonly `~/.codex/skills/voxplainer`. If it
already exists, compare and back up the existing copy before replacing it. Open a new
task and invoke the skill by name, for example:

```text
$voxplainer Create a French 60-second horizontal product explainer in Editorial
Motion. Audience: hotel managers. Explain why request approval is different
from payment. Use the verified evidence and brand assets I provide; do not
invent product states. Start with the script and storyboard only, without
paid generation. List missing inputs before production.
```

```text
$appel-proprietaires A client is looking for a shop on the Nora road, budget
50 000 FCFA a month, urgent. Start with the script and the music pick only, no
generation yet, and confirm the spelling of every place name with me.
```

See each package's usage guide for setup, modes, and review checkpoints.

## Project logbook

- [System](docs/SYSTEM.md) — how packages, production guidance, and validation work.
- [Decisions](docs/DECISIONS.md) — why we chose this structure and workflow.
- [Changelog](docs/CHANGELOG.md) — verified changes shipped to `main`.
- [Domain](docs/DOMAIN.md) — the vocabulary used in our skills and reviews.
- [Roadmap](docs/ROADMAP.md) — accepted work still to finish.

The logbook documents this skills repository, not the Roogo application's release
history. `logbook` is used to maintain these records; it is not bundled as a skill
in this repository.

## Validation

Use Python 3.10 or newer, PyYAML 6, FFmpeg (including ffprobe), Git and Bash:

```sh
python3 scripts/validate_skills.py
python3 -m unittest discover -s tests -v
```

CI runs the same package and executable checks and checks committed changes for
whitespace errors. Reference validation follows links from each `SKILL.md`, including
nested references; a disconnected reference cycle fails. When the Codex skill-creator tools
are installed, also run their `quick_validate.py` against each changed package.
Public behavioral review cases live in `tests/fixtures/voxplainer-review.md`; they
require judgment and are not represented as automatic rendering tests.

## License and voice configuration

The repository's original instructions and code use the [MIT License](LICENSE).
This license does not grant rights to Roogo trademarks, third-party media, or any
person's voice. Those assets retain their own rights and provider terms.

The named voice IDs are intentional Roogo configuration, not API keys or account
credentials. Publishing an ID does not make its voice available to every provider
account or grant permission to clone or use it. Validate access and usage rights
before generation; if a voice is unavailable, request an authorized alternative
instead of silently substituting one. Keep credentials and private access records
outside this repository.
