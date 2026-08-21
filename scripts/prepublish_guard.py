#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import re
import sys

TEXT_SUFFIXES = {
    ".md", ".txt", ".py", ".toml", ".yml", ".yaml", ".json", ".svg", ".sh", ".ini", ".cfg", ".gitignore"
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|access[_-]?token|secret|password)\s*[:=]\s*['\"]?[^\s'\"]{8,}"),
    re.compile(r"sk-[A-Za-z0-9_-]{16,}"),
    re.compile(r"AIza[0-9A-Za-z_-]{20,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9]{20,}"),
]

SUSPICIOUS_PATH_PARTS = {".env", "credentials", "secrets", "private", "client"}
MAX_PUBLIC_BINARY = 10 * 1024 * 1024


def scan(root: Path) -> list[str]:
    problems: list[str] = []
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(root)
        lowered_parts = {p.lower() for p in rel.parts}
        if lowered_parts & SUSPICIOUS_PATH_PARTS:
            problems.append(f"suspicious path: {rel}")
        if path.stat().st_size > MAX_PUBLIC_BINARY and path.suffix.lower() not in TEXT_SUFFIXES:
            problems.append(f"large binary requires manual review: {rel} ({path.stat().st_size} bytes)")
        if path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "NOTICE", ".gitignore"}:
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            for pattern in SECRET_PATTERNS:
                if pattern.search(text):
                    problems.append(f"possible secret in text: {rel}")
                    break
    return sorted(set(problems))


def main() -> int:
    parser = argparse.ArgumentParser(description="Conservative public-package guard")
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    problems = scan(root)
    if problems:
        print("prepublish guard FAILED")
        for item in problems:
            print(f"- {item}")
        return 2
    print("prepublish guard OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
