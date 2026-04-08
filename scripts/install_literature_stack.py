from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


EXTERNAL_REPOS = [
    {
        "name": "cnki-skills",
        "repo": "https://github.com/cookjohn/cnki-skills.git",
        "skills_dir": "skills",
        "agents_dir": "agents",
    },
    {
        "name": "gs-skills",
        "repo": "https://github.com/cookjohn/gs-skills.git",
        "skills_dir": "skills",
        "agents_dir": "agents",
    },
]


def run_command(command: list[str], check: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, check=check, text=True, capture_output=True)


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def sync_children(src: Path, dest: Path) -> list[str]:
    ensure_dir(dest)
    copied: list[str] = []
    for child in sorted(src.iterdir()):
        target = dest / child.name
        if child.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(child, target)
        else:
            shutil.copy2(child, target)
        copied.append(child.name)
    return copied


def clone_or_update(repo_url: str, dest: Path) -> None:
    if dest.exists():
        run_command(["git", "-C", str(dest), "pull", "--ff-only"], check=True)
        return
    ensure_dir(dest.parent)
    run_command(["git", "clone", "--depth", "1", repo_url, str(dest)], check=True)


def install_browser_stack(target_root: Path, cache_root: Path) -> list[str]:
    claude_skills = ensure_dir(target_root / ".claude" / "skills")
    claude_agents = ensure_dir(target_root / ".claude" / "agents")
    installed: list[str] = []

    for repo in EXTERNAL_REPOS:
        local_repo = cache_root / repo["name"]
        clone_or_update(repo["repo"], local_repo)
        installed.extend(
            f"{repo['name']}/skills:{item}"
            for item in sync_children(local_repo / repo["skills_dir"], claude_skills)
        )
        installed.extend(
            f"{repo['name']}/agents:{item}"
            for item in sync_children(local_repo / repo["agents_dir"], claude_agents)
        )

    return installed


def install_zotero_mcp(package: str) -> str:
    command = [sys.executable, "-m", "pip", "install", "--user", "--upgrade", package]
    run_command(command, check=True)
    return " ".join(command)


def configure_claude_chrome_mcp() -> tuple[bool, str]:
    if shutil.which("claude") is None:
        return False, "`claude` command not found; skipped Chrome DevTools MCP setup."
    if shutil.which("npx") is None:
        return False, "`npx` command not found; skipped Chrome DevTools MCP setup."

    command = [
        "claude",
        "mcp",
        "add",
        "chrome-devtools",
        "--",
        "npx",
        "-y",
        "chrome-devtools-mcp@latest",
    ]
    result = run_command(command, check=False)
    if result.returncode == 0:
        return True, "Configured Claude Code with chrome-devtools MCP."
    stderr = result.stderr.strip() or result.stdout.strip() or "unknown error"
    return False, f"Chrome DevTools MCP setup returned a non-zero exit code: {stderr}"


def build_summary(
    target_root: Path,
    browser_items: list[str],
    zotero_command: str | None,
    chrome_note: str,
) -> str:
    lines = [
        "# Literature Stack Setup Summary",
        "",
        f"- target workspace: `{target_root}`",
        f"- browser acquisition items installed: `{len(browser_items)}`",
    ]
    if browser_items:
        lines.append("- installed browser items:")
        lines.extend(f"  - `{item}`" for item in browser_items)
    if zotero_command:
        lines.append(f"- Zotero MCP install command run: `{zotero_command}`")
    else:
        lines.append("- Zotero MCP install command run: skipped")
    lines.append(f"- Chrome DevTools MCP setup: {chrome_note}")
    lines.extend(
        [
            "",
            "## Manual Next Steps",
            "- Start Zotero Desktop and make sure its local API is available.",
            "- If you need client configuration, run `zotero-mcp setup` and follow the prompts.",
            "- Start Chrome with remote debugging on port `9222` before using CNKI or Google Scholar browser skills.",
            "- Log in to CNKI manually in Chrome if you plan to download authorized PDFs there.",
            "- Expect CAPTCHA and access checks on CNKI/Google Scholar; solve them manually when prompted.",
            "- Use `dan-literature-stack` to orchestrate collection, tagging, project collections, and review preparation after setup.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the Google Scholar + CNKI + Zotero literature operations stack."
    )
    parser.add_argument(
        "--target",
        type=Path,
        default=Path.cwd(),
        help="Workspace where .claude/skills and .claude/agents should be installed.",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path.home() / ".cache" / "dan-research-skillkit" / "external",
        help="Cache directory for cloned third-party repositories.",
    )
    parser.add_argument(
        "--skip-browser-skills",
        action="store_true",
        help="Skip installing Google Scholar and CNKI browser skills.",
    )
    parser.add_argument(
        "--skip-zotero",
        action="store_true",
        help="Skip installing zotero-mcp-server.",
    )
    parser.add_argument(
        "--zotero-package",
        default="zotero-mcp-server[all]",
        help="Package spec to install for Zotero MCP.",
    )
    parser.add_argument(
        "--skip-claude-chrome-mcp",
        action="store_true",
        help="Skip `claude mcp add chrome-devtools`.",
    )
    parser.add_argument(
        "--summary-file",
        type=Path,
        default=None,
        help="Optional path to save the setup summary markdown.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    target_root = args.target.resolve()
    cache_root = args.cache_dir.resolve()

    browser_items: list[str] = []
    zotero_command: str | None = None
    chrome_note = "skipped"

    if not args.skip_browser_skills:
        browser_items = install_browser_stack(target_root, cache_root)

    if not args.skip_zotero:
        zotero_command = install_zotero_mcp(args.zotero_package)

    if not args.skip_claude_chrome_mcp:
        _, chrome_note = configure_claude_chrome_mcp()

    summary = build_summary(target_root, browser_items, zotero_command, chrome_note)
    print(summary)

    if args.summary_file:
        ensure_dir(args.summary_file.resolve().parent)
        args.summary_file.resolve().write_text(summary, encoding="utf-8")


if __name__ == "__main__":
    main()
