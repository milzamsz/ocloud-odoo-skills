# Phase 3 Risk Classification

The effective policy is the most restrictive result from generated MCP policy,
the plugin guard, Odoo ACLs/record rules, and this procedural gate.

| Class | Examples | Development | Staging | Production |
|---|---|---|---|---|
| `read` | search, read, count, read-group, model metadata, access check | allow by profile | allow by profile | allow by read-only profile |
| `draft_write` | versioned draft-record capability | deny unless capability-approved | deny unless capability-approved | deny |
| `accounting_suspense_write` | bank transaction import that posts an unreconciled suspense move | deny unless capability and accounting review approve | deny unless capability and accounting review approve | deny |
| `state_transition` | confirm/post/reconcile/workflow actions with ledger or stock effect | deny | deny | deny |
| `destructive` | delete, cleanup, restore, broad SQL, irreversible workflow | deny | deny | deny |

## Read tools

The supported read candidates from the reconciled MCP contract are:

- `odoo_search`, `odoo_search_read`, `odoo_read`, `odoo_count`;
- `odoo_read_group`, `odoo_name_search`, `odoo_name_get`;
- `odoo_default_get`, `odoo_list_models`, `odoo_get_model_metadata`;
- `odoo_check_access`.

Presence in the manifest does not authorize use. The selected profile must
include the tool and Odoo access controls still apply. Procedurally, model
metadata and access checks belong to `odoo-live-context`; business-record
reads belong to `odoo-live-read`.

## Write tools

Generic `odoo_create`, `odoo_update`, `odoo_delete`, `odoo_execute`,
`odoo_workflow_action`, copy, batch, and cleanup primitives are not
agent-selectable write interfaces. Expose a closed named capability instead.

The controlled set is `create_crm_lead_draft.v1`,
`create_quotation_draft.v1`, `prepare_vendor_bill_draft.v1`,
`update_allowed_draft_fields.v1`, and `import_bank_transaction_draft.v1`.
The first four are `draft_write`. Bank import is
`accounting_suspense_write`: Odoo posts the suspense move immediately and the
capability must verify it remains unreconciled with a named correction owner.
Every exact target cell remains blocked until its runtime evidence and reviews pass.

## Escalation

Accounting posting, stock finalization, payments, reconciliation, production
configuration, and destructive operations require a later capability-specific
design and independent human approval. Phase 3 does not imply those operations
are available.
