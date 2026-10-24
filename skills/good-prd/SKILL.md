---
name: good-prd
description: >-
  Write product requirements documents (PRDs) that get people to agree on the
  problem before anyone argues about the solution. One PRD per ask: a request
  with several asks becomes several atomic PRDs, each answering "what are we
  doing?" with one thing. Grounded in evidence (code, data, logs) with a
  before/after, goals and non-goals, testable Must/Should/Could requirements,
  2 to 4 metrics with a guardrail, and honest open questions. Use for "write a
  PRD", "fais un PRD", "écris les PRDs", "spec this", "product requirements",
  "turn this request into PRDs", or whenever a feature request should be
  agreed before building. Do not use for release notes, user guides, or a
  bug fix small enough to just do.
---

# Good PRD

A PRD is a tool for getting people to agree on the problem before anyone argues
about the solution. It passes when engineering could start building, and
approvers could say yes, **without a meeting**.

Read [references/principles.md](references/principles.md) once per session. Write
each PRD from [references/template.md](references/template.md). A complete
example is in [references/example.md](references/example.md).

## Rule 1: one PRD, one ask

Each PRD answers "what are we doing?" with **one thing**. Before writing,
split the request into its asks:

- List every distinct change the requester asked for, in their words.
- Split any item joined by "and" that could ship, be approved or be rejected
  on its own (a label change and a layout change are two PRDs).
- Keep together only what cannot ship separately.
- Name each PRD by its subject, not by date or number: `PRD - <what it does>`.

One file per PRD. Cross-link siblings in a "Related PRDs" line, and state in
each PRD's non-goals what a sibling covers, so scope never overlaps.

## Rule 2: evidence before writing

Never write a problem from the request alone. For each PRD, find out:

1. **Current behaviour.** Read the code or the product. Cite files, screens
   and copy exactly ("the star is grey `neutral[500]`, 11 pt").
2. **Numbers.** Count what you can (records, logs, usage) and give each number
   its source and date.
3. **What already exists**, so nothing is rebuilt.
4. **Conflicts** with pricing, policy, promises to customers or other teams'
   work. A PRD that hides one will be rejected later.

Read-only. Gathering evidence never changes data, code or settings. Surprising
findings (a feature that silently never worked) go in the problem, plainly.

## Rule 3: write it

Follow the template's order: summary, problem (with **Before / After**), goals
and non-goals, users and needs, requirements table, constraints, dependencies
and owners, success metrics, open questions.

- **Problem first, one sharp sentence** on who is hurting and why, then the
  evidence.
- **Requirements as outcomes**, testable, each with an ID and Must / Should /
  Could. An implementation detail is an example, not the rule.
- **Metrics:** 2 to 4, each tied to a goal, with baseline, target, timeframe
  and data source, plus at least one guardrail. If there is no data source,
  say what must be set up first.
- **Open questions:** real ones, each with your recommendation, so the
  approver can answer in one word.
- Quote the requester's words for the source line, with the date.

## Rule 4: judgment calls

When a PRD involves a judgment call (removing a feature, a pricing effect, a
policy change), and the project uses a structured method for recommendations,
include it in the PRD. For Roogo that is the LLM Council: Analyst, Devil's
Advocate, Pragmatist, Contrarian give independent takes, then a Chairman
recommends. Disagree with the requester when the evidence says so. A
recommendation is not a decision.

## Rule 5: status and storage

- Every new PRD is `status: draft-awaiting-<approver>`. It becomes approved
  only when the approver says so; record who and when. Never present a draft
  as policy, or "merged" as "in production".
- Save PRDs where the project keeps product decisions. For Roogo: the business
  vault, folder `06 Product and technology/`, one note per PRD, frontmatter
  `type: prd`, and a row in `Roadmap and delivery status` linking them all.
- Keep the project's language rules: Roogo vault notes are in English, with
  French interface copy quoted in French; no em dash mid-sentence and no emoji
  in product copy.

## Final check, per PRD

- [ ] Answers "what are we doing?" with one thing.
- [ ] Problem backed by cited evidence, with Before / After.
- [ ] Non-goals name what sibling PRDs cover.
- [ ] Every requirement testable, with ID and priority.
- [ ] 2 to 4 metrics, each with baseline, target, timeframe, source; one guardrail.
- [ ] Conflicts surfaced; open questions carry a recommendation.
- [ ] Status is draft until approved; saved and linked where the project keeps PRDs.

End by telling the requester which PRDs were written, where, and the one or
two decisions each needs from them.
