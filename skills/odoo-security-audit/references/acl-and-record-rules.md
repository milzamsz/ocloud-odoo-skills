# ACL and Record Rule Review

Build a matrix for every persistent model:

| Model | Group/user | Read | Create | Write | Unlink | Company/owner boundary | Negative test |
|---|---|---:|---:|---:|---:|---|---|

## ACL review

- ACL permissions are additive across a user's groups. A narrow ACL does not
  cancel a broad ACL granted by another group.
- Absence of an ACL normally denies ordinary users but is not a substitute for
  a deliberate administrator-only design.
- Require explicit business justification for internal-user write or unlink,
  and inspect inherited models whose access may come from another module.

## Record-rule review

- Record rules filter records after model-level ACL access. ACLs alone do not
  provide row, owner, or company isolation.
- Evaluate the effective composition: global rules intersect; applicable group
  rules can broaden access within the global boundary. Do not assess one rule
  in isolation.
- Check each CRUD operation because a read-only rule or omitted `perm_*` intent
  can differ from write/create/unlink behavior.
- For owner rules, verify empty owner values cannot become shared
  unintentionally and that caller-controlled owner fields cannot grant access.

## Multi-company review

- A `company_id` field does not enforce isolation by itself. Require an
  effective company rule where the business object is company-scoped.
- Check records with a company, intentionally shared records with no company,
  users allowed in multiple companies, active-company switching, related
  records, and privileged jobs.
- `sudo()` bypasses access rights and record rules; company context is not an
  authorization substitute. Validate the caller and constrain the elevated
  recordset before elevation.

## Verification

Use static inspection plus negative tests for unauthorized group, other owner,
and disallowed company. Do not create users or records in a live system merely
to prove a review finding.
