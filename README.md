<p align="center">
  <img src="https://lightfast.ai/images/github-banner.png" alt="Lightfast" width="100%" />
</p>

# Ship

Turn an accepted code outcome into repository-native completion.

`ship` is a standalone Codex Orchestrator that owns one bounded request to ship code. It can work directly or coordinate native Target Tasks, while each Target Project retains its product authority, instructions, work state, approvals, and completion evidence.

Shipping means reaching the completion boundary defined by the target—not merely producing a patch or a reviewed branch. `ship` reconciles the live evidence, continues work that can safely progress, and remains accountable for the integrated outcome.

## Use `ship`

Start a Codex task from an exact revision of this repository and describe the code outcome and Target Scope you want shipped. The Orchestrator resolves the request against current Target Project instructions and available authority before causing effects.

## Read the contract

- [Architecture](docs/architecture.md) — purpose, outcomes, planning, and terminal conditions.
- [Authority](docs/authority.md) — accepted requests, Target Scope, effects, approvals, and evidence.
- [Recovery](docs/recovery.md) — reconciliation, interruption, duplicate prevention, and resumption.
- [Scenarios](tests/scenarios/) — reviewable traces that pressure-test the contract.

`ship` runs independently. The [`lightfastai/orchestrator`](https://github.com/lightfastai/orchestrator) Workbench designs and evaluates exact revisions but is never consulted at runtime.

## Verify

Run the local scenario suite:

```bash
python3 -m unittest discover -s tests -v
```

Structural conformance is checked externally from a Workbench checkout:

```bash
python3 -m conformance.v0_1_0 /path/to/ship
```

## Status

`ship` implements Orchestrator Standard `0.1.0`. Its [initial revision and evaluation](https://github.com/lightfastai/orchestrator/blob/main/evaluations/ship/91f5a2b4b09545c0404c6eb943092194d6093a5b/2026-08-27-initial.md) establish structural conformance and synthetic scenario coverage; real Target Project traces will drive future revisions.

## License

MIT © Lightfast
