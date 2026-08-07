#!/usr/bin/env python3
"""Validate Super PM lens structure, aliases, and source-free role cards."""

from __future__ import annotations

import re
import sys
from pathlib import Path


THINKER_FILES = {
    "jobs.md": ("SJ", "乔老师"),
    "zhang-xiaolong.md": ("ZX", "张老师"),
    "liang-ning.md": ("LN", "梁老师"),
    "yu-jun.md": ("YJ", "俞老师"),
    "wang-shimu.md": ("WS", "王老师"),
    "li-xiang.md": ("LX", "李老师"),
    "lei-jun.md": ("LJ", "雷老师"),
}
PRINCIPLE_RE = re.compile(r"^### (?P<id>[A-Z]{2}-P\d{2})\b", re.MULTILINE)
URL_RE = re.compile(r"https?://|www\.", re.IGNORECASE)
FORBIDDEN_NAMES = (
    "Steve Jobs",
    "Zhang Xiaolong",
    "Liang Ning",
    "Yu Jun",
    "Wang Shimu",
    "Li Xiang",
    "Lei Jun",
    "乔布斯",
    "张小龙",
    "梁宁",
    "俞军",
    "王诗沐",
    "李想",
    "雷军",
)


def validate_file(path: Path, prefix: str, alias: str) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    principle_ids = [match.group("id") for match in PRINCIPLE_RE.finditer(text)]

    if len(principle_ids) < 10:
        errors.append(
            f"{path.name}: expected at least 10 principle cards, "
            f"found {len(principle_ids)}"
        )
    if len(principle_ids) != len(set(principle_ids)):
        errors.append(f"{path.name}: duplicate principle IDs found")
    wrong_prefix = [item for item in principle_ids if not item.startswith(f"{prefix}-P")]
    if wrong_prefix:
        errors.append(
            f"{path.name}: principle IDs use the wrong prefix: "
            f"{', '.join(wrong_prefix)}"
        )
    if not text.startswith(f"# {alias} Lens\n"):
        errors.append(f"{path.name}: expected alias heading '# {alias} Lens'")

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
        if count != len(principle_ids):
            errors.append(
                f"{path.name}: expected {len(principle_ids)} '{field}' fields, "
                f"found {count}"
            )

    if URL_RE.search(text):
        errors.append(f"{path.name}: role files must not contain research links")
    if "Source basis" in text or "## Sources" in text:
        errors.append(f"{path.name}: role files must not contain source metadata")
    exposed = [name for name in FORBIDDEN_NAMES if name in text]
    if exposed:
        errors.append(
            f"{path.name}: user-visible real names found: {', '.join(exposed)}"
        )

    return errors


def main() -> int:
    references = Path(__file__).resolve().parent.parent / "references"
    errors: list[str] = []

    for filename, (prefix, alias) in THINKER_FILES.items():
        path = references / filename
        if not path.exists():
            errors.append(f"missing thinker reference: {filename}")
            continue
        errors.extend(validate_file(path, prefix, alias))

    if errors:
        print("Lens validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Lens validation passed for {len(THINKER_FILES)} aliased thinker "
        "references with no role-file links or source metadata."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
