# Publishing and Release Hygiene

This repository is intended to contain only the public Open Character Workbench package.

## Before every release

Run:

```bash
python scripts/prepublish_guard.py .
python -m pip install -e .
python -m compileall -q src
python -m unittest discover -s tests -v
ocw --help
```

Then review the diff manually for private references, client assets, credentials, absolute local paths, and unexpectedly large binaries.

## Never publish a mixed private history as a shortcut

Git retains deleted files in old commits. If you develop OCW inside another private repository that also contains client work, export the public package into a fresh repository/history before publication.

## Release checklist

- no credentials or secret values;
- no private character/client assets;
- every bundled example has redistribution permission;
- `LICENSE`, `NOTICE`, `SECURITY.md`, and `CONTRIBUTING.md` are present;
- package installs;
- tests and smoke workflow pass;
- README claims match current behavior;
- release notes include an explicit timestamp.
