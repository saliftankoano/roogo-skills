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

## Frame

- Set the viewport with CDP `Emulation.setDeviceMetricsOverride`: 1600x825 CSS
  pixels, `deviceScaleFactor: 2`. Captures are 3200x1650 PNG: sharp enough to
  zoom to 2x in a 1920x1080 video.
- Move the mouse to a corner before each shot so no hover state is captured,
  unless the hover is the point.
- Scroll the element into view with an offset so it sits in the upper half.

## Privacy and hygiene, before every shot

- Hide the signed-in email and any personal phone number or name in the
  navigation bar.
- Hide development badges.
- When scrolled, hide fixed bars that cover the content.
- Pick test, public or staff-owned listings. Never show a customer's personal
  data, payment details or private messages.
- Reset per-browser settings the app stores locally (volumes, toggles) before
  filming, so the video shows the defaults staff will see.

## Steps

Write one function per script paragraph, each saving numbered captures
(`s01-…`, `s02-…`). Keep the capture script rerunnable step by step, so one
broken step does not mean re-filming everything. Capture the loading and empty
states when the script mentions them.

Anything the agent creates while filming (test projects, uploads, generated
items) is listed at delivery so the user can decide whether to delete it.
