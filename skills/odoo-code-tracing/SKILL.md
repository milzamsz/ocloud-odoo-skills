---
name: odoo-code-tracing
description: Use this skill when reconstructing a specific Odoo execution path from a controller, button, cron, ORM hook, or frontend call to its verified side effects and security boundaries. Do not use for a broad code review or implementation without a concrete entry point.
license: MIT
compatibility: Hermes Agent and Agent Skills clients with source access; Odoo 18 and 19 Community, and Odoo 20 Community and Enterprise.
metadata:
  version: "0.2.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0", "19.0", "20.0"]
    editions: [community, enterprise]
    editions_by_version:
      "18.0": [community]
      "19.0": [community]
      "20.0": [community, enterprise]
  hermes:
    tags: [odoo, tracing, call-chain, impact-analysis]
---

# Odoo Code Tracing

## Purpose and boundary

Produce a bounded source-evidenced call-chain and side-effect map for one specified entry point. For unspecified environment context, use `odoo-context-discovery` first. Hand off defect judgments to `odoo-code-review`, security conclusions to `odoo-security-audit`, and changes to `odoo-addon-development`.

## Use when

- a specific button, route, cron, ORM hook, or frontend call must be followed to its side effects;
- an impact analysis needs `path:line` evidence before a change or review;
- a defect report names a symptom and the entry point is known or enumerable.

## Do not use when

- the request is a broad review of an addon (use `odoo-code-review`);
- the request is to implement or change behavior (use `odoo-addon-development`);
- the version or edition is unknown (run `odoo-context-discovery` first).

## Workflow

1. Confirm target version, edition, repository, entry point, and path boundary. If the caller or entry point is ambiguous, list candidates and stop before asserting behavior.
2. Read the entry declaration and its XML ID, route, button, cron, registry, or ORM wiring. Cite file and line for each edge.
3. Follow local method calls, inheritance and `super()` in the available source. Inspect decorators and computed, onchange, inverse, constraint, and create/write/unlink hooks only where reachable. Mark missing addon or dynamically selected implementation as unknown.
4. Identify reads and writes, transaction boundaries, external calls, and user-visible effects. Separate proven effects from possible effects.
5. For each crossed boundary, record current user, groups, ACL/record-rule expectations, company context, elevation, and portal/public exposure. Do not treat a view restriction as server authorization.
6. Stop at the chosen depth or missing evidence; never imply that a static trace proves runtime order across installed but unavailable extensions.

## Safety and evidence

Read-only source analysis is the default. Do not query live business data, invoke routes, run jobs, install addons, or change a database to complete a trace. Quote only short identifiers and line references; do not reproduce upstream source. Independently verify version-sensitive behavior using exactly one matching version reference and the target checkout.

## Required output

Use `assets/code-trace-report.md`. Return entry point/version/edition, bounded call-chain edges with `path:line` citations, side effects, authorization/company boundaries, confirmed versus inferred versus unknown behavior, and the smallest proposed verification test. State unavailable source and runtime checks not run. Every edge cell holds a `path:line` citation, `NOT FOUND`, `UNCERTAIN: <what>`, or `AMBIGUOUS: <candidates>`; never a guess.

## Verification

- Every edge and side effect cites a file and line in the available source.
- Runtime, query-count, and access-control claims are marked unverified unless a test was run.
- Missing addons or dynamically selected implementations are listed as unknown, not omitted.

## Failure and escalation

Stop and list candidates when the entry point is ambiguous. Stop at the chosen depth when source is unavailable; do not fill the gap with generic Odoo behavior. Hand a suspected defect to `odoo-code-review` and a suspected exposure to `odoo-security-audit`.

## References to load

After confirming Odoo version and edition, read exactly one matching file:

- Odoo 18: `references/odoo-18-community.md`
- Odoo 19: `references/odoo-19-community.md`
- Odoo 20: `references/odoo-20-{community,enterprise}.md`

Odoo 20 remains experimental; source-level evidence does not prove runtime behavior. For any other version, or Enterprise on 18 or 19, do not claim compatibility; hand off to context discovery and target-version source inspection.
