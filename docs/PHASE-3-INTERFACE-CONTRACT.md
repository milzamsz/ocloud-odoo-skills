# Phase 3 Interface Contract

This contract defines the minimum evidence exchanged between the procedural
skill, Hermes plugin, and typed MCP execution layer.

## Context envelope

| Field | Required | Rule |
|---|---|---|
| `instance_id` | yes | Selected from the generated instance registry. |
| `company_id` | yes for company-owned data | Must be visible to the selected profile. |
| `profile` | yes | Names the generated tool policy profile. |
| `environment` | yes | `development`, `staging`, or `production`. |
| `odoo_version` | yes | Confirmed from configured or live evidence. |
| `odoo_edition` | yes | `community` or `enterprise`; never inferred from installed source alone. |
| `protocol` / `auth_mode` | yes | Exact target-cell values (`jsonrpc`/username-password or `json2`/API key). |
| `target_identity` / `registry_revision` | yes | Bind database/target and generated contract revision without exposing credentials. |
| `operation_class` | yes | `read`, `draft_write`, `accounting_suspense_write`, `state_transition`, `administrative`, or `destructive`. |

The plugin may block a call but never grants access. MCP policy and Odoo ACLs
remain authoritative.

## Read request

A read request must state:

- exact model, domain, fields, company scope, limit, order, and purpose;
- expected sensitivity and required redaction;
- tool name from the reconciled MCP manifest;
- freshness and completion evidence.

Empty or broad fields, unbounded limits, unexplained cross-company context, or
secret-bearing fields are blockers.

## Mutation request

A mutation uses a versioned capability, never caller-selected model, method, or
arbitrary fields. The packet contains:

- `capability_id`;
- trusted instance and company;
- actor and authorized reviewer;
- canonical business payload;
- idempotency key and payload hash;
- preview result and approval identifier;
- approval expiry and single-use state;
- operation class;
- exact support cell, capability/input/output/receipt schema hashes, required modules, and model fingerprint;
- verification and rollback or compensation.

Execution must reject expiry, replay, reviewer mismatch, company mismatch,
payload mutation, audit failure, or unavailable returned-record verification.
The plugin signs this packet with HMAC-SHA256 and invokes only
`odoo_execute_capability`. The MCP runtime independently reloads the normalized
registry, validates the exact target and input schema, claims durable
idempotency state, performs the bounded mapping/write/verification, and owns
the final receipt. Controlled mode hides and rejects generic mutation tools.

`update_allowed_draft_fields.v1` invokes the installed, fingerprinted
`oc_mcp_mutation` helper. The helper locks the target row and checks company,
draft state, expected `write_date`, and the closed field allowlist before its ORM
write. A read-then-write sequence remains unsupported.

## Result and audit evidence

All branches validate against the shared normalized receipt schema and report
target cell, status, capability, operation class, actor/approval references,
idempotency key, payload digest, correlation/audit identifiers, record reference,
verification, and compensation. Audit logs use a strict metadata allowlist. They exclude
raw arguments, raw results, credentials, documents, private identifiers, and
client data.

Production exposes read tools only. A support decision is per capability and
cell; no aggregate version/edition claim authorizes mutation.
