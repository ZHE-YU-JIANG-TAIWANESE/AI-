from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from open_character_workbench.manifest import Job, SCHEMA_VERSION, now_iso, reference_from_path
from open_character_workbench.validate import validate_delivery
from open_character_workbench.workspace import stage_job


class WorkbenchTests(unittest.TestCase):
    def test_stage_only_declared_references(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            front = root / "front.png"
            side = root / "side.png"
            front.write_bytes(b"front-evidence")
            side.write_bytes(b"side-evidence")
            job_path = root / "job.json"
            job = Job(
                schema_version=SCHEMA_VERSION,
                job_id="unit-test",
                created_at=now_iso(),
                task_type="character-body-from-two-view-references",
                references=[reference_from_path("front", front), reference_from_path("side", side)],
                evidence_policy={"repository_history_visible": False},
                delivery={"required": ["editable .blend"]},
            )
            job.write(job_path)
            studio = stage_job(job_path, root / "studio")
            self.assertTrue((studio / "references" / "front.png").is_file())
            self.assertTrue((studio / "references" / "side.png").is_file())
            self.assertTrue((studio / "JOB.json").is_file())
            evidence = json.loads((studio / "EVIDENCE.json").read_text(encoding="utf-8"))
            self.assertEqual({r["label"] for r in evidence["references"]}, {"front", "side"})

    def test_stage_detects_changed_reference(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            front = root / "front.png"
            side = root / "side.png"
            front.write_bytes(b"a")
            side.write_bytes(b"b")
            job = Job(
                schema_version=SCHEMA_VERSION,
                job_id="hash-test",
                created_at=now_iso(),
                task_type="test",
                references=[reference_from_path("front", front), reference_from_path("side", side)],
            )
            job_path = root / "job.json"
            job.write(job_path)
            front.write_bytes(b"changed")
            with self.assertRaises(ValueError):
                stage_job(job_path, root / "studio")

    def test_delivery_validation(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            delivery = Path(td)
            (delivery / "model.blend").write_bytes(b"blend")
            (delivery / "FRONT.png").write_bytes(b"png")
            (delivery / "SIDE.png").write_bytes(b"png")
            (delivery / "THREEQ.png").write_bytes(b"png")
            (delivery / "HANDOFF.md").write_text("done", encoding="utf-8")
            result = validate_delivery(delivery)
            self.assertTrue(result.ok, result.errors)

    def test_delivery_validation_reports_missing_files(self) -> None:
        with tempfile.TemporaryDirectory() as td:
            result = validate_delivery(Path(td))
            self.assertFalse(result.ok)
            self.assertIn("missing editable .blend", result.errors)


if __name__ == "__main__":
    unittest.main()
