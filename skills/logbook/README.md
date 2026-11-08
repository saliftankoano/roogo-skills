# Logbook

The agent keeps a project's shared memory current, so reasons, plans and the
exact state of what is live do not get lost between sessions or people.

## What it maintains

Five files under `docs/` in the project:

| File | Answers |
|---|---|
| `DECISIONS.md` | Why we chose this, what we ruled out, settled or open |
| `SYSTEM.md` | How the thing we built works, with a small diagram when it helps |
| `CHANGELOG.md` | What shipped and when, only with release evidence |
| `DOMAIN.md` | What words mean in this project |
| `ROADMAP.md` | What we still intend to do: Now, Next, Later |

If they do not exist, the skill creates them, starting `DOMAIN.md` and
`ROADMAP.md` from the templates in `assets/`.

## When it runs

After a non-obvious decision, a stable answer about how the system works, a
shipped feature or fix, a newly explained term, or an accepted "later". Routine
edits do not earn an entry. Add this line to a repository's `AGENTS.md` or
`CLAUDE.md` to make it a habit:

> After any non-obvious decision, answered conceptual question, shipped
> feature/fix, newly coined/clarified domain term, or accepted future
> commitment, use the `logbook` skill to record it.

## Example prompts

- "Log what we just decided about the sale price rule."
- "We merged and released it: update the changelog and roadmap."
- "Review the logbook coverage for the last two weeks" (read-only review).
- "Backfill the logbook for what shipped this month" (writes entries).

## Limits

- A changelog entry needs proof of release (a deploy, a store or OTA release,
  or a merge only where merge means release). Open PRs and local tests are not
  shipped.
- A coverage review only lists gaps; it edits nothing unless asked to repair.
- It records work; it does not start or reprioritize roadmap work.

## Contents

- `SKILL.md`: the agent's operating instructions.
- `assets/domain-template.md`, `assets/roadmap-template.md`: starting files.
- `references/mermaid-system-diagrams.md`: guidance for diagrams in `SYSTEM.md`.
- `references/behavior-trials.md`: scenarios to check after changing the skill.
