# ship

`ship` is a standalone Codex Orchestrator for owning one bounded request to ship code to repository-native completion.

It can work directly or dispatch native Target Tasks when useful, while each Target Project retains its product authority, instructions, work state, and completion evidence. Runtime does not consult the Orchestrator Design Workbench.

The operating design is documented in:

- [architecture](docs/architecture.md);
- [authority](docs/authority.md);
- [recovery](docs/recovery.md); and
- [reviewable scenarios](tests/scenarios/).

Run the local scenario checks with:

```bash
python3 -m unittest discover -s tests -v
```
