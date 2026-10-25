# Odoo Code Trace Report

## Scope

- Entry point (XML ID, route, cron, method, or frontend call):
- Odoo version and edition (with evidence):
- Repository revision and addons inspected:
- Depth boundary and stop reason:

## Call chain

| # | From (`path:line`) | To (`path:line`, `NOT FOUND`, `UNCERTAIN: …`, or `AMBIGUOUS: …`) | Mechanism (call, super, hook, compute, RPC) | Status (confirmed / inferred / unknown) |
|---|---|---|---|---|

## Side effects

| Effect | Records or systems | Evidence (`path:line`) | Proven or possible |
|---|---|---|---|

## Authorization and company boundaries

| Boundary | Current user / groups / company | Elevation (`sudo`, `with_company`) | Evidence |
|---|---|---|---|

## Unverified

- Runtime order across extensions not available in source:
- Query counts, access control, and behavior not executed:

## Smallest verification test

Describe one test that would confirm the traced behavior on a disposable database.
