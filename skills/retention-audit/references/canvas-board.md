# Retention board on a Claude Design canvas

A design canvas holds live artboards side by side, which suits this audit: the
reader sees today and the proposal together, one principle per row.

## Mechanics

Create the canvas with the Artifact tool's Design type (ask the tool for its
design quickstart first, then follow the instructions the new canvas returns).
Those instructions govern how artboards are written and published. This file
only governs what is on them. If a design system is available for the product,
use it.

When reviewing a canvas that already exists, read it first and add to it. Do
not replace artboards the user made.

## Layout

One section per audience when they differ. Within a section:

| Row | Left artboard | Right artboard(s) |
|---|---|---|
| 0. Scorecard | Six principles with a 0 to 3 score each and a one-line reason | "Do first": the three best changes |
| 1. The Itch | Lock screen with today's notification | Rewritten notification, and the screen it opens |
| 2. Lazy Thumb | Core flow today, every screen numbered | Shortened flow, same scale, with thumb reach shaded |
| 3. Paved Path | First screen on open today, decisions marked | First screen with the core action under way and defaults in place |
| 4. Slot Machine | Home or results as a returning user sees it today | The same screen on three different visits, plus the quiet-day state |
| 5. Bottomless Pit | Each dead end as it looks today | Each with its next step, plus the good ending |
| 6. Piggy Bank | Key screen for a brand-new user | The same screen after a month of use, plus the "your space" surface |

Name artboards so the pairing is obvious: `2 Lazy Thumb / before`,
`2 Lazy Thumb / after`.

## Rules for the artboards

- **Real layout.** Every screen sits inside the product's actual navigation,
  headers and tab bar, at real device size. A screen floating without its
  chrome hides the constraints that matter.
- **Real content.** Real strings, plausible real data, final copy for empty
  states and notifications. No placeholder text.
- **Before is honest.** Draw "today" from a screenshot or the code, not from
  memory, and do not make it worse than it is.
- **Few words.** The pairing carries the argument. Give each "after" one short
  note saying what changed and which principle it serves.
- **Only what can be true.** Do not draw a signal, a count or a
  personalisation the product cannot truthfully produce.
- **Skip empty rows.** If a principle is already strong, say so on the
  scorecard and leave its row out.

## When the canvas is the starting point

For a new screen or flow, run the six checks on the plan before drawing, then
draw only the "after" column. Add the scorecard as the first artboard so a
reviewer can see which principles the design claims to satisfy and challenge
each one.

## Hand-off

End with the same ranked list as the written report (change, principle,
impact, effort), either as a final artboard or in the reply. The board is a
proposal until the product owner approves it.
