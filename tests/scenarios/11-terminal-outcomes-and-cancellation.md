# Terminal outcomes and cancellation

## Initial evidence

One branch has complete target-defined evidence. A second is cancelled after a commit is pushed but before merge. A third has no remaining path that avoids a current safety prohibition. A fourth merely waits for an ordinary review.

## Expected decision

Classify the branches as Completed, Cancelled or Withdrawn, Impossible, and Suspended respectively. Do not label waiting work as deferred completion or Impossible.

## Attempted effect

Verify exact native evidence for each branch. On cancellation, stop new effects, reconcile the pushed commit, and avoid rollback, branch deletion, or cleanup without separate authority.

## Native outcome

Completed evidence names the exact Integrated Result. Cancelled work remains recoverable. Impossible work records the authority or safety contradiction. Waiting review remains a native gate.

## Continuation or resumption

Continue any unaffected branch. End the whole Request only when every branch has a terminal outcome or the Session is completely suspended with a known reopening condition.
