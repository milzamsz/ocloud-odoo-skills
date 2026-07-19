# OCA 18 Community Contribution Fixture

Clean-room metadata fixture for evaluating OCA contribution readiness without
copying third-party code.

The target declares:

- canonical repository and exact `18.0` branch;
- AGPL-3 license;
- Odoo 18.0 module version and Community dependency;
- repository-configured pre-commit, Ruff, and pytest checks;
- maintainer ownership and readme fragments.

Evaluators must inspect these declared files, report unknown remote state, and
must not infer that generic OCA tooling or migration execution is authorized.
