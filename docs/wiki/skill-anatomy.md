# Skill anatomy

What a skill directory contains and exactly what the validator enforces.
Source of truth: [../../scripts/validate_repository.py](../../scripts/validate_repository.py),
[../../scripts/package_check.py](../../scripts/package_check.py),
[../SKILL-AUTHORING-STANDARD.md](../SKILL-AUTHORING-STANDARD.md),
[../../DESIGN.md](../../DESIGN.md).

## Layout

```text
skills/odoo-<outcome>/
├── SKILL.md                      # frontmatter + concise procedure
├── references/                   # loaded on demand, named in SKILL.md
│   ├── odoo-<major>-<edition>.md # one per claimed cell, e.g. odoo-20-enterprise.md
│   └── <topic>.md
├── assets/                       # output templates, e.g. report or packet skeletons
└── scripts/                      # optional deterministic helpers, with tests in tests/
```

Start from [../../templates/skill/SKILL.md](../../templates/skill/SKILL.md).

## Frontmatter

```yaml
---
name: odoo-example-outcome          # lowercase-hyphen, equals the directory name
description: Use this skill when …  # what and when, plus "Do not use it for …"
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients. …
metadata:
  version: "0.1.0"
  author: OCloud
  status: experimental              # draft | experimental | stable | deprecated
  risk: advisory                    # read-only | advisory | controlled-write | destructive
  odoo:
    versions: ["18.0", "20.0"]
    editions: [community, enterprise]
    editions_by_version:            # optional; narrows versions × editions
      "18.0": [community, enterprise]
      "20.0": [community]
  hermes:
    tags: [odoo, example]
---
```

Every `(version, edition)` pair this yields is a claimed cell. Leave `odoo`
out entirely when support is decided elsewhere, as `odoo-live-mutation` does.

## Body sections

Use the standard order from the template: Purpose, Use when, Do not use when,
Required inputs, Preconditions, Workflow, Decision rules, Safety rules,
Required output, Verification, References to load, Failure and escalation.
Keep mandatory instructions short and push detail into `references/`.

## Validator rules

Errors fail CI. Warnings print but pass.

| Check | Level |
|---|---|
| `SKILL.md` exists with YAML frontmatter | error |
| `name` matches `^[a-z0-9]+(-[a-z0-9]+)*$` and equals the directory | error |
| `description` is a non-blank string, at most 1024 characters, and starts with exactly `Use this skill when` (case-sensitive). "Do not use it for …" is a convention, not checked | error |
| `metadata.status` and `metadata.risk` in the allowed sets above | error |
| Markdown links resolve and stay inside the skill directory | error |
| Backtick paths under `references/`, `assets/`, `scripts/` exist; `{a,b}` braces are expanded | error |
| Secret literals (password, token, AWS key, private key block) in any text file | error |
| Every claimed cell has evidence (see [version-matrix.md](version-matrix.md)) | error |
| A file in `references/` or `assets/` that `SKILL.md` never mentions | warning |
| A repository path such as `evals/…` or `docs/…` inside the skill, which breaks single-skill installs | warning |
| Body over 500 lines or 7000 words | warning |
| Dangerous shell or SQL pattern in `SKILL.md` | warning |
| No `evals/trigger/<name>.json` | warning in validate, error in package-check |

`make package-check` also requires that `skills.sh.json` lists exactly the
skills in `skills/` and that bundle members exist.

## Writing rules that matter most

- One primary outcome per skill. Check [skill-catalog.md](skill-catalog.md)
  for neighbours before adding scope.
- The description decides activation. Name both what and when, and say what
  the skill is not for, so near-miss prompts route elsewhere.
- Load version references conditionally: "load `references/odoo-20-community.md`
  only after context discovery confirms 20.0 Community".
- Mark assumptions and unknowns. Source presence is not runtime proof.
- Scripts validate inputs and paths, avoid shell construction, and get tests.
