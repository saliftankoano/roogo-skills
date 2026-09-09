# Third-party asset provenance and licensing

Read this reference before sourcing, downloading, editing, or redistributing icons,
photography, footage, music, or sound effects. Apply it to source files and to assets
supplied by the user when their redistribution rights are not already documented.

## Source ledger

Create one asset-manifest entry per downloaded or supplied third-party asset. Record:

- a stable asset ID and local untouched-source path;
- the exact public item URL, not only a search or collection page;
- collection, author, uploader, or source library when shown;
- the license stated on that item page and the retrieval date;
- commercial-use, attribution, modification, and redistribution requirements;
- every derived working path and a short description of the modifications;
- the scenes, compositions, or masters that use the asset.

Do not infer a license from the website, collection, file extension, or neighboring
items. The individual asset page controls. Exclude an asset when its rights are
unclear or incompatible with the intended commercial release. Retain required
notices in the project and delivery package.

Keep the original download byte-for-byte unchanged. Recolor, simplify, optimize,
crop, or convert only a clearly named derived copy. Do not hotlink production media.
Never put API keys, authenticated download URLs, cookies, or private account data in
the manifest.

## SVG Repo

[SVG Repo](https://www.svgrepo.com/) is an approved discovery source, not a blanket
license. Inspect and record the license on each icon's own page. For hotel-service
concepts, begin with the user's preferred
[Hotel Services 8 collection](https://www.svgrepo.com/collection/hotel-services-8/)
when its icons are semantically correct and visually coherent with the film. Move to
another coherent set when the collection lacks the required meaning; do not force a
near-match merely to preserve collection purity.

For every chosen SVG:

1. Download the original SVG and record its item URL and license.
2. Inspect the file for embedded scripts, external references, raster payloads,
   unexpected metadata, masks, and unsupported paint behavior.
3. Create a derived production SVG for palette, stroke, or optimization changes.
4. Test the derived icon at its actual rendered size, on light and dark brand fields
   when both occur.
5. Hide its label during review. If the icon's object or action is ambiguous, replace
   it instead of explaining it with more copy.

Do not use third-party icons as the Roogo logo or imply that a generic icon is an
official product mark. Brand marks require the approved source asset and their own
trademark handling.

## Photography, footage, music, and effects

For photography and footage, record model, property, location, and editorial-use
limitations when known. Do not present editorial imagery as a live product capture.
When a real photo is expected inside the product UI, re-capture that UI after upload.

For music and effects, preserve the original file and document every trim, loop,
fade, loudness adjustment, and derived mix asset. Prefer a user-approved licensed
library before searching elsewhere. A technically usable track still fails when its
emotional direction contradicts the story.

## Release gate

Before release, verify that every non-original asset in the master resolves to a
complete manifest entry, every required attribution or notice is present, and every
distributed source file is permitted by its license. Missing provenance is a release
blocker, not post-production paperwork.
