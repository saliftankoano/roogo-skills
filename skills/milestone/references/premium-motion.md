# Premium path: generated motion

Image-to-video makes the graphic's own decorative elements, confetti, sparkles,
light rays, actually move, while the typography and logo stay locked and sharp.

This path is deliberately **not automated end to end**. Each generated clip
needs a quality check before spending on the next, and whether to chain a
second clip is itself a cost decision. Run the steps manually, checking frames
between each.

## 1. Confirm the spend

Check the account balance before starting. A 15 second clip has run in the low
single dollars in practice, so a 30 second two-clip build is a real cost.
Confirm it is acceptable for this specific milestone before generating the
second clip, not only the first.

## 2. Generate the first clip

Upload the composited still and generate a clip of at most 15 seconds at the
target 9:16 aspect ratio, high quality, with a prompt built from this template:

> Static celebratory graphic comes alive: gold and orange confetti pieces
> continue falling and gently swirling through the air, tiny sparkle particles
> twinkle and drift, soft light rays subtly pulse in the background. The camera
> stays completely still, locked off, no zoom, no pan. All text, numbers, and
> the logo remain perfectly sharp, static, and unchanged, never warping or
> morphing. Only the confetti, sparkles, and background light are in motion.
> Elegant, premium, subtle motion graphics feel, no camera movement, no
> distortion of typography.

Adapt the named decorative elements to whatever the actual graphic contains.
Naming elements the graphic does not have invites the model to invent them.

## 3. Check frames before doing anything else

Extract four or five frames spread across the clip and look specifically for
typography and logo warping. This is the main failure mode. Catching it on the
first clip saves the cost of a second.

```bash
for t in 0.5 4 8 12 14.5; do
  ffmpeg -y -ss "$t" -i anim_clip1.mp4 -frames:v 1 "check_${t}.png" -loglevel error
done
```

## 4. Chain beyond 15 seconds

Extract the exact last frame of the clip just generated, upload it, and
generate the next clip **from that frame** with the same prompt, changing
"comes alive" to a "continues" framing since the motion is already established.
This keeps the motion continuous instead of visibly resetting at the cut.

```bash
ffmpeg -y -sseof -0.1 -i anim_clip1.mp4 -frames:v 1 lastframe.png -loglevel error
```

Check the new clip's frames too, before proceeding.

## 5. Join with a crossfade

Normalise both clips to 1080x1920 at 30 frames per second, then join them with
a short crossfade, offset at the first clip's duration minus the crossfade
duration:

```bash
ffmpeg -y -i c1.mp4 -i c2.mp4 -filter_complex \
  "[0:v][1:v]xfade=transition=fade:duration=0.4:offset=14.6[vout]" \
  -map "[vout]" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p video_silent.mp4
```

Spot-check a frame at the join itself. The seam is invisible when both clips
came from the same continuous-motion chain, but verify it on every build rather
than assuming.

## 6. Report the spend

Check the balance after each clip and state the total spend to the requester
directly in the final summary, not only in a log.
