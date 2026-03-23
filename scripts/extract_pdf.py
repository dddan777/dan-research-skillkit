from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
from collections import Counter
from pathlib import Path

from common import ensure_dir, guess_pack_from_relpath, load_csv_rows, write_json, write_text
from project_config import BOOK_DATA_DIR, PRIVATE_CACHE_DIR, WORKSPACE_ROOT


PDF_OUTPUT_ROOT = PRIVATE_CACHE_DIR / "pdf_extracts"


def sha1_for_path(path: Path) -> str:
    hasher = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def load_pdf_paths(all_pdfs: bool) -> list[tuple[str, Path, str | None]]:
    if all_pdfs:
        rows = load_csv_rows(BOOK_DATA_DIR / "raw_inventory.csv")
        return [
            (row["path"], WORKSPACE_ROOT / row["path"], row.get("sha1") or None)
            for row in rows
            if row["ext"] == ".pdf"
        ]

    sources = load_csv_rows(BOOK_DATA_DIR / "sources_catalog.csv")
    items = []
    for row in sources:
        if row["file_type"] != ".pdf":
            continue
        rel_path = row["canonical_path"]
        items.append((rel_path, WORKSPACE_ROOT / rel_path, row.get("sha1") or None))
    return items


def run_command(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, text=True, capture_output=True, check=False)


def safe_read_json(path: Path) -> dict[str, object] | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return None


def split_pages(raw_text: str) -> list[str]:
    return [page for page in raw_text.split("\f") if page.strip()]


def strip_boilerplate(raw_text: str) -> tuple[str, list[str]]:
    pages = split_pages(raw_text)
    if len(pages) <= 1:
        return raw_text.strip(), []

    line_counts: Counter[str] = Counter()
    page_lines: list[list[str]] = []
    for page in pages:
        lines = [line.strip() for line in page.splitlines() if line.strip()]
        page_lines.append(lines)
        line_counts.update(set(lines))

    threshold = max(2, int(len(pages) * 0.6))
    repeated = {
        line
        for line, count in line_counts.items()
        if count >= threshold and 1 < len(line) <= 80
    }

    cleaned_pages = []
    for lines in page_lines:
        kept = [
            line
            for line in lines
            if line not in repeated and not looks_promotional_line(line)
        ]
        cleaned_pages.append("\n".join(kept).strip())
    return "\n\n".join(page for page in cleaned_pages if page), sorted(repeated)


def looks_promotional_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    bar_count = stripped.count("|") + stripped.count("｜")
    symbol_count = sum(ch in stripped for ch in "@#%&*[]【】<>→←")
    emoji_like = any(ch in stripped for ch in "😾👉🔺🔸⭐️")
    if bar_count >= 2:
        return True
    if symbol_count >= 3 and len(stripped) <= 120:
        return True
    if emoji_like and len(stripped) <= 80:
        return True
    return False


def extract_one(
    rel_path: str,
    pdf_path: Path,
    render_preview: bool,
    force: bool = False,
    known_sha1: str | None = None,
) -> dict[str, object]:
    source_hash = known_sha1
    if not source_hash:
        try:
            source_hash = sha1_for_path(pdf_path)
        except (OSError, TimeoutError):
            source_hash = hashlib.sha1(rel_path.encode("utf-8")).hexdigest()
    source_id = f"pdf-{source_hash[:12]}"
    target_dir = ensure_dir(PDF_OUTPUT_ROOT / source_id)
    metadata_path = target_dir / "metadata.json"
    content_path = target_dir / "content.md"
    if metadata_path.exists() and content_path.exists() and not force:
        cached = safe_read_json(metadata_path)
        if cached is not None:
            return cached
    try:
        info = run_command(["pdfinfo", str(pdf_path)])
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as handle:
            txt_path = Path(handle.name)
        run_command(["pdftotext", "-layout", str(pdf_path), str(txt_path)])
        raw_text = txt_path.read_text(encoding="utf-8", errors="ignore") if txt_path.exists() else ""
        cleaned_text, boilerplate = strip_boilerplate(raw_text)
        txt_path.unlink(missing_ok=True)
        extraction_status = "ok"
        error_message = None
        file_sha1 = source_hash
    except Exception as exc:  # noqa: BLE001
        cleaned_text = ""
        boilerplate = []
        extraction_status = "error"
        error_message = f"{type(exc).__name__}: {exc}"
        file_sha1 = source_hash

    preview_rel = None
    if render_preview and extraction_status == "ok":
        preview_prefix = target_dir / "preview"
        run_command(
            [
                "pdftoppm",
                "-png",
                "-f",
                "1",
                "-singlefile",
                str(pdf_path),
                str(preview_prefix),
            ]
        )
        preview_path = preview_prefix.with_suffix(".png")
        if preview_path.exists():
            preview_rel = str(preview_path.relative_to(PDF_OUTPUT_ROOT))

    metadata = {
        "source_id": source_id,
        "relative_path": rel_path,
        "theme_guess": guess_pack_from_relpath(rel_path),
        "sha1": file_sha1,
        "pdfinfo": info.stdout.strip() if extraction_status == "ok" else "",
        "extraction_status": extraction_status,
        "error_message": error_message,
        "boilerplate_lines_removed": boilerplate,
        "preview": preview_rel,
    }
    markdown = f"# {source_id}\n\n## Source\n- relative_path: `{rel_path}`\n- theme_guess: `{metadata['theme_guess']}`\n\n## Extracted Text\n\n{cleaned_text}\n"
    write_json(target_dir / "metadata.json", metadata)
    write_text(target_dir / "content.md", markdown)
    return metadata


def write_summary_index(summary: list[dict[str, object]]) -> None:
    write_json(PDF_OUTPUT_ROOT / "index.json", summary)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all", action="store_true", help="Process every PDF listed in raw_inventory.csv")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--render-preview", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    items = load_pdf_paths(all_pdfs=args.all)
    if args.limit:
        items = items[: args.limit]

    summary = []
    for idx, (rel_path, pdf_path, known_sha1) in enumerate(items, start=1):
        if not pdf_path.exists():
            continue
        summary.append(
            extract_one(
                rel_path,
                pdf_path,
                render_preview=args.render_preview,
                force=args.force,
                known_sha1=known_sha1,
            )
        )
        if idx % 25 == 0:
            write_summary_index(summary)

    write_summary_index(summary)


if __name__ == "__main__":
    main()
