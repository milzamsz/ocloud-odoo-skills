# Odoo 19 Community tracing evidence

Supported cell: 19.0 Community (verified-experimental). Consult registered sources `odoo-19-ce-source` and `odoo-19-developer` and the target 19.0 checkout before asserting any Odoo framework call edge. Matrix fixture: repository evaluation fixture `version-matrix-19-community`. Source presence does not prove that an optional addon is installed.

- Begin at the target's declared Python, XML, or frontend entry point; follow only version-19 source and observed inheritance order. Record each edge with a path and line, or mark it unknown.
- For frontend entry points, verify the target's actual registered asset and service endpoint. Do not backport 18.0 frontend patterns or infer runtime browser events from source alone.
- Record effective user, groups, companies, elevation, and transaction/side-effect boundaries separately. Do not treat UI restrictions as server authorization.
- A static trace is not measured query count or executed authorization. Runtime confirmation needs a disposable target-version environment and explicit authorization.
