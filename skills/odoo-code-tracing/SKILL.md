---
name: odoo-code-tracing
description: Use this skill when reconstructing a specific Odoo execution path from a controller, button, cron, ORM hook, or frontend call to its verified side effects and security boundaries. Do not use for a broad code review or implementation without a concrete entry point.
license: MIT
compatibility: Hermes Agent and Agent Skills clients with source access; Odoo 18, 19, and 20 Community only.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0", "19.0", "20.0"]
    editions: [community]
  hermes:
    tags: [odoo, tracing, call-chain, impact-analysis]
---

# Odoo Code Tracing

## Purpose and boundary

Produce a bounded source-evidenced call-chain and side-effect map for one specified entry point. For unspecified environment context, use `odoo-context-discovery` first. Hand off defect judgments to `odoo-code-review`, security conclusions to `odoo-security-audit`, and changes to `odoo-addon-development`.

## Workflow

1. Confirm target version, edition, repository, entry point, and path boundary. If the caller or entry point is ambiguous, list candidates and stop before asserting behavior.
2. Read the entry declaration and its XML ID, route, button, cron, registry, or ORM wiring. Cite file and line for each edge.
3. Follow local method calls, inheritance and `super()` in the available source. Inspect decorators and computed, onchange, inverse, constraint, and create/write/unlink hooks only where reachable. Mark missing addon or dynamically selected implementation as unknown.
4. Identify reads and writes, transaction boundaries, external calls, and user-visible effects. Separate proven effects from possible effects.
5. For each crossed boundary, record current user, groups, ACL/record-rule expectations, company context, elevation, and portal/public exposure. Do not treat a view restriction as server authorization.
6. Stop at the chosen depth or missing evidence; never imply that a static trace proves runtime order across installed but unavailable extensions.

## Safety and evidence

Read-only source analysis is the default. Do not query live business data, invoke routes, run jobs, install addons, or change a database to complete a trace. Quote only short identifiers and line references; do not reproduce upstream source. Independently verify version-sensitive behavior using exactly one matching Community reference and the target checkout.

## Required output

Return entry point/version/edition, bounded call-chain edges with `path:line` citations, side effects, authorization/company boundaries, confirmed versus inferred versus unknown behavior, and the smallest proposed verification test. State unavailable source and runtime checks not run.

## References to load

After confirming Odoo version and Community edition, read exactly one matching file:

- Odoo 18: `references/odoo-18-community.md`
- Odoo 19: `references/odoo-19-community.md`
- Odoo 20: `references/odoo-20-community.md`

Odoo 20 remains experimental; source-level evidence does not prove runtime behavior. For any other version or Enterprise target, do not claim compatibility; hand off to context discovery and target-version source inspection.
