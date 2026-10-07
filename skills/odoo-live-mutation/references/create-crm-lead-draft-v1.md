# `create_crm_lead_draft.v1` contract

Load this reference only after the shared contract approves the exact target
cell for `create_crm_lead_draft.v1`. The runtime contract is authoritative;
all current target cells remain blocked.

## Outcome

Create exactly one unqualified `crm.lead` draft in the approved company.
Creation does not authorize conversion, stage advancement, assignment,
activity creation, chatter posting, deduplication overrides, or related
contact creation.

## Approval-bound request

- `capability`: exactly `create_crm_lead_draft.v1`
- `target`: exact instance, database, environment, and company identifiers
- `payload`: canonical object accepted by the runtime contract
- `payload_sha256`: digest of that canonical object
- `idempotency_key`: unique, single-purpose key matching the runtime pattern
- `approval`: approver identity, decision, timestamp, expiry, and matching
  capability, target, company, payload digest, and idempotency key

The closed input contract (additional properties denied) requires:

- `title` (maps to Odoo `crm.lead.name`)
- `organization` (nullable; maps to `partner_name` when set)
- `contact_name` (nullable)
- `email` (nullable; maps to `email_from` when set)
- `phone` (nullable)
- `description` (nullable)
- `evidence_ref` (audit/source reference; not persisted on the lead)
- `idempotency_key` (pattern `crm-lead:v1:<64 hex>`)

Optional envelope field when advertised: `approval_id`. Company is not a
caller-chosen payload field; the trusted active/target company from live
context is forced. Runtime also forces `type=lead`. Reject unknown fields,
team/user assignment, relational command tuples, context overrides,
server-action or method names, and values added or normalized after approval.

## Runtime behavior required

The capability implementation, not this skill, must enforce schema validation,
ACLs and record rules, company scope, environment policy, approval binding,
idempotency, and audit logging. It must return a structured receipt containing
the shared normalized receipt fields, including target cell, `draft_write`,
verification, and compensation status.

Reusing an idempotency key with an identical request may return the original
receipt but must not create another lead. Reuse with any changed binding is
denied. An indeterminate timeout is not permission to retry. Multiple
duplicate candidates are a conflict, never an automatic merge.

## Verification

Use a bounded read-only lookup of the receipt's `crm.lead` identifier. Confirm
the approved company and approved business fields, and confirm that no
unapproved side effects are claimed. Do not search broadly by personal data.

## Refusal boundary

If the named capability is unavailable, do not fall back to generic ORM/RPC
operations such as `create`, `write`, `unlink`, `execute_kw`, arbitrary model
methods, direct SQL, or shell/database access. Report runtime blocked until all
capability gates pass.
