# Brand system

Every value below is fixed configuration for this ad format. Brand fonts,
logos, and music are supplied from the team's own asset library; they are not
bundled in this package and their licenses are not granted by it.

## Palette

| Role | Value |
| --- | --- |
| Primary orange, Terracotta Ember | `#C96A2E` |
| Navy, text and contrast | `#1F3A52` |
| Background | White `#FFFFFF` |
| Panels | Light gray `#F8F8F8` |
| Accent, Sand Dune | `#F4E8D7` |

## Type and marks

- Font: Urbanist variable, weights selected with
  `set_variation_by_name("Bold")`, `"SemiBold"`, or `"Regular"`.
- Logo: the transparent Roogo mark. On an orange field, always place it on a
  white rounded chip with a radius near 52 to 56 pixels, otherwise the orange
  wordmark disappears into the background.
- All on-screen text is drawn with PIL. An image model must never render text.

## Copy rules

- No em dashes and no emoji in ad copy.
- The phone number is always visible and large.
- The site link belongs in every social caption, on its own line near the phone
  number.
- Final files carry real French titles, for example `Roogo - <hook>.mp4`,
  because platforms use the filename as the default upload title.

## Flat field, the house style for static frames

Cards and posters use a solid terracotta field with the logo on a white chip, a
giant qualifier headline, short cream sublines, a framed photo card, a navy
budget pill, one call-to-action line, and the phone number as the largest
element on the frame. A white background with gray panels is not the house
style; use it only when a brief explicitly demands it.

## Imagery direction

Photographs are generated modest, clean, and realistic for the stated budget:
cement or banco walls, a swept red-earth courtyard, neither luxurious nor
run-down. No text, no signage, no imported suburban look, and no people who do
not belong to the local context. For an owner-facing frame, a smiling local
owner holding keys in front of the house is the established composition.
