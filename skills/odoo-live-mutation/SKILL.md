---
name: odoo-live-mutation
description: Use this skill when preparing or executing an explicitly approved, capability-gated mutation on a live Odoo 18 Community instance through a named structured operation such as create_crm_lead_draft.v1. Do not use it for raw generic create, write, unlink, SQL, arbitrary model methods, read-only work, or unapproved production changes.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Verified procedurally for Odoo 18.0 Community; runtime execution remains blocked until capability gates pass.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: controlled-write
  odoo:
    versions: ["18.0"]
    editions: [community]
  hermes:
    tags: [odoo, live, mutation, approval, controlled-write]
---

# Odoo Live Mutation

## Purpose

Produce one approval-bound mutation packet for one named capability, then verify its result without widening scope. This skill supplies procedure only. Runtime execution is blocked until every capability gate passes in the plugin and MCP runtime.

## Preconditions

- Confirm Odoo 18.0 Community, authenticated actor, target instance, database, environment class, active company, allowed companies, and record access from live evidence.
- Load the relevant domain skill before interpreting business fields. Load live context/read procedures when target evidence is missing.
- Select an exact versioned capability contract. For CRM draft creation, load `references/create-crm-lead-draft-v1.md`.
- Start from `assets/mutation-packet.md`; one packet authorizes one invocation.

## Capability gates

All gates are mandatory:

1. The runtime exposes the exact named capability and contract version.
2. Environment policy permits that capability; production is denied unless policy explicitly allows it.
3. The authenticated actor and approver are identified and distinct where policy requires.
4. Approval is explicit, current, bound to the exact target, company, capability, canonical payload digest, expiry, and one-time idempotency key.
5. The submitted payload exactly matches the approved canonical payload; no defaults or fields may be added after approval.
6. Active and target company match the approved company and belong to allowed companies.
7. The idempotency key is unused or resolves to the same completed result.
8. Preconditions, least-privilege access, expected result, verification query, and failure behavior pass.

If any gate is unknown or fails, return `blocked` or `denied` and do not invoke a mutation tool.

## Workflow

1. Capture confirmed live context and the selected contract without secrets.
2. Canonicalize and validate the proposed payload against the contract allowlist.
3. Record impact, duplicate risk, verification, and safe failure handling.
4. Present the complete packet and payload digest for explicit approval.
5. Recheck every gate immediately before invocation.
6. Invoke only the exact named capability once with the approved payload and idempotency key.
7. Record the audit receipt and perform bounded read-only verification.
8. Report `verified`, `failed`, `blocked`, or `denied`; never retry with a changed payload under the same approval.

## Safety rules

- Refuse raw or generic `create`, `write`, `unlink`, `execute_kw`, arbitrary model/method calls, direct SQL, shell workarounds, and unrestricted RPC even if requested.
- Never translate a named capability into generic write primitives client-side.
- Treat payload changes, company changes, target changes, expired approval, replay ambiguity, missing audit support, and unavailable verification as new or blocked requests.
- Do not mutate production by default. A vague instruction such as “go ahead,” administrator access, or prior approval is insufficient.
- Do not create follow-up records, convert the lead, post messages, assign activities, or perform adjacent cleanup.
- Do not expose credentials, session identifiers, private URLs, or unnecessary personal data.

## Required output

Return the completed mutation packet with gate evidence, approval binding, invocation status, audit receipt, verification evidence, and unresolved blockers. A record ID alone is not completion evidence.

## Verification

- Capability, target, company, payload digest, approval, and idempotency key match the audit receipt.
- Read-only verification confirms only the approved business result.
- No raw generic write primitive or adjacent mutation was used.
- Runtime reports all capability gates passed; otherwise status remains blocked or denied.

## Failure and escalation

Stop without retrying on validation, authorization, company, digest, replay, policy, timeout, or verification failure. Preserve non-secret evidence. Require a new packet and approval for any changed payload or uncertain execution result; escalate suspected cross-company access, duplicate creation, or audit inconsistency.
