# Capturing the Roogo app

## Browser

- Use a separate Chrome (Chrome for Testing works) with its own profile and
  remote debugging on a local port, for example:
  `"<chrome>" --user-data-dir=<profile dir> --remote-debugging-port=9333`.
- The user signs in to roogobf.com in that window themselves. Never type a
  password or code for them.
- Connect with Playwright `chromium.connectOverCDP("http://127.0.0.1:9333")`.
  Work in your own tab, marked with `window.name`, so the user's tabs are never
  touched. Reuse it across runs.
- Call `page.bringToFront()` before capturing. A background tab does not paint
  and screenshots time out.
- The template checks before every shot that the page is not a sign-in page
  and stops with an error if it is. A session that expired mid-run otherwise
  films the sign-in page without complaint.

## Frame

- Set the viewport with CDP `Emulation.setDeviceMetricsOverride`: 1600x825 CSS
  pixels, `deviceScaleFactor: 2`. Captures are 3200x1650 PNG: sharp enough to
  zoom to 2x in a 1920x1080 video.
- Move the mouse to a corner before each shot so no hover state is captured,
  unless the hover is the point.
- Scroll the element into view with an offset so it sits in the upper half.

## Privacy and hygiene, before every shot

- Hide the signed-in email and any personal phone number or name in the
  navigation bar. Roogo's own public numbers (`ROOGO_NUMBERS` in the template)
  stay visible: hiding them blurs whole scripts and footers that are meant to
  be read.
- Hide development badges.
- When scrolled, hide fixed bars that cover the content.
- Pick test, public or staff-owned listings. Never show a customer's personal
  data, payment details or private messages.
- Re-read the status of every example record right before filming, not only
  when writing the script: staff keep working in production. For a step that
  changes state (publish, approve), prefer a test listing, and cancel instead
  of confirming.
- Reset per-browser settings the app stores locally (volumes, toggles) before
  filming, so the video shows the defaults staff will see.

## Public pages on a phone

For pages anyone sees without signing in (careers, a listing, a public form),
film what a candidate or visitor sees on an Android phone:

- Run the template with `PUBLIC=1`: a fresh, signed-out browser context, never
  the owner's signed-in Chrome, so no session, staff menu or saved data shows.
- 390x844 CSS pixels at scale 3 (captures 1170x2532), French locale, touch on.
- Build a 1080x1920 video with `capture_width` 1170 in the plan. Keep zoom at
  1.15 or less: the phone site has 16 px side margins, and a closer zoom cuts
  text at the edges. Zoom further only on a single button.
- Fill a form up to its last step, film every step, then submit once. Each
  extra submission leaves more test data behind.

## Steps

Write one function per script paragraph, each saving numbered captures
(`s01-…`, `s02-…`). Keep the capture script rerunnable step by step, so one
broken step does not mean re-filming everything. Capture the loading and empty
states when the script mentions them.

## Test data created while filming

Record every row, upload, message or generated item a step creates with
`created(what, where, id)` in the template; it lands in `created.jsonl` next to
the captures. The delivery report lists each one with where it lives (table,
storage bucket, inbox) and how to find it, so the owner can decide what to
delete. The agent never deletes production data on its own.
