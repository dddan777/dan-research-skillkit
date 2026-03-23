from __future__ import annotations

from pathlib import Path

from common import ensure_dir, write_json, write_text
from project_config import REPO_ROOT, SKILLS


SKILLS_SRC_ROOT = REPO_ROOT / "skills-src"
MANIFESTS_ROOT = REPO_ROOT / "knowledge" / "manifests"


def build_skill_md(skill: dict[str, object]) -> str:
    triggers = "\n".join(f"- {item}" for item in skill["triggers"])
    scope_in = "\n".join(f"- {item}" for item in skill["scope_in"])
    scope_out = "\n".join(f"- {item}" for item in skill["scope_out"])
    related = "\n".join(f"- `{item}`" for item in skill["related_skills"])
    pack_ref = f"../../knowledge/packs/{skill['dir_name']}/README.md"
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

## Working Style / 工作方式
1. Clarify the user's research stage, target output, and current bottleneck.
2. Route the request through the pack-specific framework instead of giving generic motivation.
3. Produce a practical next step: checklist, outline, matrix, workflow, or decision note.
4. Recommend one adjacent `dan-*` skill when the task crosses boundaries.

## Scope In / 负责范围
{scope_in}

## Scope Out / 不负责范围
{scope_out}

## Knowledge Pack / 对应知识包
- Read `{pack_ref}` when you need the pack summary, frameworks, and checklists.

## Related Skills / 关联技能
{related}

## Output Contract / 输出要求
- Keep answers concrete and stage-aware.
- Prefer structured notes, checklists, and decision matrices over abstract encouragement.
- If the user needs another `dan-*` skill, say so explicitly and explain why.
"""


def build_openai_yaml(skill: dict[str, object]) -> str:
    default_prompt = skill["triggers"][0]
    return f"""display_name: "{skill['skill_id']}"
short_description: "{skill['description_en']}"
default_prompt: "{default_prompt}"
"""


def main() -> None:
    skills_manifest = []
    for skill in SKILLS:
        skill_dir = ensure_dir(SKILLS_SRC_ROOT / skill["skill_id"])
        agents_dir = ensure_dir(skill_dir / "agents")
        write_text(skill_dir / "SKILL.md", build_skill_md(skill))
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
