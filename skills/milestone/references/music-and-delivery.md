# Music, mix, verification, and delivery

## Music

If the requester supplies a specific track with an instruction to cut a
specific offset, modify that file **in place** as asked, but back it up first.
It is a shared asset used across projects, and only the explicit instruction to
trim the file itself justifies mutating a shared source.

Otherwise pick from a rights-cleared instrumental library, leave the source
file untouched, and apply any trim at render time only.

## Mix

Fade in around 0.8 seconds, fade out around 1.5 to 1.8 seconds before the end,
then a final loudness pass on the finished mix:
`loudnorm=I=-14:TP=-1.5:LRA=11`.

## Verify before archiving

Spot-check frames across the **entire** timeline, not just the first one: the
start, every crossfade seam, and the very end. A single frame checked at the
beginning would have missed a transient motion-blur artefact that appeared mid
clip on a real premium build. It resolved by the next frame, but it had to be
actually looked at to know that.

Confirm the output is exactly 1080x1920 and that the video and audio durations
agree.

## Delivery and naming

Archive to the team's milestone folder with a real French title, for example
`Roogo - <hook>.mp4`.

When revising an existing milestone video, keep the previous version alongside
with a descriptive suffix, for example a "simple zoom" marker on the cheap
version, rather than silently overwriting it. The cheap version is often still
wanted elsewhere after a premium one ships.

Log the build, the technique, and any real generation spend, and state the
spend to the requester directly as well.
