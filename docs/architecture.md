# Architecture

## Purpose

`ship` owns one bounded Request to ship code to Target Project-defined completion. It dynamically performs or coordinates the research, reversible design clarification, implementation, testing, repair, review, integration, tracker reconciliation, and verification necessary for that outcome.

## Non-goals

`ship` does not:

- accept purely advisory research as a Shipping Request;
- invent a materially different product objective or prioritize unrelated work;
- decide an incompatible product-value choice that the Request and target evidence cannot resolve;
- infer a Target Scope expansion or consequential effect;
- replace Target Project instructions, product authority, or native work state;
- require a Target Project adoption file, pre-existing issue, or specification;
- maintain a registry, charter, programme, checkpoint, or copied work graph;
- prescribe fixed phases, mandatory task decomposition, or one pull request per work item; or
- consult the Orchestrator Design Workbench or Orchestrator Map at runtime.

## Inputs and admission

One root Orchestrator Session accepts one explicit Shipping Request containing:

- a bounded code-delivery outcome;
- named Target Projects or a bounded selection rule;
- material constraints and exclusions; and
- every requested consequential effect.

The Target Scope is resolved to a visible snapshot before external effects. The Request and current Target Project evidence must make the intended outcome and observable completion sufficiently determinate before consequential mutation. `ship` may investigate ambiguity, prepare designs or specifications, and make reversible delivery choices; it asks the user only when incompatible product or value choices remain.

## Observable outcomes

- The exact Integrated Result satisfies the Target Project's acceptance and integration boundary.
- Every effect remains within effective authority.
- Compatible native work is resumed and conflicting duplicate mutation is prevented.
- A blocker affects only the work that depends on it while other in-scope work continues.
- The Request ends as Completed, Cancelled or Withdrawn, or Impossible without treating unfinished work as deferred completion.

## Invariants

- Effective authority is the narrowest intersection of the Request, snapshotted Target Scope, this Operating Contract, current Target Project instructions, platform permissions and approvals, and safety rules.
- Target Scope expansions require explicit user approval. Contractions apply immediately.
- Changed instructions, permissions, credentials, approval rules, cancellation, or safety constraints immediately narrow new effects even when a prior Workflow Plan used older controls.
- Durable work and completion evidence remain in native authority homes.
- Direct work and Target Task work obey the same reconciliation, duplicate-prevention, user-change-preservation, and recovery rules.
- An unchanged failed action is not repeated without materially changed evidence.
- Cancellation stops new effects but does not authorize rollback.
- Workbench absence cannot change runtime behavior.

## Tuning Envelope

Within effective authority, `ship` may:

- work directly or dispatch native Target Tasks;
- discover and use available skills, tools, apps, plugins, and providers;
- order, branch, loop, suspend, or parallelize non-overlapping work;
- choose reversible implementation details; and
- adjust evidence burden to current risk and target policy.

It may not tune or expand the Request, Target Scope, product objective, consequential effects, safety boundaries, approvals, or authority model.

## Evidence-driven planning

Each Workflow Plan is Session-local and disposable. It is constructed from current instructions, native evidence, platform state, and unresolved gates. Direct work and Target Task dispatch are strategies, not phases.

Use a Target Task only when it provides real leverage: Target Project instructions require it; work can proceed independently; or context isolation, specialist capability, parallelism, long-running ownership, or recovery materially helps. A Target Task inherits a bounded sub-objective and current target rules. The root Session retains terminal accountability.

When reconsidering this direct-or-dispatch boundary, read [the outcome-owned delivery decision](adr/0001-outcome-owned-direct-or-delegated-delivery.md).

## Continuation-First

For every plan:

1. replan around an unavailable or incompatible branch;
2. continue unaffected in-scope work;
3. persist native evidence and resume temporary constraints;
4. ask the user only for an indispensable decision; and
5. end only when Completed, Cancelled or Withdrawn, or every remaining path necessarily violates authority or safety.

A waiting approval, production action, unavailable optional capability, or closed Operating Window suspends only its dependent work. The whole Session yields only when no productive in-scope path remains.

## Resource ceilings

There is no `ship`-specific numeric task, concurrency, repair, retry, or Orchestrator Delegation budget. The effective ceiling is the narrowest live bound from the Request, platform capacity, Target Project policy, non-overlapping write surfaces, approvals, and safety. Uncertain overlap blocks affected mutations until reconciled. Read-only work may proceed when it does not violate those controls.

## Review and verification

`ship` adds no universal independent-review requirement. It satisfies the Target Project's current checks and review policy, then verifies acceptance at the exact Integrated Result. A reviewed pull-request head is not completion when merge, deployment, or production verification is part of the target-defined boundary.

## Dependencies and direct relationships

`ship` has no hard runtime dependency beyond native Codex, repository, task, and platform surfaces. Optional capabilities are discovered dynamically; their absence isolates only dependent work.

Native Target Task dispatch is not capital-D Orchestrator Delegation. v1 declares no child Orchestrator relationship. An unavailable, incompatible, undeclared, or cyclic Orchestrator edge is rejected and control remains with `ship`; it neither consults the Workbench Map nor silently substitutes another Orchestrator.

## Terminal conditions

**Completed** requires target-defined acceptance and integration evidence at the exact Integrated Result. Where deployment or production verification is explicitly part of completion, merge alone is insufficient. Where it is not, `ship` does not infer production authority.

**Cancelled or Withdrawn** means the user or Target Project authority ended the Request or an in-scope branch. Stop new effects, reconcile in-flight and native results, and leave recoverable evidence. Cleanup or reversal occurs only when separately authorized and safe.

**Impossible** means every remaining path necessarily violates authority or safety. Temporary blockers, unavailable optional capabilities, failed checks, pending decisions, and closed Operating Windows are not Impossible.
