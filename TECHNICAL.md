# Technical Specification

## 1. Technology choices

| Concern | Choice | Rationale |
|---|---|---|
| Skill format | Agent Skills `SKILL.md` | Portable and supported by Hermes. |
| Primary runtime | Hermes Agent | Required target and bundle/tap support. |
| Documentation | Markdown | Native to skills and Git workflows. |
| Metadata | YAML frontmatter | Required by skill specification. |
| Bundle format | YAML | Native Hermes bundle schema. |
| Source registry | YAML | Human-readable structured governance. |
| Evaluation records | JSON and YAML | JSON for trigger cases; YAML for outcome scenarios. |
| Validation scripts | Python 3.11+ | Portable, readable, and suitable for CI. |
| Unit tests | pytest | Common and expressive. |
| Schema validation | jsonschema | Enforce evaluation and registry structure. |
| YAML parsing | PyYAML | Reliable frontmatter and configuration parsing. |
| Formatting/linting | Ruff | Fast Python lint and formatting. |
| CI | GitHub Actions | Natural for a GitHub skill tap. |

## 2. Agent Skills requirements

Every skill directory must contain `SKILL.md` with YAML frontmatter.

Required metadata:

```yaml
---
name: odoo-context-discovery
description: Use this skill when an Odoo task requires discovering the exact version, edition, repository layout, addons paths, module dependencies, runtime, database risk, or project instructions before analysis, implementation, review, testing, or migration.
---
```

Repository rules:

- `name` must match its parent directory.
- `name` uses lowercase letters, digits, and single hyphens.
- `description` must explain what and when.
- Core instructions should remain below 5,000 tokens and preferably below 500 lines.
- Supporting files are referenced with relative paths.
- Avoid chains of references deeper than one level from `SKILL.md`.

## 3. OCloud metadata convention

Optional portable fields may be placed under `metadata`:

```yaml
metadata:
  version: "0.1.0"
  author: "OCloud"
  status: experimental
  odoo:
    versions: ["18.0"]
    editions: [community, enterprise]
  risk: advisory
  hermes:
    tags: [odoo, erp, discovery]
```

Do not rely on custom metadata for safety enforcement. Safety requirements must also appear in the skill body and, for executable tools, in the plugin or MCP implementation.

## 4. Standard skill layout

```text
skill-name/
├── SKILL.md
├── references/
│   ├── decision-table.md
│   └── odoo-18.md
├── scripts/
│   └── inspect.py
└── assets/
    └── output-template.yaml
```

Not every skill needs every directory. Empty ceremonial directories should not be added to released skills.

## 5. `SKILL.md` content contract

Recommended sections:

1. Purpose
2. Use when
3. Do not use when
4. Required inputs
5. Preconditions
6. Workflow
7. Decision rules
8. Safety rules
9. Required output
10. Verification
11. Resource loading instructions
12. Failure and escalation behavior

### 5.1 Required language

Use imperative and operational language. Avoid persona inflation such as “You are the world's best Odoo expert.” Expertise is demonstrated by decisions, not by YAML cosplay.

### 5.2 Output contracts

Every skill defines its expected result. Example:

```yaml
context_summary:
  odoo_version: "18.0"
  edition: "enterprise"
  evidence: []
  repository_root: "."
  target_modules: []
  risks: []
  unknowns: []
  permitted_next_actions: []
```

## 6. Source hierarchy

The skill must use evidence in this order:

1. Current user requirement and approved project documents.
2. Repository instructions such as `AGENTS.md`, `CLAUDE.md`, `README.md`, and contribution guides.
3. Target Odoo and addon source code.
4. Official Odoo documentation for the exact target version.
5. OCA repository and maintainer documentation.
6. OCloud curated references.
7. Reviewed community sources.
8. General model knowledge.

When sources conflict, document the conflict and prefer the higher authority.

## 7. Odoo context discovery protocol

### 7.1 Repository inspection

Inspect, when available:

- repository root markers;
- `AGENTS.md`, `README.md`, and project docs;
- `odoo.conf`, Docker Compose, Dockerfiles, devcontainer, and deployment manifests;
- addon manifests;
- Git branch or version pins;
- Odoo core and Enterprise source paths;
- OCA submodules or aggregate repositories;
- test and lint tooling;
- migration directories;
- environment examples without exposing secret values.

### 7.2 Version evidence priority

1. Explicit project configuration or pinned image.
2. Odoo release information in source.
3. branch name or Git commit.
4. addon manifest compatibility.
5. user statement.
6. inference, clearly labeled as unresolved.

### 7.3 Edition evidence

Enterprise is confirmed only when Enterprise source, Enterprise dependency, subscription deployment configuration, or explicit project evidence exists. Never infer Enterprise merely because Accounting is discussed.

## 8. Odoo development protocol

### 8.1 Design order

1. Standard feature.
2. Configuration.
3. Trusted OCA or vendor addon.
4. Native low-code.
5. Custom addon.
6. External service or middleware.

### 8.2 Required implementation areas

- manifest and dependency correctness;
- model inheritance strategy;
- data model and constraints;
- compute, inverse, onchange, and store behavior;
- access rights and record rules;
- multi-company isolation;
- views and stable inheritance selectors;
- data loading order;
- controllers and request security;
- reports and assets when relevant;
- tests;
- migration and uninstall impact;
- documentation.

### 8.3 Prohibited defaults

- modifying Odoo core;
- direct SQL without documented justification;
- blanket `sudo()`;
- public mutation methods without authorization validation;
- wildcard administrator ACLs;
- production database upgrade as first verification;
- broad speculative refactors unrelated to the requirement.

## 9. Script requirements

A bundled script must:

- have a single clear purpose;
- expose `--help`;
- validate arguments;
- avoid network access unless essential and documented;
- avoid secret output;
- default to read-only or dry-run where relevant;
- return non-zero on failure;
- print machine-readable output when consumed by another tool;
- include tests for meaningful logic;
- be reviewed for command injection and unsafe paths.

## 10. Validation commands

```bash
make validate
make test
make package-check
```

Expected checks:

- YAML frontmatter parsing;
- name-directory equality;
- required fields;
- description length;
- broken relative links;
- line and token budget warning;
- source references present;
- trigger file presence;
- bundle member resolution;
- secret patterns;
- dangerous command patterns;
- Python tests and lint.

## 11. Trigger evaluation

Each skill has approximately 16 to 24 realistic prompts split between:

- should trigger;
- should not trigger;
- near-miss negative cases;
- indirect intent cases;
- terse and detailed wording;
- version-specific wording;
- mixed tasks where the target need is embedded.

Evaluation should be repeated because model activation is probabilistic.

## 12. Outcome evaluation

Outcome cases define:

- fixture or repository snapshot;
- user request;
- skill set;
- required evidence;
- required findings;
- prohibited actions;
- expected artifact structure;
- executable checks;
- human review criteria.

## 13. Versioning

### 13.1 Skill version

Use semantic versioning:

- patch: wording, references, or evaluation fixes without changed contract;
- minor: additive workflow or version support;
- major: changed task boundary, output contract, or safety behavior.

### 13.2 Repository release

Repository releases may contain multiple skill versions. A changelog lists changes per skill.

## 14. CI pipeline

```mermaid
flowchart LR
    A[Pull Request] --> B[Validate structure]
    B --> C[Lint scripts]
    C --> D[Run unit tests]
    D --> E[Static safety scan]
    E --> F[Validate trigger datasets]
    F --> G[Package tap check]
    G --> H[Human Odoo review]
    H --> I[Merge]
```

## 15. Compatibility strategy

- Avoid Hermes-only metadata in mandatory workflows where portable text is sufficient.
- Place Hermes-specific distribution details under `metadata.hermes` and `bundles/`.
- Do not assume other agents support Hermes bundles.
- Use exact Odoo version references and explicitly state unvalidated versions.
