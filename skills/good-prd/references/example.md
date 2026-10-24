# Example: one atomic PRD from a multi-ask request

The requester asked, in one message, for: optional fields to be labelled, the
required star to be more visible, video uploads removed, a bigger description
box, guided description questions, and a staff review of descriptions. That is
**six PRDs**, not one. Below is the first, showing the expected depth. Names
are generic.

---

```markdown
---
type: prd
status: draft-awaiting-founder
recorded: "2026-10-24"
owner: Founder
tags: [product, listing-form, prd]
---

# PRD: optional fields say « (facultatif) » in the listing form

**Summary:** every field that can be left empty in the listing form says so in
its label, so owners and staff never wonder whether they must fill it.

Source: Founder, 2026-10-24, after a staff member thought the virtual tour link
had become mandatory. One of six atomic PRDs from that request.

## Problem

Owners and staff cannot tell which fields they may skip, so they stall on
optional ones. The virtual tour link is optional in validation (an empty value
always passes, `forms/listingSchema.ts`), but nothing on screen says so.

**Before:** optional fields look exactly like required ones; only one field in
step 1 says « (optionnel) ».
**After:** each optional field label ends with « (facultatif) » in a lighter
weight, on mobile and web, in both languages.

## Goals and non-goals

**Goals:** a person filling the form knows, field by field, what can be skipped.

**Non-goals:**
- Changing which fields are required.
- The required-field star (PRD « Champs obligatoires bien visibles »).
- Removing the video field (PRD « Retrait de la vidéo des annonces »).

## Users and their needs

- **Owners:** finish fast, skip what they don't have.
- **Staff posting for owners:** know the tour link can wait.

## Requirements

| ID | Requirement | Priority |
| --- | --- | --- |
| 1.1 | Every optional field in the mobile form shows « (facultatif) ». | Must |
| 1.2 | Same on the web form and the staff edit form. | Must |
| 1.3 | The optional list comes from the validation rules, so a field labelled optional can never block a step. | Must |
| 1.4 | Translated: « (optional) » in English. | Must |
| 1.5 | The mark is lighter than the label. | Should |

## Constraints

No em dash mid-sentence, no emoji. Mobile and web ship together.

## Dependencies and owners

Founder approves wording; engineering builds both apps; staff check the list.

## Success metrics

- **« Is this required? » questions to the team:** from at least one a week
  to zero within 30 days of release (source: team chat).
- **Guardrail:** no field marked optional ever blocks a step (source: form
  error logs).

## Open questions

1. « Facultatif » or « optionnel »? Recommendation: « facultatif » everywhere.

## Related PRDs

Champs obligatoires bien visibles · Retrait de la vidéo des annonces · Champ
description plus grand · Questions guidées pour la description · Relecture des
descriptions par l'équipe
```
