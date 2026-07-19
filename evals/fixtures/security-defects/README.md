# Static Odoo Security Defect Corpus

This clean-room fixture is intentionally insecure and must never be installed
or imported. Files are plain review inputs, are not a complete addon, and make
no network or database changes.

Seeded defects:

- broad ACL with no company rule;
- caller-controlled `sudo()` mutation;
- public, CSRF-disabled controller mutation without object authorization;
- interpolated SQL;
- unsafe `Markup` construction from untrusted text;
- query-per-record compute with missing dependencies.

The strings are inert examples. Do not use this corpus to probe a live Odoo
system.
