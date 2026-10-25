# Portal Access Pattern

Verified by read-only inspection of local Odoo 17, 18, and 19 Community and
Enterprise source; the same structure is present in all six cells.

## Building blocks

- `portal.mixin` (`addons/portal/models/portal_mixin.py`) gives a model
  `access_url`, `access_token`, and `_get_access_action`. A model exposed in
  the portal must inherit it; a custom portal page over a model without the
  mixin has no token-based sharing.
- `CustomerPortal._document_check_access(model_name, document_id,
  access_token=None)` in `addons/portal/controllers/portal.py` is the access
  helper. It checks ORM read access for the logged-in user and falls back to a
  matching access token. Use it (or the portal page helpers that call it) for
  every document route; do not reimplement the check.
- `_prepare_home_portal_values` and `_prepare_portal_layout_values` extend the
  portal home counters and layout; override them to add a document type.
- `_get_page_view_values` builds the standard document page context,
  including breadcrumbs and history.

## Rules

1. Routes that serve a document use `auth="public"` only when access-token
   sharing is required; otherwise `auth="user"`. Either way the access helper
   runs before any read.
2. Filtering a list by `partner_id == request.env.user.partner_id` is not an
   access check; combine it with record rules on the model.
3. After the helper proves access, elevated reads use a `_sudo` recordset and
   never return raw elevated records to the template beyond what the page
   needs.
4. Attachments served from a portal page go through the same helper with the
   `ir.attachment` model.
5. Cross-company portal users exist; test the matrix in the output template.
6. Public routes (`auth="public"`) run as the public user; check
   `request.env.user._is_public()` when behavior differs for anonymous
   visitors.

## Not verified here

Runtime behavior, record rules of the specific model, and Enterprise-only
portal extensions. Cite the target source line when designing.
