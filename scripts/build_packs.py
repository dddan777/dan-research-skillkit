from __future__ import annotations

import csv
import json
from pathlib import Path

import re

from common import chapter_id_from_filename, ensure_dir, load_csv_rows, write_json, write_text
from project_config import BOOK_DATA_DIR, PRIVATE_CACHE_DIR, REPO_ROOT, SKILLS


PACKS_ROOT = REPO_ROOT / "knowledge" / "packs"
MANIFESTS_ROOT = REPO_ROOT / "knowledge" / "manifests"
EXTRACT_INDEX = PRIVATE_CACHE_DIR / "pdf_extracts" / "index.json"


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
    situations = "\n".join(f"- {item}" for item in skill.get("situations", []))
    workflow = "\n".join(
        f"{idx}. {item}" for idx, item in enumerate(skill.get("workflow_steps", []), start=1)
    )
    rules = "\n".join(f"- {item}" for item in skill.get("decision_rules", []))
    deliverables = "\n".join(f"- {item}" for item in skill.get("deliverables", []))
    pitfalls = "\n".join(f"- {item}" for item in skill.get("pitfalls", []))
    prompts = "\n".join(f"- {item}" for item in skill.get("example_prompts", []))
    corpus = build_corpus_snapshot(skill)
    return f"""# {skill['title_zh']} / {skill['title_en']}

## Summary / 简介
{skill['pack_summary_en']}

{skill['pack_summary_zh']}

## When To Use / 何时调用
{triggers}

## Research Situations / 适用情境
{situations}

## Core Concepts / 核心概念
{concepts}

## Frameworks / 方法框架
{frameworks}

## Expanded Workflow / 扩展工作流
{workflow}

## Decision Rules / 判断规则
{rules}

## Checklists / 检查清单
{checklists}

## Templates / 模板与清单框
{templates}

## Suggested Deliverables / 建议产出
{deliverables}

## Common Pitfalls / 常见误区
{pitfalls}

## Local Corpus Signals / 本地语料覆盖信号
{corpus}

## Example Prompts / 调用示例
{prompts}

## Related Skills / 关联技能
{related}

## Pack Coverage / Pack 覆盖
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
        "situations": skill.get("situations", []),
        "workflow_steps": skill.get("workflow_steps", []),
        "decision_rules": skill.get("decision_rules", []),
        "deliverables": skill.get("deliverables", []),
        "pitfalls": skill.get("pitfalls", []),
        "example_prompts": skill.get("example_prompts", []),
        "corpus_snapshot": corpus_snapshot(skill),
        "source_ids": source_ids,
    }


def load_local_extracts() -> list[dict[str, object]]:
    if not EXTRACT_INDEX.exists():
        return []
    try:
        items = json.loads(EXTRACT_INDEX.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return []
    unique = {}
    for item in items:
        source_id = item.get("source_id")
        if isinstance(source_id, str) and source_id:
            unique[source_id] = item
    return list(unique.values())


LOCAL_EXTRACTS = load_local_extracts()


def corpus_snapshot(skill: dict[str, object]) -> dict[str, object]:
    buckets = []
    total = 0
    for bucket in skill.get("corpus_buckets", []):
        count = 0
        for item in LOCAL_EXTRACTS:
            rel_path = str(item.get("relative_path", "")).lower()
            if any(keyword.lower() in rel_path for keyword in bucket["keywords"]):
                count += 1
        buckets.append({"label": bucket["label"], "count": count})
        total += count
    return {
        "matched_extracts": total,
        "bucket_counts": buckets,
    }


def build_corpus_snapshot(skill: dict[str, object]) -> str:
    snapshot = corpus_snapshot(skill)
    if not snapshot["bucket_counts"]:
        return "- Local extraction snapshot is not available yet."
    lines = [f"- matched unique extracts: {snapshot['matched_extracts']}"]
    for bucket in snapshot["bucket_counts"]:
        lines.append(f"- {bucket['label']}: {bucket['count']}")
    return "\n".join(lines)


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
