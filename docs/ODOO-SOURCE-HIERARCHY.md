# Odoo Source Hierarchy

## 1. Purpose

Prevent community examples, stale model knowledge, or generalized skill text from overriding the actual target project and Odoo version.

## 2. Authority tiers

### Tier 1: Project authority

- approved BRD, PRD, scope, architecture, and technical documents;
- repository `AGENTS.md` and contribution instructions;
- acceptance criteria;
- client-approved process decisions.

### Tier 2: Executable target evidence

- target repository code;
- target Odoo source and edition;
- module manifests and dependencies;
- configuration and deployment files;
- tests and observed runtime behavior.

### Tier 3: Official target-version documentation

- Odoo developer reference;
- security, ORM, testing, performance, controller, report, and API documentation;
- official migration and upgrade material where applicable.

### Tier 4: OCA authority

- target OCA repository branch;
- OCA maintainer tools;
- OpenUpgrade documentation and migration analysis;
- repository-specific contribution rules.

### Tier 5: OCloud curated references

Original procedural synthesis validated for declared versions.

### Tier 6: Reviewed community material

Public skills, playbooks, blog posts, code examples, and repositories. Use for discovery and inspiration, not as unquestioned authority.

### Tier 7: General model knowledge

Use only when higher evidence is unavailable and label uncertainty.

## 3. Conflict resolution

When sources conflict:

1. identify exact statements in conflict;
2. check version and edition applicability;
3. prefer executable target evidence;
4. verify against official target-version sources;
5. record unresolved ambiguity;
6. do not implement a fragile assumption silently.

## 4. Version rules

- Use documentation for the exact major version.
- Do not apply Odoo 19 behavior to Odoo 18 without verification.
- For migration, inspect both source and target versions.
- SaaS intermediate-version behavior is not automatically valid for major on-premise branches.
- Module compatibility labels do not prove functional compatibility.

## 5. Edition rules

- Enterprise source and dependencies are license-restricted.
- Do not redistribute Enterprise code or derived proprietary documentation.
- Community alternatives must be evaluated explicitly rather than assumed equivalent.

## 6. Community source use

For each community source:

- register URL;
- identify scope;
- identify license or mark it unresolved;
- classify usage as inspiration, reference, or fixture;
- verify claims against authoritative sources;
- avoid verbatim copying unless approved.

## 7. Regulatory sources

For Indonesian accounting and tax skills, use current authoritative regulation and professional interpretation. State effective dates and assumptions. Do not rely on community Odoo modules as proof of legal compliance.
