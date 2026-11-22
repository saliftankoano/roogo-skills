# Retention Audit

Runs all six retention principles on one app, flow or design and returns a scored report with ranked changes, or a before/after board on a Claude Design canvas.

## What you get

- Audiences and the healthy usage rhythm.
- A 0 to 3 scorecard across the six principles.
- Findings with evidence.
- Changes ranked by impact and effort, with the three to do first.
- Tactics rejected on the honest line.
- On a design canvas: one before/after row per principle.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "Run the retention audit on the mobile app."
- "Why do people not come back after the first week?"
- "Review this design canvas against the six retention principles before we build it."

## Adapted on purpose

The original idea comes from entertainment feeds built to maximise time spent. This package keeps what helps a useful product (real freshness, no accidental dead ends) and rules out the rest: fake urgency, randomness around money, hidden exits, auto-advance. Do not remove the honest-line section.

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `lazy-thumb`, `paved-path`, `slot-machine`, `bottomless-pit`, `piggy-bank`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
- [references/six-principles.md](references/six-principles.md): the checks and honest line for each principle.
- [references/canvas-board.md](references/canvas-board.md): the board layout for a Claude Design canvas.
