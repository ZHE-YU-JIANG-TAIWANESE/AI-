from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

from .doctor import inspect_workstation
from .manifest import Job, SCHEMA_VERSION, now_iso, reference_from_path
from .validate import validate_delivery
from .workspace import stage_job


def _slug(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9._-]+", "-", text.strip()).strip("-")
    return value or "character-job"


def cmd_doctor(args: argparse.Namespace) -> int:
    result = inspect_workstation(args.blender)
    print(result.to_json())
    return 0 if result.ok else 2


def cmd_new_job(args: argparse.Namespace) -> int:
    front = Path(args.front)
    side = Path(args.side)
    job_id = _slug(args.job_id or Path(args.output).stem)
    job = Job(
        schema_version=SCHEMA_VERSION,
        job_id=job_id,
        created_at=now_iso(),
        task_type="character-body-from-two-view-references",
        references=[
            reference_from_path("front", front),
            reference_from_path("side", side),
        ],
        evidence_policy={
            "declared_references_are_geometry_evidence": True,
            "prior_models_visible": False,
            "prior_geometry_scripts_visible": False,
            "repository_history_visible": False,
        },
        delivery={
            "required": [
                "editable .blend",
                "front preview",
                "side preview",
                "three-quarter preview",
                "handoff note",
            ]
        },
    )
    output = Path(args.output)
    job.write(output)
    print(output.resolve())
    return 0


def cmd_stage(args: argparse.Namespace) -> int:
    studio = stage_job(Path(args.job), Path(args.studio), force=args.force)
    print(studio)
    return 0


def cmd_validate(args: argparse.Namespace) -> int:
    result = validate_delivery(Path(args.delivery))
    payload = {"ok": result.ok, "errors": result.errors, "discovered": result.discovered}
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if result.ok else 2


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="ocw", description="Open Character Workbench")
    sub = parser.add_subparsers(dest="command", required=True)

    p_doctor = sub.add_parser("doctor", help="Inspect the local Blender workstation")
    p_doctor.add_argument("--blender", help="Optional explicit Blender executable")
    p_doctor.set_defaults(func=cmd_doctor)

    p_new = sub.add_parser("new-job", help="Create a two-view character job manifest")
    p_new.add_argument("--front", required=True, help="Front reference image")
    p_new.add_argument("--side", required=True, help="Side reference image")
    p_new.add_argument("--output", required=True, help="Output JOB.json path")
    p_new.add_argument("--job-id", help="Optional stable job identifier")
    p_new.set_defaults(func=cmd_new_job)

    p_stage = sub.add_parser("stage", help="Create an evidence-isolated studio")
    p_stage.add_argument("--job", required=True, help="Job manifest")
    p_stage.add_argument("--studio", required=True, help="Studio directory")
    p_stage.add_argument("--force", action="store_true", help="Replace an existing non-empty studio")
    p_stage.set_defaults(func=cmd_stage)

    p_validate = sub.add_parser("validate", help="Validate a character delivery")
    p_validate.add_argument("--delivery", required=True, help="vendor-output directory")
    p_validate.set_defaults(func=cmd_validate)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
