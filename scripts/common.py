from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Iterable

from project_config import TOP_LEVEL_PREFIX_HINTS


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_json(path: Path, data: object) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(path: Path, rows: Iterable[dict[str, object]], fieldnames: list[str]) -> None:
    ensure_dir(path.parent)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def chapter_id_from_filename(filename: str | None) -> str | None:
    if not filename:
        return None
    match = re.match(r"(ch\d{2})_", filename)
    return match.group(1) if match else None


def normalize_whitespace(text: str) -> str:
    return re.sub(r"[ \t]+", " ", text).strip()


def prefix_from_relpath(rel_path: str) -> str:
    first_segment = rel_path.split("/", 1)[0]
    return first_segment.split(".", 1)[0]


def guess_pack_from_relpath(rel_path: str) -> str:
    return TOP_LEVEL_PREFIX_HINTS.get(prefix_from_relpath(rel_path), "unknown")
