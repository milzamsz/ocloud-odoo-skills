# Contributing

## 1. Contribution types

- new skill proposal;
- skill correction;
- Odoo version reference update;
- trigger evaluation improvement;
- outcome fixture or test;
- source registry update;
- security improvement;
- documentation correction.

## 2. Before starting

Open or create an issue containing:

- problem;
- intended user outcome;
- why an existing skill cannot handle it;
- target Odoo versions and editions;
- risk class;
- proposed sources;
- evaluation approach.

## 3. Skill proposal checklist

A proposal should answer:

1. What exact task should activate the skill?
2. What nearby tasks should not activate it?
3. What required evidence must the agent inspect?
4. Which decisions are flexible and which are prescriptive?
5. What output proves success?
6. What could damage a repository, database, or business process?
7. How will trigger and outcome quality be measured?

## 4. Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
make validate
make test
```

## 5. Authoring

Start from `templates/skill/`.

Do not copy a public skill and rename it. Extract the useful concept, verify it against authoritative sources, write original instructions, and record provenance.

## 6. Pull request requirements

A pull request must include:

- concise problem and outcome;
- files and skills affected;
- target versions and editions;
- source records;
- risk assessment;
- trigger evaluation changes;
- outcome evaluation changes;
- validation output;
- screenshots only when they convey meaningful UI or report behavior.

## 7. Review gates

| Change | Required review |
|---|---|
| Documentation only | Maintainer. |
| Skill workflow | Skill maintainer and Odoo reviewer. |
| Executable script | Odoo reviewer and security reviewer. |
| Accounting or Indonesian tax | Functional/accounting reviewer. |
| New version support | Odoo reviewer plus regression evidence. |
| Controlled-write guidance | Security reviewer and product owner. |
| Third-party derived material | License/provenance review. |

## 8. Commit conventions

Examples:

```text
feat(skill): add context discovery output contract
fix(security): reject broad admin ACL recommendation
docs(source): register Odoo 18 security reference
test(trigger): add near-miss controller review cases
refactor(eval): split trigger and outcome runners
```

## 9. Deprecation

Do not silently remove a stable skill. Mark it deprecated, identify the replacement, provide migration notes, and remove it only after a documented release window.

## 10. Code of conduct

Be direct about defects and respectful toward contributors. Review the work, not the person's alleged relationship with YAML.
