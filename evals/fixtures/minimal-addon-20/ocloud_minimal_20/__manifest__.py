{
    "name": "OCloud Minimal 20",
    "version": "20.0.1.0.0",
    "category": "Technical",
    "summary": "Clean-room fixture for Odoo 20 addon and test evaluation",
    # MIT content; Odoo 20 rejects "MIT" on module update, so use the accepted selection value.
    "license": "Other OSI approved licence",
    "author": "OCloud",
    "depends": ["base"],
    "data": [
        "security/ir.access.csv",
        "views/minimal_item_views.xml",
    ],
    "installable": True,
    "application": False,
}
