# Piggy Bank

Retention principle 6 of 6. Makes an app more valuable to each person the more they use it, so returning continues something.

## What you get

- A loss check at one week, one month and six months.
- Signals recorded and signals wasted.
- Deposits the user can build and see.
- How each deposit pays back on the next visit.
- On a design canvas: the same screen on day 1 and day 30.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "People use it once and never return. What would make them come back?"
- "What should we track to personalise the home screen?"
- "Draw the home screen for a new user and for one with a month of history."

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `lazy-thumb`, `paved-path`, `slot-machine`, `bottomless-pit`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
