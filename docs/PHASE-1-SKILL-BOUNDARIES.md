# Phase 1 Skill Boundaries and Output Contracts

Each skill owns one primary outcome. A skill may load an adjacent skill, but it
must not silently replace that skill's decision or artifact.

| Skill | Primary outcome | Required artifact | Boundary |
|---|---|---|---|
| `odoo-context-discovery` | Verified repository and runtime context | `assets/context-summary.yaml` | Stops before solution selection, implementation, or mutation. |
| `odoo-solution-design` | Approved standard-first solution decision | `assets/solution-design-template.md` | Stops before code changes. |
| `odoo-addon-development` | Implemented approved addon change | `assets/implementation-report.md` | Does not resolve material product ambiguity or act as review-only workflow. |
| `odoo-code-review` | Prioritized correctness and readiness findings | `assets/review-report.md` | Read-only unless fixes are separately requested; delegates deep security coverage. |
| `odoo-security-audit` | Defensive Odoo security findings | `assets/security-audit-report.md` | No exploitation or production mutation; does not replace a broad code review. |
| `odoo-testing` | Executable verification evidence | `assets/test-evidence.md` | Tests approved behavior; does not redesign the solution. |
| `odoo-oca-development` | Branch-specific OCA contribution readiness | `assets/contribution-report.md` | Applies only to OCA or explicitly OCA-style contribution work. |
| `odoo-version-upgrade` | Controlled major-version migration plan and evidence | `assets/upgrade-plan.md` | Keeps compatibility work separate from feature work and requires mutation approval. |

All artifacts must state confirmed version and edition where relevant, label
unknowns, report safety constraints, and identify completion evidence. These
contracts are additive templates rather than runtime schemas; changing a
required section is a skill behavior change and belongs in the changelog.
