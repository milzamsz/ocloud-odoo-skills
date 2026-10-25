# Odoo 18.0 Enterprise website and portal evidence

Verified by read-only inspection of the local Odoo 18.0 Enterprise source tree.

- `portal.mixin` exists at `addons/portal/models/portal_mixin.py` with
  `access_url`, `access_token`, and `_get_access_action`.
- `CustomerPortal._document_check_access` exists in
  `addons/portal/controllers/portal.py`; portal document routes must use it.
- `website.page` exists at `addons/website/models/website_page.py`;
  `website=True` routes are used throughout `addons/website/controllers/main.py`.
- Public JavaScript uses the legacy public widget registry; no `Interaction` layer exists in this tree. Hoot and QUnit both ship.
- Enterprise tree verified by the presence of `web_enterprise`; no Enterprise-specific portal or website behavior is claimed beyond Community.
- `website_sale` is present; eCommerce policy remains out of scope.

Runtime behavior, installed addons, and record rules are not proven by source
presence. Cite target lines when designing.
