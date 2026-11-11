# process.json format

All coordinates are page px on the 1920×1080 canvas. Text is plain (HTML in panel strings is allowed but avoid it).

| Key | Type | Meaning |
|---|---|---|
| `title` | string | Browser tab title on the overview |
| `kicker` | string | Small caps text top-left, before `heading` |
| `heading` | string | Name of the map (header and first breadcrumb item) |
| `lang` | string | `lang` attribute, e.g. `id`, `en` |
| `footnote` | string | Right side of the footer (e.g. "data = simulation") |
| `legend` | `{node, check, case, dash}` | Legend words; leave one empty to hide it |
| `labels` | `{show, menu, watch, shot, map, close, theme}` | Panel headings, ▶ button text, screenshot caption prefix, chapter-bar name of the overview, modal close button, tooltip of the light/dark button (default "Theme") |
| `sections` | `{ "<name>": "<stepId>" }` | Breadcrumb link target per section |
| `phases` | `[[key, LABEL, color]]` | Case panel rows in order. `key` is the step field holding the text. `color` is one of `red`, `amber`, `purple-l`, `green`, `muted` |
| `lanes` | `[{id, name: [lines], y, h}]` | Swimlanes, top to bottom |
| `nodes` | `[{id, x, y, lbl: [lines], sub: [lines], w?, h?, kind?}]` | `kind`: `diamond` or `hold`; default is a box |
| `edges` | `[{from, to, d, dash?, lbl?: [text, x, y]}]` | `d` = SVG path; lit when both ends are in a chapter's focus |
| `cases` | `[{id, at: [[x, y], ...]}]` | Exception pills, centre points |
| `steps` | see below | Chapters, in reading order |

Step (chapter):

| Key | Meaning |
|---|---|
| `id` | Unique; equal to a case id to light that pill |
| `title` | Panel title and breadcrumb |
| `code` | Optional panel kicker; default `SECTION · id` |
| `section`, `group` | Breadcrumb levels and chapter-bar gaps |
| `role` | Line under the title (who does it) |
| `focus` | Node ids to highlight; `null` = overview (nothing dimmed); `[]` = everything dimmed |
| `allCases` | `true` lights every case pill |
| `cases` | Extra case ids to light |
| `groups` | `[{k, v}]` heading + text blocks (overview, section intros) |
| `show`, `menu` | Bullet list + one "where in the app" line |
| `<phase key>` | Text per phase row (for example `m`, `t`, `s`, `h`) |

## Layout limits

- Canvas 1920×1080. The map uses x 200–1430; the chapter panel starts at x 1460. The lane label column is x 20–190. The header ends at y ≈ 100 and the footer starts at y ≈ 1010.
- Lanes stack without gaps. A lane with two rows of steps needs ±290 px; a single row needs ±160–200 px.
- A box is 200×92 by default, so keep centres on one row at least 230 px apart.
- Labels: at most 2 lines of ±18 characters. Sub-lines: at most 26 characters.
- A diamond is 170×100. A `hold` box is dashed red; give it an explicit `w`/`h`.
- Edges are orthogonal (`M x y H x V y`) and run from box edge to box edge. An edge label sits 8–12 px off its line, never on a case pill.
- A case pill is 56×26. It sits beside its step, never on a box or an arrow.
- Numbered badges appear on nodes whose id is a number. Give main steps numbers and other nodes words (`chk`, `hold`).

## Optional media

A `media.js` file next to `index.html` sets `window.MEDIA`:

```js
window.MEDIA = {
  "<chapterId>": { "t": 73.4, "shot": "shots/<chapterId>.jpg", "caption": "..." },
  "_video": { "src": "video.mp4" }
};
```

The live page then shows a screenshot (click to zoom) and a ▶ button that plays `_video` from `t`. Without the file, the page shows no media.

## Modes

- Default URL: live page, scaled to the window, with clickable map, breadcrumb, chapter bar, previous/next, Back, ←/→ and Esc.
- `?export&step=<id>`: plain 1920×1080 chapter card without UI chrome, which `scripts/shoot.mjs` captures.
