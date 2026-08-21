from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "ocw.job.v1"


def now_iso() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass(slots=True)
class Reference:
    label: str
    path: str
    sha256: str
    bytes: int


@dataclass(slots=True)
class Job:
    schema_version: str
    job_id: str
    created_at: str
    task_type: str
    references: list[Reference]
    evidence_policy: dict[str, Any] = field(default_factory=dict)
    delivery: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def write(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(self.to_dict(), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    @classmethod
    def read(cls, path: Path) -> "Job":
        payload = json.loads(path.read_text(encoding="utf-8"))
        refs = [Reference(**r) for r in payload.pop("references")]
        return cls(references=refs, **payload)


def reference_from_path(label: str, path: Path) -> Reference:
    p = path.expanduser().resolve()
    if not p.is_file():
        raise FileNotFoundError(p)
    return Reference(label=label, path=str(p), sha256=sha256_file(p), bytes=p.stat().st_size)
