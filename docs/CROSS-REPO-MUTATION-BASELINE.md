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
