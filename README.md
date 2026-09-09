# Roogo Skills

Reusable Codex skills for Roogo product, operations, marketing, and engineering workflows.

This repository currently contains only the repository structure. Existing skills will be reviewed, improved, sanitized for a public repository, and migrated in a later pass.

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

## Current status

- Public GitHub repository shell created.
- No production skill content has been published.
- Licensing, the initial skill catalog, and automated validation will be finalized before the first push.

