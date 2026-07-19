# AGENTS.md

## Mission

Develop and maintain OCloud Odoo Skills as a safe, version-aware procedural layer for Hermes Agent and compatible Agent Skills clients.

## Source of truth

Use this priority order:

1. Current task and approved project documents.
2. This `AGENTS.md` and repository documentation.
3. Existing repository code, schemas, tests, and fixtures.
4. Official Hermes and Agent Skills specifications.
5. Official Odoo documentation and target-version source code.
6. OCA repositories and maintainer documentation.
7. Registered community sources.

Do not replace observed repository facts with generic knowledge.

## Required workflow

1. Read `PRODUCT-SCOPE.md`, `ARCHITECTURE.md`, `TECHNICAL.md`, and `DESIGN.md` before structural changes.
2. Inspect existing skill scope and adjacent skills before adding or expanding one.
3. Confirm target Odoo versions and editions.
4. Register or update sources before using new external material.
5. Keep `SKILL.md` focused and use progressive disclosure.
6. Add or update trigger and outcome evaluations.
7. Run validation and tests.
8. Update documentation and changelog.

## Architecture boundaries

- Skills contain procedures, decision rules, references, and deterministic helper scripts.
- `hermes-plugin-odoo` contains Hermes-specific tools, hooks, and integration policy.
- `odoo-rust-mcp-agent` contains precise Odoo access and state-changing execution.
- Do not move credentials, authentication logic, or production mutation into skills.

## Odoo principles

- Business value first.
- Standard, configuration, and OCA before custom addons.
- Never modify Odoo core by default.
- Preserve upgradeability.
- Treat ACLs, record rules, multi-company, multi-currency, accounting, and taxes as first-class concerns.
- Separate operational documents from journal entries.
- Explain debit, credit, posting, and reconciliation when accounting is relevant.
- State exact version and edition support.

## Skill rules

- One primary outcome per skill.
- Directory name equals frontmatter `name`.
- Description explains both what and when.
- Avoid descriptions that overlap generic Python or web development.
- Keep mandatory instructions concise.
- Load references conditionally and explicitly.
- Define required output and completion evidence.
- Mark assumptions and unknowns.
- Avoid unsupported claims of compatibility.

## Safety rules

- Read-only is the default for live Odoo systems.
- Do not execute database-changing commands without explicit authorization.
- Never test migrations on the only database copy.
- Do not add secrets, tokens, private URLs, client data, or proprietary Enterprise code.
- Do not copy third-party skill text or scripts until license and attribution are reviewed.
- Scripts must validate paths and inputs and avoid unsafe shell construction.
- Direct SQL requires documented necessity, parameterization, transaction awareness, and tests.

## Evaluation requirements

For every stable skill:

- structural validation passes;
- trigger dataset includes realistic positive and near-miss negative cases;
- task evaluation proves the expected outcome;
- regressions are checked against the previous release;
- human Odoo review is recorded.

## Change discipline

Separate:

- bug fixes;
- skill behavior changes;
- reference updates;
- evaluation changes;
- new version support;
- formatting-only changes.

Avoid speculative broad changes. When blocked by missing product, security, licensing, or migration decisions, document the blocker and continue only with independent work.

## Commands

```bash
make validate
make test
make package-check
```

## Completion report

Every material change must report:

- skills changed;
- behavior changed;
- source changes;
- version support changes;
- safety impact;
- evaluations added or changed;
- commands executed and results;
- unresolved risks.
