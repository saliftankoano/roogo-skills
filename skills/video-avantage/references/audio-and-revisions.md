# Audio mixing, cost, and revisions

## Mixing

- **When mixing several delayed voice tracks, always use a longest duration
  mix, never a first-input duration.** A first-input duration truncates the
  whole mix to whichever input is listed first, with no error. This produced a
  real bug: a 43 second video whose audio silently cut off at 5.6 seconds.
  Verify with a volume detection pass and cross-check the transcribed word
  count against what the script expects before trusting a render.
- Background music comes from a rights-cleared instrumental library unless the
  requester supplies a specific track. Mix it low under the full runtime, with
  a fade of about one to 1.5 seconds in and out.
- **Run the final loudness pass on the fully mixed output**, narration and
  music together, not on the narration alone. Layering music in after an
  already-normalised narration track measurably drops the combined level.
- Relative requests such as "music up a little" are implemented as an explicit,
  reproducible gain change and rechecked on the encoded file.

## Cost

Generated character clips are the expensive line item, roughly a dollar each
for a few seconds at high quality. Narration and dialogue lines are cheap by
comparison. Check the account balance before starting and state the actual
spend to the requester in the final summary.

## Revisions

- **When only audio, text, or captions change, reuse the existing footage.**
  Extract the segments from the prior render by timecode rather than
  regenerating them. On the reference build, revision rounds two through seven
  triggered zero new character generations; only a genuinely new shot, a silent
  reaction clip added to fix lip sync, needed fresh generation.
- If a revision changes no segment duration, the existing audio mix and caption
  track can often be reused directly, or rebuilt only in part.
- Make feedback operational before acting on it: what is wrong, where and when
  it occurs, the desired visible behaviour, what must stay unchanged, and the
  evidence that will be used to accept the fix.
