# Cross-repository mutation baseline

Frozen on 2026-07-20 before mutation-alignment edits. The commit and dirty-state
columns are the authoritative starting point; later generated artifacts must pin
back to these repositories or an explicitly reviewed successor.

| Repository | Commit / branch | Initial dirty state | Version |
|---|---|---|---|
| `ocloud-odoo-skills` | `fe2991d91d397cd886fcbcb6e2f97b0f95288b12` / `main` | clean | `0.1.0` dev tools |
| `odoo-rust-mcp` | `173608ce9409e86d926a3ec1c21f31c7187ec9e2` / `release/v0.5.3` | owner changes listed below | `0.5.2` runtime/UI/desktop manifests |
| `odoo-rust-mcp-agent` | `cce94be9fbe5644aeb4441d214daaa8c85ee36c9` / `main` | clean | `0.1.0` |
| `hermes-plugin-odoo` | `6f4145d3244ef9f4df9ba5898c1f5f229e8998fe` / `main` | clean | `0.1.0` |

## Preserved owner changes

The MCP repository already contained these unrelated changes. Alignment work must
not edit, stage, package, or remove them:

- modified `desktop/package.json`;
- modified `desktop/src-tauri/tauri.conf.json`;
- modified generated desktop binary
  `desktop/src-tauri/binaries/rust-mcp-x86_64-unknown-linux-gnu`;
- untracked `BASELINE.md`;
- untracked private updater material under `desktop/.tauri/`.

No private updater material was read or copied.

## Manifest pins

| Contract surface | Baseline SHA-256 |
|---|---|
| MCP `rust-mcp/config/tools.json` | `2a1bc376fbe46c5cb11012ca50813fe4a1bcff4346d7f372d184d535f674046b` |
| MCP `rust-mcp/config-defaults/tools.json` | `2a1bc376fbe46c5cb11012ca50813fe4a1bcff4346d7f372d184d535f674046b` |
| Agent staging manifest | `ba47e234c3617a8b0c776628c3588e15b4209d120f83c4be9340342ecd5b671f` |
| Agent production manifest | `e662f2c14dd911cb326537fa6d870a3ca11aa1732c30160bc8686ddc9447d12c` |
| Plugin `src/hermes_plugin_odoo/plugin.yaml` | `e432a58ebeae892c56e4a40430ef82a3c20363cc19e77c574dbc3b3d9acdf5a6` |
| Skills `bundles/odoo-live.yaml` | `23bd831450fb4587baf0193e748773530a8b534a485cd94370bf3fe1399f8e27` |
| Skills `sources/VERSION-MATRIX.yaml` | `c7b43c8493288f3e5153c8b81be8f0a9cce65bf90ebe60b38298cec4c9cda38f` |

## Starting support posture

- Five named capabilities have approved disposable Odoo 19 Community staging
  evidence in `odoo-rust-mcp-agent/docs/evidence/phase7/`, but that launcher used
  legacy JSON-RPC credentials and therefore does not approve the target JSON-2 cell.
- All other Odoo 17/18/19 Community/Enterprise mutation cells are blocked until
  their own runtime evidence and reviews pass.
- Odoo 18 Enterprise production is read-only. No production mutation is in scope.

## Repository gates

- Skills: `make validate`, `make test`, `make package-check`.
- MCP: Rust format, clippy, and all-feature tests; Config UI lint, typecheck,
  tests, and build; relevant transport/config smoke checks.
- Agent compiler: `cargo fmt --all --check`, `cargo clippy --all-targets -- -D warnings`,
  `cargo test --workspace` plus release/doctor gates.
- Plugin: `pytest`; PostgreSQL contract/integration tests when the test DSN is
  available; plugin install/host compatibility checks.

## Baseline risks

- The MCP `BASELINE.md` describes commit `848a349`, not the frozen commit above.
- Existing instance YAML labels the local Odoo 19 targets as Enterprise while the
  approved Phase 7 live evidence states Community; no new cell claim may rely on
  that stale label.
- The current runtime still exposes generic primitives and does not enforce the
  named-capability contract at its final execution boundary.

## Odoo 20 addendum (2026-10-25)

A disposable Odoo 20.0 Community and Enterprise matrix (JSON-2/API key) passed
all five capabilities, exact replay at plugin and runtime, stale-update
conflict on `sale.order` and draft vendor bills, the six-case boundary suite
before mutation, and no-sales denial. Both databases were dropped. The changes
it needed were merged through pull requests cut from each repository's `main`
(runtime `feceefa`, agent `5237ec8`); the owners' uncommitted working trees
were not touched:

| Repository | Pull request | Change |
|---|---|---|
| `odoo-rust-mcp` | milzamsz/odoo-rust-mcp#15 | Odoo 20 line fields (`line_commands()` was pinned to the literal `"19.0"`); a receipt preflight before the claim and the write, closing the orphan-record path; Odoo `AccessError` on create or guarded update reported as a persisted `denied` receipt instead of `uncertain`. 246 library tests and the capability tests (7, three new) pass; The PR also made the smoke and HTTP transport tests hermetic (they had silently loaded the developer's `~/.config/odoo-rust-mcp/instances.json`, including production entries, through the runtime's default-path fallback) and allowed Clippy's new `double_must_use` lint on the `async_trait` client trait; CI passed on Linux, macOS, and Windows before merge. |
| `odoo-rust-mcp-agent` | milzamsz/odoo-rust-mcp-agent#1 | `odoo20-community` and `odoo20-enterprise` cells approved for development and staging (production denied); receipt `target_cell.version` accepts `20.0`; `replay` added to the output status enum; loader test at eight cells; evidence in `docs/evidence/mutation-matrix-20/`. 69 tests pass. |

The skills-side validator `scripts/validate_mutation_capabilities.py` accepts
the Odoo 20 pair as an all-or-nothing optional group and passes against the
current contract and the pull-request contract. The whole-second optimistic-lock gap is closed by helper `oc_mcp_mutation`
1.1.0 (milzamsz/odoo-rust-mcp#16): a computed `oc_mcp_write_version` field
exposes `write_date` with microseconds for the preview read, and the guarded
update compares at full precision when given that token, which its tests prove
on Odoo 17, 18, 19, and 20 Community and Enterprise. Whole-second tokens still
work with the old blind spot. Remaining residual risk: the staging `prepare-draft-config.sh` marker no
longer matches the owners' files. Owners pulling `main` must commit or set aside
their local `support.yaml` and loader-test edits first, because the merged
Odoo 20 entries touch the same files.
