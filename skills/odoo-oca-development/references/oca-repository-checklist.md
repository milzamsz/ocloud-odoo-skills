# OCA Repository Checklist

Use the target repository and target branch as evidence. OCA conventions are
shared, but their concrete tooling and supported modules are branch-specific.

## Evidence sequence

1. Confirm the canonical `OCA/<repository>` URL and exact target branch.
2. Search the generated addon table and manifests for overlapping modules.
3. Read root contribution instructions and configured tooling.
4. Inspect two maintained modules on that branch for layout and metadata.
5. Record what was observed; do not fill gaps from another branch.

## Repository checks

- Root `README.md`: target-branch badges, generated addon list, and repository
  license. A repository license does not replace the module's manifest license.
- Module `__manifest__.py`: version begins with the target Odoo series, declares
  the actual license and dependencies, and contains no client-specific metadata.
- `readme/`: use only fragments present in the branch (for example
  `DESCRIPTION.md`, `USAGE.md`, `CONFIGURE.md`, `CONTRIBUTORS.md`, or
  `ROADMAP.md`). Do not hand-edit generated root/module README sections.
- `.pre-commit-config.yaml`, `.pylintrc`, `.ruff.toml`, `pyproject.toml`, CI
  workflows, and repository scripts: run the configured checks rather than a
  remembered generic command set.
- Maintainers and ownership: use repository/module metadata and current
  contribution guidance; do not invent maintainers.
- Dependencies: verify Odoo, OCA, Python, and external dependencies on the same
  branch; inspect `oca_dependencies.txt` or equivalent when present.
- Migration directories: follow examples in the target branch only, keep
  migration and feature commits separate, and document data assumptions.

## Locally verified boundaries (2026-07-19)

- Usable local 19.0 checkouts show generated branch-specific READMEs, manifest
  versions such as `19.0.1.0.0`, per-module `readme/` fragments, root
  pre-commit/Pylint/Ruff configuration, module `pyproject.toml` files, and
  versioned `migrations/` directories where needed.
- A locally misplaced checkout named `account-financial-tools-18.0` under the
  `19.0/` aggregate folder contains 18.0 badges and `18.0.*` manifests. Trust
  repository content and Git branch evidence, not the aggregate parent path.
- **OCA 18 local gap:** there is no complete, canonical local 18.0 checkout set.
  The partial checkout above is useful corroboration only. Verify any 18.0
  contribution against the canonical remote target branch and registered OCA
  sources before claiming branch compliance.

## Stop conditions

Stop and report a blocker when the target repository/branch is absent, the
module duplicates existing functionality, licensing is unclear, dependencies
are unavailable for that branch, or configured checks cannot be reproduced.
