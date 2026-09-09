# Repository instructions

## Scope

This repository contains reusable Roogo skills. Keep every published file suitable for a public repository.

## Skill packages

- Put each skill in `skills/<skill-name>/`.
- Every skill requires a valid `SKILL.md` with `name` and `description` frontmatter.
- Keep the entrypoint concise and route conditional detail to focused references.
- Keep a skill self-contained unless a repository-level dependency is intentional and documented.
- Add `agents/openai.yaml` only when UI metadata or invocation policy is needed.
- Add scripts, references, and assets only when they materially support the workflow.

## Public-safety rules

- Never commit API keys, tokens, cookies, account identifiers, private database data, or production credentials.
- Replace private customer, employee, hotel, booking, and payment data with synthetic fixtures.
- Do not commit generated renders, raw captures, dependency directories, or temporary working files.
- Confirm that every third-party asset is redistributable and record its source and license when required.

## Validation

- Validate every new or changed skill with the Codex skill validator.
- Test executable helpers directly.
- Use public-safe behavioral fixtures for complex skill changes.
- Keep repository-level validation in `scripts/` and CI orchestration in `.github/workflows/`.

## Human documentation and logbook

- Keep each published skill's human-facing `README.md` aligned with its operating instructions: explain purpose, setup, supported modes, examples, limits, and deliverables. Keep package-local links self-contained.
- Read `docs/DOMAIN.md` in full when orienting to the repository's terminology.
- After any non-obvious decision, answered conceptual question, shipped feature/fix, newly coined/clarified domain term, or accepted future commitment, use the `logbook` skill to record it.
- If `logbook` is unavailable, follow the five documents' conventions directly; do not claim the skill was used. Record unfinished work in `docs/ROADMAP.md`, and add `docs/CHANGELOG.md` entries only after verifying shipment to `main`.
