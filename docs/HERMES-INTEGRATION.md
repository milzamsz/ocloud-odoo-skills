# Hermes Integration

## 1. Supported integration modes

### 1.1 External skill directory

Recommended for active OCloud development.

```yaml
skills:
  external_dirs:
    - ${OCLOUD_ODOO_SKILLS}/skills
```

Advantages:

- edit in the normal Git repository;
- share the same skill checkout with compatible tools;
- no repeated installation during development.

Risk:

Hermes may modify a writable external skill when agent-managed skill actions are enabled. Use read-only filesystem permissions, branch protection, or a separate development profile when changes require review.

### 1.2 Custom skill tap

Recommended for versioned distribution.

```bash
hermes skills tap add ocloudpro/ocloud-odoo-skills
hermes skills search odoo
hermes skills install ocloudpro/ocloud-odoo-skills/odoo-security-audit
```

A tap uses the repository `skills/` path by default. Each immediate subdirectory must contain `SKILL.md`.

### 1.3 Direct installation

```bash
hermes skills install ocloudpro/ocloud-odoo-skills/skills/odoo-context-discovery
```

Use direct installation for a single skill without subscribing to the complete tap.

## 2. Bundles

Hermes bundles live under:

```text
~/.hermes/skill-bundles/
```

Install by copying or symlinking files from `bundles/`.

```bash
mkdir -p ~/.hermes/skill-bundles
ln -s "$OCLOUD_ODOO_SKILLS/bundles/odoo-dev.yaml" \
  ~/.hermes/skill-bundles/odoo-dev.yaml
hermes bundles reload
```

A bundle does not install skills. Missing members are skipped by Hermes, so packaging checks must verify the complete intended set before release.

## 3. Recommended profiles

### `odoo-dev`

- writable project repository;
- OCloud skills read-only;
- terminal and test tools;
- no production credentials;
- plugin configured for development or sandbox Odoo only.

### `odoo-review`

- repositories mounted read-only where possible;
- no Odoo write tools;
- review and security bundles;
- output stored outside target source if strict immutability is required.

### `odoo-ops`

- tightly controlled plugin and MCP tools;
- explicit approval gates;
- audit logs;
- production access only when operationally justified;
- no automatic skill self-modification.

## 4. Skill write controls

For shared or production profiles:

- enable Hermes skill write approval;
- keep the shared checkout read-only;
- do not let session learning commit directly to the stable branch;
- capture suggested changes as patches for review;
- run evaluation before merging learned procedures.

## 5. Plugin relationship

Use a Hermes plugin when the capability requires:

- authentication;
- precise structured execution;
- custom tool schema;
- hooks;
- approval enforcement;
- binary or streaming behavior;
- robust error mapping.

Use a skill when the capability is primarily:

- procedure;
- decision framework;
- source selection;
- review checklist;
- output contract;
- shell workflow using existing tools.

## 6. Odoo MCP relationship

The MCP agent should expose narrow, typed operations such as:

- discover server version and installed modules;
- inspect model metadata;
- query records read-only;
- create or update controlled draft records;
- execute named workflow actions;
- return audit evidence.

The skill explains when and why to use these operations. It does not duplicate their implementation.

## 7. Installation verification

```bash
hermes skills tap list
hermes skills search odoo
hermes bundles list
```

Then test:

```text
/odoo-context-discovery inspect this repository before changing the addon
/odoo-review review the target module and separate blockers from refactoring
```

## 8. Distribution checklist

- all referenced files are inside the skill directory;
- no required resource is reachable only through a repository-wide relative path;
- bundle members match installed names;
- `skills.sh.json` categories are valid;
- public tap contains no private sources or customer data;
- changelog and version metadata agree.
