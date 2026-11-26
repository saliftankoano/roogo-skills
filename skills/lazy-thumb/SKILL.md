---
name: lazy-thumb
description: >-
  Retention principle 2 of 6, the easy first action: find an app's core action,
  count the steps to reach it, cut them toward one, put the control big and
  within thumb reach, and lower the bar for what counts as done. Use when
  designing or reviewing a home screen, a primary button, a form, a posting or
  booking flow, or onboarding, when a Claude Design canvas needs a before/after
  of a core flow, or when someone says "too many steps", "people start but do
  not finish", "simplify this flow", "where should the main button go", "make
  it one tap", "lazy thumb". For the full six-part review use `retention-audit`.
---

# The Lazy Thumb

Motivation rises and falls through the day and nobody controls it. Effort is
the part a designer controls. If the core action is easy enough, people do it
even on a low-motivation day; if it takes a menu, a scroll and some typing,
only the highly motivated finish.

Background: BJ Fogg's behaviour model (behaviour needs motivation, ability and
a prompt at the same moment).

## What to produce

1. **Core action.** The one thing a user does that delivers the app's value,
   named per audience (a seeker and an owner have different core actions).
2. **Step count.** Every tap, scroll, field and decision from opening the app
   to completing that action, counted on the real build, not from memory.
3. **Cut list.** For each step: remove, merge, defer until after the action,
   or fill automatically. State the target count.
4. **Control placement.** Where the control sits, how large it is, and whether
   one thumb reaches it.
5. **Definition of done.** The smallest version of the action that still counts
   as a success, so a partial effort is rewarded instead of discarded.

## How to work

- Walk the flow on a device or in the running app and number each step. Read
  the screen code to catch steps hidden behind conditions (sign-in walls,
  permission prompts, required fields).
- Ask of every field: can the app know this already, can it be asked later,
  can a photo, a tap or a default replace typing?
- Put the core control in the lower part of the screen. Many people hold the
  phone in one hand, so the top corners cost a grip change.
- Make it the most visible thing on the screen. If three buttons have the same
  weight, none of them is the core action.
- Lower the bar honestly: save a draft, accept a first photo and finish later,
  count a short session. Do not count something that gives the user nothing.

## Honest line

Remove friction that serves nobody. Keep friction that protects the user:
confirming a payment, a price, a deletion or anything that cannot be undone
stays a deliberate step.

## On a Claude Design canvas

Start the canvas with the Artifact tool's Design type and follow that type's own
instructions for mechanics. This skill decides what goes on the artboards:

- **Flow strip, before:** every current screen of the core action in order,
  each numbered, with the total count as the strip's title.
- **Flow strip, after:** the shortened flow directly under it, same scale, so
  the difference in length is visible at a glance.
- **Thumb reach:** the key screen with the easy-reach area for one-handed use
  shaded, showing the core control inside it.
- **Smallest done:** the success state for the minimum version of the action.

Draw every screen inside the app's real layout (tab bar, headers) and design
system. A simplified flow that ignores the real navigation is not a result.

## Marketplace note (Roogo and similar)

Typical core actions: for a seeker, contacting about a listing or requesting a
visit; for an owner, publishing a listing. Publishing is usually the longest
flow, so the largest gains are there: photos first, the rest filled from the
photos or asked after the listing exists as a draft. On slow connections every
extra screen is also a loading wait, so step count matters more, not less.

## Report format

```
# Lazy Thumb: <app or flow>
Core action (per audience)
Steps today: numbered list, total N
Steps proposed: numbered list, total M
Control placement and size
Smallest version that counts as done
Top 3 changes, smallest effort first
```
