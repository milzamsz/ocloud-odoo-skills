# Workflows

Step-by-step recipes for the common changes. Source of truth:
[../../AGENTS.md](../../AGENTS.md), [../DEVELOPMENT-WORKFLOW.md](../DEVELOPMENT-WORKFLOW.md),
[../RELEASE-AND-DISTRIBUTION.md](../RELEASE-AND-DISTRIBUTION.md),
[../../TECHNICAL.md](../../TECHNICAL.md) (section 13, versioning),
[../../sources/SOURCE-POLICY.md](../../sources/SOURCE-POLICY.md).

Before any structural change, read `PRODUCT-SCOPE.md`, `ARCHITECTURE.md`,
`TECHNICAL.md`, and `DESIGN.md`, as `AGENTS.md` requires.

## Add a skill

1. Check [skill-catalog.md](skill-catalog.md) and the boundary documents. The
   new outcome must not overlap an existing skill.
2. Copy `templates/skill/` to `skills/odoo-<outcome>/`, and set `name` to the
   directory name.
3. Write the description as "Use this skill when …", followed by "Do not use it for …".
4. Add `references/odoo-<major>-<edition>.md` for each cell you claim, plus an output template in `assets/`.
5. Add `evals/trigger/odoo-<outcome>.json` with at least 8 positive and 8 near-miss negative prompts.
6. Add at least one outcome case per claimed cell to `evals/outcome/cases.yaml`.
7. Add the skill to a grouping in `skills.sh.json` and to the relevant `bundles/*.yaml`.
8. Add a row to [skill-catalog.md](skill-catalog.md) and to the README skill table.
9. Update `MANIFEST.md` counts and `CHANGELOG.md`.
10. Run all four `make` targets.

## Change an existing skill

1. Reproduce the problem with an evaluation case first.
2. Classify the defect: trigger, workflow, reference, output, or safety.
3. Make the smallest coherent change.
4. Bump `metadata.version` when behavior changes. A patch is wording or
   references. A minor is additive workflow or version support. A major changes
   the boundary, the output contract, or safety behavior.
5. Update the changelog. Keep bug fixes, behavior changes, reference
   updates, evaluation changes, version support, and formatting in separate changes.

## Add an Odoo version or edition cell

Example: Odoo 21.0 Community.

1. Register the sources, such as the Odoo 21 source tree and docs, in `sources/SOURCES.yaml` (see the next section).
2. Add a fixture `evals/fixtures/version-matrix-21-community/` whose README
   records fingerprints, for example SHA-256 of `release.py` and selected
   manifests, and what was observed.
3. Add the cell to `sources/VERSION-MATRIX.yaml` with `version: '21.0'`,
   `edition: community`, a status, `source_ids`, `fixture`, and `notes`. Start at
   `verified-experimental`. `stable` needs executed evidence and a named human review.
4. For each skill that should claim it:
   - add `"21.0"` to `metadata.odoo.versions`, with `editions_by_version` if needed;
   - add `references/odoo-21-community.md` and load it conditionally from `SKILL.md`;
   - add an outcome case with `odoo_version: '21.0'`.
   Steps 1 to 4 are what `make validate` enforces. The reference filename is
   built from the major version and the edition, for example `odoo-21-community.md`.
5. Not enforced, but required: record the evidence in `docs/VERSION-EVIDENCE.md`. Update the README status and the changelog.
6. For mutation support, change the shared contract in `odoo-rust-mcp-agent`,
   and `OPTIONAL_CELL_GROUPS` in `scripts/validate_mutation_capabilities.py`.
   Version claims for skills do not grant mutation support.

## Register a source

1. Add a record to `sources/SOURCES.yaml` with `id`, `name`, `url` (which must be `https://`),
   `authority_tier` (1 to 8), `usage`, `license_status`, `odoo_versions`, `notes`, and `last_reviewed`.
2. Follow the clean-room policy. Paraphrase verified facts and never copy
   third-party text or scripts until the license is reviewed. Never redistribute Enterprise source.
3. `make validate` checks the record against `schemas/source-registry.schema.json`.

## Update a reference

1. Verify each fact against the target-version source or an executed run. Say
   which, and keep "present in source" separate from "observed at runtime".
2. Keep the file reachable from `SKILL.md`. An unmentioned file only warns, but it will never load.
3. Do not link outside the skill directory. Skills install one at a time.

## Release

1. Freeze scope, then run `make validate`, `make test`, and `make package-check`.
2. Review source registry dates and license status.
3. Confirm skill versions, the plugin version in `.claude-plugin/plugin.json`, and the changelog.
4. Tag and publish release notes listing sources, tested versions, untested editions, and security-relevant changes.
5. Test tap installation from a clean Hermes profile, and test bundles separately.

## Finish every change with the completion report

`AGENTS.md` requires it. List:

- skills changed;
- behavior changed;
- source changes;
- version support changes;
- safety impact;
- evaluations added or changed;
- commands run, with results;
- unresolved risks.
