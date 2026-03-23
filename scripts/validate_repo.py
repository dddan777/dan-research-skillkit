from __future__ import annotations

import argparse
import json
from pathlib import Path

from project_config import REPO_ROOT, SKILLS


FORBIDDEN_EXTENSIONS = {".pdf", ".docx", ".pptx", ".xlsx", ".mp3"}
IGNORED_TOP_LEVELS = {"private_cache", ".git", "__pycache__"}


def load_text_files() -> list[Path]:
    return [
        path
        for path in REPO_ROOT.rglob("*")
        if path.is_file()
        and not any(part in IGNORED_TOP_LEVELS for part in path.parts)
        and path.suffix not in FORBIDDEN_EXTENSIONS
    ]


def check_forbidden_extensions() -> list[str]:
    findings = []
    for path in REPO_ROOT.rglob("*"):
        if any(part in IGNORED_TOP_LEVELS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in FORBIDDEN_EXTENSIONS:
            findings.append(str(path.relative_to(REPO_ROOT)))
    return findings


def check_host_layouts() -> list[str]:
    findings = []
    expected = sorted(skill["skill_id"] for skill in SKILLS)
    for host_root in [REPO_ROOT / ".claude" / "skills", REPO_ROOT / ".agents" / "skills"]:
        actual = sorted(path.name for path in host_root.iterdir() if path.is_dir())
        if actual != expected:
            findings.append(f"{host_root.relative_to(REPO_ROOT)} skill directories do not match expected list")
        for skill_id in expected:
            skill_md = host_root / skill_id / "SKILL.md"
            if not skill_md.exists():
                findings.append(f"Missing {skill_md.relative_to(REPO_ROOT)}")
    return findings


def check_manifests() -> list[str]:
    findings = []
    manifests_root = REPO_ROOT / "knowledge" / "manifests"
    for name in ["skills.json", "packs.json", "topics.json"]:
        if not (manifests_root / name).exists():
            findings.append(f"Missing manifest: knowledge/manifests/{name}")
    return findings


def check_forbidden_terms(forbidden_terms: list[str]) -> list[str]:
    findings = []
    if not forbidden_terms:
        return findings
    for path in load_text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for term in forbidden_terms:
            if term and term in text:
                findings.append(f"Forbidden term found in {path.relative_to(REPO_ROOT)}")
                break
    return findings


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--forbidden-file", type=Path, default=None)
    args = parser.parse_args()

    forbidden_terms = []
    if args.forbidden_file and args.forbidden_file.exists():
        forbidden_terms = [
            line.strip()
            for line in args.forbidden_file.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]

    findings = []
    findings.extend(check_forbidden_extensions())
    findings.extend(check_host_layouts())
    findings.extend(check_manifests())
    findings.extend(check_forbidden_terms(forbidden_terms))

    if findings:
        print(json.dumps(findings, ensure_ascii=False, indent=2))
        raise SystemExit(1)

    print("Repository validation passed.")


if __name__ == "__main__":
    main()
