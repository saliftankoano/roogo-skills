# The Itch

Retention principle 1 of 6. Finds the feeling that makes people open an app and rewrites notifications and copy to speak to it.

## What you get

- A feeling statement per audience.
- The moments in the day or week that feeling occurs.
- Every current notification and message, tagged and rewritten.
- On a design canvas: lock screen before and after, and the screen each message opens.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "Nobody opens the app after day one. Run the itch on our notifications."
- "Write the push notifications for saved-search alerts."
- "On the canvas, show today's lock-screen notification next to a better one."

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`lazy-thumb`, `paved-path`, `slot-machine`, `bottomless-pit`, `piggy-bank`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
