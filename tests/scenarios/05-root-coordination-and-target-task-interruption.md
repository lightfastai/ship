# Root coordination and Target Task interruption

## Initial evidence

The coordination-only root identifies one bounded Target Task as sufficient for a coherent change. One interruption occurs before dispatch, after the plan was built but before the target was revalidated. A second occurs after the Target Task creates a branch and edits but before commit; a third occurs after it pushes an exact commit and opens a pull request but before checks finish.

## Expected decision

Keep all Target Project mutation inside the Target Task while the root reconciles evidence, replans, monitors native lineage, prevents duplicates, and retains terminal accountability.

## Attempted effect

After resumption, the root first rereads current instructions and native evidence. Where mutation began, it inspects the same Target Task, worktree, branch, diff, commit, pull request, checks, and any intervening user changes before resuming or dispatching mutation.

## Native outcome

The original compatible Target Task and artifacts are resumed. User changes are preserved. No root mutation, replacement branch, duplicate pull request, blind force-push, or repeated mutation is created.

## Continuation or resumption

Construct a fresh Workflow Plan from current evidence. If the original Target Task is unsafe or unavailable, preserve its exact artifacts and dispatch one evidence-bound replacement without substituting direct root mutation. Independent in-scope coordination and work continue.
