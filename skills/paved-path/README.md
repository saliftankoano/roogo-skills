# Paved Path

Retention principle 3 of 6. Makes the core action the first thing seen and gives every forced decision a default that serves the user.

## What you get

- A first-screen check.
- An inventory of every decision the app forces.
- A default for each, with where it comes from.
- Decisions that can be deleted.
- On a design canvas: first open before and after, and a decision map.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "The home screen is a menu. Pave the path."
- "What should the default filters be?"
- "Mark every decision on this canvas and propose a default for each."

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `lazy-thumb`, `slot-machine`, `bottomless-pit`, `piggy-bank`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
