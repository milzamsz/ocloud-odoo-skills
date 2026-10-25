# SQL items

Load this only when an item has `data_calculation_type` `sql`.

## When SQL is justified

Use SQL only when the ORM cannot express the metric: joins across models without
a stored relation, window functions, or a ratio of two aggregates over different
models. Record the reason in the design. Everything else is an ORM item or a KPI.

## Why SQL needs extra care

On the local database the addon runs the query on Odoo's own cursor, inside a
savepoint. ACLs, record rules, and the company switcher do **not** apply. Every
SQL item therefore needs:

- `allowed_group_ids` limited to the audience that may see all rows it returns;
- an explicit company filter, `company_id = {company_id}`, on every company-owned table;
- state filters written out (`parent_state = 'posted'`, `active`), since nothing hides archived or draft rows;
- no personal data columns (NIK, phone, email, bank account) unless the audience is entitled to them.

## What the addon accepts

The addon (source) strips comments and then requires:

- one statement only (a trailing `;` is tolerated, inner `;` is rejected);
- the statement starts with `SELECT` or `WITH`;
- none of these words anywhere, even as functions or column names: `INSERT,
  UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, GRANT, REVOKE, COPY, EXECUTE, EXEC,
  CALL, MERGE, REPLACE, ATTACH, DETACH, VACUUM, REINDEX, CLUSTER, COMMENT, LISTEN,
  NOTIFY, LOAD`, `INTO OUTFILE`, `INTO DUMPFILE`, `SET ROLE`, `SET SESSION`,
  `SECURITY DEFINER`. Alias around them: `replace()` and a column named `comment` both fail.

## Placeholders

Replaced as plain text after validation, so quote dates yourself:

| Placeholder | Value |
|---|---|
| `{start_date}`, `%START_DATE%` | Start of the item's or board's date filter (`1900-01-01` when none) |
| `{end_date}`, `%END_DATE%` | End of the date filter (`2099-12-31` when none) |
| `{uid}`, `{user_id}`, `%UID%`, `%USER_ID%` | Current user id |
| `{company_id}`, `%COMPANY_ID%` | Current company id |

Example: `WHERE l.date BETWEEN '{start_date}' AND '{end_date}' AND l.company_id = {company_id}`.

A `LIMIT` of `sql_row_limit` (default 5000) is appended when the query has none.
Add your own `LIMIT` for top-N charts.

## How columns become a chart

- Tile or KPI: the column named `value`, `amount`, `total`, `sum`, or `count`;
  otherwise the last column.
- Chart: the label is `sql_label_column` (or the first column); every other column
  is a series. Return one row per label.
- List: all columns, in query order.

## Before handing over

- The validator passes the query.
- Run the query read-only on a development copy and compare its totals with an
  ORM view of the same records.
- State in the design which groups see it and why the bypass of record rules is acceptable.
