# Existing and overlapping work

## Initial evidence

One target already has a compatible branch and pull request for the requested outcome. Another target has an active writer on the same files but with contradictory intent. A stale local worktree also exists.

## Expected decision

Resume the compatible native artifacts, preserve all user changes, and block conflicting mutation until ownership and intent are resolved. Never infer that elapsed time makes the other writer inactive.

## Attempted effect

Search native tasks, worktrees, branches, commits, pull requests, checks, and tracker evidence before creating anything.

## Native outcome

The compatible pull request is continued at its exact head. No duplicate branch, task, pull request, or overwrite is created for the conflicting surface. The stale worktree is preserved until its ownership and recovery value are known.

## Continuation or resumption

Continue every non-overlapping branch. Reconcile or obtain the smallest ownership decision for the conflict, then construct a fresh plan from the resulting native evidence.
