---
name: piggy-bank
description: >-
  Retention principle 6 of 6, stored value: make an app more valuable to each
  person the more they use it, so that coming back continues something instead
  of starting over. Lists what a user would lose by uninstalling today, what to
  record with their knowledge, and what they can build up (saved items,
  preferences, history, progress, reputation). Use when designing or reviewing
  favourites, saved searches, profiles, history, personalisation,
  recommendations, progress or reputation features, when a Claude Design canvas
  needs a profile, saved or "your activity" surface, or when someone says
  "people use it once and never return", "why would they come back", "what
  should we track", "personalise the app", "add favourites", "piggy bank". For
  the full six-part review use `retention-audit`.
---

# The Piggy Bank

Each use of a good product leaves something of the user behind: their taste,
their saved things, their connections, their history. The product gets better
for them, and leaving means giving that up. A recommendation engine that has
learned what someone likes is the clearest case. Starting again on a fresh
account feels like a loss.

The test is one question: if this person uninstalled the app today, what would
they lose? If the answer is nothing, there is no reason to return.

## What to produce

1. **Loss check.** What a user with one week, one month and six months of use
   would lose by leaving today. Write "nothing" where that is the truth.
2. **Signals.** What users already tell the app through their actions
   (searches, filters, views, saves, contacts, time spent) and which of those
   signals are recorded, which are thrown away.
3. **Deposits.** The things a user can build up and see: saved items and
   searches, preferences the app remembers, a history, progress toward
   something, a reputation or track record.
4. **Payback.** How each deposit visibly improves the next visit. A deposit
   that changes nothing for the user is only data collection.

## How to work

- Read the data model and the analytics events. List what is stored per user
  and what is used to change their experience. The gap between the two is the
  opportunity.
- Find state that resets between sessions (filters, location, sort, drafts).
  Remembering it is the cheapest deposit there is.
- Make the deposits visible: a place where the user sees what they have built
  and that it is theirs.
- Show the payback quickly. The first save should already change something on
  the next screen or the next visit.
- Prefer simple rules before any learned model: "more like the ones you
  saved" from three saves is enough to start.

## Honest line

- Record only what improves the user's experience, tell them plainly, and
  follow the privacy rules that apply where they live.
- The value belongs to the user. Let them see it, export or delete it, and
  leave. Stored value is a reason to stay; it must not be a hostage.
- No guilt mechanics: no threats about losing a streak, no punishing absence.

## On a Claude Design canvas

Start the canvas with the Artifact tool's Design type and follow that type's own
instructions for mechanics. This skill decides what goes on the artboards:

- **Day 1 and day 30:** the same key screen for a new user and for a user with
  a month of history, side by side. The difference between them is the stored
  value; if they look the same, there is none.
- **Your space:** the surface where the user sees what they have built (saved
  items, searches, history, progress).
- **Deposit moment:** the small interaction where a deposit is made (save,
  follow, set a preference), and the immediate payback after it.

Draw every screen inside the app's real layout and design system, with
realistic personal data. Show only what that user should see about themselves.

## Marketplace note (Roogo and similar)

Seeker deposits: saved listings, saved searches with alerts, a remembered
city, budget and property type, a visit history. Owner deposits: their
listings and photos, enquiry history, response record, a verified profile that
makes the next listing faster and more trusted. Because housing is an
occasional need, stored value matters most across the gap between needs: the
next search, or the next vacancy, should start from where the last one ended.

## Report format

```
# Piggy Bank: <app or flow>
Loss check: after 1 week | 1 month | 6 months
Signals: action | recorded today? | used today?
Deposits: what | where the user sees it | payback on the next visit
Honest-line check: data recorded, user told, can be deleted
Top 3 changes, smallest effort first
```
