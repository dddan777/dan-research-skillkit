# Install for Codex

## Repo-Local
Codex-compatible hosts can discover repo-local skills from `.agents/skills/`.

```bash
git clone https://github.com/dddan777/dan-research-skillkit.git
cd dan-research-skillkit
```

## User-Global
Copy the generated skill directories into `~/.codex/skills/`:

```bash
mkdir -p ~/.codex/skills
cp -R .agents/skills/dan-* ~/.codex/skills/
```

## Optional `AGENTS.md` Snippet
```md
This workspace includes repo-local skills under `.agents/skills/`.
Use `dan-research` to route research workflow questions to the right `dan-*` skill.
```

## Optional Zotero-Backed Literature Stack

Codex works especially well with Zotero MCP, project organization, and review generation after your references are already in Zotero.

Use [`dan-literature-stack`](../skills-src/dan-literature-stack/SKILL.md) for this workflow. Its setup reference is:

- [`skills-src/dan-literature-stack/references/stack-setup.md`](../skills-src/dan-literature-stack/references/stack-setup.md)

Note:
- Google Scholar and CNKI browser collection in this stack is Claude Code-first because the upstream browser skills are distributed for `.claude/skills/`.
- A practical pattern is: collect/export in Claude Code, then manage and synthesize in Codex through Zotero MCP plus the `dan-*` skills.
