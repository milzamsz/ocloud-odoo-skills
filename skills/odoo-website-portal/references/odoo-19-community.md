# Odoo 19.0 Community website and portal evidence

Verified by read-only inspection of the local Odoo 19.0 Community source tree.

- `portal.mixin` exists at `addons/portal/models/portal_mixin.py` with
  `access_url`, `access_token`, and `_get_access_action`.
- `CustomerPortal._document_check_access` exists in
  `addons/portal/controllers/portal.py`; portal document routes must use it.
- `website.page` exists at `addons/website/models/website_page.py`;
  `website=True` routes are used throughout `addons/website/controllers/main.py`.
- The `Interaction` layer (`addons/web/static/src/public/interaction.js`, `addons/website/static/src/interactions/`) exists alongside the legacy public widget registry; prefer interactions for new code. Hoot and QUnit both ship.
- Community tree; `web_enterprise` is absent.
- `website_sale` is present; eCommerce policy remains out of scope.

Runtime behavior, installed addons, and record rules are not proven by source
presence. Cite target lines when designing.
