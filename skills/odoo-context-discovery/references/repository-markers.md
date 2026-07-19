# Repository Markers

Inspect manifests, Odoo configuration, Compose files, Dockerfiles, submodules,
aggregate repository files, migration directories, test configuration, and
deployment documentation. Read secret-bearing files only to identify key names
and structure; never reproduce values.

## Real OCloud layout patterns

The following marker combinations were observed in the read-only
`odoo-dev/projects` evidence workspace. They are examples of how to reason,
not portable path assumptions.

### Community project (`erp-ocloud`)

- `AGENTS.md` and `README.md` explicitly identify Odoo 18 Community and
  `addons/custom/` with an `oc_` prefix.
- `config/odoo.conf` lists standard, custom, third-party, OCA, MuK, and base
  addon roots. Odoo does not recurse into nested addon repositories, so each
  effective checkout may need its own `addons_path` entry.
- Root and deployment Compose files describe different local and deployed
  topologies. Merely finding Compose does not establish which database is safe.
- Project instructions distinguish local Odood work from Dokploy staging and
  production operations. Discovery may record commands, but must not run them.

### Enterprise-dependent project (`erp-ca`)

- `AGENTS.md`, `README.md`, a dated `odoo:18.0-*` image pin, an
  `odoo==18.0` requirement, and an `addons/enterprise` submodule marker provide
  converging Odoo 18 Enterprise evidence.
- `addons/` is a mapping/symlink layer. The runtime truth is the
  `addons_path` in `config/odoo.conf`, including explicit nested OCA repository
  directories.
- Custom, Enterprise, OCA, and vendor trees coexist. Inventory origin and
  dependencies per target module instead of assigning one edition or origin to
  every addon.
- Odood commands run from the matching `environments/odoo18ee` environment,
  while Docker/Dokploy assets serve other lifecycle stages.
- Documentation can conflict: the verified README marks Odoo 19 references as
  legacy. Record the conflict and follow the project's stated source hierarchy.

## Marker interpretation

| Marker | What it can prove | What it cannot prove alone |
|---|---|---|
| Pinned `odoo:<version>` image or package | Intended runtime version | Active database version or edition |
| Odoo source release/commit | Source version | Deployed image or database target |
| Enterprise source path/submodule plus matching dependency | Enterprise dependency and edition evidence | Subscription validity or installed module state |
| `web_enterprise` or another Enterprise manifest dependency | Target addon requires Enterprise | Every environment is Enterprise |
| OCA checkout/submodule metadata | Third-party origin and candidate branch | Compatibility without checking branch and manifest |
| `addons_path` | Runtime search roots | Recursive discovery beneath aggregate roots |
| Odood assembly/environment marker | Local development association | Permission to start, test, install, or upgrade |
| Compose or deployment manifest | Available topology and service definitions | Which topology is active or safe |
| `.env.example` | Expected variable names | Real values or a safe database target |

## Inspection sequence

1. Read controlling instructions and their conflict rules.
2. Identify repository root, symlinks/submodules, and repository revision.
3. Compare image/package pins, source release data, branch names, and manifests.
4. Parse configured addon roots; do not assume recursive discovery.
5. Identify local, test, staging, production, and migration-copy markers
   separately.
6. Record exact safe validation commands only when repository documentation
   defines them.
7. Report conflicts and unknowns before loading version-sensitive procedures.
