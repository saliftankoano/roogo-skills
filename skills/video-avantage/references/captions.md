# Captions

Captions are hand-rolled for this format. A hosted animated-caption operation
reproduces the look faithfully, but its position is pinned to the bottom edge
with no exposed parameter to move it, confirmed by passing a dozen plausible
parameter names plus a deliberately bogus key: none errored and none changed
the render. When the video's own graphics live near the bottom, price labels,
comparison cards, an end-card contact bar, bottom-pinned captions collide with
them and become unreadable.

## Build

1. **Word timestamps** come from transcribing the fully mixed narration track.
   Upload the extracted audio, not the video; the transcription operation
   accepts audio attachments only.
2. **Chunk the words** into short display groups, resetting every four words or
   at sentence-ending punctuation.
3. **Render each state** as a PNG with PIL: the accumulated line with the
   current word highlighted in an orange rounded box, white fill with a black
   stroke, in Nunito ExtraBold.
4. **Position per segment.** Assign each chunk a centre-Y based on what is
   already on screen at that moment. A segment showing a comparison card gets
   captions just below the card; a segment with bottom price labels gets
   captions in the upper middle; a segment with dense centred text gets
   captions in whatever clear space remains. Toward the centre, never the
   bottom edge, never over a graphic.
5. **Composite as one flattened overlay track.** Render every caption state as
   a short looped clip, concatenate them into a single transparent video track,
   then perform exactly one overlay of that track onto the base video.

   Never chain many individually timed overlay filters. One attempt chained
   about a hundred timed overlays in a single filter graph and ran for over
   three hours before being killed, because every overlay stage reprocesses the
   whole video even when its enable window is mostly false. The flattened track
   produces the same result in seconds.
6. **Use frame-exact accounting when concatenating**, not a per-clip duration in
   seconds. Seconds-based durations round independently and accumulate drift;
   one build landed the caption track three seconds out of sync with a 46
   second video after about 114 clips. Compute each clip's frame count as the
   difference between successive **rounded cumulative** target frames. See
   [scripts/caption_timing.py](../scripts/caption_timing.py).

## Check

Confirm the flattened track's total frame count equals the base video's, and
review captions on the encoded file with playback controls visible, not only in
a source preview. Correct the brand name and any misheard proper nouns against
the approved script before rendering.
