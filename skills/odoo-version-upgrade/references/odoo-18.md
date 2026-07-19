# Odoo 18.0 Migration Reference

Stable Community target for the clean-room 17 → 18 fixture:

- target code defines `external_reference` and no longer depends on the legacy
  field name;
- the renamed XML ID must address the existing view record rather than create
  a duplicate view;
- Odoo 18 view architecture uses `<list>` and `list,form` in the evaluated
  addon fixture;
- registry startup is intermediate evidence only; installation, focused tests,
  preserved field/XML-ID mappings, and relevant functional reconciliation must
  all pass.

Use the exact Odoo 18 Community source and fixture evidence. Enterprise modules
remain advisory and require licensed source inspection.
