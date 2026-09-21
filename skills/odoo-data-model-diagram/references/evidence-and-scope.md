# Evidence and Scope

## Bounded discovery

Start from explicit root models. Use `odoo_list_models` only to resolve an
unknown root name, then request `odoo_get_model_metadata` for roots and their
direct relation targets. Do not enumerate every accessible model. Stop at 30
models and split by bounded context unless the requester explicitly expands it.

## Source evidence

Inspect the target addon and its dependencies for `_name`, `_inherit`,
`_inherits`, `_auto`, `_table`, fields, `comodel_name`, `inverse_name`,
`relation`, compute/store/related behavior, constraints, and module ownership.
Source may describe intended customizations that are not installed.

## Live evidence

`odoo_get_model_metadata` supplies the model currently registered by the
selected instance. It is metadata, not physical database introspection. Its
available field attributes vary by Odoo version and MCP protocol, so missing
attributes remain Unknown rather than false.

## Merge rule

When both sources are available, use live metadata for the current model and
field set, then attach source structural facts to matching items. Keep
source-only and live-only items in the report. A conflicting type, relation, or
field presence is an unresolved drift finding, not a winner selected by guess.

## Drift confirmation

An absent field is not evidence that a module is missing. Confirm a suspected
missing dependency with positive controls: sibling fields from the same addon
that must exist if it is installed. Report a missing dependency only when those
controls pass and the target field is absent across every model the dependency
extends.

A mixin declared on `models.AbstractModel` creates no `ir.model` row, so its
absence from `odoo_list_models` proves nothing. Check the fields it injects into
concrete models instead of the mixin itself.

When the installed module list cannot be read, pin the deployed revision with
independent markers: the wording of a field `string`/`help`, and the presence of
fields introduced by a specific commit. Two agreeing markers support a revision
finding; a single marker does not.

## Field profiles

The standard profile includes `id`, a display/name field, requested and custom
fields, relational fields, required fields, `state`, `active`, `company_id`,
`currency_id`, and create/write audit fields. Include all returned fields only
when the requester explicitly asks for full detail.
