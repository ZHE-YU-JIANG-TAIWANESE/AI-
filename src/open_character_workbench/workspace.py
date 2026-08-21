from __future__ import annotations

import json
from pathlib import Path
import shutil

from .manifest import Job, sha256_file


def stage_job(job_path: Path, studio: Path, *, force: bool = False) -> Path:
    job_path = job_path.expanduser().resolve()
    studio = studio.expanduser().resolve()
    job = Job.read(job_path)

    if studio.exists() and any(studio.iterdir()):
        if not force:
            raise FileExistsError(f"studio is not empty: {studio}")
        shutil.rmtree(studio)

    refs_dir = studio / "references"
    output_dir = studio / "vendor-output"
    refs_dir.mkdir(parents=True, exist_ok=True)
    output_dir.mkdir(parents=True, exist_ok=True)

    staged_refs: list[dict[str, object]] = []
    for ref in job.references:
        src = Path(ref.path)
        if not src.is_file():
            raise FileNotFoundError(src)
        actual = sha256_file(src)
        if actual != ref.sha256:
            raise ValueError(f"reference hash mismatch for {ref.label}: {src}")
        suffix = src.suffix.lower() or ".bin"
        dst = refs_dir / f"{ref.label}{suffix}"
        shutil.copy2(src, dst)
        staged_refs.append({
            "label": ref.label,
            "file": f"references/{dst.name}",
            "sha256": actual,
            "bytes": dst.stat().st_size,
        })

    (studio / "JOB.json").write_text(
        json.dumps(job.to_dict(), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (studio / "EVIDENCE.json").write_text(
        json.dumps({"references": staged_refs, "policy": job.evidence_policy}, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    (studio / "ARTIST_README.md").write_text(
        "# OCW staged studio\n\n"
        "Use `references/` as the declared geometry evidence. Put editable work and review renders in `vendor-output/`.\n"
        "Do not silently import undeclared prior models, scripts, ledgers, or derivatives.\n",
        encoding="utf-8",
    )
    return studio
