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

- `voxplainer` — research-led editorial explainers in vertical, long-form, and
  horizontal product formats, with narration, Remotion production, asset provenance,
  and release QA guidance.

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
