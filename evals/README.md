# Evaluation Suite

- `trigger/`: prompt datasets for skill activation.
- `outcome/`: task scenarios with required findings and prohibited behavior.
- `fixtures/`: minimal OCloud-authored repositories or files used by outcome tests.
- `results/`: generated evaluation results; avoid committing private data.

Run `make validate` to enforce at least eight positive and eight negative cases per trigger
set, outcome coverage for every skill, and non-empty `required_findings` and
`prohibited_actions`.

Use [MANUAL-EVALUATION.md](MANUAL-EVALUATION.md) to record reproducible Claude or Codex
runs under the gitignored `results/` directory. Model invocation remains adapter-specific;
do not embed provider credentials in this repository.
