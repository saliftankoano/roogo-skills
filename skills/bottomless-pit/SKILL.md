---
name: bottomless-pit
description: >-
  Retention principle 5 of 6, no dead ends, adapted for useful products: find
  every screen that leaves the user with nowhere to go (empty search results,
  end of a list, error states, blank first-run screens, post-action
  confirmations) and give each one a relevant next step, while keeping a clear
  exit once the user's job is done. Use when designing or reviewing empty
  states, zero-results pages, error screens, success screens, list endings or
  offline states, when a Claude Design canvas needs empty-state or
  after-action artboards, or when someone says "the search shows nothing",
  "what happens after they submit", "users drop off after X", "design the empty
  state", "bottomless pit". For the full six-part review use `retention-audit`.
---

# The Bottomless Pit (the honest version)

Every natural stopping point asks the user a silent question: keep going or
leave? The end of a page, an empty result, an error and a bare "Done" screen
are all stopping points. Most apps are full of them by accident, so they push
people out without meaning to. Infinite feeds remove them entirely, which is
why they are so hard to put down; the designer of infinite scroll, Aza Raskin,
has spoken publicly about regretting that cost.

This skill takes the useful half. Remove the accidental dead ends. Keep the
honest endings.

## What to produce

1. **Dead-end inventory.** Every screen or state with no onward action:
   zero search results, end of a list, empty first-run screens, errors,
   offline, permission denied, success confirmations, expired or removed
   content, signed-out walls.
2. **Next step per dead end.** One relevant onward action for each, chosen
   from what the user was trying to do.
3. **Honest endings.** The points where the user's job is complete, and what a
   good ending looks like there.

## How to work

- Search the code for empty-state components, error boundaries, "no results"
  strings, list footers and success screens. Then trigger each one in the
  running app; many are never seen by the team.
- For each dead end, answer what the user wanted and offer the nearest thing:
  - zero results: loosen one filter for them, show close matches, offer to
    alert them when a match appears;
  - end of a list: nearby or similar items, or a saved-search prompt;
  - error or offline: retry, plus what still works;
  - success: the natural follow-up to what they just did;
  - removed content: similar items that still exist.
- One clear next step, at most a second quiet one. A dead end replaced by a
  menu is still a stop.
- Say what happened in plain words before offering the next step.

## Honest line (this is the adaptation, do not remove it)

- Do not hide the way out. Back, close, sign out, cancel and unsubscribe stay
  where people expect them.
- No autoplay or auto-advance into something the user did not ask for.
- When the user has finished what they came for, tell them it is done and let
  them go. A person who found what they needed and left is a success, and they
  come back because the app respected their time.
- Suggestions must be relevant. Padding an empty result with unrelated items
  to look full is worse than an honest empty state.

## On a Claude Design canvas

Start the canvas with the Artifact tool's Design type and follow that type's own
instructions for mechanics. This skill decides what goes on the artboards:

- **Dead-end wall:** every dead-end state as it looks today, side by side, so
  the number of them is visible.
- **After, per state:** each one redrawn with its next step, placed directly
  beside or under its "before".
- **Good ending:** the completion screen for the main job, showing a clear
  "you are done" and an easy exit.

Draw every state inside the app's real layout and design system, with the real
message text. Empty states are where placeholder copy hides, so write the
final words.

## Marketplace note (Roogo and similar)

The most expensive dead end is a search with no listings in the chosen area or
budget. Offer the closest matches (next district, slightly wider budget) and a
one-tap alert for new matches. After a visit request or a published listing,
show what happens next and when. The honest ending is the best one: a seeker
who found a home, or an owner whose property is taken, should get a clean
close-out, not more listings pushed at them.

## Report format

```
# Bottomless Pit: <app or flow>
Dead-end inventory: screen or state | how to trigger | what the user wanted | proposed next step
Honest endings: where the job is done | what the ending shows
Honest-line check: anything proposed that fails it, removed
Top 3 changes, smallest effort first
```
