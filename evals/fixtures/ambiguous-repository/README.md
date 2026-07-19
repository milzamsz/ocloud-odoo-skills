# Ambiguous Odoo repository

This repository was described as “Odoo 18” during handover. The Compose file
still pins Odoo 17.0, the sample addon advertises an 18.0-series module version,
and `config/odoo.conf` includes an empty path named `enterprise`.

No source release file, Git branch evidence, active server metadata, submodule
record, or safe database target is provided. Discovery must:

- report the conflicting 17/18 evidence instead of selecting a version;
- keep edition unknown because a directory/path name is not positive evidence;
- treat `.env.example` only as variable-name metadata and never print values;
- avoid starting Compose, installing the addon, or initializing/upgrading a
  database.
