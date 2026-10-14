// Capture the Roogo app from the user's own signed-in Chrome, over the DevTools protocol.
// Copy this file next to your project, fill in `steps`, then: node capture.mjs <step> [<step> ...]
// Chrome must run with --remote-debugging-port (CDP_PORT, default 9333). The user signs in; never type credentials.
// Output: CAPTURE_DIR (default ./captures), 1600x825 CSS px at 2x = 3200x1650 PNG.
import { mkdirSync } from "node:fs";
import { chromium } from "playwright";

const OUT = process.env.CAPTURE_DIR ?? "captures";
const PORT = process.env.CDP_PORT ?? "9333";
const START = process.env.START_URL ?? "https://www.roogobf.com/admin/studio";
mkdirSync(OUT, { recursive: true });

const browser = await chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
const ctx = browser.contexts()[0];

// Our own tab, marked by window.name, so the user's tabs are never touched.
let page = null;
for (const p of ctx.pages()) {
  if ((await p.evaluate(() => window.name).catch(() => "")) === "roogo-capture") page = p;
}
if (!page) {
  page = await ctx.newPage();
  await page.goto(START);
  await page.evaluate(() => { window.name = "roogo-capture"; });
}
await page.bringToFront(); // a background tab does not paint: screenshots would time out

const cdp = await ctx.newCDPSession(page);
await cdp.send("Emulation.setDeviceMetricsOverride", { width: 1600, height: 825, deviceScaleFactor: 2, mobile: false });
await page.evaluate(() => window.dispatchEvent(new Event("resize")));
await page.waitForTimeout(1500);

const wait = (ms) => page.waitForTimeout(ms);
const top = () => page.evaluate(() => window.scrollTo({ top: 0, behavior: "instant" }));

// Before every shot: hide dev badges, the signed-in email, and fixed bars covering scrolled content.
const hidePrivate = async () => {
  await page.addStyleTag({ content: "nextjs-portal{display:none!important}" }).catch(() => {});
  await page.evaluate(() => {
    for (const el of document.querySelectorAll("header *, nav *")) {
      if (el.childElementCount === 0 && /@|\+?\d[\d ]{7,}/.test(el.textContent ?? "")) el.style.visibility = "hidden";
    }
    for (const el of document.querySelectorAll("body *")) {
      const s = getComputedStyle(el);
      if (s.position === "fixed" && el.getBoundingClientRect().top < 40 && el.offsetHeight < 120) {
        el.style.visibility = window.scrollY > 60 ? "hidden" : "";
      }
    }
  }).catch(() => {});
};

const shot = async (name) => {
  await hidePrivate();
  await page.mouse.move(1595, 820); // park the cursor so no hover state is captured
  await wait(400);
  await page.screenshot({ path: `${OUT}/${name}.png`, scale: "device", animations: "disabled" });
  console.log("saved", name);
};

const scrollTo = async (locator, offset = -120) => {
  await locator.evaluate((el, off) => {
    window.scrollTo({ top: window.scrollY + el.getBoundingClientRect().top + off, behavior: "instant" });
  }, offset);
  await wait(1200);
};

// One function per script paragraph. Keep each rerunnable on its own.
const steps = {
  async home() {
    await page.goto(START);
    await page.evaluate(() => { window.name = "roogo-capture"; });
    // Reset settings the app keeps in this browser, so the video shows the defaults staff will see.
    // await page.evaluate(() => { for (const k of Object.keys(localStorage)) if (/^roogo-studio-/.test(k)) localStorage.removeItem(k); });
    await wait(3000); await top();
    await shot("s01-home");
  },
  async nouveau() {
    await page.getByRole("button", { name: /Nouveau/ }).first().click();
    await wait(900);
    await shot("s02-nouveau-menu");
  },
};

for (const name of process.argv.slice(2)) {
  if (!steps[name]) throw new Error(`unknown step ${name}; known: ${Object.keys(steps).join(", ")}`);
  await steps[name]();
}
process.exit(0); // leave the user's Chrome and tabs open
