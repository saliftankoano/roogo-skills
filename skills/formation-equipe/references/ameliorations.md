# Improving this skill

Every run ends with improvement candidates. This is a required step, not an
option: the skill only gets better if each run reports what it got wrong.

## When

At delivery, in the same message as the video. Also immediately, mid-run, when
something blocks the work (a failed step, a correction from the user), so the
evidence is fresh. Collect evidence while you work: keep a short running log in
the project folder (`ameliorations.md`) with what broke, what you measured and
what the user said.

## What counts as a candidate

A change to this skill (instructions, references, scripts, defaults, checks)
that would have made this run faster, cheaper, more accurate, or avoided a
correction. It must come from something that **happened in this run**.

Not candidates: rewording that changes nothing, personal style preferences,
ideas with no evidence, features of the Roogo app itself (report those
separately as product feedback), or anything already in the skill.

## Required format

Number each candidate. Every field is required; a candidate missing its gap or
its evidence is not reported.

```markdown
### 1. <short title>

- **Gap:** what the skill does today, or fails to say, and what goes wrong
  because of it.
- **Evidence:** what happened in this run that proves it. One or more of: a
  command and its error, a measurement (dB, seconds, file size, cost), a frame
  or file path, the user's words quoted, the number of retries or minutes lost.
- **Proposed change:** the exact edit, and the file it belongs in
  (`SKILL.md`, `references/<file>`, `scripts/<file>`).
- **Expected effect:** what improves next run, and how we would know.
- **Confidence:** high, medium or low, and why.
```

Rank candidates by expected effect, most useful first. Three strong candidates
beat ten weak ones.

## If you find nothing

Say "No candidate this run" and give the evidence that the skill held up: the
steps that ran first time, the checks that passed, and that the user made no
correction. Do not invent a candidate to fill the section; do not skip the
section either.

## What happens next

1. The user accepts, changes or rejects each candidate.
2. Accepted candidates go into the skill repository through a branch and a
   pull request, never by editing an installed copy of the skill. The local
   copy is updated from the repository after merge.
3. Each accepted change adds one line to
   [journal-des-lecons.md](journal-des-lecons.md): date, the lesson, and where
   the evidence came from. Rejected candidates are not recorded.
4. Keep the skill short: when a new rule replaces an old one, remove the old
   one in the same change.
