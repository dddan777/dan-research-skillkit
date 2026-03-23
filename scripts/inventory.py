from __future__ import annotations

import hashlib
import os
from collections import Counter
from pathlib import Path

from common import write_csv, write_json
from project_config import PRIVATE_CACHE_DIR, REPO_ROOT, WORKSPACE_ROOT


SKIP_DIRS = {
    ".git",
    "__pycache__",
    REPO_ROOT.name,
}


def sha1_for_path(path: Path) -> str:
    hasher = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def main() -> None:
    rows = []
    ext_counter: Counter[str] = Counter()
    for root, dirs, files in os.walk(WORKSPACE_ROOT):
        dirs[:] = [item for item in dirs if item not in SKIP_DIRS]
        for filename in files:
            path = Path(root) / filename
            if REPO_ROOT in path.parents:
                continue
            rel_path = path.relative_to(WORKSPACE_ROOT)
            suffix = path.suffix.lower() or "[no_ext]"
            ext_counter[suffix] += 1
            rows.append(
                {
                    "relative_path": str(rel_path),
                    "suffix": suffix,
                    "size_bytes": path.stat().st_size,
                    "sha1": sha1_for_path(path),
                }
            )

    write_csv(
        PRIVATE_CACHE_DIR / "inventory" / "workspace_inventory.csv",
        rows,
        ["relative_path", "suffix", "size_bytes", "sha1"],
    )
    write_json(
        PRIVATE_CACHE_DIR / "inventory" / "workspace_inventory_summary.json",
        {
            "workspace_root": str(WORKSPACE_ROOT),
            "file_count": len(rows),
            "suffix_counts": dict(ext_counter.most_common()),
        },
    )


if __name__ == "__main__":
    main()
