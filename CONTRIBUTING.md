# Contributing

## Principles
- Keep public materials original, reconstructed, and neutral.
- Do not add raw source files, scans, screenshots, or original path names.
- Keep `skills-src/` as the only manual edit surface for skills.
- Regenerate `.claude/skills/` and `.agents/skills/` after skill changes.

## Local Build
```bash
python3 scripts/build_skills.py
python3 scripts/build_packs.py
python3 scripts/build_host_layouts.py
python3 scripts/normalize_sources.py
python3 scripts/validate_repo.py
```

## Pull Request Checklist
- [ ] `skills-src/` updated, if relevant
- [ ] both host layouts regenerated
- [ ] manifests regenerated
- [ ] no forbidden file types added
- [ ] no raw source identifiers added
