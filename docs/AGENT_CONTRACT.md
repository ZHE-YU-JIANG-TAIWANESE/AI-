# Agent Contract

An OCW-compatible character artist receives a staged studio and returns a reviewable delivery.

## Inputs

The studio may contain:

- `JOB.json` — task and delivery contract;
- `EVIDENCE.json` — declared evidence and hashes;
- `references/` — only the references declared for this run;
- `vendor-output/` — output directory.

The agent must not silently treat undeclared historical meshes, scripts, ledgers, generated derivatives, or repository history as geometry authority.

## Allowed methods

OCW itself is vendor-neutral and method-neutral. A run may impose additional restrictions, but those restrictions must be declared. The agent may use Blender, Python, Geometry Nodes, sculpting, external services, local models, or other tools if the run policy permits them.

## Required two-view delivery

A default character-body run should produce under `vendor-output/`:

- an editable `.blend`;
- a front preview image;
- a side preview image;
- a three-quarter preview image;
- a concise handoff note describing what was done and what remains uncertain.

## Reporting

Do not claim production quality merely because files exist or CI is green. Report failures explicitly, especially when the runtime never reached the modeling step.

## Provenance

Keep timestamps, runtime/model identity when available, input hashes, and tool/runtime failures. This allows later comparison between runs without reconstructing history from memory.
