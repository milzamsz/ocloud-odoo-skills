# Product Scope

## 1. Executive summary

OCloud Odoo Skills is a curated procedural knowledge layer for AI agents working with Odoo. It converts OCloud's ERP delivery standards into reusable, version-aware skills that can be loaded on demand by Hermes Agent.

The product is not merely a collection of prompts. It is a governed skill system with explicit scope, source provenance, safety policies, trigger evaluation, task evaluation, release controls, and an evolution path toward functional, accounting, Indonesian localization, integration, and operations skills.

## 2. Business problem

AI coding agents can generate Odoo code quickly, but speed does not solve the primary delivery risks:

- selecting customization when standard configuration would be sufficient;
- using APIs or XML patterns from the wrong Odoo version;
- overlooking ACLs, record rules, multi-company behavior, or accounting impact;
- modifying a database before understanding the environment;
- declaring completion without installation, upgrade, access, and functional verification;
- applying community guidance without checking provenance or license;
- coupling knowledge to one agent, one IDE, or one MCP implementation.

These failures create expensive rework, unstable upgrades, security exposure, and inconsistent consulting outcomes.

## 3. Product vision

Create OCloud's trusted Odoo procedural layer so that AI agents behave like controlled ERP engineering collaborators rather than autocomplete systems with administrator access.

## 4. Objectives

### 4.1 Business objectives

- Reduce avoidable custom development.
- Improve consistency across OCloud Odoo projects.
- Preserve upgradeability and maintainability.
- Shorten analysis, review, testing, and migration cycles.
- Make OCloud delivery knowledge reusable across Hermes profiles and repositories.
- Establish a foundation for Indonesian accounting and tax skills.

### 4.2 Product objectives

- Publish coherent, outcome-based Agent Skills.
- Support Hermes progressive disclosure and skill bundles.
- Detect Odoo version and edition before applying version-sensitive guidance.
- Provide safe defaults for repository, database, and production operations.
- Measure trigger accuracy and task outcome quality.
- Maintain source provenance and clean-room authoring controls.

### 4.3 Engineering objectives

- Validate every `SKILL.md` against naming and metadata rules.
- Keep the core skill body concise and move detail into references.
- Make scripts deterministic, inspectable, and dependency-light.
- Separate knowledge from integration tools.
- Support repository-local and profile-level installation.

## 5. Users

| Persona | Need |
|---|---|
| OCloud solution architect | Compare standard, OCA, custom, and external approaches before implementation. |
| Odoo developer | Implement version-correct, secure, testable addons. |
| ERP functional consultant | Translate business needs into Odoo processes and functional requirements. |
| Reviewer or technical lead | Identify functional, security, performance, and upgrade risks. |
| Migration engineer | Plan module and data migration with evidence and reconciliation. |
| Hermes Agent | Load the minimum relevant procedures and references for a task. |
| Future external contributor | Add skills without weakening quality, safety, or source controls. |

## 6. Product principles

1. Business value before technology.
2. Standard before customization.
3. Inspect before proposing.
4. Version and edition before syntax.
5. Read-only before state change.
6. ORM before SQL.
7. Least privilege before convenience.
8. Tests and reconciliation before completion.
9. Evidence before confidence.
10. Small coherent skills before comprehensive monoliths.

## 7. Scope

### 7.1 Phase 1 in scope

- Repository and environment discovery.
- Solution classification and customization decisions.
- Addon development workflow.
- Code review.
- Security audit.
- Testing strategy.
- OCA-oriented development.
- Major-version upgrade workflow.
- Hermes skill tap layout.
- Hermes bundle definitions.
- Trigger and task evaluation framework.
- Source registry and version matrix.
- Local validation and CI design.

### 7.2 Phase 2 in scope

- Sales, CRM, Purchase, Inventory, POS, Manufacturing, Project, Helpdesk, and Website functional skills.
- Accounting foundations.
- Indonesian localization, PSAK, and tax workflows.
- Integration and API design.
- Reporting and QWeb.
- Deployment and operations.
- Technical data-model visualization from source and read-only metadata.

### 7.3 Phase 3 in scope

- Controlled live-instance operations through `hermes-plugin-odoo` and `odoo-rust-mcp-agent`.
- Read/write policy enforcement.
- Approval-gated workflows.
- Odoo metadata-assisted context discovery.
- Audit evidence capture.
- Organization-specific private skill overlays.

### 7.4 Out of scope

- Autonomous destructive production administration.
- Credential storage inside skills.
- A replacement for official Odoo documentation or source code.
- A complete copy of third-party Odoo skill repositories.
- Automatic legal, accounting, or tax conclusions without stated assumptions and current validation.
- A universal compatibility promise across all Odoo editions, branches, hosting models, and third-party addons.

## 8. Component classification

Every recommendation produced by a design skill must classify components as:

| Classification | Definition |
|---|---|
| Standard | Available in the target Odoo edition without custom development. |
| Configured | Achieved through settings, records, security groups, workflows, or views. |
| Third-party | Delivered by a reviewed OCA or vendor addon. |
| Low-code | Implemented through supported native low-code capabilities. |
| Custom | Implemented as an OCloud-maintained addon or code change. |
| External | Implemented outside Odoo through middleware, service, worker, or automation platform. |

## 9. Success metrics

### 9.1 Quality metrics

- 100% skills pass structural validation.
- 100% released skills include trigger evaluation.
- 100% state-changing scripts include explicit risk classification and dry-run behavior where feasible.
- No released skill includes secrets, copied proprietary content, or unverified destructive commands.
- Version-specific guidance identifies its supported versions.

### 9.2 Trigger metrics

- Target precision: at least 90% on validation near-miss prompts.
- Target recall: at least 90% on intended prompts.
- No core skill description is so broad that it triggers for unrelated generic Python tasks.

### 9.3 Outcome metrics

- Context discovery produces the required environment summary fields.
- Solution design evaluates standard and OCA alternatives before custom code.
- Security audit detects seeded ACL, record-rule, controller, `sudo()`, and SQL issues.
- Upgrade skill keeps migration work separate from unrelated feature work.
- Development skill produces installable output with tests and documentation in controlled fixtures.

## 10. Constraints

- Hermes behavior may evolve, so runtime-specific metadata must be isolated from portable instructions.
- Odoo APIs and behavior vary by version and edition.
- Enterprise source access is license-restricted.
- Community repositories have different quality and licensing terms.
- Agent evaluation is probabilistic; run repeated trigger tests.
- Skills can increase token usage or reduce performance when they are over-broad or version-mismatched.

## 11. Assumptions

- OCloud controls the Git repository and release process.
- Odoo 18.0 Community is the stable baseline. Odoo 20.0 Community is source-evidence-only experimental until every specific skill claim passes its evidence and evaluation gates; no Odoo 20 Enterprise or OCA 20 compatibility is assumed.
- Hermes remains the primary consumer, but portability is valuable.
- `odoo-rust-mcp-agent` is responsible for precise Odoo integration operations.
- Human approval remains required for high-risk changes.

## 12. MVP definition

The MVP is complete when:

- the eight Phase 1 skills are structurally valid;
- four Hermes bundles are available;
- each skill has trigger evaluations;
- the repository can be used as an external skills directory;
- the repository can be published as a Hermes tap;
- core workflows pass fixture-based acceptance tests;
- source and license policies are enforced in review;
- installation and contributor documentation are complete.
