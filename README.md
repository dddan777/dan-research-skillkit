# dan-research-skillkit

Academic skills and knowledge packs for researchers, designed for both Claude Code and Codex.  
一个同时适用于 Claude Code 与 Codex 的科研技能工具箱，面向硕士生、博士生与研究写作者。

- Dual-host ready: `.claude/skills/` and `.agents/skills/`
- Bilingual skills and knowledge packs
- Checklists, manifests, and build scripts for academic work

Quick links:
- [Quick Start](docs/quickstart.md)
- [Chinese README](README.zh-CN.md)

## What This Is / 项目简介
`dan-research-skillkit` is a bilingual research workflow toolkit. It turns a long-term academic workflow library into reusable `dan-*` skills, knowledge packs, manifests, and build scripts.

这个仓库把长期积累的科研方法材料整理成可调用的技能、知识包、清单和构建脚本，方便在 Claude Code 与 Codex 中直接使用。

## Who This Is For / 适合谁
- Master's students who need a structured research workflow
- PhD students who need stage diagnosis, output planning, and paper production support
- Research assistants, academic writers, and independent scholars
- Anyone who wants skills for literature work, question formation, theory, design, writing, review papers, submission, defense, and long-term planning

## What You Get / 你会得到什么
- `dan-*` topic skills for literature work, research framing, design, writing, review papers, submission, defense, and planning
- topic-based knowledge packs with concepts, frameworks, and checklists
- dual-host layouts for Claude Code and Codex
- manifests, coverage catalogs, and validation scripts for ongoing maintenance
- local extraction and build tools for expanding the toolkit over time

## Quick Start / 快速开始
1. Clone the repository.
2. Read [`docs/quickstart.md`](docs/quickstart.md).
3. Pick a skill from [`docs/skills.md`](docs/skills.md).
4. Use repo-local skills directly, or install them globally for Claude Code or Codex.
5. Rebuild generated layouts with `python3 scripts/build_skills.py && python3 scripts/build_host_layouts.py`.

## Install for Claude Code and Codex / Claude Code 与 Codex 安装
For Claude Code, see [`docs/install-claude.md`](docs/install-claude.md).  
For Codex, see [`docs/install-codex.md`](docs/install-codex.md).

## Skills Overview / Skills 总览
| Skill | Purpose |
| --- | --- |
| `dan-research` | Route users by stage, bottleneck, and next output |
| `dan-literature` | Build a literature workflow and evidence pool |
| `dan-question-gap` | Turn a topic into a question, gap, and contribution |
| `dan-theory` | Build conceptual frameworks and theoretical claims |
| `dan-design` | Align question, evidence, data, and analysis |
| `dan-paper-writing` | Structure papers and manage section logic |
| `dan-review-paper` | Organize review article strategy and synthesis |
| `dan-submission` | Prepare submission packages and response logic |
| `dan-defense` | Prepare presentations, proposal defenses, and final defenses |
| `dan-planning` | Plan stages, rhythms, and milestones |
| `dan-method-atlas` | Compare method families and evidence forms |
| `dan-academic-tools` | Route tools, templates, and AI boundaries |
| `dan-upgrade` | Maintain packs, mappings, and dual-host builds |

Use a skill when you need action; read a knowledge pack when you need depth.  
需要执行时调用 skill，需要深入理解时阅读 knowledge pack。

## Knowledge Packs Overview / Knowledge Packs 总览
Knowledge packs live under [`knowledge/packs`](knowledge/packs). Each pack includes:
- bilingual summary
- core concepts
- frameworks
- checklists
- template names
- related skills and pack metadata

## Repository Structure and Build Flow / 仓库结构与生成方式
- `skills-src/`: single source of truth for all `dan-*` skills
- `.claude/skills/`: generated Claude Code layout
- `.agents/skills/`: generated Codex-compatible layout
- `knowledge/`: public packs and manifests
- `catalog/`: coverage indexes, pack maps, and release backlogs
- `scripts/`: inventory, extraction, normalization, build, and validation tools
- `schemas/`: JSON schemas for packs, skills, and source cards

See [`docs/architecture.md`](docs/architecture.md).

## Usage Patterns and Troubleshooting / 常见用法与故障排查
Typical usage patterns:
- route a research problem to the right `dan-*` skill
- read one pack deeply before drafting a chapter or proposal
- vendor repo-local skills into a project workspace
- rebuild both host layouts after adding or revising a skill

Troubleshooting docs:
- [`docs/install-claude.md`](docs/install-claude.md)
- [`docs/install-codex.md`](docs/install-codex.md)
- [`docs/extraction-pipeline.md`](docs/extraction-pipeline.md)

## Roadmap, License, and Author / 路线图、许可与作者
Roadmap:
- expand OCR coverage for image-heavy PDFs in the private extraction layer
- deepen templates and pack examples
- improve similarity checks and source refresh automation

Licenses:
- Code and scripts: [`LICENSE`](LICENSE)
- Documentation and packs: [`LICENSE-docs`](LICENSE-docs)

Author / 作者：南洋理工DAN读博笔记（小红书）
