# OpenUpgrade Workflow

## Planning and analysis (read-only)

1. Pin source and target Odoo, Enterprise (when licensed), OCA, vendor, and
   custom revisions.
2. Inventory installed modules and map each to target coverage: migrated,
   native replacement, custom script, archive, or blocker.
3. Compare source/target models, fields, constraints, XML IDs, configuration,
   and semantics. An apparent rename needs evidence; matching labels are not
   enough.
4. Define pre-, schema/data-, and post-migration operations, assertions, and
   reconciliation evidence before execution.

## Execution boundary

Analysis does not authorize execution. Run OpenUpgrade only after explicit
approval on a disposable database and matching filestore copy, with a verified
backup and disabled outbound effects. Never use the sole database copy.

For authorized rehearsals:

- capture exact revisions, configuration, commands, logs, and run duration;
- fail loudly if expected source columns, XML IDs, or record counts differ;
- preserve stable external references with an explicit XML-ID rename mapping;
- preserve values during field renames before old schema is removed;
- make repeated trials disposable and migration steps idempotent where the
  framework expects reruns;
- separate compatibility/migration commits from feature changes.

Technical startup is only an intermediate checkpoint. Complete functional,
security, performance, inventory, and accounting reconciliation before a
go/no-go decision.

## Retry discipline for rehearsals

Observed from repeated multi-hop rehearsals; each rule prevents a failure mode
that has already cost a run.

- Restore from the clean SQL plus filestore backup before every retry. A
  partially migrated database hides which script actually failed.
- Keep project-specific upgrade scripts in a project-local directory and put
  that directory before the upstream OpenUpgrade scripts in the upgrade path.
  Never patch upstream Odoo or OpenUpgrade source in place.
- Fix only the first actionable traceback, then restore clean and rerun.
  Later tracebacks are usually consequences of the first.
- Before taking the post-hop backup verify: `base` is at the target version,
  no module is left in a pending state, every critical custom module is
  installed and upgraded, no stale views remain, the registry boots, the
  translated JSONB fields were audited, and a UI and RPC smoke test passed.
- Refresh the post-hop backup after any runtime fix made on the copy so the
  next hop starts from a known state.
- Record each hop's commands, revisions, duration, and blockers; a hop with
  no record cannot be reproduced.
