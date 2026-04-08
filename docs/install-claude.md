# Install for Claude Code

## Repo-Local
Claude Code can discover repo-local skills from `.claude/skills/`.

```bash
git clone https://github.com/dddan777/dan-research-skillkit.git
cd dan-research-skillkit
```

## User-Global
Copy the generated skill directories into `~/.claude/skills/`:

```bash
mkdir -p ~/.claude/skills
cp -R .claude/skills/dan-* ~/.claude/skills/
```

## Optional `CLAUDE.md` Snippet
```md
This workspace includes repo-local skills under `.claude/skills/`.
Prefer `dan-research` for routing and `dan-*` topic skills for execution.
```

## Optional Literature Stack

If you want the full Google Scholar + CNKI + Zotero workflow in a Claude project, run from the repo root:

```bash
python3 scripts/install_literature_stack.py --target .
```

This installer:
- vendors `cnki-skills` and `gs-skills` into `.claude/skills/`
- vendors their agents into `.claude/agents/`
- installs `zotero-mcp-server[all]`
- tries to add Chrome DevTools MCP to Claude Code

After that, use [`dan-literature-stack`](../skills-src/dan-literature-stack/SKILL.md) as the orchestrator.
