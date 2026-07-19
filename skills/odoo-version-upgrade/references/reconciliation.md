# Reconciliation

Capture source baselines before migration and compare target evidence using the
same company, date, state, currency, and rounding scope. Assign an owner and
tolerance to every check; explain every accepted variance.

## Fixture-level checks

For a renamed field and XML ID:

- source non-null count equals target non-null count;
- values match by stable business key, including empty and Unicode values;
- the old field is not used by target Python, XML, domains, exports, or
  integrations;
- the target XML ID resolves to the same intended record;
- no duplicate `ir.model.data` row or accidental replacement record exists;
- downstream references and configuration use the target XML ID.

## Business checks

- Master/open documents: counts and totals by company, state, and currency.
- Accounting: posted debit equals credit; trial balance, retained/opening
  balances, receivables, payables, taxes, aged reports, and bank reconciliation
  match agreed baselines. Distinguish operational documents from journal
  entries and record posting/reconciliation timing.
- Inventory: on-hand and reserved quantities, quants by location/lot/package,
  valuation layers, inventory valuation, and accounting valuation agree.
- Other: users and access, company-dependent properties, rates, attachments,
  scheduled actions, integrations, and critical reports.

## Acceptance

Do not accept “database starts” or record counts alone. Record query/report
evidence, variance, owner sign-off, unresolved exceptions, and rollback trigger.
