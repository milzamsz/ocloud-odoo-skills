---
name: odoo-website-portal
description: Use this skill when designing or reviewing Odoo website pages, portal document views, public or portal controller routes, QWeb frontend templates, or public asset bundles, including which access check, template anchor, and JavaScript layer the target version requires. Do not use it for backend addon implementation, a full security audit, eCommerce pricing or tax policy, or theme styling alone.
license: MIT
compatibility: Hermes Agent and Agent Skills compatible clients with read access to the target Odoo source tree. Verified for Odoo 17.0, 18.0, 19.0, and 20.0 Community and Enterprise from local source inspection; runtime behavior still requires target-specific tests.
metadata:
  version: "0.1.1"
  author: OCloud
  status: experimental
  risk: advisory
  odoo:
    versions: ["17.0", "18.0", "19.0", "20.0"]
    editions: [community, enterprise]
  hermes:
    tags: [odoo, website, portal, controllers, qweb, frontend]
---

# Odoo Website and Portal

## Purpose

Produce a bounded design for one website or portal outcome: which routes, access checks, templates, records, and JavaScript layer it needs on the confirmed Odoo version, with every claim tied to target source.

## Use when

- a customer or public user must see or act on a business document outside the backend;
- a website page, menu, snippet, or form must be added or changed by code rather than the editor;
- a public or portal route exists and its access, template inheritance, or asset wiring must be reviewed;
- a port between Odoo versions touches public JavaScript or portal templates.

## Do not use when

- the work is backend models, views, or ACLs only (use `odoo-addon-development`);
- the request is a security verdict on an existing route (use `odoo-security-audit`; this skill only flags boundaries);
- the request is website editor styling, theme choice, or copywriting with no code;
- eCommerce pricing, tax, payment, or delivery policy is the question (use the functional skills).

## Required inputs

- Confirmed Odoo version and edition from `odoo-context-discovery`.
- The business document or page, the audience (public, portal, internal), and the actions allowed.
- Whether `website` or only `portal` is installed; whether `website_sale` is involved.

## Workflow

1. Confirm the audience and the exposure boundary: public (`auth="public"`), portal (`auth="user"` plus portal group), or internal. Record it before any template work.
2. Choose the mechanism in this order: existing portal page or standard website feature; website editor configuration; an OCA website or portal module; a custom controller plus QWeb template. State why earlier options were rejected.
3. For portal documents, require the target model to use `portal.mixin` and the controller to go through the portal access helper with an access token; never filter by `partner_id` alone. Read `references/portal-access.md`.
4. For website pages, decide between a `website.page` record, a QWeb template with `website=True` on the route, or a snippet; list the menu, SEO, multi-website, and language consequences. Read `references/website-patterns.md`.
5. Anchor template inheritance on stable `xpath` targets in the target version's template, not on editor-generated structure.
6. Pick the JavaScript layer from the version reference: legacy public widgets on 17 and 18, `Interaction` classes from 19. Do not mix layers in one module.
7. Hand security conclusions to `odoo-security-audit`, implementation to `odoo-addon-development`, and tests to `odoo-testing` with the access matrix from the output.

## Safety rules

- Read-only source analysis; never call routes, edit live pages, or publish on a live site to confirm a design.
- A visibility condition in a template is not an authorization check; the server-side check must exist independently.
- Portal `sudo()` is allowed only after the access helper has proven the caller may see the record; bind elevated recordsets to `_sudo` names.
- Do not copy upstream templates or JavaScript into the design; cite file paths and line references only.

## Required output

Copy `assets/website-portal-design.md`. It must contain the exposure boundary, chosen mechanism with rejected alternatives, route table with auth and CSRF settings, access check per route, template anchors with `path:line` citations, asset bundle and JavaScript layer, an access test matrix (anonymous, other portal user, own portal user, cross-company), and unknowns.

## Verification

- Every route in the design has an explicit auth value and a server-side access check or a stated reason none is needed.
- Every template anchor and JavaScript API cites the target version source.
- Version-sensitive claims use exactly one matching version reference.
- Items the design did not verify are listed, not omitted.

## References to load

Read exactly one `references/odoo-{17,18,19,20}-{community,enterprise}.md` file after the target version and edition are confirmed.

- Read `references/portal-access.md` when a portal user must see or act on a business document.
- Read `references/website-patterns.md` when adding pages, menus, snippets, or website-scoped routes.

## Failure and escalation

Stop when the version is unconfirmed, when the target model has no portal mixin and the user wants portal access without adding one, or when the only way to meet the request bypasses the access helper. Escalate suspected existing exposure to `odoo-security-audit`.
