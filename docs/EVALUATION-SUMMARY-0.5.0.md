# Evaluation Summary 0.5.0

Evaluation date: 2026-07-19

This summary records one clean read-only Claude/Codex-style review pass per
skill. Trigger figures describe classification of the committed datasets.
Outcome scores use the weighting in `evals/MANUAL-EVALUATION.md`.

| Skill | Trigger labels | Outcome score | Prohibited actions | Disposition |
|---|---:|---:|---|---|
| `odoo-context-discovery` | 16/16 | 96/100 | Pass | Experimental |
| `odoo-solution-design` | 16/16 | 94/100 | Pass | Experimental |
| `odoo-addon-development` | 16/16 | 92/100 | Pass | Experimental |
| `odoo-testing` | 16/16 | 94/100 | Pass | Experimental |
| `odoo-code-review` | 16/16 | 100/100 on both cases | Pass | Experimental |
| `odoo-security-audit` | 16/16 | 100/100 on both cases | Pass | Experimental |
| `odoo-oca-development` | 16/16 | 88/100 | Pass | Experimental |
| `odoo-version-upgrade` | 16/16 | 91/100 | Pass | Experimental |

## Runtime evidence

The clean-room `minimal-addon-18` fixture was installed and tested in a
uniquely named disposable Odoo 18 Community PostgreSQL database. Three test
methods completed with exit code 0, zero failures, and zero errors. The
database was dropped automatically.

## Review findings

- No prohibited production mutation, exploit execution, secret disclosure, or
  Enterprise-source redistribution was observed.
- Skill boundaries and trigger near-misses are coherent.
- Odoo 18 Community is the strongest evidence baseline.
- Odoo 17/19 and Enterprise coverage is not yet equivalent.
- OCA 18 local source coverage remains incomplete.
- Version-upgrade version references remain intentionally concise.

## Stable-promotion blockers

This evidence supports experimental `0.5.0`, not stable `1.0.0`. Stable
promotion still requires:

- repeated model runs and release-regression evidence;
- named independent human Odoo review sign-off;
- broader declared-version and edition outcome coverage;
- deeper version-specific upgrade references.
