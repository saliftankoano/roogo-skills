# House rules learned in the iterations

0. **Match every photo to the format.** Choose photos separately for each
   version. The 16:9 website version uses only landscape photos (ratio 1.3 or
   wider) that fill the frame; the 9:16 social version uses only portrait photos
   (ratio 0.85 or narrower) that fill the frame, and landscape photos only where
   the layout box is itself landscape (for example the picture frame beside the
   step cards). A portrait photo on a blurred landscape frame, or a landscape
   photo on a blurred portrait frame, breaks the immersion; generated clips are made natively for each format (a 9:16 still and clip
   for the vertical version, a 16:9 one for the horizontal), so nothing needs blur bars. If a format lacks enough good photos of the right
   shape, say so and ask rather than filling it with the wrong ones.

1. **Real assets first.** Real photos beat generated ones everywhere except
   people and objects that do not exist. Generated people: still image, then
   image-to-video. A profile shot of a rider with the camera tracking alongside
   works well.
2. **Fast cuts.** On photo scenes show 4 to 5 photos at 1.5 to 2 seconds each
   with a 0.18 s crossfade and a gentle alternating zoom made with animation
   transforms (not ffmpeg `zoompan`, which shakes on stills).
3. **Captions.** White text with a thick black outline, the active word in
   orange, 3 to 4 words per line (3 vertical), centered, never on the bottom
   edge. Live text timed to word timestamps. **None on the outro.**
4. **Outro.** Elements enter one at a time, about 0.3 s apart: logo, headline,
   availability line, App Store badge, Google Play badge, website button,
   WhatsApp number. While the number is spoken, each pair swells and turns
   orange as it is said, then returns to normal before the next pair. Draw the
   badges yourself; do not use the stores' official artwork without permission.
5. **Watermark.** The round brand badge top-right from the first frame until
   the outro.
6. **Music.** One instrumental you have the rights to, at volume 0.14, fading
   out over the last 1.6 seconds. Never louder than the voice.
7. **Vertical version.** A separate layout, not a crop: portrait photos and the
   natively vertical generated clips fill the frame; cards stack in one column; captions sit below the picture area.
8. **Cards.** Give each its own entrance on the spoken word. Keep captions off
   the cards.
9. **Verification.** Render stills at every scene midpoint and in both outros;
   check the levels of the quiet sections; check that cuts, captions and cards
   line up with the voice.
