from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from common import write_csv, write_json, write_text
from project_config import BOOK_DATA_DIR, REPO_ROOT, SKILLS


EXTRACT_ROOT = REPO_ROOT / "private_cache" / "pdf_extracts"
CATALOG_ROOT = REPO_ROOT / "catalog"
DOCS_ROOT = REPO_ROOT / "docs"


def load_extracts() -> list[dict[str, object]]:
    index_path = EXTRACT_ROOT / "index.json"
    if index_path.exists():
        try:
            return json.loads(index_path.read_text(encoding="utf-8"))
        except Exception:  # noqa: BLE001
            pass
    items = []
    for path in sorted(EXTRACT_ROOT.glob("*/metadata.json")):
        try:
            items.append(json.loads(path.read_text(encoding="utf-8")))
        except Exception:  # noqa: BLE001
            continue
    return items


def normalized_status(item: dict[str, object]) -> str:
    status = item.get("extraction_status")
    if isinstance(status, str) and status:
        return status
    if item.get("error_message"):
        return "error"
    return "ok"


def build_skill_theme_map() -> dict[str, set[str]]:
    mapping: dict[str, set[str]] = defaultdict(set)
    for skill in SKILLS:
        if skill["pack_id"] == "upgrade":
            continue
        for theme in skill["source_themes"]:
            mapping[skill["skill_id"]].add(theme)
    return mapping


def build_release_note(summary: dict[str, object]) -> str:
    theme_lines = "\n".join(
        f"- `{theme}`: {count}"
        for theme, count in summary["theme_counts"]
    )
    skill_lines = "\n".join(
        f"- `{skill_id}`: {count} local extracts routed to this skill family"
        for skill_id, count in summary["skill_counts"]
    )
    return f"""# Collection Status

## Snapshot
- processed extracts: {summary['processed']}
- unique cached extract sets: {summary['unique_extracts']}
- successful extracts: {summary['ok']}
- extraction errors: {summary['error']}
- previews generated: {summary['with_preview']}

## Theme Coverage
{theme_lines}

## Skill Coverage
{skill_lines}

## Notes
- These numbers reflect the local extraction layer only.
- Public repository content is refreshed selectively from this local cache.
- Extraction errors are reviewed before any public-layer update is generated.
"""


def main() -> None:
    extracts = load_extracts()
    status_counter = Counter(normalized_status(item) for item in extracts)
    preview_count = sum(1 for item in extracts if item.get("preview"))
    unique_items: dict[str, dict[str, object]] = {}
    for item in extracts:
        source_id = item.get("source_id")
        if isinstance(source_id, str) and source_id:
            unique_items[source_id] = item
    deduped = list(unique_items.values()) if unique_items else extracts
    theme_counter = Counter(item.get("theme_guess", "unknown") for item in deduped)
    unique_extracts = len(deduped)

    skill_theme_map = build_skill_theme_map()
    skill_counter = Counter()
    for item in deduped:
        theme = item.get("theme_guess", "unknown")
        for skill_id, themes in skill_theme_map.items():
            if theme in themes:
                skill_counter[skill_id] += 1

    summary = {
        "processed": len(extracts),
        "unique_extracts": unique_extracts,
        "ok": status_counter.get("ok", 0),
        "error": status_counter.get("error", 0),
        "with_preview": preview_count,
        "theme_counts": theme_counter.most_common(),
        "skill_counts": skill_counter.most_common(),
    }

    write_json(CATALOG_ROOT / "extraction_summary.json", summary)
    write_csv(
        CATALOG_ROOT / "extraction_by_theme.csv",
        [
            {"theme": theme, "count": count}
            for theme, count in theme_counter.most_common()
        ],
        ["theme", "count"],
    )
    write_csv(
        CATALOG_ROOT / "extraction_by_skill.csv",
        [
            {"skill_id": skill_id, "count": count}
            for skill_id, count in skill_counter.most_common()
        ],
        ["skill_id", "count"],
    )
    write_text(DOCS_ROOT / "collection-status.md", build_release_note(summary))


if __name__ == "__main__":
    main()
