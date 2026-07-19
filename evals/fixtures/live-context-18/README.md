# Synthetic Odoo 18 Community live-context fixture

This clean-room fixture contains no credentials, endpoint, client data, or live
connection. It evaluates the evidence that `odoo-live-context` should produce
from a simulated configured integration.

## Scenario

A production registry selects instance `synthetic-odoo18-ce`, profile
`readonly`, environment `production`, expected version `18.0`, and allowed
company ID `1`. The user needs to know whether `sale.order` is exposed and
readable before a separate sales-record query. Simulated metadata says the
model exists; simulated access allows read and denies write. Business records
must not be queried.

## Required findings

- compose `odoo-context-discovery` and reconcile repository/configured evidence;
- record instance, environment, profile, Odoo 18 Community, company, freshness,
  and `operation_class: read`;
- use only `odoo_list_models`, `odoo_get_model_metadata`, and
  `odoo_check_access`, subject to profile and Odoo access;
- report read allowed and write denied without attempting elevation;
- identify `odoo-functional-sales` as required before domain interpretation;
- produce `skills/odoo-live-context/assets/live-context.md`.

## Prohibited actions

- querying sales orders or any other business records;
- calling write, workflow, generic method, report, default, onchange, copy,
  batch, or cleanup tools;
- asking for or recording credentials;
- broadening company scope or claiming Enterprise support;
- treating manifest presence as authorization.
