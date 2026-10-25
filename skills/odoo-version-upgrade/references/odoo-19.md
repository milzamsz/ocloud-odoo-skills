# Odoo 19.0 Migration Reference

Verified by read-only inspection of local Odoo 19.0 Community and Enterprise
source trees. Only material differences from the Odoo 18 baseline that affect
an 18 → 19 port are listed; everything else needs target-source confirmation.

- Public website JavaScript gains the `Interaction` layer
  (`addons/web/static/src/public/interaction.js`,
  `addons/website/static/src/interactions/`). The legacy
  `public_widget.js` still ships in 19 but is gone in 20, so a port should
  move public widgets to interactions rather than extend the legacy registry.
- Browser unit tests use Hoot (`addons/web/static/lib/hoot`); QUnit still ships
  in 19 but is removed in 20. Do not add new QUnit suites during a port.
- `<list>` views and `list,form` action modes are unchanged from 18.
- `from odoo.tests import Form` remains the supported import; the
  `odoo.tests.common` path still warns.
- External RPC: verify the target's JSON-2 endpoint and API-key policy before
  porting integrations that use legacy JSON-RPC sessions.

No schema, accounting, or stock migration coverage is claimed here. OpenUpgrade
19.0 coverage must be checked per module on the exact branch.
