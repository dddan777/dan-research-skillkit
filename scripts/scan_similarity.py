from __future__ import annotations

import argparse
import itertools
import re
from pathlib import Path

from project_config import BOOK_CHAPTERS_DIR, REPO_ROOT


PUBLIC_GLOBS = ["README.md", "README.zh-CN.md", "docs/**/*.md", "skills-src/**/*.md", "knowledge/packs/**/*.md"]


def normalize(text: str) -> list[str]:
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"\s+", " ", text.strip().lower())
    return text.split()


def ngrams(tokens: list[str], n: int = 8) -> set[str]:
    if len(tokens) < n:
        return set()
    return {" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def read_public_files() -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for pattern in PUBLIC_GLOBS:
        for path in REPO_ROOT.glob(pattern):
            if path.is_file():
                files.append((path, path.read_text(encoding="utf-8")))
    return files


def read_private_chapters() -> list[tuple[Path, str]]:
    return [
        (path, path.read_text(encoding="utf-8"))
        for path in sorted(BOOK_CHAPTERS_DIR.glob("*.md"))
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--threshold", type=int, default=4)
    args = parser.parse_args()

    public_files = read_public_files()
    private_files = read_private_chapters()

    findings = []
    for public_path, public_text in public_files:
        public_ngrams = ngrams(normalize(public_text))
        if not public_ngrams:
            continue
        for private_path, private_text in private_files:
            overlap = public_ngrams & ngrams(normalize(private_text))
            if len(overlap) >= args.threshold:
                findings.append(
                    {
                        "public_file": str(public_path.relative_to(REPO_ROOT)),
                        "private_file": str(private_path.relative_to(BOOK_CHAPTERS_DIR.parent)),
                        "shared_8grams": len(overlap),
                    }
                )

    if findings:
        for finding in findings:
            print(
                f"{finding['public_file']} overlaps with {finding['private_file']} "
                f"({finding['shared_8grams']} shared 8-grams)"
            )
        raise SystemExit(1)

    print("Similarity scan passed.")


if __name__ == "__main__":
    main()
