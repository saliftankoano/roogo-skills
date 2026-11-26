---
name: paved-path
description: >-
  Retention principle 3 of 6, defaults: choose the next step for the user so
  they never face a blank menu. Makes the core action the first thing seen on
  open, lists every decision the app forces, and gives each one a sensible
  default. Use when designing or reviewing a home screen, filters, search,
  settings, pickers, forms or onboarding choices, when a Claude Design canvas
  needs a first-open screen or a decision map, or when someone says "users do
  not know where to start", "too many options", "what should the default be",
  "the home screen is a menu", "decision fatigue", "paved path". For the full
  six-part review use `retention-audit`.
---

# The Paved Path

People mostly take the option that is already chosen. Leaving the prepared
path costs effort, so few do it, even for decisions that matter far more than
anything in an app. The well-known case is organ donation: countries where
people are donors unless they opt out have far higher consent rates than
countries where people must opt in (Johnson and Goldstein, 2003).

The lesson for a product is to decide for the user wherever a good decision
exists, and to keep the alternative one tap away.

## What to produce

1. **First screen check.** What a user sees on opening the app, and whether it
   is the core action or a menu of options.
2. **Decision inventory.** Every place the app makes the user choose: filters,
   sort order, categories, pickers, toggles, permission prompts, plan choices,
   empty forms.
3. **Default per decision.** The preselected value, why it is right for most
   users, and where it comes from (their last choice, their location, the most
   common choice, a safe choice).
4. **Removals.** Decisions that can be deleted because one option is right
   almost every time.

## How to work

- Open the app cold and screenshot the first screen. If it asks "what do you
  want to do?", the path is not paved.
- Search the code for pickers, selects, radio groups, toggles and filter
  state. Note each one's initial value. An initial value of "none" or "all" is
  usually a missing default.
- Prefer defaults in this order: what this user chose last time, what their
  context implies (city, role, language), what most users choose.
- A default must be easy to change and visibly a choice. Show the selected
  value; do not hide the decision.
- Remember the user's changes. A default that resets every visit is a tax.

## Honest line

A default must be the choice that is good for the user. Preselecting the
option that mainly benefits the business (a paid add-on, marketing consent,
data sharing, a higher price tier) is a dark pattern and is off limits here.
Consent and money are never defaulted to "yes".

## On a Claude Design canvas

Start the canvas with the Artifact tool's Design type and follow that type's own
instructions for mechanics. This skill decides what goes on the artboards:

- **First open, before and after:** the current first screen beside one where
  the core action is already under way (content showing, next step lit).
- **Decision map:** the screens that force choices, with each decision marked
  and its default written beside it. Decisions to delete are struck through.
- **Default in place:** each key picker or filter drawn in its preselected
  state, with the alternative visibly one tap away.

Draw every screen inside the app's real layout and design system, with real
values in the defaults (a real city, a real price range), never "Option 1".

## Marketplace note (Roogo and similar)

Open on listings, not on a category chooser: default to the user's city or
last search, and to the transaction type they used last. In filters, start
from the most common range instead of an empty form. For an owner, default the
listing form from their previous listing (same city, same contact details).
Never default a price, a fee or a contract term on the owner's behalf.

## Report format

```
# Paved Path: <app or flow>
First screen today, and proposed
Decision inventory: where | current initial value | proposed default | source of default
Decisions to delete
Top 3 changes, smallest effort first
```
