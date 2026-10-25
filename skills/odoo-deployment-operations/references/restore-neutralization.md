# Restore and Neutralization

Use when a production database copy is restored into any non-production
environment (staging, migration rehearsal, local developer copy).

## Why

A restored production copy still carries live cron jobs, outgoing mail
servers, payment and integration credentials, webhooks, and the production
`web.base.url`. Starting it unneutralized can send real email, charge real
payment providers, push data to real integrations, or redirect users.

## Checklist (verify each, do not assume)

1. Database and filestore come from the same recovery point.
2. Odoo's built-in neutralization ran (`--neutralize`, or the hosting
   tool's equivalent such as `odood db restore --stun`), or every step below
   was applied manually.
3. Outgoing mail servers are disabled or pointed at a catch-all sink.
4. Scheduled actions are inactive unless a named job is explicitly required.
5. Payment providers, delivery carriers, bank sync, and other integration
   records are in test mode or disabled; stored credentials are removed.
6. `web.base.url` and `web.base.url.freeze` match the non-production host.
7. Website and portal are not reachable on the production domain.
8. `list_db` and master password follow the environment's policy.
9. A visible banner or database name marks the copy as non-production.
10. The neutralization result is recorded in the runbook with the command
    and checked values, never with secrets.

## Boundaries

- Neutralization is a mutation of the copy: it requires the exact-target
  authorization defined in the skill, even though it protects production.
- Never neutralize the only copy or the production database itself.
- Refresh the backup after any runtime fix made on the copy so the next
  rehearsal starts from a known state.
