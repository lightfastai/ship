# Recovery

## Evidence precedence

Reconcile evidence in this order:

1. current Target Project instructions, platform permissions, approvals, and safety constraints;
2. current native integration and external state, including default-branch heads, deployments when in scope, and tracker outcomes;
3. native tasks, branches, worktrees, commits, pull requests, checks, and reviews;
4. harness-native source task identifiers and Session history; and
5. the prior Workflow Plan, which is disposable and never overrides current native evidence.

Missing or contradictory evidence isolates the affected work. Unaffected in-scope work continues.

## Reconciliation before mutation

Before any mutation, the root searches the Target Project's native systems for compatible or overlapping work. Preserve user changes. Resume compatible Target Tasks and artifacts when their ownership, objective, authority, and exact identity agree with the Request. Do not dispatch or continue a competing mutation when another writer or unresolved artifact owns the same surface.

There is no mandatory Delivery Item database, Delivery Line abstraction, issue-first rule, one-task rule, or one-pull-request rule. Duplicate prevention is an invariant derived from native evidence rather than a copied work graph.

## Root coordination recovery

After interruption, reconcile the same root Session, disposable Workflow Plan, native Target Task lineage, exact artifacts, checks, and target instructions. Legacy or contradictory root-owned mutation is recoverable evidence, not authority to continue directly: preserve its exact artifacts and resume or dispatch a compatible Target Task before any further Target Project mutation. If continuation is unavailable or unsafe, preserve the evidence and select another bounded Target Task path without overwriting user changes or duplicating mutation.

## Target Task recovery and lineage

A Target Task is the required native execution boundary for Target Project mutation. Harness-native source task identifiers link it to the root Request. Prefer the same compatible task and artifacts after interruption. Replacement is allowed only when evidence shows continuation is unavailable or unsafe; bind replacement work to the same bounded objective, snapshotted Target Scope, native artifacts, and unresolved evidence.

Target Task dispatch is not Orchestrator Delegation. v1 declares no direct Orchestrator relationships. Reject an unavailable, incompatible, undeclared, or cyclic Orchestrator edge, retain control, and replan without Workbench Map lookup or silent substitution.

## Interruption points

- **Before mutation:** discard the stale plan, reread current controls, reconcile native evidence, and dispatch or resume a bounded Target Task from the present state.
- **During work:** identify the exact Target Task, native artifacts, and ownership, preserve user changes, then resume or replan without duplicate mutation.
- **After native completion but before reconciliation:** verify the exact Integrated Result and record completion rather than redispatching work.

## Idempotency and retries

Use native task IDs, branches, worktrees, commit hashes, pull-request IDs, tracker references, deployment identifiers, and other authority-home identities to recognize prior effects. Search before creation and verify after an ambiguous response.

No numeric retry or repair limit is imposed. A repeated action requires materially changed evidence such as changed code, restored access, revised instructions, new approval, or a recoverable replacement path. Repeating the same failed action without new evidence is forbidden and suspends at the smallest indispensable gate.

## Operating Windows, decisions, and cancellation

At Operating Window close, reconcile durable native evidence and yield the same Session completely. At reopening, reread current controls and construct a fresh Workflow Plan.

A pending approval, credential, production action, or user decision suspends only dependent work. Continue every independent in-scope branch.

On cancellation or Target Scope contraction, stop new affected effects immediately, reconcile in-flight and completed outcomes, and leave recoverable evidence. Do not infer cleanup, reversal, deletion, or rollback authority.

## Unavailable capabilities and Workbench loss

An unavailable optional skill, tool, app, plugin, provider, or Target Project isolates dependent work. Unavailable Target Task dispatch suspends only dependent mutation while root read-only investigation, orchestration-native evidence management, and unaffected work continue. Replan with compatible available Target Tasks or local read-only behavior; never substitute direct root mutation, silently substitute a provider, or expand authority. Absence alone is not Impossible.

Complete loss of Workbench access changes nothing. Runtime uses only this Revision, the Request, current Target Project instructions, platform state, Session history, and Native Delivery Evidence.
