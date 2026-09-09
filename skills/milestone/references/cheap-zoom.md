# Cheap path: Ken Burns zoom

Pure ffmpeg, effectively free, any duration. This is the right default when the
requester has not asked for anything fancier, or when several milestone posts
need to go out quickly.

**Anti-shake rule:** upscale roughly six times before the zoom. A zoom applied
directly to a 1080 pixel source jitters, because the rounding is visible.

```bash
ffmpeg -y -loop 1 -i composite_still.png -t "$DURATION" \
  -vf "scale=6480:11520,zoompan=z='min(zoom+0.0009,1.1)':\
x='(iw-iw/zoom)/2':y='(ih-ih/zoom)/2':d=$((DURATION * 30)):s=1080x1920:fps=30,setsar=1" \
  -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p video_silent.mp4
```

A zoom increment near `0.0009` per frame with a ceiling of `1.1` reads as
subtle and premium. Do not push it faster; a fast zoom reads as a cheap
slideshow effect and undoes the point of the treatment.
