from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class ValidationResult:
    ok: bool
    errors: list[str]
    discovered: dict[str, list[str]]


def _files(root: Path) -> list[Path]:
    return [p for p in root.rglob("*") if p.is_file()]


def _match(files: list[Path], needles: tuple[str, ...], suffixes: tuple[str, ...]) -> list[Path]:
    out: list[Path] = []
    for p in files:
        name = p.name.lower()
        if p.suffix.lower() in suffixes and any(n in name for n in needles):
            out.append(p)
    return out


def validate_delivery(delivery: Path) -> ValidationResult:
    root = delivery.expanduser().resolve()
    errors: list[str] = []
    if not root.is_dir():
        return ValidationResult(False, [f"delivery directory not found: {root}"], {})

    files = _files(root)
    blends = [p for p in files if p.suffix.lower() == ".blend"]
    images = (".png", ".jpg", ".jpeg", ".webp")
    front = _match(files, ("front",), images)
    side = _match(files, ("side",), images)
    threeq = _match(files, ("threeq", "three-q", "3q", "three_quarter", "three-quarter"), images)
    notes = [
        p for p in files
        if p.suffix.lower() in (".md", ".txt")
        and any(k in p.name.lower() for k in ("handoff", "readme", "report"))
    ]

    if not blends:
        errors.append("missing editable .blend")
    if not front:
        errors.append("missing front preview")
    if not side:
        errors.append("missing side preview")
    if not threeq:
        errors.append("missing three-quarter preview")
    if not notes:
        errors.append("missing handoff note")

    discovered = {
        "blend": [str(p.relative_to(root)) for p in blends],
        "front": [str(p.relative_to(root)) for p in front],
        "side": [str(p.relative_to(root)) for p in side],
        "three_quarter": [str(p.relative_to(root)) for p in threeq],
        "handoff": [str(p.relative_to(root)) for p in notes],
    }
    return ValidationResult(not errors, errors, discovered)
