# Live integration (Phase 3)

How skills relate to live Odoo reads and the five named mutation capabilities,
and which repository owns what. Source of truth:
[../PHASE-3-INTERFACE-CONTRACT.md](../PHASE-3-INTERFACE-CONTRACT.md),
[../PHASE-3-RISK-CLASSIFICATION.md](../PHASE-3-RISK-CLASSIFICATION.md),
[../CROSS-REPO-MUTATION-BASELINE.md](../CROSS-REPO-MUTATION-BASELINE.md),
[../../skills/odoo-live-mutation/SKILL.md](../../skills/odoo-live-mutation/SKILL.md),
[../../scripts/validate_mutation_capabilities.py](../../scripts/validate_mutation_capabilities.py).

## Who owns what

| Repository | Owns |
|---|---|
| `ocloud-odoo-skills` (this one) | Procedure only: when to read, how to bound a read, how to build an approval packet, how to verify a receipt. No credentials, no client, no writes. |
| `hermes-plugin-odoo` | Selected instance, company, and profile context; block-only guards; metadata-only audit; HMAC-SHA256 signing of the approval-bound envelope. It can block a call but never grants access. |
| `odoo-rust-mcp-agent` | The compiled shared contract (`config/capabilities/support.yaml`, receipt schema `receipt.v1.json`), with per-cell support decisions and evidence. |
| `odoo-rust-mcp` | The runtime: typed tools, controlled mode, idempotency, execution, the final receipt, and the `oc_mcp_mutation` Odoo helper add-on. |

The effective policy is the most restrictive of the MCP policy, the plugin
guard, Odoo ACLs and record rules, and the skill's procedural gate.

## Reads

- **`odoo-live-context`:** confirms instance, version, edition, company, model metadata, and effective access.
- **`odoo-live-read`:** reads business records with an exact model, domain, fields, company, limit, order, purpose, and redaction plan.
- **Read tools:** `odoo_search`, `odoo_search_read`, `odoo_read`, `odoo_count`, `odoo_read_group`, `odoo_name_search`, `odoo_name_get`, `odoo_default_get`, `odoo_list_models`, `odoo_get_model_metadata`, `odoo_check_access`. A tool being present in the manifest does not authorize its use. The profile must include it.
- **Production:** read-only, always.

## Mutations

Generic `create`, `write`, `unlink`, and `execute` tools are never
agent-selectable. Only these named capabilities exist:

| Capability | Operation class |
|---|---|
| `create_crm_lead_draft.v1` | `draft_write` |
| `create_quotation_draft.v1` | `draft_write` |
| `prepare_vendor_bill_draft.v1` | `draft_write` |
| `update_allowed_draft_fields.v1` | `draft_write` |
| `import_bank_transaction_draft.v1` | `accounting_suspense_write`: Odoo posts a suspense move, which must stay unreconciled with a named correction owner |

Flow: `odoo-live-mutation` builds one packet from
`assets/mutation-packet.md`. A human approves the payload digest. The plugin
signs the envelope and calls only `odoo_execute_capability`. The runtime
rechecks everything, claims the idempotency key, writes, verifies, and
returns a normalized receipt. One packet authorizes one invocation.

Support is decided per capability and per cell, where a cell is version ×
edition × protocol × auth mode × environment, in the shared contract. Today
the contract has cells for Odoo 17, 18, 19, and 20, Community and Enterprise.
Development and staging can be approved; production is denied.

## Optimistic locking for draft updates

`update_allowed_draft_fields.v1` runs inside the `oc_mcp_mutation` helper. It
locks the row and checks company, draft state, `write_date`, and the field
allowlist in one transaction. Odoo's APIs show `write_date` only to whole
seconds. Helper 1.1.0 and later therefore expose the computed field
`oc_mcp_write_version`, which carries microseconds. Read it in the preview,
pass it as `expected_write_date`, and use the returned `write_version` for any
follow-up update. Details: [../../skills/odoo-live-mutation/references/update-allowed-draft-fields-v1.md](../../skills/odoo-live-mutation/references/update-allowed-draft-fields-v1.md).

## Checking the contract from this repository

```bash
make capability-check CONTRACT=/path/to/odoo-rust-mcp-agent/config/capabilities/support.yaml
```

This requires the baseline cells for Odoo 17 to 19. It accepts the Odoo 20
Community and Enterprise pair only together. It also checks that every
capability has a reference here, an outcome case, closed input and output
schemas, and a support decision for every declared cell.
