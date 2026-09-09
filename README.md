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
    └── workflows/   Continuous validation added when the first skill lands
```

Each eventual skill belongs in `skills/<skill-name>/` and must contain a `SKILL.md`. A skill may also include `agents/`, `references/`, `scripts/`, and `assets/` when those resources have a concrete purpose.

## Skills

- `voxplainer` — research-led editorial explainers in vertical, long-form, and
  horizontal product formats, with narration, Remotion production, asset provenance,
  and release QA guidance.

Repository-wide licensing and automated CI validation remain planned follow-ups.
