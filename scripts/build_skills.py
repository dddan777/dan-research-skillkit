from __future__ import annotations

import json
from pathlib import Path

from common import ensure_dir, write_json, write_text
from project_config import REPO_ROOT, SKILLS


SKILLS_SRC_ROOT = REPO_ROOT / "skills-src"
MANIFESTS_ROOT = REPO_ROOT / "knowledge" / "manifests"
PACKS_MANIFEST = MANIFESTS_ROOT / "packs.json"

SPECIAL_NOTES = {
    "dan-research": [
        "Treat this skill as a router and stage-diagnosis layer first, not a place to solve every downstream task in depth.",
        "If the user's real bottleneck clearly belongs to literature, theory, design, writing, submission, or defense, route there after producing a short diagnosis note.",
    ],
    "dan-upgrade": [
        "Audit repository state, source freshness, generated artifacts, and host layouts before editing anything.",
        "Prefer reproducible regeneration through scripts over one-off manual changes.",
    ],
}


def load_pack_manifest() -> dict[str, dict[str, object]]:
    if not PACKS_MANIFEST.exists():
        return {}
    data = json.loads(PACKS_MANIFEST.read_text())
    return {item["pack_id"]: item for item in data}


def format_bullets(items: list[str], prefix: str = "- ") -> str:
    return "\n".join(f"{prefix}{item}" for item in items)


def format_frameworks(frameworks: list[dict[str, str]]) -> str:
    return "\n".join(
        f"1. **{item['title']}**: {item['description']}" for item in frameworks
    )


def format_related(skill_ids: list[str], skill_lookup: dict[str, dict[str, object]]) -> str:
    lines = []
    for skill_id in skill_ids:
        related = skill_lookup[skill_id]
        lines.append(
            f"- `{skill_id}`: {related['description_en']} / {related['description_zh']}"
        )
    return "\n".join(lines)


def format_scope_rule(items: list[str], heading: str) -> str:
    return f"- Use this skill when the main task is about {heading}: " + ", ".join(items) + "."


def format_corpus_snapshot(pack: dict[str, object]) -> str:
    snapshot = pack.get("corpus_snapshot") or {}
    matched = snapshot.get("matched_extracts")
    buckets = snapshot.get("bucket_counts") or []
    lines = []
    if matched is not None:
        lines.append(f"- matched local extracts: {matched}")
    for bucket in buckets[:4]:
        lines.append(f"- {bucket['label']}: {bucket['count']}")
    return "\n".join(lines) if lines else "- no local corpus snapshot available"


def build_skill_md(
    skill: dict[str, object],
    pack: dict[str, object],
    skill_lookup: dict[str, dict[str, object]],
) -> str:
    triggers = "\n".join(f"- {item}" for item in skill["triggers"])
    scope_in = "\n".join(f"- {item}" for item in skill["scope_in"])
    scope_out = "\n".join(f"- {item}" for item in skill["scope_out"])
    related = format_related(skill["related_skills"], skill_lookup)
    pack_ref = f"../../knowledge/packs/{skill['dir_name']}/README.md"
    situations = format_bullets(pack.get("situations", []))
    concepts = format_bullets(pack.get("concepts", []))
    frameworks = format_frameworks(pack.get("frameworks", []))
    workflow_steps = [
        "Start by restating the user's current stage, target output, and blocking point in one sentence."
    ]
    workflow_steps.extend(pack.get("workflow_steps", []))
    if skill["skill_id"] in SPECIAL_NOTES:
        workflow_steps.extend(SPECIAL_NOTES[skill["skill_id"]])
    workflow = "\n".join(f"1. {item}" for item in workflow_steps)
    decision_rules = format_bullets(pack.get("decision_rules", []))
    deliverables = format_bullets(pack.get("deliverables", []))
    templates = format_bullets(
        [f"`{item}`" for item in pack.get("templates", []) + pack.get("checklists", [])]
    )
    example_prompts = format_bullets(pack.get("example_prompts", []))
    corpus_snapshot = format_corpus_snapshot(pack)
    first_response_pattern = "\n".join(
        [
            "1. Diagnose the situation before offering tools or motivation.",
            "1. Choose one main framework from this skill instead of mixing multiple frameworks at once.",
            "1. Give 3-5 concrete steps that can be acted on immediately.",
            "1. Produce one usable output: outline, checklist, table, matrix, script, or note.",
            "1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.",
        ]
    )
    output_contract = "\n".join(
        [
            "- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.",
            "- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.",
            "- If the user asks for a draft, give a working draft rather than only describing what to write.",
            "- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.",
        ]
    )
    return f"""---
name: "{skill['skill_id']}"
description: "{skill['description_en']} {skill['description_zh']}"
---

# {skill['skill_id']}

## Purpose / 用途
{skill['description_en']}

{skill['description_zh']}

## When To Use / 触发场景
{triggers}

## Typical Situations / 典型情境
{situations}

## Core Concepts / 核心概念
{concepts}

## Main Frameworks / 主方法框架
{frameworks}

## First Response Pattern / 首轮回答模式
{first_response_pattern}

## Operating Procedure / 执行流程
{workflow}

## Decision Rules / 判断规则
{decision_rules}

## Default Deliverables / 默认产出
{deliverables}

## Templates And Checklists / 模板与清单
{templates}

## Example Prompts / 调用示例
{example_prompts}

## Local Corpus Signals / 本地语料信号
{corpus_snapshot}

## Scope In / 负责范围
{scope_in}

## Scope Out / 不负责范围
{scope_out}

## Routing Rules / 交接规则
{format_scope_rule(skill["scope_in"], "scope in")}
{format_scope_rule(skill["scope_out"], "scope out")}
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `{pack_ref}` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
{related}

## Output Contract / 输出要求
{output_contract}
"""


def build_openai_yaml(skill: dict[str, object]) -> str:
    default_prompt = skill["triggers"][0]
    return f"""display_name: "{skill['skill_id']}"
short_description: "{skill['description_en']}"
default_prompt: "{default_prompt}"
"""


def main() -> None:
    pack_lookup = load_pack_manifest()
    skill_lookup = {skill["skill_id"]: skill for skill in SKILLS}
    skills_manifest = []
    for skill in SKILLS:
        pack = pack_lookup.get(skill["pack_id"], {})
        skill_dir = ensure_dir(SKILLS_SRC_ROOT / skill["skill_id"])
        agents_dir = ensure_dir(skill_dir / "agents")
        write_text(skill_dir / "SKILL.md", build_skill_md(skill, pack, skill_lookup))
        write_text(agents_dir / "openai.yaml", build_openai_yaml(skill))
        skills_manifest.append(
            {
                "skill_id": skill["skill_id"],
                "name": skill["skill_id"],
                "description_zh": skill["description_zh"],
                "description_en": skill["description_en"],
                "triggers": skill["triggers"],
                "pack_ids": [skill["pack_id"]],
                "related_skills": skill["related_skills"],
                "scope_in": skill["scope_in"],
                "scope_out": skill["scope_out"],
            }
        )

    write_json(MANIFESTS_ROOT / "skills.json", skills_manifest)


if __name__ == "__main__":
    main()
