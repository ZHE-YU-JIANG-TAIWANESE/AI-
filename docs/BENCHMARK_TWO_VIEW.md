# Two-View Character Benchmark

This benchmark gives every artist/agent the same declared front and side references, then asks for the same editable and visual outputs.

## Input condition

- one front reference;
- one side reference;
- exact file hashes recorded in `JOB.json`;
- prior character meshes, prior geometry scripts, historical anchor ledgers, and repository history hidden unless explicitly declared.

## Output condition

- editable `.blend`;
- front preview;
- side preview;
- three-quarter preview;
- handoff note.

## Review dimensions

Keep these dimensions separate:

1. **Infrastructure** — did the runner and Blender actually execute?
2. **Delivery completeness** — are the required files present?
3. **Reference fidelity** — do front and side proportions match the evidence?
4. **3D plausibility** — does the model hold together in three-quarter and other views?
5. **Character-art quality** — anatomy, transitions, silhouette, forms, topology, editability.
6. **Production readiness** — deformation, cleanup, naming, scene organization, downstream usability.

## Optional numeric metrics

Future versions may add silhouette IoU, landmark error, depth-profile comparison, mesh health, topology, and deformation tests. Numeric scores should supplement, not replace, visual/artistic review.

## Fair comparison

Record runtime, model, tool policy, timestamps, evidence hashes, and failures. Do not compare an unrestricted run to a restricted clean-room run without stating the difference.
