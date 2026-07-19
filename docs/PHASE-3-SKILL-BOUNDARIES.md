# Phase 3 Skill Boundaries

Phase 3 skills explain when and why to use controlled Odoo tools. They never
store credentials, implement an Odoo client, or grant permission.

| Skill | Primary outcome | Artifact | Boundary |
|---|---|---|---|
| `odoo-live-context` | Verified live instance, company, model, and access context | `assets/live-context.md` | Read-only metadata; stops before business record queries. |
| `odoo-live-read` | Bounded read plan and evidence | `assets/live-read-evidence.md` | Read-only; no mutation or unrestricted extraction. |
| `odoo-live-mutation` | Approval-bound mutation packet and verification evidence | `assets/mutation-packet.md` | Named capability only; no raw generic write tools. |

## Composition

- Use `odoo-context-discovery` for repository and runtime discovery; add
  `odoo-live-context` only when a configured live instance supplies evidence.
- Load the relevant Phase 2 domain skill before interpreting business records.
- Use `odoo-security-audit` for access-control concerns and
  `odoo-functional-accounting` for posting, reconciliation, or financial
  impact.
- The Hermes plugin owns selected instance/company/profile context, block-only
  guards, and metadata-only audit.
- The MCP layer owns typed operations, policy enforcement, idempotency, and
  state-changing execution.

## Runtime posture

Production is read-only. Development and staging writes remain denied unless a
versioned named capability is exposed and its exact approval contract passes.
