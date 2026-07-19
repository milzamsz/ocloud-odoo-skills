# Odoo 18 Community Reporting Notes

Verified baseline: Odoo 18 Community. Enterprise reporting and spreadsheet
features are not implied by this baseline.

- Standard Odoo reporting surfaces include list/search, graph and pivot views
  where supported, exports subject to access, and QWeb report actions for
  printable HTML/PDF documents.
- QWeb reports render with user, company, language, and context-sensitive data.
  Define paper format, localization, page behavior, and attachment rules
  explicitly; verify them against the target Odoo 18 source and installed
  addons.
- A report action or menu restriction does not replace model security. ORM
  reads must respect ACLs, record rules, allowed companies, and sensitive-field
  boundaries.
- Do not add elevated access to bypass missing rows. Determine whether absence
  is intended security, incorrect company context, or a data-definition defect.
- Avoid per-record searches in templates and report value preparation. Bound
  datasets, aggregate deliberately, prefetch or batch related data, and measure
  query count, render duration, memory, pages, and concurrent demand.
- Cached/attached reports need an invalidation and confidentiality policy;
  generated files may outlive the source record's visibility.
- For multi-currency totals, state company, rate source/date, rounding, and
  whether values are transactional or converted. For accounting, state posted
  versus draft treatment and reconciliation/tax assumptions.
- Native spreadsheet authoring, advanced accounting statements, and designer
  features may be edition/module-specific. Verify before recommending them;
  otherwise use a bounded export, reviewed OCA/vendor option, or external
  analytics boundary.

Relevant official source areas include `odoo/addons/base`, `odoo/addons/web`,
`odoo/addons/base/models/ir_actions_report.py`, and the target business addon's
views/reports. This reference does not replace source inspection.
