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
