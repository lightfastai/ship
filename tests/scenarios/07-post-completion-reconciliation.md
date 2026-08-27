# Completion before reconciliation

## Initial evidence

An authorized mutation returns an ambiguous response. The interruption continues after native completion: the pull request is merged and its exact head appears on the default branch, but the root Session has not recorded reconciliation.

## Expected decision

Inspect native integration and tracker evidence before retrying or dispatching work. Verify the exact Integrated Result rather than trusting the stale plan or ambiguous response.

## Attempted effect

Read the pull request, merged and reviewed heads, merge commit, default-branch state, required checks, tracker status, and any explicitly in-scope post-merge verification.

## Native outcome

Existing completion is recognized. No duplicate pull request, merge, tracker update, or implementation task is created.

## Continuation or resumption

If all target-defined completion evidence exists, mark the branch Completed. Otherwise continue only the missing authorized verification or reconciliation work.
