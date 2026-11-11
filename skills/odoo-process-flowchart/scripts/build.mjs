#!/usr/bin/env node
// build.mjs <process.json> <outDir>: template/index.html + process.js (+ media.js and assets you put in outDir yourself)
import fs from "node:fs";
import path from "node:path";

const [src, out] = process.argv.slice(2);
if (!src || !out) { console.error("usage: node build.mjs <process.json> <outDir>"); process.exit(2); }
const P = JSON.parse(fs.readFileSync(src, "utf8"));

// fail early on data that would render wrong (structural; layout overlaps are checked by shoot.mjs --check)
const err = [];
const ids = new Set(P.nodes.map((n) => n.id));
for (const k of ["title", "heading", "labels", "lanes", "nodes", "edges", "steps"]) if (!P[k]) err.push(`missing "${k}"`);
for (const e of P.edges || []) for (const end of [e.from, e.to]) if (!ids.has(end)) err.push(`edge ${e.from}->${e.to}: unknown node ${end}`);
for (const s of P.steps || []) for (const f of s.focus || []) if (!ids.has(f)) err.push(`step ${s.id}: unknown focus node ${f}`);
const stepIds = (P.steps || []).map((s) => s.id);
if (new Set(stepIds).size !== stepIds.length) err.push("duplicate step ids");
for (const [sec, to] of Object.entries(P.sections || {})) if (!stepIds.includes(to)) err.push(`section ${sec}: unknown step ${to}`);
for (const n of P.nodes || []) if (!P.lanes.some((l) => n.y > l.y && n.y < l.y + l.h)) err.push(`node ${n.id}: centre outside every lane`);
if (err.length) { console.error(err.join("\n")); process.exit(1); }

fs.mkdirSync(out, { recursive: true });
fs.copyFileSync(path.join(import.meta.dirname, "../assets/flowchart-template.html"), path.join(out, "index.html"));
fs.writeFileSync(path.join(out, "process.js"), `window.PROCESS = ${JSON.stringify(P, null, 1)};\n`);
console.log(`built ${out}: ${P.steps.length} steps, ${P.nodes.length} nodes, ${(P.cases || []).length} cases`);
