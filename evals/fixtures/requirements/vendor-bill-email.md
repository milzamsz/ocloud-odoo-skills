# Vendor Bill Email Intake Requirement

## Confirmed context

- Odoo 18.0 Enterprise is the target; exact installed apps still require
  read-only confirmation.
- Two legal companies share some vendors but keep separate payable journals,
  taxes, currencies, and approval responsibilities.
- AP processes about 600 PDF invoices per month through company-specific
  mailboxes. English and Indonesian invoices are common.

## Current process and problem

AP downloads email attachments, checks invoice number and vendor manually,
finds the purchase order/receipt, creates a draft vendor bill, selects taxes,
and retains the email as evidence. Duplicate invoices and wrong-company tax
selection are the material risks. The requester's preferred technology is
“use n8n and AI,” but that is a suggestion, not an approved constraint.

## Required outcome

- Preserve original email sender, received time, subject, and attachment.
- Detect likely duplicates using company, vendor, invoice reference, date,
  amount, and attachment hash; never silently discard a possible duplicate.
- Match the correct company, vendor, purchase order, and received quantities.
- Create draft vendor bills only. AP validates uncertain vendor, company,
  account, tax, currency, and amount data before posting.
- Keep posted-bill authorization and reconciliation in Odoo.
- Provide a review queue with reason/confidence and a recoverable failure path.
- Prevent one company's AP users from seeing another company's intake records
  unless explicitly authorized.

## Accounting and control assumptions

- Email receipt and draft creation create no journal entry.
- Posting follows Odoo's payable accounting and remains a human-authorized
  action. The design must state debit/credit, tax, currency, posting, and
  reconciliation assumptions without inventing account mappings.
- PO matching is evidence, not permission to bypass vendor bill controls.
- No production mailbox or database mutation is authorized for this design.

## Evaluation requirements

The design must compare Standard, Configured, OCA/vendor, Low-code, Custom, and
External options in order. OCA research must identify candidate repositories,
target branch, manifest/license/maintenance checks, and may conclude no verified
fit. The recommendation must define idempotency, audit evidence, security,
multi-company behavior, failure recovery, acceptance criteria, and reasons for
rejecting or combining alternatives.
