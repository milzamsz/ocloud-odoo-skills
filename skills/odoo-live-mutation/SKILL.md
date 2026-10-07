---
name: odoo-live-mutation
description: Use this skill when preparing, approving, executing, or verifying one contract-approved named Odoo mutation capability for CRM leads, quotations, vendor-bill drafts, allowed draft-field updates, or bank transaction imports in development or staging. Do not use it for raw CRUD, bulk writes, posting, reconciliation, workflow actions, cleanup, production mutation, or read-only work.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Runtime support is decided per capability and exact Odoo version/edition/protocol/environment cell; no target mutation cell is currently approved.
metadata:
  version: "0.2.0"
  author: OCloud
  status: experimental
  risk: controlled-write
  hermes:
    tags: [odoo, live, mutation, approval, controlled-write]
---

# Odoo Live Mutation

## Purpose

Produce one approval-bound mutation packet for one named capability, then verify its normalized receipt without widening scope. This skill supplies procedure only; the shared runtime contract decides support.

## Preconditions

- Confirm authenticated actor, target identity, database reference, environment, exact Odoo version and edition, protocol, auth mode, installed modules, active company, allowed companies, registry revision, and model-metadata fingerprint.
- Load the relevant domain skill before interpreting business fields. Load live context/read procedures when target evidence is missing.
- Select one exact versioned capability and load its reference listed below.
- Start from `assets/mutation-packet.md`; one packet authorizes one invocation.

## Capability gates

All gates are mandatory:

1. The shared contract approves the exact capability × version × edition × protocol × auth mode × environment cell, with schema hashes, runtime evidence, and required reviews.
2. Runtime and plugin registry revisions match that contract; production is always denied.
3. The authenticated actor and approver are identified and distinct where policy requires.
4. Approval is explicit, current, bound to the exact target, company, capability, canonical payload digest, expiry, and one-time idempotency key.
5. The submitted payload exactly matches the approved canonical payload; no defaults or fields may be added after approval.
6. Active and target company match the approved company and belong to allowed companies.
7. The idempotency key is unused or resolves to the same completed result.
8. Required modules, model fingerprint, least-privilege access, postconditions, verification, audit durability, and compensation ownership pass.

If any gate is unknown or fails, return `blocked` or `denied` and do not invoke a mutation tool.

## Workflow

1. Capture confirmed live context and the selected contract without secrets.
2. Canonicalize and validate the proposed payload against the contract allowlist.
3. Record impact, duplicate risk, verification, and safe failure handling.
4. Present the complete packet and payload digest for explicit approval.
5. Recheck every gate immediately before invocation.
6. Invoke only the exact named capability once; the plugin must sign the approval-bound envelope and the MCP runtime must execute `odoo_execute_capability`—never a raw write tool.
7. Validate the MCP runtime's normalized final receipt against the shared output schema and perform bounded read-only verification.
8. Report `verified`, `failed`, `blocked`, or `denied`; never retry with a changed payload under the same approval.

## Safety rules

- Refuse raw or generic `create`, `write`, `unlink`, `execute_kw`, arbitrary model/method calls, direct SQL, shell workarounds, and unrestricted RPC even if requested.
- Never translate a named capability into generic write primitives client-side.
- Treat payload changes, company changes, target changes, expired approval, replay ambiguity, missing audit support, and unavailable verification as new or blocked requests.
- Never mutate production. A vague instruction such as “go ahead,” administrator access, or prior approval is insufficient.
- Do not post, confirm, reconcile, pay, create adjacent records, run workflows, or perform cleanup unless the selected reference explicitly defines that effect; none of the five current capabilities does.
- Do not expose credentials, session identifiers, private URLs, or unnecessary personal data.

## Required output

Return the completed mutation packet plus the normalized receipt: target cell, capability, operation class, status, actor/approval references, idempotency key, payload digest, correlation/audit IDs, record reference, verification, and compensation. A record ID alone is not completion evidence.

## Verification

- Target cell, capability, operation class, target/company, payload digest, approval, idempotency key, and registry revision match the receipt.
- Read-only verification confirms only the approved business result.
- No raw generic write primitive or adjacent mutation was used.
- Runtime reports all capability gates passed; otherwise status remains blocked or denied.

## Failure and escalation

Stop without retrying on validation, authorization, company, digest, replay, policy, timeout, or verification failure. Preserve non-secret evidence. Require a new packet and approval for any changed payload or uncertain execution result; escalate suspected cross-company access, duplicate creation, or audit inconsistency.

## Capability reference to load

Read exactly one:

- CRM lead: [create-crm-lead-draft-v1.md](references/create-crm-lead-draft-v1.md)
- Quotation: [create-quotation-draft-v1.md](references/create-quotation-draft-v1.md)
- Vendor bill: [prepare-vendor-bill-draft-v1.md](references/prepare-vendor-bill-draft-v1.md)
- Allowed draft update: [update-allowed-draft-fields-v1.md](references/update-allowed-draft-fields-v1.md)
- Bank import: [import-bank-transaction-draft-v1.md](references/import-bank-transaction-draft-v1.md)
