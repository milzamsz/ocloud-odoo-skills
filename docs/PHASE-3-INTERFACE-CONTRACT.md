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
| `operation_class` | yes | `read`, `draft_write`, `posting`, or `destructive`. |

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
- verification and rollback or compensation.

Execution must reject expiry, replay, reviewer mismatch, company mismatch,
payload mutation, audit failure, or unavailable returned-record verification.

## Result and audit evidence

Results report status, capability/tool name, instance/company/profile,
operation class, correlation identifier, duration/result class, verification,
and rollback status. Audit logs use a strict metadata allowlist. They exclude
raw arguments, raw results, credentials, documents, private identifiers, and
client data.
