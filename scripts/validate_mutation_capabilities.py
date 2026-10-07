#!/usr/bin/env python3
"""Validate public mutation-skill coverage against the compiler-owned contract."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CELLS = {
    f"odoo{version}-{edition}"
    for version in (17, 18, 19)
    for edition in ("community", "enterprise")
}
EXPECTED_CAPABILITIES = {
    "create_crm_lead_draft.v1",
    "create_quotation_draft.v1",
    "prepare_vendor_bill_draft.v1",
    "update_allowed_draft_fields.v1",
    "import_bank_transaction_draft.v1",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--contract", required=True, type=Path)
    args = parser.parse_args()
    contract_path = args.contract.resolve()
    contract = yaml.safe_load(contract_path.read_text())
    errors: list[str] = []
    cells = contract.get("cells", {})
    capabilities = contract.get("capabilities", {})

    if set(cells) != EXPECTED_CELLS:
        errors.append(f"cells must be exactly {sorted(EXPECTED_CELLS)}")
    if set(capabilities) != EXPECTED_CAPABILITIES:
        errors.append(f"capabilities must be exactly {sorted(EXPECTED_CAPABILITIES)}")

    receipt = (contract_path.parent / contract.get("receipt_schema", "")).resolve()
    try:
        receipt_schema = json.loads(receipt.read_text())
    except (OSError, json.JSONDecodeError):
        errors.append("shared receipt schema is missing")
        receipt_schema = {}
    required_receipt = {
        "receipt_version",
        "target_cell",
        "capability",
        "operation_class",
        "status",
        "actor_ref",
        "approval_ref",
        "approval_decided_at",
        "idempotency_key",
        "payload_digest",
        "correlation_id",
        "audit_id",
        "registry_revision",
        "verification",
        "compensation",
    }
    if receipt_schema.get("additionalProperties") is not False or not required_receipt <= set(
        receipt_schema.get("required", [])
    ):
        errors.append("shared receipt schema lacks the closed normalized vocabulary")
    required_target = {
        "version",
        "edition",
        "protocol",
        "auth_mode",
        "environment",
        "instance_id",
        "database_ref",
        "target_identity",
        "company_id",
    }
    target = receipt_schema.get("properties", {}).get("target_cell", {})
    if not required_target <= set(target.get("required", [])):
        errors.append("shared receipt target cell lacks exact target identity fields")
    outcomes = yaml.safe_load((ROOT / "evals/outcome/cases.yaml").read_text()).get("cases", [])
    fixture = ROOT / "evals/fixtures/live-mutation-capabilities/README.md"
    if not fixture.is_file():
        errors.append("shared mutation fixture is missing")

    for capability_id, capability in capabilities.items():
        prefix = capability_id.removesuffix(".v1").replace("_", "-") + "-v1"
        reference = ROOT / "skills/odoo-live-mutation/references" / f"{prefix}.md"
        if not reference.is_file():
            errors.append(f"{capability_id}: public reference is missing")
        if not any(capability_id in str(case.get("request", "")) for case in outcomes):
            errors.append(f"{capability_id}: outcome case is missing")
        if set(capability.get("support", {})) != EXPECTED_CELLS:
            errors.append(f"{capability_id}: every exact support cell is required")

        for kind in ("input", "output"):
            schema = (contract_path.parent / capability.get(f"{kind}_schema", "")).resolve()
            try:
                value = json.loads(schema.read_text())
            except (OSError, json.JSONDecodeError):
                errors.append(f"{capability_id}: {kind} schema is missing or invalid")
                continue
            if (
                value.get("$id") != f"{capability_id}.{kind}"
                or value.get("additionalProperties") is not False
            ):
                errors.append(f"{capability_id}: {kind} schema is not the exact closed contract")
            if kind == "output" and "receipt" not in value.get("required", []):
                errors.append(f"{capability_id}: output does not require the normalized receipt")
            if kind == "output" and "replay" not in value.get("properties", {}).get(
                "status", {}
            ).get("enum", []):
                errors.append(f"{capability_id}: output cannot represent a durable replay")
            if (
                capability_id == "import_bank_transaction_draft.v1"
                and kind == "input"
                and "correction_owner_ref" not in value.get("required", [])
            ):
                errors.append(f"{capability_id}: correction owner is not approval-bound")

        for cell_id, support in capability.get("support", {}).items():
            decisions = [support.get(environment) for environment in ("development", "staging")]
            if any(decision not in {"blocked", "approved"} for decision in decisions):
                errors.append(f"{capability_id}/{cell_id}: invalid environment decision")
            evidence = support.get("evidence", [])
            reviews = support.get("reviews", [])
            if "approved" in decisions and (not evidence or not reviews):
                errors.append(
                    f"{capability_id}/{cell_id}: approved support lacks evidence or reviews"
                )
            for relative in evidence:
                if not (contract_path.parent / relative).resolve().is_file():
                    errors.append(f"{capability_id}/{cell_id}: missing evidence {relative}")
            for review in reviews:
                relative = review.get("evidence", "")
                if (
                    not review.get("role")
                    or not review.get("status")
                    or not (contract_path.parent / relative).resolve().is_file()
                ):
                    errors.append(f"{capability_id}/{cell_id}: invalid named review")

    print(json.dumps({"valid": not errors, "errors": errors}, indent=2))
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
