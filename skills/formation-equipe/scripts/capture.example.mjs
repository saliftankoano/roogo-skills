// Capture the Roogo app over the DevTools protocol, or a public page on a phone.
// Copy this file next to your project, fill in `steps`, then: node capture.mjs <step> [<step> ...]
// Signed-in app (default): the user's own Chrome with --remote-debugging-port (CDP_PORT, default 9333).
//   The user signs in; never type credentials. 1600x825 CSS px at 2x = 3200x1650 PNG.
// Public pages (PUBLIC=1): a fresh signed-out browser, never the user's Chrome, at phone size
//   390x844 CSS px at 3x = 1170x2532 PNG, in French.
// Output: CAPTURE_DIR (default ./captures). Anything a step creates goes in created.jsonl there.
import { appendFileSync, mkdirSync } from "node:fs";
import { chromium } from "playwright";

const OUT = process.env.CAPTURE_DIR ?? "captures";
const PORT = process.env.CDP_PORT ?? "9333";
const PUBLIC = process.env.PUBLIC === "1";
const START = process.env.START_URL ?? (PUBLIC ? "https://www.roogobf.com/" : "https://www.roogobf.com/admin/studio");
const VIEW = PUBLIC ? { width: 390, height: 844 } : { width: 1600, height: 825 };
mkdirSync(OUT, { recursive: true });

let browser, page;
if (PUBLIC) {
  // A new, empty context: signed out, no cookies, nothing from the owner's sessions.
  browser = await chromium.launch();
  const ctx = await browser.newContext({
    viewport: VIEW, deviceScaleFactor: 3, isMobile: true, hasTouch: true,
    locale: "fr-FR", timezoneId: "Africa/Ouagadougou",
  });
  page = await ctx.newPage();
  await page.goto(START);
} else {
  browser = await chromium.connectOverCDP(`http://127.0.0.1:${PORT}`);
  const ctx = browser.contexts()[0];
  // Our own tab, marked by window.name, so the user's tabs are never touched.
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
  await cdp.send("Emulation.setDeviceMetricsOverride", { ...VIEW, deviceScaleFactor: 2, mobile: false });
  await page.evaluate(() => window.dispatchEvent(new Event("resize")));
}
await page.waitForTimeout(1500);

// Every test row, upload or message a step creates: what it is, where it lives, how to find it.
// The delivery report lists them all so the owner can decide what to delete.
const created = (what, where, id) => {
  appendFileSync(`${OUT}/created.jsonl`, JSON.stringify({ what, where, id, at: new Date().toISOString() }) + "\n");
  console.log("created", what, "in", where, id ?? "");
};

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
  await page.mouse.move(VIEW.width - 5, VIEW.height - 5); // park the cursor so no hover state is captured
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
  // Public form on a phone: fill it up to the last step, film, then submit once only.
  // async formulaire() {
  //   await page.goto("https://www.roogobf.com/carrieres");
  //   ... fill with test data, shot("s03-formulaire") ...
  //   await page.getByRole("button", { name: /Envoyer/ }).click();
  //   created("candidature de test", "table candidatures (production)", "nom: Test Formation");
  //   created("CV de test", "stockage des fichiers (production)", "test-formation.pdf");
  // },
};

for (const name of process.argv.slice(2)) {
  if (!steps[name]) throw new Error(`unknown step ${name}; known: ${Object.keys(steps).join(", ")}`);
  await steps[name]();
}
if (PUBLIC) await browser.close();
process.exit(0); // leave the user's Chrome and tabs open
