# Release and Distribution

## 1. Release channels

- **Experimental**: development branches or prerelease tags.
- **Stable**: versioned GitHub release and default tap branch.
- **Private overlay**: separate access-controlled repository for OCloud or client-specific procedures.

## 2. Release contents

A release contains:

- skill directories and referenced resources;
- bundles;
- source registry and review dates;
- schemas and validation tools;
- changelog;
- evaluation summary;
- known limitations.

## 3. Semantic versioning

Repository major version changes when skill contracts or distribution expectations break. Individual skill versions remain in metadata for finer tracking.

## 4. Tap publishing

The repository root contains `skills/`. Hermes discovers each immediate skill subdirectory and its `SKILL.md`.

Before publishing:

```bash
make validate
make test
make package-check
```

## 5. Clean-profile test

Create or use a disposable Hermes profile without previously installed OCloud skills. Add the tap, install each Phase 1 skill, verify resource inclusion, and invoke every bundle.

The exact experimental checklist and unresolved publication gates are recorded
in [EXPERIMENTAL-RELEASE-0.5.0.md](EXPERIMENTAL-RELEASE-0.5.0.md).

## 6. Provenance

Release notes must list:

- reviewed official sources;
- community sources that materially influenced changes;
- Odoo versions tested;
- untested editions or deployment modes;
- security-relevant changes.

## 7. Rollback

If a release degrades behavior:

- pin the previous release or commit;
- remove or deprecate the affected skill from the tap branch;
- publish an advisory;
- add a regression case before re-release.
