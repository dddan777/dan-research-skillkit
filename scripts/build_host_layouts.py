from __future__ import annotations

import shutil
from pathlib import Path

from common import ensure_dir
from project_config import REPO_ROOT


SKILLS_SRC_ROOT = REPO_ROOT / "skills-src"
HOST_ROOTS = [
    REPO_ROOT / ".claude" / "skills",
    REPO_ROOT / ".agents" / "skills",
]


def copy_skill_tree(src: Path, dest: Path) -> None:
    if dest.exists():
        shutil.rmtree(dest)
    shutil.copytree(src, dest)


def main() -> None:
    skill_dirs = [path for path in SKILLS_SRC_ROOT.iterdir() if path.is_dir()]
    for host_root in HOST_ROOTS:
        ensure_dir(host_root)
        for skill_dir in skill_dirs:
            copy_skill_tree(skill_dir, host_root / skill_dir.name)


if __name__ == "__main__":
    main()
