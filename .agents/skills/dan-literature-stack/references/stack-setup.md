# Literature Stack Setup

Use this reference when the user wants to install or configure the full literature operations stack.

## What This Stack Connects

1. `zotero-mcp`
   - Library search, metadata, full text, notes, tags, collections, semantic search, duplicates.
   - Official repo: [54yyyu/zotero-mcp](https://github.com/54yyyu/zotero-mcp)
2. `gs-skills`
   - Google Scholar search, cited-by tracking, full-text link discovery, Zotero export.
   - Official repo: [cookjohn/gs-skills](https://github.com/cookjohn/gs-skills)
3. `cnki-skills`
   - CNKI search, journal lookup, indexing status, export, and authorized download flows.
   - Official repo: [cookjohn/cnki-skills](https://github.com/cookjohn/cnki-skills)

## Host Matrix

- Claude Code:
  - Best host for Google Scholar and CNKI browser automation.
  - Needs Chrome DevTools MCP and Chrome remote debugging.
  - Can also use Zotero MCP.
- Codex:
  - Strong host for Zotero MCP, project organization, collection cleanup, and downstream literature review tasks.
  - Browser acquisition via `cnki-skills` and `gs-skills` is not the primary path here because those upstream repos are distributed for Claude Code.
- Combined workflow:
  - Use Claude Code to discover, export, and ingest.
  - Use Zotero as the canonical project library.
  - Use Codex or Claude Code to manage collections, tags, notes, and review generation.

## One-Command Installer

From the repository root:

```bash
python3 scripts/install_literature_stack.py --target .
```

Optional flags:

```bash
python3 scripts/install_literature_stack.py --target . --summary-file docs/literature-stack-status.md
python3 scripts/install_literature_stack.py --target . --skip-claude-chrome-mcp
python3 scripts/install_literature_stack.py --target . --skip-zotero
```

## What The Installer Does

- clones or updates `cnki-skills` and `gs-skills` into a local cache
- copies their `skills/` into `.claude/skills/`
- copies their `agents/` into `.claude/agents/`
- installs `zotero-mcp-server[all]` through `python -m pip install --user --upgrade`
- tries to run `claude mcp add chrome-devtools -- npx -y chrome-devtools-mcp@latest`

## Manual Requirements That Remain

- start Zotero Desktop and keep it available
- run `zotero-mcp setup` if your MCP client needs explicit configuration
- start Chrome with `--remote-debugging-port=9222`
- log in to CNKI manually if you need authorized downloads there
- solve CAPTCHA manually on Google Scholar or CNKI when prompted

## Boundary Rules

- only download PDFs or full texts you are authorized to access
- do not describe CAPTCHA or anti-bot bypasses as automatic
- treat Zotero as the project source of truth after acquisition
