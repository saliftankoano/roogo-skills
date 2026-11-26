# Slot Machine

Retention principle 4 of 6, adapted. Keeps an app's real reward fresh between visits without gambling mechanics, fake scarcity or randomness around money.

## What you get

- The real reward users come for.
- What a returning user sees today on later visits.
- Real sources of variation and where each is shown.
- The quiet-day state.
- On a design canvas: the same screen on three different visits.

Two ways to use it: audit an existing app from its code and screens, or apply
it while designing on a Claude Design canvas (the Artifact tool's Design type).
Recommendations are proposals until the product owner approves them.

## Example prompts

- "The app looks the same every time I open it. Fix that."
- "Should we add badges or points?"
- "Draw the home screen as a returning user sees it on three different days."

## Adapted on purpose

The original idea comes from entertainment feeds built to maximise time spent. This package keeps what helps a useful product (real freshness, no accidental dead ends) and rules out the rest: fake urgency, randomness around money, hidden exits, auto-advance. Do not remove the honest-line section.

## Requirements and limits

No scripts and no paid services. For an audit it needs access to the app's
code or screens; findings without evidence are marked as guesses. Canvas
output needs an agent with the Artifact tool's Design type; without it the
skill returns the written report only. It does not change the app or send
notifications by itself.

## Related packages

`the-itch`, `lazy-thumb`, `paved-path`, `bottomless-pit`, `piggy-bank`, `retention-audit`. Each works alone. The framework is a six-step retention model taught in
a public app-design talk; the references behind it are Nir Eyal's *Hooked*,
BJ Fogg's behaviour model, Johnson and Goldstein (2003) on defaults, and
B. F. Skinner's work on variable rewards.

## Files

- [SKILL.md](SKILL.md): the agent's operating instructions.
