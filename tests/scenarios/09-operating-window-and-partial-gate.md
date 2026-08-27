# Operating Window and partial gate

## Initial evidence

The Operating Window closes while one branch has durable commits and another awaits production approval. A third independent in-scope branch can progress when the next window opens.

## Expected decision

Reconcile native evidence and yield the same Session completely at close. Do not let the production gate block independent work after reopening.

## Attempted effect

Record exact native tasks, branches, commits, pull requests, checks, approvals, and unresolved gates without copying them into an Orchestrator checkpoint file.

## Native outcome

No model activity continues outside the window. Durable state remains native. The production branch stays suspended without inferring production authority.

## Continuation or resumption

When the window reopens, reread current instructions and evidence and construct a fresh plan. Continue the independent branch while awaiting the indispensable production decision.
