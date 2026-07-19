# Private Skill Overlays

Client- or organization-specific procedures belong in a separate,
access-controlled repository loaded after the public OCloud skill directory.

## Rules

- Never store credentials, tokens, private URLs, client records, tax
  identifiers, database dumps, or Enterprise source.
- An overlay may narrow allowed tools, companies, fields, thresholds, and
  approval roles. It may not widen generated MCP policy.
- Keep authentication and authorization in plugin/MCP/Odoo controls, not prose.
- Pin the public skills release and record the overlay's compatible version.
- Run the public repository gates plus private trigger/outcome evaluations.

## Layout

Copy `templates/overlay/` into a private repository and replace only the marked
organization fields. Load both repositories through Hermes external skill
directories; keep the private checkout read-only in operational profiles.

The included example targets synthetic OCloud staging and contains no client
data.
