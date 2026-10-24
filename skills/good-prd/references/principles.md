# The Art of a Good PRD

A PRD is a tool for getting people to agree on the problem before anyone argues about the solution.

## Core Principles

1. **Lead with the problem.** One sharp sentence on who's hurting and why. If the pain isn't convincing, nothing else matters.
2. **Non-goals are as important as goals.** They stop scope creep before it starts.
3. **Write requirements as outcomes, not implementations.** "Claude cannot post to Slack" is a requirement. A specific API scope is an example, not the rule.
4. **Make every requirement testable, with a priority.** If you can't tell whether it's done, it's a wish. Use Must / Should / Could.
5. **List open questions honestly.** They show the thinking and give reviewers something specific to react to.

## Success Metrics

- **Tie each metric to a goal.** A goal with no metric can't be verified; a metric with no goal is noise.
- **Measure outcomes, not output.** "Feature shipped" is output. "Browser workaround no longer used" is an outcome.
- **Make it measurable: baseline, target, timeframe.** "Reduce stale answers" becomes "stale answers drop from about 4 in 10 to under 1 in 10 within 30 days of launch."
- **Pair a success metric with a guardrail.** Guardrails catch harm while you chase the target, like "zero unintended Slack messages."
- **Know how you'll collect it before launch.** If there's no data source, the metric is a hope. Name it: logs, a survey, a count.
- **Keep it to 2–4 metrics.** More than that and nobody watches any of them.

## Standard Structure

1. Title and one-line summary
2. Problem
3. Goals and Non-Goals
4. Users and their needs
5. Requirements (ID, requirement, priority)
6. Security / constraints
7. Dependencies and owners
8. Success metrics (with guardrails)
9. Open questions

## Final Test

Could engineering start building, and could approvers say yes, without a meeting? If so, the PRD did its job.
