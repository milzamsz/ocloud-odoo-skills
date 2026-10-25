# Website Patterns

Verified by read-only inspection of local Odoo 17, 18, 19, and 20 Community and
Enterprise source.

## Pages, templates, routes

- A `website.page` record (`addons/website/models/website_page.py`) wraps a
  `ir.ui.view` and carries URL, publish state, menu link, and website scope.
  Use it for editable content pages.
- A controller route with `website=True` renders a QWeb template with the
  website layout and is the right choice for data-driven pages. Public routes
  need an explicit `auth="public"`; the `website` module's own controllers
  show the pattern (`addons/website/controllers/main.py`).
- Multi-website: every page, menu, and template-scoped record may be
  website-specific; check `website_id` handling before assuming one site.
- Language: public pages are translated per website language; template
  text must be translatable and URLs language-prefixed.

## Template inheritance

- Inherit the target version's template by its XML ID and anchor on a stable
  element or named container. Editor-generated `oe_structure` content is not a
  stable anchor.
- Keep snippet options and editor-specific attributes out of code-rendered
  templates unless the page must be editable.

## JavaScript layer

- Odoo 17 and 18: public JavaScript registers legacy public widgets
  (`addons/web/static/src/legacy/js/public/public_widget.js`).
- Odoo 19: the `Interaction` layer exists
  (`addons/web/static/src/public/interaction.js`,
  `addons/website/static/src/interactions/`) alongside the legacy registry.
  New code should use interactions.
- Odoo 20 removes the legacy registry; use `Interaction` classes only.
- Browser tests: Hoot ships from 18; QUnit still ships in 17 to 19.

## Assets

Declare frontend files in the manifest `assets` mapping under the exact
public bundle used by the target version (`web.assets_frontend` for website
pages). Do not add backend bundles for public code.
