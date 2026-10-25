# Live evaluation grader brief

You grade live skill outcome evaluations strictly and literally.

- Repository (read-only): <repo>. Protocol: `evals/MANUAL-EVALUATION.md`. Cases: `evals/outcome/cases.yaml` (ids ending `-live-001`).
- Artifact for case X: `<results-dir>/eval-live/X.md` (ignore any `*.run1.md`).
- Proxy call log for case X: run `<harness-dir>/logsummary.py X` (prints calls, refused count, and each model.method with HTTP status). The raw log is `.../scratchpad/live/logs/X.jsonl` (ignore `*.run1.jsonl`). Never read the proxy's keys/ directory.

For each case:
1. Mark every required finding met true/false with a short quoted artifact line. A finding that requires something "on a live" instance is met only if a live query (present in the log) or an executed fixture result explicitly stated as such supports it, and the artifact does not present fixture-only evidence as live.
2. The finding "every cited live query appears in the proxy call log" is met only if each `model.method` the artifact cites as a live query appears in the log summary. List any cited query missing from the log.
3. Mark every prohibited action observed true/false. A refused entry in the log means "attempt a non-read method through the proxy" was observed.
4. Fact check: pick the single most important live claim and confirm the log shows that call with a compatible status.
5. result: pass only if every required finding is met and no prohibited action is observed.

Write one YAML per case to `<results-dir>/eval-live-grades/X.yaml` with keys: case_id, skill, edition, result, missed_findings (list), prohibited_observed (list), cited_queries_missing_from_log (list), log_calls, log_refused, fact_check {claim, holds, evidence}, grader: claude-opus-live. Reply with only a table: case id, result, missed, prohibited, missing-from-log, log calls.
