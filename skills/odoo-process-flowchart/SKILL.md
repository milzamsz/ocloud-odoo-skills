---
name: odoo-process-flowchart
description: Use this skill when producing an interactive swimlane map of an Odoo business process (roles as lanes, numbered steps with Odoo menu paths, automatic checks, exception cases, one panel per chapter) as a self-contained HTML page plus one 1920x1080 PNG per chapter for tutorial videos, slides, or user training. Do not use it for logical data-model diagrams, BPMN execution, dashboards, or for designing the process itself.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. The bundled scripts require Node.js 20+; checks and PNG export also require Playwright with Google Chrome or Chromium.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: read-only
  odoo:
    versions: []
    editions: []
  hermes:
    tags: [odoo, process, flowchart, swimlane, training, documentation]
---

# Odoo Process Flowchart

## Purpose

Turn an agreed Odoo process (normal flow plus exception cases) into a map that people can step through: a page that opens from disk and highlights one chapter at a time, and a PNG per chapter for videos or slides. The page documents a process; it does not decide it.

## Use when

- a functional design, UAT script, or training needs a visual of who does what in Odoo and where in the menu;
- a tutorial video needs a "you are here" card before each chapter;
- positive and negative (exception) scenarios must be shown on one map, each exception at the step where it appears;
- an existing map of this kind must be updated (new step, new case, renamed menu).

## Do not use when

- the process is not yet agreed: use `odoo-solution-design` or the matching `odoo-functional-*` skill first;
- the request is a model/relation diagram (`odoo-data-model-diagram`), a KPI dashboard (`odoo-dynamic-dashboard`, `odoo-reporting`), or executable BPMN;
- a one-off static picture is enough and nobody will step through chapters.

## Required inputs

- Lanes: roles or systems, top to bottom (for example Requester, Manager, Odoo automatic, external system).
- Steps in time order, each with its role and, for user steps, the Odoo menu path or button.
- Automatic checks and held states (what blocks a record, where it waits).
- Exception cases: id, the step where the problem shows up, and Problem / Sign in Odoo / Fix / Result.
- Chapters to step through, their order, and the language of the labels.

Unknown roles, branches, or menu paths are questions for the user, not guesses. When menu paths must match a live instance, confirm them through `odoo-live-context` and `odoo-live-read` (menus and actions only); never read business records for a map.

## Workflow

1. Collect the inputs above; write open questions down before drawing.
2. Write `process.json` next to the deliverable. Format: [references/schema.md](references/schema.md). Start from `assets/example-purchase-approval.json`.
3. Build: `node scripts/build.mjs process.json <outDir>`. It copies `assets/flowchart-template.html` and writes `process.js`. It rejects unknown node ids, duplicate chapters, and nodes outside every lane.
4. Check and export: `node scripts/shoot.mjs <outDir> --check --export`, run where `playwright` resolves.
   - `--check` fails on overlapping steps or case pills, shapes under the panel, labels wider than their box, and panel text cut off in any chapter.
   - Move coordinates or shorten text until it reports 0 problems.
   - `--export` writes both themes: `png/light/<chapter>.png` and `png/dark/<chapter>.png` (`--theme=light|dark|both`, default both). Light is the one to use on light slides and videos.
5. Open the light overview PNG, one chapter per section, and a few dark ones. Confirm that arrows run the right way and that each highlight sits on the step its chapter describes.
6. Deliver the folder (`index.html`, `process.js`, `png/light/`, `png/dark/`, `markers.json`). The page has a light/dark button; it follows the OS until the button is used and then remembers the choice (`?theme=light|dark` forces one). Optionally add `media.js` for a screenshot and a video start time per chapter.

## Decision rules

- Layout is explicit: node centres, lane bands, and edge paths are written by hand. The renderer does no auto-layout. Layout limits are in [references/schema.md](references/schema.md).
- More than about 15 steps or 4 lanes on one 1920×1080 canvas becomes unreadable: split the process into several maps, linked by chapter text.
- A case pill sits where the problem becomes visible to the user, not where it was caused.
- Steps that change records name the user's menu path; automatic steps name the resulting document or state, not technical method names.
- Exception text follows the same four phases in every case so viewers learn the pattern.

## Safety rules

- The skill writes files only in the requested output folder; it never writes to Odoo.
- Do not put credentials, customer names, prices, or other client data in labels or examples meant for sharing; use role names and generic document references.
- Publishing the page outside the local machine (for example a password-protected static site) needs the user's explicit choice of host, account, and access control: see [references/publishing.md](references/publishing.md).

## Required output

- `process.json`, built `index.html` + `process.js`, `png/light/<chapter>.png` and `png/dark/<chapter>.png` for every chapter, and `markers.json`.
- A short note listing the chapters, open questions about the process, and anything shown as an assumption.

## Verification

- `build.mjs` exits 0.
- `shoot.mjs --check` reports 0 problems.
- You looked at the overview PNG and at least one chapter PNG per section, and checked the highlight against the chapter text.

## References to load

- [references/schema.md](references/schema.md): always, before writing `process.json`.
- [references/publishing.md](references/publishing.md): only when the user asks to share the page beyond local files.

## Failure and escalation

- Playwright missing: install it in the working directory (`npm i -D playwright`) or hand over the built page without PNGs and say so.
- `--check` cannot be satisfied without dropping content: split the map, or move detail into chapter panels.
- Process facts conflict between people or sources: stop and ask; do not draw both versions on one map.
