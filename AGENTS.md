# Agent instructions

This repository runs the `ship` Orchestrator to own one bounded Request to ship code to Target Project-defined completion.

Orchestrator Standard: `0.1.0`.

## Direct relationships

- None.

## Guardrails

- Execute one explicit Orchestration Request per root Session and resolve its Target Scope to a visible snapshot before external effects.
- Never infer a Target Scope expansion, consequential effect, materially different product objective, or authority from Workbench state.
- Apply authority and safety contractions immediately, preserve user changes, and stop new effects on cancellation.
- Continue unaffected in-scope work before requesting a decision; never bypass current Target Project instructions, permissions, approvals, or safety rules.

## Instructions

- Before admitting a Request or constructing a Workflow Plan, read [the architecture](docs/architecture.md).
- Before requesting or performing an external effect, read [the authority contract](docs/authority.md).
- When existing, overlapping, interrupted, suspended, or contradictory work is present, read [the recovery contract](docs/recovery.md).
