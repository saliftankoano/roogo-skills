---
name: retention-audit
description: >-
  Run all six retention principles on one app, flow or design, in order (the
  itch, lazy thumb, paved path, slot machine, bottomless pit, piggy bank), and
  return a single scored report with the changes ranked by impact and effort,
  or lay the same review out as a before/after board on a Claude Design
  canvas. Use when someone asks "why do people not come back", "audit
  retention", "review this app for engagement", "what would make people keep
  using this", "apply the six retention principles", "run the retention
  audit", wants a design canvas reviewed for stickiness before it is built, or
  asks for a retention board. For a question about one principle only, use
  that principle's own skill.
---

# Retention Audit

Six principles, in the order a user meets them. The first three get a person
in; the last three give them a reason to return.

| # | Principle | Question it answers |
|---|---|---|
| 1 | The Itch | Why would they open it at all? |
| 2 | Lazy Thumb | How little effort does the core action take? |
| 3 | Paved Path | Is the next step already chosen for them? |
| 4 | Slot Machine | Is there something real and new each visit? |
| 5 | Bottomless Pit | Does every screen lead somewhere, and end well? |
| 6 | Piggy Bank | What would they lose by leaving? |

The checks for each are in
[references/six-principles.md](references/six-principles.md). Read it before
auditing. If the individual skills (`the-itch`, `lazy-thumb`, `paved-path`,
`slot-machine`, `bottomless-pit`, `piggy-bank`) are installed, load the one
for any principle that needs depth; this skill works without them.

Principles 4 and 5 are deliberately adapted. The originals come from
entertainment feeds built to maximise time spent. Here they mean "real
freshness" and "no accidental dead ends, with honest endings". Do not restore
the casino version, whatever the app.

## Before auditing

1. **Name the audiences.** Audit each separately when they have different
   core actions (in a marketplace, the person searching and the person
   listing).
2. **Name the healthy rhythm.** Daily, weekly, or only when a need arises.
   Judge the app against that rhythm. An app for an occasional need that
   chases daily opens will annoy people.
3. **Gather evidence.** The running app or its screens, the code for the core
   flows, notification and message templates, the data model, and any usage
   numbers with their date and source. Mark anything not verified as a guess.

## Audit

Go through the six in order. For each one:

- state what exists today, with a file path, a screenshot or a quoted string;
- give a score from 0 to 3 (0 absent, 1 weak, 2 working, 3 strong);
- list the changes, each with expected impact and effort (small, medium,
  large);
- run that principle's honest-line check and drop anything that fails it.

Stop at findings a team could act on this week. Ten ranked changes beat forty
observations.

## Output: report

```
# Retention audit: <app or flow>, <date>
Audiences and healthy rhythm
Scorecard: principle | score 0-3 | one-line reason   (per audience)
Findings by principle: today (with evidence) | changes
Ranked changes: # | change | principle | impact | effort
Do first: the three changes with the best impact for the least effort
Not recommended: tactics considered and rejected on the honest line, and why
Open questions and guesses to verify
```

Present recommendations as proposals. Nothing in the report is a decision
until the product owner approves it, and nothing is "live" until it is
verified in production.

## Output: Claude Design canvas

When the work is a design, or the user asks for a board, lay the audit out on
a canvas instead of, or alongside, the report. The layout is in
[references/canvas-board.md](references/canvas-board.md).

Use this in both directions:

- **Reviewing an existing canvas:** read the artboards, run the six checks on
  what is drawn, and add an "after" beside each screen that changes.
- **Designing something new:** run the six checks on the plan before drawing,
  so the first draft already has its trigger, its one-step core action, its
  defaults, its fresh surface, its next steps and its stored value.

## Ground rules

- Evidence over opinion: every finding points to something real.
- Design inside the app's real layout and design system.
- Respect the person: no fake urgency, no hidden exits, no defaults that
  serve only the business, no data taken without telling them.
