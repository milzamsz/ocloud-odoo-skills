# Bounded live reads

A valid request states exact model, domain, fields, company scope, finite limit,
deterministic order, purpose, sensitivity, redaction, freshness, and completion
evidence. Empty field lists, unbounded limits, unexplained cross-company scope,
and secret-bearing fields are blockers.

Choose the least-data allowed tool:

- `odoo_count`: count only;
- `odoo_read_group`: bounded aggregate;
- `odoo_search`: matching identifiers;
- `odoo_read`: named fields for known identifiers;
- `odoo_search_read`: bounded search plus named fields;
- `odoo_name_search`: bounded label lookup;
- `odoo_name_get`: labels for known identifiers.

The selected profile, MCP policy, ACLs, record rules, allowed companies, and
field restrictions all apply; the most restrictive result wins. Do not retry a
denied read with broader scope or elevated access.

Keep audit evidence metadata-only: context identifiers, tool, operation class,
query/result class, correlation identifier, freshness, duration, truncation,
redaction, and completion. Exclude credentials, raw arguments, raw results,
documents, private identifiers, and client data.
