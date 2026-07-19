# Views and Assets

## Odoo 18 CE evidence

- Load security before views that reference groups, and load actions before
  menus that reference them. Manifest `data` order is execution order.
- Odoo 18 list architectures use `<list>` and window actions use `list` in
  `view_mode`. Do not paste Odoo 17 `<tree>` examples into an 18 addon.
- Give each view, action, menu, and durable data record a stable external ID.
  Prefer a narrow inherited view over copying a standard view.
- Anchor inherited changes to stable semantic nodes such as a field or named
  container. Avoid selectors based only on layout classes or translated labels.
- Visibility modifiers help the UI but do not enforce authorization. Use
  `groups` to limit view elements and enforce the same boundary through ACLs,
  record rules, and server-side checks.
- Put frontend files in the manifest `assets` mapping under the exact target
  bundle. Do not add an asset bundle when the change has no frontend code.
- Validate XML by installing the module on a clean disposable database; parsing
  alone does not prove referenced models, fields, groups, actions, or XML IDs.

Verified official Odoo 18 CE source paths:

- `odoo/addons/base/views/*.xml` — `<list>` view architecture, actions, menus,
  groups, and inheritance examples.
- `odoo/addons/test_new_api/__manifest__.py` — ordered `data` and
  `web.assets_tests` declarations.
- `odoo/addons/base/models/ir_ui_view.py` — view loading, inheritance, and
  validation behavior.

Odoo 18 fixture application: `evals/fixtures/minimal-addon-18/` contains an
OCloud-authored list/form/action/menu chain with security loaded first.
