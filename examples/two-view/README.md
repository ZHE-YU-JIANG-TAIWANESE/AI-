# Synthetic Two-View Example

This folder contains simple redistributable SVG references made specifically for testing OCW. They are not a real person, character, or client asset.

From the repository root:

```bash
python -m pip install -e .

ocw new-job \
  --front examples/two-view/reference_front.svg \
  --side examples/two-view/reference_side.svg \
  --output .ocw/example-job.json \
  --job-id synthetic-two-view

ocw stage \
  --job .ocw/example-job.json \
  --studio .ocw/studios/synthetic-two-view
```

The staged studio will contain only the declared references plus the job/evidence contracts and an empty `vendor-output/`.

Give that directory to a human artist or agent. When it returns work, validate it with:

```bash
ocw validate --delivery .ocw/studios/synthetic-two-view/vendor-output
```

This example is intentionally simple: it tests the workbench contract, not production-quality anatomy.
