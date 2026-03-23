from __future__ import annotations

import csv
import json
from pathlib import Path

from common import chapter_id_from_filename, ensure_dir, load_csv_rows, write_json, write_text
from project_config import BOOK_DATA_DIR, REPO_ROOT, SKILLS


PACKS_ROOT = REPO_ROOT / "knowledge" / "packs"
MANIFESTS_ROOT = REPO_ROOT / "knowledge" / "manifests"


def load_source_index() -> tuple[dict[str, dict[str, str]], dict[str, list[dict[str, str]]]]:
    sources = {
        row["source_id"]: row
        for row in load_csv_rows(BOOK_DATA_DIR / "sources_catalog.csv")
    }
    chapter_map: dict[str, list[dict[str, str]]] = {}
    for row in load_csv_rows(BOOK_DATA_DIR / "chapter_map.csv"):
        chapter_map.setdefault(row["chapter_id"], []).append(row)
    return sources, chapter_map


def build_pack_markdown(skill: dict[str, object], source_ids: list[str]) -> str:
    concepts = "\n".join(f"- {item}" for item in skill["concepts"])
    frameworks = "\n".join(
        f"1. **{item['title']}**: {item['description']}" for item in skill["frameworks"]
    )
    checklists = "\n".join(f"- {item}" for item in skill["checklists"])
    templates = "\n".join(f"- `{item}`" for item in skill["templates"])
    triggers = "\n".join(f"- {item}" for item in skill["triggers"])
    related = "\n".join(f"- `{item}`" for item in skill["related_skills"])
    source_lines = "\n".join(f"- `{item}`" for item in source_ids) or "- None yet"
    return f"""# {skill['title_zh']} / {skill['title_en']}

## Summary / 简介
{skill['pack_summary_en']}

{skill['pack_summary_zh']}

## When To Use / 何时调用
{triggers}

## Core Concepts / 核心概念
{concepts}

## Frameworks / 方法框架
{frameworks}

## Checklists / 检查清单
{checklists}

## Templates / 模板与清单框
{templates}

## Related Skills / 关联技能
{related}

## Neutral Source Coverage / 中性来源映射
{source_lines}
"""


def build_pack_json(skill: dict[str, object], source_ids: list[str]) -> dict[str, object]:
    return {
        "pack_id": skill["pack_id"],
        "skill_id": skill["skill_id"],
        "title_zh": skill["title_zh"],
        "title_en": skill["title_en"],
        "summary_zh": skill["pack_summary_zh"],
        "summary_en": skill["pack_summary_en"],
        "concepts": skill["concepts"],
        "frameworks": skill["frameworks"],
        "checklists": skill["checklists"],
        "templates": skill["templates"],
        "source_ids": source_ids,
    }


def main() -> None:
    sources, chapter_map = load_source_index()
    packs_manifest: list[dict[str, object]] = []
    topics_manifest: list[dict[str, object]] = []

    for skill in SKILLS:
        chapter_id = chapter_id_from_filename(skill["chapter_file"])
        mapped_source_ids: list[str] = []
        if chapter_id and chapter_id in chapter_map:
            for row in chapter_map[chapter_id]:
                mapped_source_ids.append(row["source_id"])

        if not mapped_source_ids:
            theme_matches = [
                source_id
                for source_id, row in sources.items()
                if row["theme"] in skill["source_themes"]
            ]
            mapped_source_ids = sorted(theme_matches)

        pack_dir = ensure_dir(PACKS_ROOT / skill["dir_name"])
        markdown = build_pack_markdown(skill, mapped_source_ids)
        pack_json = build_pack_json(skill, mapped_source_ids)

        write_text(pack_dir / "README.md", markdown)
        write_json(pack_dir / "pack.json", pack_json)

        packs_manifest.append(pack_json)
        topics_manifest.append(
            {
                "pack_id": skill["pack_id"],
                "topic": skill["dir_name"],
                "skill_id": skill["skill_id"],
                "source_ids": mapped_source_ids,
            }
        )

    write_json(MANIFESTS_ROOT / "packs.json", packs_manifest)
    write_json(MANIFESTS_ROOT / "topics.json", topics_manifest)


if __name__ == "__main__":
    main()
