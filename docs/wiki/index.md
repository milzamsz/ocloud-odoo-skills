# OCloud Odoo Skills: AI wiki

Read this first. It is the shortest path from a cold start to a correct change
in this repository. Every page links to the file that is the source of truth;
when a page and its source disagree, the source wins and the page is a bug.

## What this repository is

A set of version-aware Odoo skills in the Agent Skills format (`SKILL.md`)
for Hermes Agent and Claude Code. Skills hold procedures, decision rules,
references, and small deterministic scripts. They teach an agent how to
discover, design, build, review, test, secure, upgrade, and operate Odoo 17
to 20, Community and Enterprise.

## What it is not

- Not Odoo source, not an addon, and not a live Odoo client.
- Not where credentials or database writes live. `odoo-rust-mcp` executes;
  `odoo-rust-mcp-agent` holds the per-cell support contract; `hermes-plugin-odoo`
  only guards, signs, and audits (see [live-integration.md](live-integration.md)).
- Not a copy of third-party skills. Outside material is clean-room only
  ([../../sources/SOURCE-POLICY.md](../../sources/SOURCE-POLICY.md)).

## Reading order

1. This page.
2. [../../AGENTS.md](../../AGENTS.md): mission, rules, and the completion report. Mandatory.
3. [repo-map.md](repo-map.md): where everything lives.
4. [skill-anatomy.md](skill-anatomy.md): what the validator demands of a skill.
5. The page for your task, from the table below.

## Route by task

| I need to… | Read |
|---|---|
| Find which skill covers a topic | [skill-catalog.md](skill-catalog.md) |
| Edit or add a skill | [skill-anatomy.md](skill-anatomy.md), then [workflows.md](workflows.md) |
| Claim or add an Odoo version or edition | [version-matrix.md](version-matrix.md) |
| Add trigger or outcome evaluations | [evaluations.md](evaluations.md) |
| Work on live reads or mutation capabilities | [live-integration.md](live-integration.md) |
| Register an external source | [workflows.md](workflows.md#register-a-source) |
| Understand a term | [glossary.md](glossary.md) |
| Avoid known traps | [gotchas.md](gotchas.md) |

## Commands

```bash
make validate        # structure, metadata, links, version claims, sources, bundles, wiki
make lint            # ruff on scripts, tests, and skill scripts
make test            # pytest
make package-check   # validate, then check every skill is self-contained
```

CI (`.github/workflows/ci.yml`) runs all four on every pull request with
Python 3.11. Do not merge red validation.

## Pages

- [repo-map.md](repo-map.md): directories and which docs are current or historical.
- [skill-anatomy.md](skill-anatomy.md): `SKILL.md` frontmatter, layout, and validator rules.
- [skill-catalog.md](skill-catalog.md): every skill with status, risk, cells, and bundles.
- [version-matrix.md](version-matrix.md): version and edition cells, and verified Odoo 20 differences.
- [evaluations.md](evaluations.md): trigger sets, outcome cases, fixtures, live and manual runs.
- [live-integration.md](live-integration.md): Phase 3 read and mutation stack across repositories.
- [workflows.md](workflows.md): step-by-step recipes.
- [glossary.md](glossary.md): repository vocabulary.
- [gotchas.md](gotchas.md): traps that have bitten earlier changes.
