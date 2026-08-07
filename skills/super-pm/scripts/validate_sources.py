#!/usr/bin/env python3
"""Validate source and principle structure in Super PM thinker references."""

from __future__ import annotations

import re
import sys
from pathlib import Path


THINKER_FILES = (
    "jobs.md",
    "zhang-xiaolong.md",
    "liang-ning.md",
    "yu-jun.md",
    "wang-shimu.md",
    "li-xiang.md",
)
SOURCE_RE = re.compile(
    r"^- \[(?P<id>[A-Z]{2,3}-S\d{2})\] \[Tier [123]\] .+ - "
    r"(?P<url>https?://\S+)$",
    re.MULTILINE,
)
PRINCIPLE_RE = re.compile(r"^### (?P<id>[A-Z]{2,3}-P\d{2})\b", re.MULTILINE)
BASIS_RE = re.compile(r"^- Source basis: (?P<ids>[A-Z0-9, -]+)$", re.MULTILINE)


def validate_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    sources = {match.group("id") for match in SOURCE_RE.finditer(text)}
    principles = {match.group("id") for match in PRINCIPLE_RE.finditer(text)}

    if len(sources) < 5:
        errors.append(f"{path.name}: expected at least 5 valid sources, found {len(sources)}")
    if len(principles) < 10:
        errors.append(
            f"{path.name}: expected at least 10 principle cards, found {len(principles)}"
        )

    basis_blocks = list(BASIS_RE.finditer(text))
    if len(basis_blocks) != len(principles):
        errors.append(
            f"{path.name}: expected one Source basis per principle "
            f"({len(principles)}), found {len(basis_blocks)}"
        )

    for match in basis_blocks:
        referenced = {item.strip() for item in match.group("ids").split(",")}
        unknown = referenced - sources
        if unknown:
            errors.append(
                f"{path.name}: undeclared source IDs: {', '.join(sorted(unknown))}"
            )

    required_fields = (
        "- Distilled principle:",
        "- Use when:",
        "- Ask:",
        "- Decision rule:",
        "- Guardrail:",
        "- Confidence:",
    )
    for field in required_fields:
        count = text.count(field)
        if count != len(principles):
            errors.append(
                f"{path.name}: expected {len(principles)} '{field}' fields, found {count}"
            )

    return errors


def main() -> int:
    references = Path(__file__).resolve().parent.parent / "references"
    errors: list[str] = []
    for filename in THINKER_FILES:
        path = references / filename
        if not path.exists():
            errors.append(f"missing thinker reference: {filename}")
            continue
        errors.extend(validate_file(path))

    if errors:
        print("Source validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Source validation passed for {len(THINKER_FILES)} thinker references.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
