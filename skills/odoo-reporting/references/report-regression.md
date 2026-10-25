# Report Rendering Regression

Use when an existing report must keep rendering correctly after a module
change, OCA port, or Odoo major-version upgrade.

## Protocol

1. Freeze a baseline: render the report on the source revision for a fixed
   set of records, and record Odoo version, module revisions, wkhtmltopdf or
   browser renderer version, paper format, language, and company.
2. Render the same records on the target revision with the same inputs.
3. Compare rendered output, not PDF bytes. Byte equality is neither required
   nor sufficient; renderer versions change bytes without changing content.
4. Classify every difference as one of:
   - intended (the change was requested; cite the requirement);
   - renderer noise (fonts, metadata, pagination jitter; cite the renderer);
   - regression (content, totals, layout, translation, or access changed).
5. Treat an access difference (a portal or public user sees more or less
   than before) as a security regression, not a layout difference.
6. Record the evidence level reached: rendered-output comparison, structural
   assertion in a test, or manual review only.

## Rules

- Do not "fix" differences with arbitrary CSS until the cause is classified.
- Do not invent a per-version difference list for symmetry; record only
  differences observed on the exact source and target.
- Keep the baseline artifacts out of the repository when they contain
  business data.
