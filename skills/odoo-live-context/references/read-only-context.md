# Read-only live context

Use the context envelope from the Phase 3 interface contract: `instance_id`,
`company_id` when company-owned data is involved, `profile`, `environment`,
`odoo_version`, and `operation_class: read`.

The only tools owned by this skill are:

- `odoo_list_models` for bounded model discovery;
- `odoo_get_model_metadata` for named-model field and capability metadata;
- `odoo_check_access` for the exact model and read operation.

Before each call, confirm the tool appears in the reconciled manifest and the
selected profile. The most restrictive result from plugin policy, MCP policy,
Odoo ACLs, and record rules wins. Metadata can prove what is exposed to the
current identity; it cannot prove unrestricted access, authorize elevation, or
replace repository evidence about edition and deployment.

Retain only the metadata needed for the stated purpose. Audit evidence should
contain tool name, context identifiers, result class, correlation identifier,
and freshness—not credentials, raw arguments, raw results, documents, private
identifiers, or client data.
