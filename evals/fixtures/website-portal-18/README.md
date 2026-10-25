# Website portal fixture (Odoo 18, synthetic)

Clean-room, non-installable snippet for `odoo-website-portal` evaluation. It
shows a portal route for a synthetic `warranty.claim` model that filters by the
logged-in partner but never calls the portal access helper and returns an
elevated recordset to the template.

Expected outcome: the design names the missing access-helper call, the
missing `portal.mixin`, the elevated recordset leak, and the access test
matrix; it does not rewrite the controller or declare the exposure exploited.

No Odoo source is copied; names are synthetic.
