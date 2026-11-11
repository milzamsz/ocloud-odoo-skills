#!/usr/bin/env node
// shoot.mjs <siteDir> [--check] [--export]
//   --check   every step at 1920x1080: overlapping nodes/pills, pills or labels outside the map, panel text cut off
//   --export  PNG per step (no UI chrome) in <siteDir>/png + markers.json (highlight box per step, page px)
// Needs Playwright (resolved from the cwd, then the skill dir) and Google Chrome or Chromium.
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const site = path.resolve(process.argv[2] || ".");
const want = new Set(process.argv.slice(3));
if (!want.size) want.add("--check");
let chromium;
for (const base of [process.cwd(), import.meta.dirname]) {
  try { ({ chromium } = createRequire(path.join(base, "noop.js"))("playwright")); break; } catch {}
}
if (!chromium) { console.error("Playwright not found: run `npm i -D playwright` in the working dir (no browser download needed with system Chrome)."); process.exit(2); }

const browser = await chromium.launch({ channel: process.env.PW_CHANNEL || "chrome" }).catch(() => chromium.launch());
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
const url = pathToFileURL(path.join(site, "index.html")).href;
await page.goto(`${url}?export`);
const ids = await page.evaluate(() => window.STEP_IDS);
const problems = [];
const markers = {};
if (want.has("--export")) fs.mkdirSync(path.join(site, "png"), { recursive: true });

if (want.has("--check")) {  // map geometry is the same for every step
  problems.push(...await page.evaluate(() => {
    const out = [], box = (e) => e.getBoundingClientRect();
    const hit = (a, b, m = 4) => a.left < b.right + m && b.left < a.right + m && a.top < b.bottom + m && b.top < a.bottom + m;
    const shapes = [...document.querySelectorAll(".node rect, .node polygon")].map((e) => ({ id: "node " + e.parentNode.textContent.slice(0, 24), r: box(e) }));
    const pills = [...document.querySelectorAll(".case rect")].map((e) => ({ id: "case " + e.parentNode.textContent, r: box(e) }));
    const all = [...shapes, ...pills];
    for (let i = 0; i < all.length; i++) for (let j = i + 1; j < all.length; j++)
      if (hit(all[i].r, all[j].r)) out.push(`overlap: ${all[i].id} × ${all[j].id}`);
    const map = box(document.querySelector("aside"));
    for (const x of all) if (x.r.right > map.left - 10) out.push(`under the panel: ${x.id}`);
    for (const t of document.querySelectorAll(".node text")) {  // text wider than its shape
      const s = box(t.parentNode.querySelector("rect, polygon"));
      if (box(t).width > s.width - 8 && !t.classList.contains("numt")) out.push(`text too wide: "${t.textContent}"`);
    }
    return out;
  }));
}
for (const id of ids) {
  await page.goto(`${url}?export&step=${encodeURIComponent(id)}`);
  await page.evaluate(() => document.fonts.ready);
  if (want.has("--check") && await page.evaluate(() => { const p = document.getElementById("panel"); return p.scrollHeight > p.clientHeight; }))
    problems.push(`panel text cut off: step ${id}`);
  if (want.has("--export")) {
    await page.screenshot({ path: path.join(site, "png", `${id}.png`) });
    markers[id] = { png: `png/${id}.png`, box: await page.evaluate(() => window.markerBox()) };
  }
}
if (want.has("--export")) fs.writeFileSync(path.join(site, "markers.json"), JSON.stringify(markers, null, 1));
await browser.close();
for (const p of problems) console.log("✗ " + p);
console.log(`${ids.length} steps${want.has("--export") ? ", PNGs in " + path.join(site, "png") : ""}; ${problems.length} problem(s)`);
process.exit(problems.length ? 1 : 0);
