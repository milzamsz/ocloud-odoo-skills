# Performance Review

## Query shape

- Flag ORM searches, counts, reads, or SQL executed once per record. Prefer one
  grouped query such as `_read_group`, a bulk search followed by in-memory
  mapping, or an existing aggregate field when semantics match.
- Check whether recordset operations preserve prefetching. Re-browsing IDs,
  slicing recordsets repeatedly, or accessing fields through singleton helper
  calls can defeat batching.
- Treat a query-in-loop finding as confirmed from static code; treat its
  production cost as unverified until data volume or query evidence is known.

## Compute and write amplification

- Verify `@api.depends` covers every stored input and relation used by the
  compute. Missing dependencies can produce stale values; overly broad
  dependencies can cause expensive recomputation.
- Look for writes inside compute loops, repeated recomputation, per-record
  create/write calls, and onchange logic incorrectly relied on for persisted
  invariants.

## Bounded work

- Review unbounded `search([])`, exports, reports, integrations, and scheduled
  jobs. Require explicit domains, limits or bounded batches, restart behavior,
  and idempotency where volume can grow.
- Recommend indexes only for observed or strongly evidenced query patterns.
  Include write/storage cost and verify with representative data rather than
  asserting that an index is automatically required.

## Verification

Define the smallest evidence that distinguishes the remediation: query-count
assertion, bounded fixture, profiler trace, or representative timing. Do not
run load tests against a live production database during review.
