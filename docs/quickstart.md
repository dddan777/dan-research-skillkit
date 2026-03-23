# Quick Start

## 1. Clone
```bash
git clone https://github.com/dddan777/dan-research-skillkit.git
cd dan-research-skillkit
```

## 2. Pick your host
- Claude Code reads `.claude/skills/`
- Codex-compatible hosts read `.agents/skills/`

## 3. Choose one skill
Start with:
- `dan-research` if you need stage diagnosis
- `dan-literature` if you need literature support
- `dan-question-gap` if your topic is still vague
- `dan-paper-writing` if you already have material and need structure

## 4. Rebuild after edits
```bash
python3 scripts/build_skills.py
python3 scripts/build_packs.py
python3 scripts/build_host_layouts.py
python3 scripts/normalize_sources.py
python3 scripts/validate_repo.py
```

## 5. Optional private extraction
The repository ships with a private extraction pipeline for local PDF normalization:

```bash
python3 scripts/inventory.py
python3 scripts/extract_pdf.py --limit 30 --render-preview
```
