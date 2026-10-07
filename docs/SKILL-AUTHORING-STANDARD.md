# Skill Authoring Standard

## 1. Purpose

This standard defines how to create, revise, review, and release an OCloud Odoo skill.

## 2. Start with a skill contract

Before writing instructions, define:

```yaml
name: odoo-example-outcome
problem: What recurring Odoo task is unreliable without this skill?
primary_outcome: What reusable result must the agent produce?
should_trigger:
  - realistic intended request
should_not_trigger:
  - adjacent near-miss request
required_evidence:
  - target version
  - repository instructions
risk_class: advisory
output_contract: path or concise schema
owner: maintainer name or team
```

Reject the proposal when the outcome is too broad, duplicates an existing skill, or has no credible evaluation.

## 3. Frontmatter

Minimum:

```yaml
---
name: odoo-example-outcome
description: Use this skill when ...
---
```

OCloud convention:

```yaml
---
name: odoo-example-outcome
description: Use this skill when ...
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. Requires access to the target repository for repository-grounded work.
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["18.0", "20.0"]
    editions: [community, enterprise]
    editions_by_version:
      "18.0": [community, enterprise]
      "20.0": [community]
  hermes:
    tags: [odoo, example]
---
```

When a skill supports different editions by release, include
`editions_by_version` so `versions` × `editions` does not accidentally claim an
unsupported cell. The validator retains the legacy cross-product behavior when
this field is absent. Custom metadata is informational. Do not assume every
client enforces it.

## 4. Description rules

A good description:

- starts with “Use this skill when”;
- matches user intent rather than internal implementation;
- includes specific Odoo vocabulary;
- distinguishes adjacent skills;
- remains below 1,024 characters;
- avoids claiming universal expertise.

Test descriptions with realistic prompts. Include near-miss negatives sharing Odoo keywords.

## 5. Body rules

### 5.1 Mandatory content

- purpose;
- use and non-use boundaries;
- evidence and inputs;
- ordered workflow;
- safety boundaries;
- output contract;
- verification;
- conditional references;
- escalation or blocker handling.

### 5.2 Writing style

- Use clear imperative steps.
- Prefer a recommended default and briefly state alternatives.
- Explain why fragile constraints exist.
- Mark facts, inferences, assumptions, and unknowns.
- Do not waste tokens on motivational prose.

### 5.3 Length

Treat 500 lines and 5,000 tokens as warnings, not targets to heroically approach. When core instructions exceed the limit, split detail into references or split the skill by outcome.

## 6. References

A reference must have a specific loading instruction, for example:

```markdown
Read `references/odoo-18.md` only after Odoo 18.0 is confirmed.
Read `references/controller-security.md` when the affected module exposes HTTP routes.
```

Avoid:

```markdown
See references for more information.
```

That instruction saves the author effort and transfers confusion to the agent, an arrangement software has enjoyed for decades.

## 7. Scripts

Add a script only when deterministic execution improves reliability. The skill must explain:

- when to run it;
- required arguments;
- whether it is read-only;
- expected output;
- failure behavior;
- how its output affects the workflow.

## 8. Odoo version and edition

- Discover version and edition before version-sensitive advice.
- Keep version-neutral workflow in the core skill.
- Load only the matching version reference.
- State unsupported or unvalidated versions.
- Never infer Enterprise from business terminology alone.

## 9. Standard-first decision rule

Any skill proposing a solution must evaluate, in order:

1. Odoo Standard.
2. Configuration.
3. Trusted OCA or vendor addon.
4. Native low-code.
5. Custom addon.
6. External service or middleware.

The output must classify the chosen components.

## 10. Safety language

Use explicit boundaries:

- “Do not run module upgrades against the only database copy.”
- “Treat a live Odoo instance as read-only unless the user explicitly authorizes the exact mutation.”
- “Do not use `sudo()` to bypass an unresolved access design.”

Avoid vague phrases such as “be careful.” A database has never been restored by an adjective.

## 11. Output contracts

Outputs should be reusable and testable. Prefer structured Markdown or YAML sections with required fields.

## 12. Evaluation

Before stable release:

- at least 8 should-trigger prompts;
- at least 8 should-not-trigger prompts;
- near-miss cases;
- at least one outcome fixture;
- at least one prohibited-behavior assertion;
- regression comparison with prior release after material changes.

## 13. Review questions

- Is the task coherent?
- Does the description activate on intent?
- Can it be confused with another skill?
- Is version handling safe?
- Are tool and database boundaries explicit?
- Are output requirements verifiable?
- Are sources authoritative and licensed appropriately?
- Does the skill measurably improve the task?
