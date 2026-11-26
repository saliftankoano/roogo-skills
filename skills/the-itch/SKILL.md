---
name: the-itch
description: >-
  Retention principle 1 of 6, the trigger: tie an app to the feeling that makes
  people open it, so the feeling does the reminding instead of a generic push.
  Names the feeling the app answers, finds when users feel it, and rewrites
  notifications, badges and in-app copy to speak to that feeling. Use when
  designing or reviewing notifications, push copy, re-engagement messages,
  onboarding promises or empty home screens, when a Claude Design canvas needs
  lock-screen or notification artboards, or when someone says "people download
  it and never open it again", "nobody opens the app", "our notifications get
  ignored", "write the push notifications", "the itch". For the full six-part
  review use `retention-audit`.
---

# The Itch

People open an app for one of two reasons. An outside trigger tells them to
(a notification, a badge, a message), or an inside trigger pushes them (a
feeling: bored, curious, worried about missing something). Outside triggers
start the habit. The habit holds only once the app is tied to a feeling, because
then the feeling does the reminding and no notification is needed.

The usual failure is that the feeling is still there but the app is not linked
to it. A message such as "We miss you" speaks for the company. A message such as
"Someone liked you" speaks to the person.

Background: internal and external triggers come from Nir Eyal's *Hooked*.

## What to produce

1. **Feeling statement.** One sentence per audience: "When I feel ___, I open
   this app to ___." If an app serves several audiences, write one each. Do not
   blend them.
2. **Trigger moments.** When and where that feeling shows up in a real day or
   week, taken from evidence (support messages, analytics by hour, interviews),
   not guessed. Mark every guess as a guess.
3. **Message inventory.** Every notification, badge, email, SMS and
   re-engagement line that exists today, each tagged: speaks to the feeling,
   speaks for the company, or pure noise.
4. **Rewrites.** A replacement for each message that is not tagged "speaks to
   the feeling", plus the moment it should be sent.

## How to work

- Read the real strings first: notification templates, push payloads, email
  templates, onboarding copy. Quote the current text next to each rewrite.
- A good message names something that happened for this person: a reply, a new
  match, a price change on something they looked at. If nothing happened, send
  nothing. Silence is better than noise, because every empty ping teaches the
  person to ignore the next one.
- Send at the moment the feeling occurs, not at the moment that suits the team.
- Keep the first screen after the tap consistent with the message. A
  notification about one item that opens a generic home screen breaks the link
  being built.

## Honest line

Speak to a feeling the app really answers. Do not manufacture anxiety, invent
activity ("5 people are looking at this" when they are not), or send a
notification whose content is empty. These work once and cost trust after.

## On a Claude Design canvas

Start the canvas with the Artifact tool's Design type and follow that type's own
instructions for mechanics. This skill decides what goes on the artboards:

- **Feeling board:** one artboard per audience with the feeling statement and
  the moments in the day it occurs, drawn as a simple day strip.
- **Lock screen, before and after:** the current notification as it really
  reads, beside the rewrite, on a phone lock screen at real size.
- **Landing screen:** the screen each rewritten notification opens, showing
  that it delivers what the message promised.

Draw every screen inside the app's real layout and design system. Use real
strings and real data shapes, never placeholder text.

## Marketplace note (Roogo and similar)

A property marketplace has at least two feelings, and they are not the same.
A seeker feels "I might miss the right place". An owner feels "is anyone
interested in my property?". Good triggers are events: a new listing that
matches a saved search, a price change, a visit request, a first view on a new
listing. Housing is an occasional need, so judge success by return visits
during an active search, not by daily opens.

## Report format

```
# The Itch: <app or flow>
Feeling statement(s)
Trigger moments (evidence or "guess")
Message inventory: current text | tag | rewrite | when to send
Top 3 changes, smallest effort first
```
