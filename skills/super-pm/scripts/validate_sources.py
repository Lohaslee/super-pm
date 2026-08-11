#!/usr/bin/env python3
"""Validate Super PM lens cards, workflow contracts, and local references."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


THINKER_FILES = {
    "乔帮主.md": ("SJ", "乔帮主"),
    "龙哥.md": ("ZX", "龙哥"),
    "梁老师.md": ("LN", "梁老师"),
    "俞老师.md": ("YJ", "俞老师"),
    "师母.md": ("WS", "师母"),
    "想哥.md": ("LX", "想哥"),
    "军哥.md": ("LJ", "军哥"),
}
OFFICIAL_ALIASES = ("乔帮主", "龙哥", "梁老师", "俞老师", "师母", "想哥", "军哥")
DEPRECATED_ALIASES = ("乔老师", "张老师", "王老师", "李老师", "雷老师")
PRINCIPLE_RE = re.compile(r"^### (?P<id>[A-Z]{2}-P\d{2})\b", re.MULTILINE)
CONFIDENCE_RE = re.compile(r"^- Confidence: (?P<value>\S+)\s*$", re.MULTILINE)
ZH_CONFIDENCE_RE = re.compile(r"^- 可信度：(?P<value>\S+)\s*$", re.MULTILINE)
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\((?P<target>[^)]+)\)")
URL_RE = re.compile(r"https?://|www\.", re.IGNORECASE)
ALLOWED_CONFIDENCE = {"high", "medium", "tentative"}
ALLOWED_ZH_CONFIDENCE = {"高", "中", "暂定"}
MIN_ZH_PRINCIPLES = 13
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


def normalized_principle(value: str) -> str:
    """Normalize formatting-only differences without judging semantic similarity."""
    return re.sub(r"[\W_]+", "", value.casefold())


def duplicate_principles(text: str, field: str) -> list[str]:
    values = re.findall(rf"^- {re.escape(field)}\s*(.+?)\s*$", text, re.MULTILINE)
    seen: dict[str, str] = {}
    duplicates: list[str] = []
    for value in values:
        normalized = normalized_principle(value)
        if normalized in seen:
            duplicates.append(value)
        else:
            seen[normalized] = value
    return duplicates


def validate_file(path: Path, prefix: str, alias: str) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    principle_ids = [match.group("id") for match in PRINCIPLE_RE.finditer(text)]
    confidence_values = [
        match.group("value") for match in CONFIDENCE_RE.finditer(text)
    ]

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

    if len(confidence_values) != len(principle_ids):
        errors.append(
            f"{path.name}: expected {len(principle_ids)} confidence values, "
            f"found {len(confidence_values)}"
        )
    invalid_confidence = sorted(set(confidence_values) - ALLOWED_CONFIDENCE)
    if invalid_confidence:
        errors.append(
            f"{path.name}: invalid confidence values: "
            f"{', '.join(invalid_confidence)}"
        )

    repeated_principles = duplicate_principles(text, "Distilled principle:")
    if repeated_principles:
        errors.append(
            f"{path.name}: duplicate distilled principles found: "
            f"{'; '.join(repeated_principles)}"
        )

    if URL_RE.search(text):
        errors.append(f"{path.name}: role files must not contain research links")
    if "Source basis" in text or "## Sources" in text:
        errors.append(f"{path.name}: role files must not contain source metadata")
    return errors


def validate_zh_file(path: Path, prefix: str, alias: str) -> list[str]:
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    principle_ids = [match.group("id") for match in PRINCIPLE_RE.finditer(text)]
    confidence_values = [
        match.group("value") for match in ZH_CONFIDENCE_RE.finditer(text)
    ]

    if len(principle_ids) < MIN_ZH_PRINCIPLES:
        errors.append(
            f"zh-CN/{path.name}: expected at least {MIN_ZH_PRINCIPLES} "
            "native Chinese principle cards, "
            f"found {len(principle_ids)}"
        )
    if len(principle_ids) != len(set(principle_ids)):
        errors.append(f"zh-CN/{path.name}: duplicate principle IDs found")
    wrong_prefix = [item for item in principle_ids if not item.startswith(f"{prefix}-P")]
    if wrong_prefix:
        errors.append(
            f"zh-CN/{path.name}: principle IDs use the wrong prefix: "
            f"{', '.join(wrong_prefix)}"
        )
    if not text.startswith(f"# {alias}视角\n"):
        errors.append(
            f"zh-CN/{path.name}: expected alias heading '# {alias}视角'"
        )

    required_fields = (
        "- 提炼原则：",
        "- 适用：",
        "- 追问：",
        "- 决策规则：",
        "- 边界：",
        "- 可信度：",
    )
    for field in required_fields:
        count = text.count(field)
        if count != len(principle_ids):
            errors.append(
                f"zh-CN/{path.name}: expected {len(principle_ids)} "
                f"'{field}' fields, found {count}"
            )

    if len(confidence_values) != len(principle_ids):
        errors.append(
            f"zh-CN/{path.name}: expected {len(principle_ids)} confidence "
            f"values, found {len(confidence_values)}"
        )
    invalid_confidence = sorted(set(confidence_values) - ALLOWED_ZH_CONFIDENCE)
    if invalid_confidence:
        errors.append(
            f"zh-CN/{path.name}: invalid confidence values: "
            f"{', '.join(invalid_confidence)}"
        )

    repeated_principles = duplicate_principles(text, "提炼原则：")
    if repeated_principles:
        errors.append(
            f"zh-CN/{path.name}: duplicate distilled principles found: "
            f"{'; '.join(repeated_principles)}"
        )

    if "不是英文卡片" not in text:
        errors.append(
            f"zh-CN/{path.name}: must state that Chinese principles are not "
            "translated from the English cards"
        )
    if "- Distilled principle:" in text or "- Decision rule:" in text:
        errors.append(
            f"zh-CN/{path.name}: English role-card fields found in Chinese file"
        )
    if URL_RE.search(text):
        errors.append(f"zh-CN/{path.name}: role files must not contain research links")
    if any(marker in text for marker in ("Source basis", "## Sources", "## 资料来源")):
        errors.append(
            f"zh-CN/{path.name}: role files must not contain source metadata"
        )
    return errors


def validate_local_links(skill_root: Path) -> list[str]:
    errors: list[str] = []

    for path in skill_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group("target").strip()
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue

            target_path = unquote(target.split("#", 1)[0].strip("<>"))
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            if not resolved.exists():
                relative_path = path.relative_to(skill_root)
                errors.append(
                    f"{relative_path}: broken local link '{target}'"
                )

    return errors


def validate_alias_exposure(skill_root: Path) -> list[str]:
    errors: list[str] = []

    for path in skill_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        exposed = [name for name in FORBIDDEN_NAMES if name in text]
        if exposed:
            relative_path = path.relative_to(skill_root)
            errors.append(
                f"{relative_path}: user-visible real names found: "
                f"{', '.join(exposed)}"
            )
        deprecated = [alias for alias in DEPRECATED_ALIASES if alias in text]
        if deprecated:
            relative_path = path.relative_to(skill_root)
            errors.append(
                f"{relative_path}: deprecated lens aliases found: "
                f"{', '.join(deprecated)}"
            )

    for relative_path in (
        "SKILL.md",
        "references/voice-guidance.md",
        "references/zh-CN/voice-guidance.md",
    ):
        text = (skill_root / relative_path).read_text(encoding="utf-8")
        missing = [alias for alias in OFFICIAL_ALIASES if alias not in text]
        if missing:
            errors.append(
                f"{relative_path}: official lens aliases missing: "
                f"{', '.join(missing)}"
            )

    return errors


def validate_workflow_contract(skill_root: Path) -> list[str]:
    errors: list[str] = []
    required_markers = {
        "SKILL.md": (
            "Choose The Working Language",
            "Default to Simplified Chinese",
            "references/zh-CN/",
            "Focused shaping",
            "Default Decision Loop",
            "If one pass can answer the user's question, answer it now",
            "Deliver The Smallest Useful Explanation",
            ".super-pm/decisions.md",
            "Principle IDs are maintenance metadata",
            "Validation Record",
            "Primary Owner",
            "references/product-dimensions.md",
            "product-lens alias",
        ),
        "references/lens-router.md": (
            "Primary Ownership",
            "Challenger Rule",
        ),
        "references/product-dimensions.md": (
            "Adaptive Product Dimensions",
            "Cross-Cutting Constraints",
            "AI product",
            "Hardware or physical product",
            "Service",
        ),
        "references/prd-template.md": (
            "Adaptive PRD Template",
            "One-Page Decision Brief",
            "Optional Product-Type Modules",
            "Observed result",
            "Decision changed or retained",
        ),
        "references/voice-guidance.md": (
            "short original quotation",
            "Never extend, remix, or fabricate",
            "Professional And Plain",
            "Deep Reasoning, Selective Delivery",
            "Pointed Closing",
            "internal principle IDs",
            "product-lens alias",
        ),
        "references/zh-CN/lens-router.md": (
            "产品视角路由",
            "主责分工",
            "挑战者门槛",
        ),
        "references/zh-CN/product-dimensions.md": (
            "自适应产品维度",
            "AI 产品",
            "硬件或实体产品",
            "服务产品",
            "横向约束",
        ),
        "references/zh-CN/conflict-resolution.md": (
            "产品视角冲突处理",
            "处理顺序",
        ),
        "references/zh-CN/prd-template.md": (
            "自适应 PRD 模板",
            "一页决策简报",
            "按产品类型选用的模块",
            "实际结果",
            "保留或修改的决定",
        ),
        "references/zh-CN/voice-guidance.md": (
            "中文表达指引",
            "原文锚点",
            "不延伸、拼接或编造引语",
            "专业但说人话",
            "深入简出",
            "点睛式收尾",
            "我所说的都是错的",
            "内部原则编号",
            "产品视角化名",
        ),
        "references/worked-example.md": (
            "Worked Example",
            "User-Facing Answer",
            "Why The Workflow Stops Here",
        ),
        "references/zh-CN/worked-example.md": (
            "中文工作样例",
            "面向用户的回答",
            "我所说的都是错的",
            "为什么不继续展开",
        ),
        "references/behavior-evals.md": (
            "Behavior Evaluations",
            "Existing Decision File Without Write Authorization",
            "Lens Conflict",
            "General-Audience Clarity And Hidden IDs",
            "Selective Delivery With Material Lenses",
            "Distinctive Without Catchphrase Theater",
        ),
        "references/zh-CN/behavior-evals.md": (
            "中文行为评测",
            "已有决策文件但未授权修改",
            "视角冲突",
            "普通用户可读性与编号隐藏",
            "深入简出但保留有效视角",
            "有味道但不变成口号",
        ),
    }

    for relative_path, markers in required_markers.items():
        path = skill_root / relative_path
        if not path.exists():
            errors.append(f"missing workflow reference: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                errors.append(
                    f"{relative_path}: missing workflow marker '{marker}'"
                )

    interface_path = skill_root / "agents" / "openai.yaml"
    if not interface_path.exists():
        errors.append("missing interface metadata: agents/openai.yaml")
    else:
        interface_text = interface_path.read_text(encoding="utf-8")
        if "不要急着写报告或 PRD" not in interface_text:
            errors.append(
                "agents/openai.yaml: default prompt must keep reports and PRDs optional"
            )

    return errors


def main() -> int:
    skill_root = Path(__file__).resolve().parent.parent
    references = skill_root / "references"
    zh_references = references / "zh-CN"
    errors: list[str] = []

    for filename, (prefix, alias) in THINKER_FILES.items():
        path = references / filename
        if not path.exists():
            errors.append(f"missing thinker reference: {filename}")
            continue
        errors.extend(validate_file(path, prefix, alias))

        zh_path = zh_references / filename
        if not zh_path.exists():
            errors.append(f"missing Chinese thinker reference: zh-CN/{filename}")
            continue
        errors.extend(validate_zh_file(zh_path, prefix, alias))

    errors.extend(validate_local_links(skill_root))
    errors.extend(validate_alias_exposure(skill_root))
    errors.extend(validate_workflow_contract(skill_root))

    if errors:
        print("Lens validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        f"Super PM validation passed for {len(THINKER_FILES)} bilingual aliased "
        "thinker references, language routing, adaptive workflow contracts, "
        "and local links."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
