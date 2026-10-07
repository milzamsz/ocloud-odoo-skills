# `create_quotation_draft.v1` contract

Load only after the shared contract approves the exact target cell. All current
target cells remain blocked.

## Outcome and bounds

Create one `sale.order` in `draft` for the trusted company. Map the approved
customer, currency, pricelist, payment term, validity date, client reference,
and 1–100 lines exactly. Each line binds product, UoM, description, quantity,
unit price, discount, and taxes.

Do not confirm the quotation, create delivery or invoice documents, recompute an
approved payload client-side, or substitute taxes, UoM, currency, or pricing.

## Required evidence

- Verify customer, products, UoMs, pricelist, currency, payment term, and taxes
  belong to or are usable by the approved company before approval.
- Bind the canonical header and line payload, target, company, evidence reference,
  idempotency key, digest, actor, reviewer, and expiry.
- Verify returned state, company, header, every line mapping, untaxed amount,
  currency, pricing, discounts, taxes, and UoM without confirming the order.
- Return the normalized `draft_write` receipt. Duplicate or changed requests are
  conflicts; uncertain execution is never retried automatically.
