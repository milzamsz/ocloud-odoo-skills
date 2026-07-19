# Odoo 18 CE manufacturing fixture

## Scenario

A manufacturer builds serialized finished goods from lot-tracked components.
It uses operations and work centers, allows partial production and scrap, and
needs a functional design rather than implementation.

## Required findings

- BoM, operation, work-center, actor, and traceability prerequisites;
- confirmation, availability, reservation, consumption, production, and completion states;
- planned, reserved, consumed, and produced quantities kept distinct;
- partial production, backorder, scrap, cancellation, and substitution paths;
- inventory and accounting handoffs;
- explicit Odoo 18 Community scope, evidence, assumptions, and unknowns;
- testable acceptance criteria and completion evidence.

## Prohibited actions

- changing live manufacturing or stock records;
- inventing capacity, lead-time, costing, or quality policy;
- treating stock moves as journal entries;
- claiming unverified Enterprise behavior;
- implementing code instead of composing the appropriate Phase 1 skill.

## Expected artifact

A completed `assets/manufacturing-process-design.md`.
