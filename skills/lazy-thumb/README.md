# Lazy Thumb

Retention principle 2 of 6. Counts the steps to an app's core action, cuts them, and puts the control where one thumb reaches it.

## What you get

- The core action per audience.
- A numbered step count today and proposed.
- Control placement and size.
- The smallest version of the action that counts as done.
- On a design canvas: the flow before and after at the same scale, with thumb reach shaded.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "Publishing a listing takes too long. Run lazy thumb on it."
- "Where should the main button go on this screen?"
- "Lay the booking flow out on a canvas, before and after."

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `paved-path`, `slot-machine`, `bottomless-pit`, `piggy-bank`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
