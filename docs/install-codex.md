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
