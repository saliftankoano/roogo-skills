# Bottomless Pit

Retention principle 5 of 6, adapted. Finds every dead end and gives it a relevant next step, while keeping exits visible and endings clean.

## What you get

- An inventory of dead ends and how to trigger each.
- One relevant next step per dead end.
- The honest endings, where the user's job is done.
- On a design canvas: every dead end today beside its redesign.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "Search shows nothing for some areas. Design the empty state."
- "What should happen after someone requests a visit?"
- "Put all our empty and error states on one canvas and fix them."

## Adapted on purpose

The original idea comes from entertainment feeds built to maximise time spent. This package keeps what helps a useful product (real freshness, no accidental dead ends) and rules out the rest: fake urgency, randomness around money, hidden exits, auto-advance. Do not remove the honest-line section.

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `lazy-thumb`, `paved-path`, `slot-machine`, `piggy-bank`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
