# Architecture

## Design Goal
One canonical skill source, two host layouts, and one public knowledge layer.

## Layers
### 1. Private Extraction Layer
- local-only
- stored under `private_cache/`
- built with `inventory.py` and `extract_pdf.py`
- never pushed to GitHub

### 2. Skill Source Layer
- `skills-src/` is the only manual source for public skills
- each skill has `SKILL.md` and `agents/openai.yaml`

### 3. Dual Host Distribution Layer
- `.claude/skills/` for Claude Code
- `.agents/skills/` for Codex-compatible hosts
- both are generated from `skills-src/`

### 4. Public Knowledge Layer
- `knowledge/packs/` for pack content
- `knowledge/manifests/` for `skills.json`, `packs.json`, and `topics.json`
- `catalog/` for neutral provenance and coverage data

## Build Flow
1. Normalize source mappings
2. Build knowledge packs
3. Build skill source files
4. Generate host layouts
5. Validate repository contents
