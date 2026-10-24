# PRD template

Copy this for each PRD. One file per ask. Replace every `<...>`; delete a
section only if it truly does not apply, and say why in one line.

```markdown
---
type: prd
status: draft-awaiting-<approver>
recorded: "<YYYY-MM-DD>"
owner: <approver>
tags: [product, <area>, prd]
---

# PRD: <what we are doing, in one line>

**Summary:** <one sentence: the change and who it is for.>

Source: <requester>, <date>: « <their words, quoted> ». <If part of a set:
"One of N atomic PRDs from that request.">

## Problem

<One sharp sentence: who is hurting and why.> <Evidence: current behaviour
with file, screen or copy cited; numbers with source and date; any surprising
finding.>

**Before:** <what people see and do today.>
**After:** <what they will see and do once this ships.>

## Goals and non-goals

**Goals:** <the outcome, in one or two lines.>

**Non-goals:**
- <what this PRD does not do; name the sibling PRD that covers it.>

## Users and their needs

- **<user group>:** <what they need from this change.>

## Requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| <n>.1 | <testable outcome> | Must |
| <n>.2 | <testable outcome> | Should |
| <n>.3 | <testable outcome> | Could |

## Constraints

<Security, privacy, pricing, legal, platform, release-path or house-rule
limits. Data changes that need someone to run a migration.>

## Council (only for judgment calls, if the project uses it)

- **Analyst:** <evidence-led take.>
- **Devil's Advocate:** <the strongest case against.>
- **Pragmatist:** <what to ship first.>
- **Contrarian:** <the question nobody asked.>
- **Chairman:** <the recommendation. Not a decision until approved.>

## Dependencies and owners

<Who approves, who builds, who tests, who runs migrations.>

## Success metrics

- **<metric tied to a goal>:** from <baseline> to <target> within <timeframe>
  (source: <logs, database query, survey, count>).
- **Guardrail:** <the harm to avoid while chasing the target, and its source.>

## Open questions

1. <question>? Recommendation: <your answer>.

## Related PRDs

<links to the sibling PRDs from the same request>
```

## Priorities

- **Must:** without it the PRD's goal is not met.
- **Should:** expected, but the release can go without it if blocked.
- **Could:** nice to have; first to cut.
