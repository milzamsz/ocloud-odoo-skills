# OCloud Odoo Skills

A curated, version-aware collection of Odoo skills for Hermes Agent and other clients compatible with the Agent Skills specification.

The repository teaches agents how to analyze, design, implement, review, test, secure, migrate, and operate Odoo solutions. It does **not** replace Odoo source code, project specifications, official documentation, OCA repositories, or controlled integration tools.

## Project status

- Stage: Development specification and Phase 1 scaffold
- Primary target: Odoo 18.0 Community and Enterprise
- Secondary targets: Odoo 17.0 and 19.0
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
