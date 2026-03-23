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

## Choose A Workflow / 按科研情境选择工作流
| If you need... | Start with |
| --- | --- |
| a quick diagnosis of your current stage, bottleneck, and next output | [`dan-research`](skills-src/dan-research/SKILL.md) |
| a reusable literature workflow, search plan, or note matrix | [`dan-literature`](skills-src/dan-literature/SKILL.md) |
| help turning a broad topic into a question, gap, and contribution | [`dan-question-gap`](skills-src/dan-question-gap/SKILL.md) |
| help matching theory, design, evidence, and methods | [`dan-theory`](skills-src/dan-theory/SKILL.md) + [`dan-design`](skills-src/dan-design/SKILL.md) |
| support for paper structure, review writing, submission, or defense | [`docs/skills.md`](docs/skills.md) |

## Research Workflow Directory / 科研工作流目录
| Skill | Use it when | Typical output |
| --- | --- |
| [`dan-research`](skills-src/dan-research/SKILL.md) | you need stage diagnosis, routing, or next-output planning | stage note, next-output list, routing decision |
| [`dan-literature`](skills-src/dan-literature/SKILL.md) | you need search terms, reading layers, or a literature matrix | keyword grid, screening logic, literature workflow |
| [`dan-question-gap`](skills-src/dan-question-gap/SKILL.md) | you need a tighter research question or contribution claim | question statement, gap note, contribution ladder |
| [`dan-theory`](skills-src/dan-theory/SKILL.md) | you need a conceptual framework or theory contribution | concept map, mechanism statement, theory paragraph |
| [`dan-design`](skills-src/dan-design/SKILL.md) | you need to align question, data, evidence, and analysis | design alignment table, method-fit note |
| [`dan-paper-writing`](skills-src/dan-paper-writing/SKILL.md) | you need paper structure or section-level writing logic | outline, section interface note, writing checklist |
| [`dan-review-paper`](skills-src/dan-review-paper/SKILL.md) | you need a review-paper workflow, not just a literature review | review type decision, screening plan, synthesis frame |
| [`dan-submission`](skills-src/dan-submission/SKILL.md) | you need submission materials or reviewer-response logic | submission checklist, comment matrix, response skeleton |
| [`dan-defense`](skills-src/dan-defense/SKILL.md) | you need presentation, proposal, or defense preparation | talk outline, slide logic, defense checklist |
| [`dan-planning`](skills-src/dan-planning/SKILL.md) | you need pacing, milestones, or execution repair | milestone plan, weekly rhythm, recovery note |
| [`dan-method-atlas`](skills-src/dan-method-atlas/SKILL.md) | you need cross-method comparison before committing | method comparison table, evidence map |
| [`dan-academic-tools`](skills-src/dan-academic-tools/SKILL.md) | you need templates, toolchains, or AI-use boundaries | tool stack, template list, workflow support note |
| [`dan-upgrade`](skills-src/dan-upgrade/SKILL.md) | you maintain the toolkit and need rebuild/release discipline | update checklist, rebuild plan, release validation |

Use a skill when you need action. Read the linked pack when you need deeper frameworks, pitfalls, and coverage signals.  
需要执行时调用 skill；需要更完整的框架、误区和语料覆盖线索时，再读对应的 pack。

## How To Work With A Skill / 一个 skill 应该怎么用
1. Start with [`dan-research`](skills-src/dan-research/SKILL.md) when you are unsure which bottleneck matters most.
2. Move into one domain skill and stay there long enough to produce a visible output.
3. Open the matching pack under [`knowledge/packs`](knowledge/packs) when you need more depth.
4. Hand off to the next `dan-*` skill only after the current output is clear.
5. Use [`docs/skills.md`](docs/skills.md) as the full routing directory.

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
- [`docs/collection-status.md`](docs/collection-status.md)

## Roadmap, License, and Author / 路线图、许可与作者
Roadmap:
- expand OCR coverage for image-heavy PDFs in the private extraction layer
- deepen templates and pack examples
- improve similarity checks and source refresh automation

Licenses:
- Code and scripts: [`LICENSE`](LICENSE)
- Documentation and packs: [`LICENSE-docs`](LICENSE-docs)

Author / 作者：南洋理工DAN读博笔记（小红书）
