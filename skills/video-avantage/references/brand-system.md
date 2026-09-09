# Brand system

Brand fonts, logos, and music come from the team's own asset library. They are
not bundled here, and this package grants no rights to them.

## Palette

| Role | Value |
| --- | --- |
| Primary orange, Terracotta | `#C96A2E` |
| Clay brown, secondary background | `#5A2D0C` |
| Sand, accent text | `#F4E8D7` |

## Type and marks

- Font: Nunito, in ExtraBold, Bold, and SemiBold.
- Logo: the transparent Roogo mark, used full and centred on title and end
  cards, and as the corner badge everywhere else.
- All on-screen text is drawn with PIL. An image model must never render text.

## Copy rules

- No em dashes and no emoji in spoken or on-screen copy.
- Contact details stay visible on the end card.
- Final files carry real French titles, for example `Roogo - <hook>.mp4`,
  because platforms use the filename as the default upload title.

## Canvas

Vertical, 1080x1920, 30 frames per second unless the requester specifies
otherwise. Keep important content clear of the platform's own interface at the
top and bottom of the frame.
