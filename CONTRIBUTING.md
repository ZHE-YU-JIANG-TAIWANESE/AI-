# Contributing

Thanks for improving Open Character Workbench.

## Ground rules

- Keep the core vendor-neutral: adapters may target specific agents, but the job/evidence/delivery contracts should not require one model provider.
- Do not commit private references, client art, credentials, API keys, access tokens, or proprietary model files.
- Prefer deterministic, inspectable helpers for measurements, staging, validation, and rendering.
- Preserve timestamps and provenance when adding run records or benchmark results.
- A green CI run is not proof of artistic quality. Keep infrastructure checks separate from human/artistic review.

## Development

```bash
python -m pip install -e .
python -m compileall -q src
python -m unittest discover -s tests -v
ocw --help
```

## Pull requests

Describe what changed, why it is useful, how it was tested, and whether any new asset has redistribution permission. For benchmark changes, state the evidence conditions clearly so results remain comparable.
