# Component Classification

- Standard: available without custom development in the target edition.
- Configured: settings, records, security, or supported configuration.
- Third-party: reviewed OCA or vendor addon.
- Low-code: supported native low-code customization.
- Custom: OCloud-maintained addon.
- External: middleware, worker, automation, or service outside Odoo.

Classify each material component, not the whole solution. A solution can combine
standard vendor bills, configured aliases, a reviewed document-capture addon,
and a narrow external extraction service.

## Decision gates

1. Confirm capability in the exact version and edition.
2. Test whether configuration and master data close the requirement gap.
3. Search OCA by business capability and technical model in likely functional
   repositories; check the target-version branch and module manifest.
4. Review vendor options with the same license, source availability, security,
   maintenance, and upgrade criteria.
5. Use low-code only where deployment, review, testing, and migration remain
   controlled.
6. Justify custom code with a specific uncovered requirement and ownership.
7. Use an external boundary for capabilities Odoo should not own, but define
   authentication, idempotency, retries, reconciliation, observability, and
   failure recovery.

Record evidence and rejection reason for every level. “No module found” is
provisional unless repositories, branches, and search terms are stated.
