# Roadmap

OCW 0.1 focuses on reproducible staging and delivery. The next useful layers are intentionally separated so contributors can improve them independently.

## Near term

- reference-landmark schema;
- silhouette comparison helpers;
- richer delivery metadata with start/end timestamps and runtime identity;
- Blender scene health checks;
- optional topology/manifold/deformation checks;
- first-class adapter examples for major CLI agents;
- reusable GitHub Actions workflow for clean-room agent runs.

## Character-art tooling

- front/side image-plane setup helpers;
- automated camera alignment for review renders;
- named body landmark overlays;
- controlled measurement extraction;
- side-depth profile comparison;
- mesh-vs-reference review reports;
- pose/deformation smoke tests.

## Benchmarking

- versioned benchmark cases with clearly licensed references;
- machine-readable run manifests;
- human review rubric;
- optional silhouette IoU and landmark-error metrics;
- agent/runtime comparison reports that distinguish tool failure from modeling quality.

## Non-goals

OCW does not aim to hide the construction process behind a single opaque score or promise one-click production-ready characters. The workbench should make the process easier to inspect, reproduce, compare, and improve.
