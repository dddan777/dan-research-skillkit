from __future__ import annotations

from collections import defaultdict

from common import chapter_id_from_filename, load_csv_rows, write_csv, write_json
from project_config import BOOK_DATA_DIR, REPO_ROOT, SKILLS


CATALOG_ROOT = REPO_ROOT / "catalog"


def build_chapter_skill_map() -> dict[str, list[dict[str, str]]]:
    mapping: dict[str, list[dict[str, str]]] = defaultdict(list)
    for skill in SKILLS:
        chapter_id = chapter_id_from_filename(skill["chapter_file"])
        if chapter_id:
            mapping[chapter_id].append(
                {
                    "skill_id": skill["skill_id"],
                    "pack_id": skill["pack_id"],
                }
            )
    return mapping


def main() -> None:
    chapter_skill_map = build_chapter_skill_map()
    sources = load_csv_rows(BOOK_DATA_DIR / "sources_catalog.csv")
    chapter_rows = load_csv_rows(BOOK_DATA_DIR / "chapter_map.csv")

    coverage_rows = []
    source_pack_map: dict[str, set[str]] = defaultdict(set)
    source_skill_map: dict[str, set[str]] = defaultdict(set)

    for row in chapter_rows:
        chapter_metas = chapter_skill_map.get(row["chapter_id"])
        if not chapter_metas:
            continue
        source_id = row["source_id"]
        for chapter_meta in chapter_metas:
            source_pack_map[source_id].add(chapter_meta["pack_id"])
            source_skill_map[source_id].add(chapter_meta["skill_id"])
            coverage_rows.append(
                {
                    "source_id": source_id,
                    "skill_id": chapter_meta["skill_id"],
                    "pack_id": chapter_meta["pack_id"],
                    "coverage": row["coverage"],
                }
            )

    public_rows = []
    for row in sources:
        source_id = row["source_id"]
        theme = row["theme"]
        for skill in SKILLS:
            if skill["pack_id"] == "upgrade":
                continue
            if theme in skill["source_themes"]:
                source_pack_map[source_id].add(skill["pack_id"])
                source_skill_map[source_id].add(skill["skill_id"])
        public_rows.append(
            {
                "source_id": source_id,
                "theme": theme,
                "content_type": row["file_type"].lstrip(".") if row["file_type"] else "directory",
                "derived_role": row["role"],
                "pack_ids": ";".join(sorted(source_pack_map.get(source_id, set()))),
            }
        )

    backlog_rows = [
        {
            "item_id": "audio-backlog",
            "topic": "audio",
            "status": "pending",
            "note": "Audio material stays outside the public release until it is transcribed and normalized.",
        },
        {
            "item_id": "template-backlog",
            "topic": "templates",
            "status": "pending",
            "note": "Editable templates should be reconstructed into neutral checklists before publication.",
        },
        {
            "item_id": "image-heavy-backlog",
            "topic": "ocr",
            "status": "pending",
            "note": "Image-heavy PDFs require OCR or manual normalization before deeper reuse.",
        },
    ]

    skill_map = {
        skill["skill_id"]: {
            "pack_id": skill["pack_id"],
            "title_zh": skill["title_zh"],
            "title_en": skill["title_en"],
            "related_skills": skill["related_skills"],
        }
        for skill in SKILLS
    }

    write_csv(
        CATALOG_ROOT / "sources_public.csv",
        public_rows,
        ["source_id", "theme", "content_type", "derived_role", "pack_ids"],
    )
    write_csv(
        CATALOG_ROOT / "coverage_matrix.csv",
        coverage_rows,
        ["source_id", "skill_id", "pack_id", "coverage"],
    )
    write_csv(
        CATALOG_ROOT / "backlog.csv",
        backlog_rows,
        ["item_id", "topic", "status", "note"],
    )
    write_json(CATALOG_ROOT / "skill_map.json", skill_map)


if __name__ == "__main__":
    main()
