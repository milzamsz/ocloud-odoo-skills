# Evidence Priority

Prefer pinned runtime or source evidence over names and assumptions. When
version evidence conflicts, report each source and do not execute
version-sensitive commands until resolved.

Edition requires positive evidence. Enterprise business terminology is not positive evidence.

## Version decision record

For every material claim record:

- value and evidence label;
- file/path or read-only instance response;
- whether it describes source, intended runtime, or the active database;
- conflicts and the evidence needed to resolve them.

Use this order:

1. active read-only server version when the task targets that instance;
2. pinned runtime image or package for repository deployment intent;
3. Odoo source release data or pinned commit;
4. project branch;
5. addon manifest/code compatibility;
6. user statement;
7. inference, kept unresolved.

An active database, repository source tree, and deploy target can legitimately
have different versions. Do not collapse them into one field when they differ.

## Edition decision

Confirm Enterprise only from positive evidence such as:

- accessible Enterprise source/submodule aligned to the target version;
- a target module dependency on an Enterprise technical module;
- deployment or project configuration explicitly selecting Enterprise;
- read-only installed-module metadata paired with a confirmed edition marker.

An empty directory named `enterprise`, an Enterprise-like theme name, barcode,
accounting, Studio terminology, or a user requirement is insufficient alone.
Community remains a positive project claim only when supported by controlling
instructions or a Community-only source/runtime layout; otherwise use
`unknown`.

## Conflict behavior

- Preserve each conflicting fact with its label.
- Mark version-sensitive commands as prohibited until resolved.
- Ask for the narrowest missing evidence: image digest, source release file,
  submodule state, or read-only server metadata.
- Never resolve conflict by starting services, initializing a database, or
  exposing environment values during discovery.
