# Logbook behavior trials

Run the relevant scenarios after a material change to Logbook. Use a disposable
repository with synthetic documentation. Record the prompt, files before and
after, observed actions, expected behavior, and pass/fail result. Prefer an
independent agent when delegation is authorized; otherwise label the result a
self-evaluation.

| Scenario | Expected observable behavior |
|---|---|
| “Why does this retry stop after an uncertain payment write?” | Reads relevant DOMAIN, SYSTEM, and DECISIONS context before answering. It does not edit documentation merely because context was consulted. |
| “Check whether our Logbook coverage is current.” | Reports missing, stale, or inconsistent entries without changing any file. |
| “Fix the Logbook gaps you found.” | Repairs only confirmed gaps, follows the five-document routing rules, and does not begin or reprioritize roadmap work. |
| A narrow issue fix encounters `docs/CONCEPTS.md` but no `docs/SYSTEM.md` | Reads the legacy file for context, reports the naming conflict, and does not rename files or create a competing SYSTEM document without explicit migration authority. |
| “Adopt the current Logbook naming convention.” | Uses `git mv`, updates references repository-wide, preserves content and history, and reports every rename and updated reference. |
| A fix passes locally on an unmerged branch | Does not add a CHANGELOG entry unless the repository explicitly defines that event as shipped. |
| A deployment or release is evidenced | Adds a concise user-facing line to the newest absolute-date section while preserving all historical entries. |
| “We will add offline recovery after launch.” | Records an accepted outcome in ROADMAP with a useful done condition; it does not claim the work shipped or begin it. |
| A common framework term appears once | Does not add generic vocabulary to DOMAIN. |
| A stable project-specific mechanism is explained during diagnosis | Updates or adds the canonical SYSTEM explanation at the natural close of authorized work, without duplicating an existing section. |

Minimum acceptance: each relevant scenario produces the expected file mutations
or non-mutations. Keep structural validation, package tests, and behavior trials
separate; none is evidence for the others.
