# OCloud Odoo Skills

A curated, version-aware collection of Odoo skills for Hermes Agent and other clients compatible with the Agent Skills specification.

The repository teaches agents how to analyze, design, implement, review, test, secure, migrate, and operate Odoo solutions. It does **not** replace Odoo source code, project specifications, official documentation, OCA repositories, or controlled integration tools.

## Project status

- Stage: Phase 1 stable; Phase 2 domain and technical skills experimental; Phase 3 controlled
  live integration in progress
- Stable target: Odoo 18.0 Community
- Verified-experimental targets: Odoo 17.0 Community/Enterprise, Odoo 18.0
  Enterprise, and Odoo 19.0 Community/Enterprise
- Runtime priority: Hermes Agent
- Format: Agent Skills (`SKILL.md`)
- Distribution: Hermes custom skill tap and external skill directory

## Why this repository exists

Public Odoo skill repositories contain valuable patterns, but they frequently mix:

- multiple Odoo versions without explicit boundaries;
- generic development advice with Odoo-specific constraints;
- knowledge, executable tools, and automation in one package;
- Community, Enterprise, OCA, and custom conventions;
- safe read operations with state-changing production operations.

OCloud Odoo Skills creates a controlled layer that is:

1. **Outcome-based**: each skill solves a coherent task.
2. **Version-aware**: version and edition are detected before recommendations are applied.
3. **Standard-first**: evaluate Odoo Standard, configuration, and OCA before custom code.
4. **Evidence-grounded**: repository instructions and target source code outrank generalized guidance.
5. **Safe by default**: live systems are read-only unless an authorized workflow explicitly permits mutation.
6. **Evaluated**: trigger behavior and task outcomes are tested before release.
7. **Portable**: Hermes is the primary runtime, but the skill content follows the open specification.

## Phase 1 skills

| Skill | Purpose |
|---|---|
| `odoo-context-discovery` | Detect version, edition, repository layout, dependencies, runtime, and risk context. |
| `odoo-solution-design` | Decide whether a requirement needs standard features, configuration, OCA, low-code, custom addon, or external service. |
| `odoo-addon-development` | Implement controlled Odoo addon changes with security, tests, documentation, and upgradeability. |
| `odoo-code-review` | Review correctness, maintainability, performance, upgradeability, and production readiness. |
| `odoo-security-audit` | Audit ACLs, record rules, public methods, controllers, `sudo()`, SQL, HTML, and data isolation. |
| `odoo-testing` | Select and implement the appropriate Python, JavaScript, tour, access, migration, and performance tests. |
| `odoo-oca-development` | Apply OCA-oriented module structure, tooling, documentation, and contribution conventions. |
| `odoo-version-upgrade` | Plan and verify module and database migration between major Odoo versions. |

## Phase 2 domain and technical skills

| Skill | Purpose |
|---|---|
| `odoo-functional-sales` | Design CRM and sales order-to-cash processes through invoice readiness. |
| `odoo-functional-purchase` | Design procure-to-pay processes through vendor bill matching readiness. |
| `odoo-functional-inventory` | Design warehouses, routes, stock documents, and valuation impact flags. |
| `odoo-functional-accounting` | Design accounting controls, posting, reconciliation, and closing. |
| `odoo-indonesia-accounting` | Assess Indonesian localization with assumption-bound tax and PSAK analysis. |
| `odoo-integration-design` | Design external-system boundaries, idempotency, and recovery contracts. |
| `odoo-reporting` | Choose and design Odoo report mechanisms with access and performance controls. |
| `odoo-functional-pos` | Design POS sessions, payments, offline recovery, and stock handoff. |
| `odoo-functional-manufacturing` | Design BoM-to-production processes, exceptions, and inventory handoff. |
| `odoo-deployment-operations` | Produce read-only-first deployment, backup, rollback, and monitoring runbooks. |
| `odoo-data-model-diagram` | Produce bounded logical Odoo ORM DBML diagrams from source and read-only metadata. |

These skills are experimental. They use a stable Odoo 18 Community baseline
and verified-experimental source/module evidence for the other five 17/18/19
Community/Enterprise cells. Target installation and behavior still require
case-specific evidence. They compose the Phase 1 workflows rather than
duplicating discovery, solution design, implementation, testing, assurance, or migration. See
[Phase 2 skill boundaries](docs/PHASE-2-SKILL-BOUNDARIES.md).

## Phase 3 controlled live integration

Phase 3 adds read-only live context and query procedures, followed by
capability-specific approval-gated mutation. Skills remain procedural:
`hermes-plugin-odoo` owns Hermes context, guards, and metadata-only audit;
`odoo-rust-mcp-agent` owns typed execution and policy.

Production remains read-only. Generic write tools are not agent-facing
capabilities. See [Phase 3 skill boundaries](docs/PHASE-3-SKILL-BOUNDARIES.md)
and [interface contract](docs/PHASE-3-INTERFACE-CONTRACT.md).

| Skill | Purpose |
|---|---|
| `odoo-live-context` | Verify configured instance, company, model metadata, and effective read access. |
| `odoo-live-read` | Execute bounded least-data record reads with domain interpretation handoffs. |
| `odoo-live-mutation` | Prepare capability-specific approval packets; runtime remains blocked when capability gates are incomplete. |

## Repository structure

```text
.
├── README.md
├── PRODUCT-SCOPE.md
├── DOMAIN-MODEL.md
├── ARCHITECTURE.md
├── TECHNICAL.md
├── DESIGN.md
├── PLAN.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── Makefile
├── pyproject.toml
├── skills.sh.json
├── bundles/
├── docs/
├── evals/
├── prompts/
├── schemas/
├── scripts/
├── skills/
├── sources/
└── templates/
```

## Local development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
make validate
make test
```

## Use as a Hermes external skill directory

Clone the repository and add the skills directory to the Hermes profile configuration:

```yaml
skills:
  external_dirs:
    - /absolute/path/to/ocloud-odoo-skills/skills
```

Then reload or restart Hermes. Files under an external directory may still be modified by Hermes when the process has write permission. Use filesystem permissions and review gates when the repository must be immutable.

## Use as a Hermes skill tap

After publishing the repository:

```bash
hermes skills tap add ocloudpro/ocloud-odoo-skills
hermes skills search odoo
hermes skills install ocloudpro/ocloud-odoo-skills/odoo-context-discovery
```

Bundles are installed separately under `~/.hermes/skill-bundles/` because a bundle groups already installed skills; it does not install them.

## Documentation map

- [Product scope](PRODUCT-SCOPE.md)
- [Domain model](DOMAIN-MODEL.md)
- [Architecture](ARCHITECTURE.md)
- [Technical specification](TECHNICAL.md)
- [Skill design system](DESIGN.md)
- [Implementation plan](PLAN.md)
- [Agent instructions](AGENTS.md)
- [Contribution guide](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Skill authoring standard](docs/SKILL-AUTHORING-STANDARD.md)
- [Testing and evaluation](docs/TESTING-AND-EVALUATION.md)
- [Hermes integration](docs/HERMES-INTEGRATION.md)
- [Source hierarchy](docs/ODOO-SOURCE-HIERARCHY.md)

## Non-goals

This repository does not:

- provide an unrestricted production Odoo operator;
- embed customer credentials or database secrets;
- replace `odoo-rust-mcp-agent` or `hermes-plugin-odoo`;
- guarantee compatibility based only on a version label;
- copy third-party skills without license and provenance review;
- treat generated code as complete before executable verification.

## Related OCloud repositories

```text
ocloud-odoo-skills      procedural knowledge, workflows, references, evaluation
hermes-plugin-odoo      Hermes tools, hooks, commands, and policy integration
odoo-rust-mcp-agent     controlled Odoo discovery and operation interface
```

## License

Original OCloud content is released under the MIT License. Third-party source material must remain governed by its own license and the clean-room rules in `sources/SOURCE-POLICY.md`.
