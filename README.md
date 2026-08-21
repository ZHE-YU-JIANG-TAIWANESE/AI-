# Open Character Workbench (OCW)

**An open, vendor-neutral workbench for AI-assisted character modeling in Blender.**

OCW turns a character-modeling project into a reproducible workspace that an AI agent, a human artist, or both can operate. The core idea is simple:

> references → isolated studio → Blender work → reviewable delivery → repeat

OCW does **not** ship a model or a magic image-to-3D generator. It ships the surrounding workshop: job manifests, clean-room staging, provenance, delivery contracts, validation, and benchmark conventions.

## Why this exists

A strong character agent needs more than a language model. It needs a stable workbench: exact source references, a real Blender installation, editable outputs, repeatable checks, timestamps, and a way to compare one run with another.

OCW is designed so different agents can attempt the same task under the same evidence conditions. You can use Gemini CLI, Codex, another API/CLI agent, a local model, or no AI at all.

## What is included

- `ocw doctor` — inspect the local workstation and find Blender.
- `ocw new-job` — create a timestamped job manifest and hash the source references.
- `ocw stage` — build an isolated studio containing only declared job evidence and the job contract.
- `ocw validate` — verify that a delivery contains the required editable workfile, previews, and handoff note.
- A two-view character benchmark convention (front / side → front / side / 3Q delivery).
- A vendor-neutral agent contract.
- GitHub Actions smoke tests.
- Asset/privacy rules that keep private character material out of the public framework.

## Quick start

Requirements: Python 3.11+ and Blender for actual modeling.

```bash
python -m pip install -e .

ocw doctor

ocw new-job \
  --front /path/to/front.png \
  --side /path/to/side.png \
  --output jobs/my-character.json

ocw stage \
  --job jobs/my-character.json \
  --studio .ocw/studios/my-character
```

Give the staged studio to your artist/agent. It will contain the job contract and copies of the declared reference images, but no prior character model unless the manifest explicitly declares one.

When the artist finishes:

```bash
ocw validate --delivery .ocw/studios/my-character/vendor-output
```

The default two-view contract expects:

- one editable `.blend`
- a front preview
- a side preview
- a three-quarter preview
- a short handoff note

For Linux users who do not already have Blender, the repository also ships a portable workstation bootstrap:

```bash
bash scripts/bootstrap_blender_linux.sh
```

A runnable synthetic example is included under `examples/two-view/` so the framework can be exercised without redistributing a private character.

## Project layout

```text
src/open_character_workbench/  # CLI + staging + validation
scripts/                       # workstation and publication helpers
docs/                          # architecture and contracts
examples/two-view/             # redistributable synthetic example
adapters/                      # agent-specific notes
.github/workflows/             # smoke test
```

## Design principles

1. **Evidence first.** Exact references are hashed and declared.
2. **Editable output first.** The `.blend` is a primary deliverable, not a hidden by-product.
3. **Agent-neutral.** The workshop is not tied to one model vendor.
4. **No silent inheritance.** Prior meshes, scripts, ledgers, or reference derivatives are visible only when declared in the job.
5. **Reviewable runs.** Previews and handoff notes make a green CI run insufficient by itself.
6. **Time is data.** Jobs and deliveries keep explicit timestamps so project history does not collapse into guesswork later.

## Public/private split

This repository is the public package only. Private character art, proprietary references, API keys, historical project files, and client data should stay outside it.

See `docs/PUBLISHING.md` and `docs/ASSET_POLICY.md` before adding real project material.

## Status

OCW is an early workbench, not a finished automatic character generator. The current goal is to make character-agent experiments reproducible and improvable by a community.

## License

Code and documentation are licensed under Apache License 2.0. Art assets supplied by users remain under their own licenses and are not relicensed by OCW.
