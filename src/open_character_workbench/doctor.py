from __future__ import annotations

from dataclasses import dataclass, asdict
import json
from pathlib import Path
import shutil
import subprocess


@dataclass(slots=True)
class DoctorResult:
    python_ok: bool
    blender_path: str | None
    blender_version: str | None

    @property
    def ok(self) -> bool:
        return self.python_ok and bool(self.blender_path)

    def to_json(self) -> str:
        payload = asdict(self)
        payload["ok"] = self.ok
        return json.dumps(payload, indent=2, ensure_ascii=False)


def inspect_workstation(blender: str | None = None) -> DoctorResult:
    candidate = blender or shutil.which("blender")
    version = None
    if candidate:
        try:
            proc = subprocess.run(
                [candidate, "--version"],
                check=False,
                capture_output=True,
                text=True,
                timeout=20,
            )
            if proc.stdout:
                version = proc.stdout.splitlines()[0].strip()
        except OSError:
            candidate = None
    return DoctorResult(python_ok=True, blender_path=str(Path(candidate).resolve()) if candidate else None, blender_version=version)
