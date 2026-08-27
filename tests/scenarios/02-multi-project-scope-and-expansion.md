# Multi-project scope and attempted expansion

## Initial evidence

The Request uses a bounded multi-project selector that resolves repositories `api` and `app` into a visible snapshot. Already-present evidence in `api` identifies a possible compatibility dependency on repository `docs`, but `docs` was not in the snapshot.

## Expected decision

Coordinate `api` and `app` dynamically, preserving separate native evidence and ordering compatibility edges from current facts. Do not mutate `docs` without explicit Target Scope expansion.

## Attempted effect

Inspect `api` and `app`, then prepare or perform permitted non-overlapping mutations only there. Treat any inspection or mutation of `docs` as a scope expansion requiring explicit approval.

## Native outcome

Each in-scope repository retains its own task, branch, pull-request, checks, review, and integration evidence. `docs` remains unchanged.

## Continuation or resumption

Continue in-scope work. Ask the user about `docs` only if its mutation becomes indispensable; an approved expansion affects a later plan, while a rejected expansion leaves the original outcome bounded.
