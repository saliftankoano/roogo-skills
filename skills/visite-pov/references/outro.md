# Outro

`scripts/outro-hyperframes/` is a HyperFrames 0.8.81 composition, 5.5 seconds at
1080x1920, filled with variables. `build_pov.py` crossfades the last photo into
it and holds its final frame until the audio ends.

## Layout

The listing photo sits darkened behind three groups:

1. the Roogo logo badge;
2. the property type in small spaced capitals, the location, the price as the
   only large white element, and one detail line;
3. one contact block: "Appelez ou écrivez-nous sur WhatsApp" above the number
   in an orange pill.

roogobf.com is a small footer. With no photo, the background is flat orange and
the number pill turns dark.

An earlier layout with more lines, tag pills and a white download button was
rejected for having too much text and too much white.

## Render

1. Copy `scripts/outro-hyperframes/` to a working folder. Never put listing
   photos in the package itself.
2. Put the Roogo logo in the copy as `assets/roogo-logo.png`, and one listing
   photo (faces already blurred) in `assets/`.
3. Write the variables, like `example-vars.json`.
4. From the copy, run
   `npx --yes hyperframes@0.8.81 render . --variables-file vars.json -o outro.mp4`.
5. Check a frame near 5.3 seconds.

## Variables

| Variable | Example | Notes |
| --- | --- | --- |
| `headline` | PARCELLE À VENDRE | property type |
| `location` | Tanghin, Ouagadougou | |
| `price` | 40 000 000 | digits only; long amounts shrink automatically |
| `currency` | FCFA | |
| `note` | 336 m², lotissement 1985 viabilisé | one line; empty hides it |
| `contact_label` | Appelez ou écrivez-nous sur WhatsApp | |
| `phone` | +226 67 00 61 16 | the Roogo call and WhatsApp line |
| `bg` | assets/listing.jpg | empty gives the orange fallback |
| `cta` | (empty) | optional white button; leave empty on property videos |
| `footer` | roogobf.com | |
