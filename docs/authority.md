# Authority

## Request and Target Scope

One root Session executes one active user-authorized Shipping Request. Follow-ups may clarify or narrow it; a materially different objective requires a new task. No Request creates standing authority for later Sessions.

Target Scope may resolve explicit native references or a user-approved bounded selection rule across one or several Target Projects. `ship` displays and snapshots the resolved projects before external effects. Later additions require explicit user approval; contractions apply immediately.

A mandatory issue or specification is not required. The Request plus current target evidence may be sufficient. `ship` may create or refine native issues and specifications when useful or required, without treating them as Orchestrator authority artifacts.

## Effective authority

For every effect, authority is the narrowest intersection of:

1. the Shipping Request and snapshotted Target Scope;
2. the fixed `ship` Operating Contract;
3. current Target Project instructions and product evidence;
4. current platform permissions and approvals; and
5. safety rules.

Instructions, permissions, credentials, approval rules, cancellation, and safety contractions take effect immediately. A stale Workflow Plan grants nothing.

## Effect categories

| Effect | Required authority | Native evidence | If unavailable |
| --- | --- | --- | --- |
| Inspect repositories, trackers, tasks, and delivery evidence | Request, Target Scope, and current read access | Repository, tracker, and task history | Continue another branch, narrow scope, or request indispensable access |
| Research and make reversible delivery choices | Bounded code outcome and target evidence | Native issue, specification, task, or code when material | Investigate; ask only if incompatible product/value choices remain |
| Create or refine native issues and specifications | Necessary delivery work permitted by target rules | Target-native tracker or repository | Work from sufficient Request evidence or suspend the dependent work |
| Edit, test, repair, branch, commit, and open pull requests | Ordinary delivery authority and a non-conflicting write surface | Task, branch, worktree, commit, check, and pull request | Work directly, use an optional Target Task, replan, or suspend |
| Review, merge, update trackers, and verify integration | Request to ship plus target-defined checks, reviews, and integration rules | Review, merge, default-branch, tracker, and verification state | Continue independent work or await the smallest native gate |
| Clean up safely disposable, Orchestrator-created workspaces | Reconciled native results, clear ownership, and target permission | Workspace and task evidence | Preserve when ownership, recovery value, or safety is uncertain |
| Deploy, change production, publish, release, migrate data, destroy, use paid execution, acquire broader credentials or permissions, or cause external legal, billing, security, or ownership effects | Explicit Request inclusion and applicable native approval | The owning Target Project or external system | Suspend only dependent work; never infer authority |

Merge is authorized by a Shipping Request when the exact proposed head satisfies acceptance, required native gates pass, the Request has not excluded merge, and current Target Project rules permit it. Root or Target Task may merge as those rules allow.

## Product decisions

`ship` may research ambiguity, prepare a design or specification, recommend a choice, and record reversible choices needed for delivery. It may not invent a materially different objective, reprioritize unrelated work, or decide between incompatible product-value choices unsupported by the Request and Target Project evidence.

When the indispensable decision belongs to a human or Target Project authority, suspend only its dependent work and continue every unaffected in-scope branch.

## Credentials and consequential effects

Credentials remain in platform-owned stores. Existing scoped repository access may be used for permitted ordinary delivery. New credentials, broader permissions, paid execution, deployment, production, publication, release, migration, destructive action, and comparable external effects require explicit Request inclusion and current native approval.

Loss or contraction of access immediately stops new dependent effects. It does not make unrelated work Impossible.

## Operating Windows and cancellation

An Operating Window belongs to the Request or scheduled automation. At close, reconcile and record Native Delivery Evidence, then yield the same Session completely. On reopening, read current instructions and evidence and construct a fresh Workflow Plan.

Cancellation is not rollback. Stop new effects, reconcile any in-flight or completed native result, and leave recoverable evidence. Cleanup, reversal, branch deletion, deployment rollback, or destructive action occurs only when separately authorized and safe.

## Native completion evidence

Completion evidence belongs to each Target Project or external authority home. It may include exact commits, merged heads, required checks and reviews, tracker state, published artifacts, deployments, or production verification when explicitly in scope. `ship` does not create a second completion registry or checkpoint file.

Target Projects require no `ship`-specific file, adoption record, or standing permission.
