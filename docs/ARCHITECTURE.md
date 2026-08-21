# Architecture

OCW separates the **workbench** from the **artist/agent**.

```text
source references
      ↓
  JOB.json
      ↓
 evidence staging ─────→ isolated studio
                              ↓
                    human / AI character artist
                              ↓
                         Blender + tools
                              ↓
                 editable work + review renders
                              ↓
                    delivery validation
                              ↓
                    artistic / QA review
```

## Layers

### 1. Evidence
A job declares exactly which files are geometry evidence. Each reference is hashed with SHA-256 so later runs can prove they used the same inputs.

### 2. Studio
`ocw stage` creates a clean directory containing the job contract, declared references, an evidence manifest, and an empty `vendor-output/`. Undeclared prior meshes, scripts, ledgers, or historical answers are not copied silently.

### 3. Artist runtime
The runtime is intentionally replaceable. It may be Blender operated by a human, Gemini CLI, Codex, another agent, a local model, or a deterministic script. Agent-specific details belong in adapters, not in the core evidence contract.

### 4. Delivery
The basic two-view contract expects an editable `.blend`, front/side/three-quarter previews, and a short handoff note.

### 5. Validation and review
Machine validation answers "did the run deliver the required artifacts?" It does not answer "is the anatomy good?" Artistic quality, reference fidelity, topology, deformation quality, and production readiness are separate review dimensions.

## Why this split matters

A model can be excellent but fail because its Blender path is broken. A workflow can be green while the character is poor. OCW keeps infrastructure status, delivery completeness, geometry metrics, and artistic judgment separate so experiments remain interpretable.
