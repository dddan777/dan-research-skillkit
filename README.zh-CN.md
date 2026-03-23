# dan-research-skillkit

一个同时适用于 Claude Code 与 Codex 的科研技能工具箱。它把长期积累的学术方法材料整理成可调用的 `dan-*` skills、知识包、清单和构建脚本。

- 双宿主可用：`.claude/skills/` 与 `.agents/skills/`
- 双语 skill 与 knowledge pack
- 清单、manifest 与构建脚本齐备

## 项目简介 / What This Is
这个仓库面向科研人员，尤其是硕士生、博士生、研究助理和学术写作者。它把长期积累的学术方法材料整理成一个可以被 Claude Code 和 Codex 同时发现和调用的双语 skill toolkit。

## 适合谁 / Who This Is For
- 需要系统掌握科研流程的硕士生
- 需要阶段定位、写作推进和答辩准备支持的博士生
- 需要把分散方法材料转成可复用框架的研究助理与学术写作者
- 希望把知识整理成 LLM 可调用技能的个人维护者

## 你会得到什么 / What You Get
- `dan-*` 主题技能，覆盖文献、问题、理论、方法、写作、投稿、答辩和规划
- 按主题组织的 knowledge packs，内含概念、框架、清单与模板名
- Claude Code 与 Codex 的双宿主布局
- 便于长期维护的 manifest、catalog 与校验脚本
- 可继续扩展的本地提取与构建工具

核心内容包括：
- `dan-*` skills
- knowledge packs
- catalog 与 manifest
- schema 与生成脚本

## 快速开始 / Quick Start
1. 克隆仓库。
2. 阅读 [docs/quickstart.md](docs/quickstart.md)。
3. 从 [docs/skills.md](docs/skills.md) 里选择一个 `dan-*` skill。
4. 直接使用仓库内的 `.claude/skills/` 或 `.agents/skills/`，或按安装文档复制到全局目录。
5. 如果你修改了真源技能，运行：

```bash
python3 scripts/build_skills.py
python3 scripts/build_packs.py
python3 scripts/build_host_layouts.py
python3 scripts/normalize_sources.py
python3 scripts/validate_repo.py
```

## Claude Code 与 Codex 安装 / Install for Claude Code and Codex
- Claude Code 安装说明见 [docs/install-claude.md](docs/install-claude.md)
- Codex 安装说明见 [docs/install-codex.md](docs/install-codex.md)

## 按科研情境选择工作流 / Choose A Workflow
| 如果你现在需要… | 建议先用 |
| --- | --- |
| 先判断自己卡在哪一层、下一步该产出什么 | [dan-research](skills-src/dan-research/SKILL.md) |
| 搭建找文献、筛文献、做笔记、建文献池的流程 | [dan-literature](skills-src/dan-literature/SKILL.md) |
| 把一个宽泛方向压缩成研究问题、gap 和贡献 | [dan-question-gap](skills-src/dan-question-gap/SKILL.md) |
| 对齐理论、设计、证据与方法 | [dan-theory](skills-src/dan-theory/SKILL.md) + [dan-design](skills-src/dan-design/SKILL.md) |
| 处理论文写作、综述、投稿或答辩 | [docs/skills.md](docs/skills.md) |

## 科研工作流目录 / Research Workflow Directory
| Skill | 适合何时调用 | 常见产出 |
| --- | --- |
| [dan-research](skills-src/dan-research/SKILL.md) | 不知道自己处于哪个阶段，或不确定下一步最值得做什么 | 阶段诊断、下一产出清单、路由建议 |
| [dan-literature](skills-src/dan-literature/SKILL.md) | 需要检索词、阅读层次或文献整理表 | 关键词网格、筛选逻辑、文献工作流 |
| [dan-question-gap](skills-src/dan-question-gap/SKILL.md) | 需要把方向压成问题、gap 和贡献 | 问题陈述、gap 说明、贡献梯子 |
| [dan-theory](skills-src/dan-theory/SKILL.md) | 需要搭概念框架、机制链或理论贡献 | 概念图、机制表述、理论段落 |
| [dan-design](skills-src/dan-design/SKILL.md) | 需要对齐问题、数据、证据与分析 | 设计对齐表、方法匹配说明 |
| [dan-paper-writing](skills-src/dan-paper-writing/SKILL.md) | 需要搭论文结构或处理章节接口 | 提纲、章节接口说明、写作清单 |
| [dan-review-paper](skills-src/dan-review-paper/SKILL.md) | 需要做综述论文，而不只是普通文献综述 | 综述类型判断、筛选方案、综合框架 |
| [dan-submission](skills-src/dan-submission/SKILL.md) | 需要投稿材料或返修回应逻辑 | 投稿清单、审稿意见矩阵、回应骨架 |
| [dan-defense](skills-src/dan-defense/SKILL.md) | 需要准备汇报、开题、中期或毕业答辩 | 汇报提纲、幻灯逻辑、答辩清单 |
| [dan-planning](skills-src/dan-planning/SKILL.md) | 需要里程碑、节奏治理或推进修复 | 阶段计划、每周节奏、卡点修复说明 |
| [dan-method-atlas](skills-src/dan-method-atlas/SKILL.md) | 需要在不同方法之间先做导航和比较 | 方法比较表、证据地图 |
| [dan-academic-tools](skills-src/dan-academic-tools/SKILL.md) | 需要工具链、模板或 AI 使用边界 | 工具栈、模板列表、支持流程说明 |
| [dan-upgrade](skills-src/dan-upgrade/SKILL.md) | 你在维护这个 toolkit，需要刷新和发布 | 更新清单、重建计划、发布前校验 |

需要执行时调用 skill；需要更完整的框架、误区和语料覆盖线索时，再读对应的 pack。

## Knowledge Packs 总览 / Knowledge Packs Overview
知识包位于 [knowledge/packs](knowledge/packs)。每个 knowledge pack 都包含：
- 中英双语简介
- 核心概念
- 方法框架
- 检查清单
- 模板名称
- 关联 skill 与 pack 元数据

## 一个 skill 应该怎么用 / How To Work With A Skill
1. 如果你不确定该先处理什么，先用 [dan-research](skills-src/dan-research/SKILL.md) 做阶段定位。
2. 进入一个主题 skill 后，先把它要求的默认产出做出来，不要同时切来切去。
3. 需要更多方法深度时，再打开对应的 [knowledge/packs](knowledge/packs)。
4. 当前产出清楚之后，再交接到下一个 `dan-*` skill。
5. 完整目录和交接关系见 [docs/skills.md](docs/skills.md)。

## 仓库结构与生成方式 / Repository Structure and Build Flow
- `skills-src/`：唯一真源
- `.claude/skills/`：Claude Code 生成布局
- `.agents/skills/`：Codex 生成布局
- `knowledge/`：知识包与 manifest
- `catalog/`：覆盖矩阵、pack 映射与 backlog
- `scripts/`：盘点、提取、构建、校验脚本
- `schemas/`：结构化 schema

详细说明见 [docs/architecture.md](docs/architecture.md)。

## 常见用法与故障排查 / Usage Patterns and Troubleshooting
常见用法：
- 先用 `dan-research` 做阶段定位，再路由到具体 skill
- 在开题、写作、投稿、答辩前先读对应 knowledge pack
- 在项目仓库内 vendoring `.claude/skills/` 或 `.agents/skills/`
- 新增或修改技能后重新生成双宿主布局

相关文档：
- [docs/install-claude.md](docs/install-claude.md)
- [docs/install-codex.md](docs/install-codex.md)
- [docs/extraction-pipeline.md](docs/extraction-pipeline.md)
- [docs/collection-status.md](docs/collection-status.md)

## 路线图、许可与作者 / Roadmap, License, and Author
路线图：
- 扩展图像型 PDF 的 OCR 能力
- 增加模板与案例深度
- 完善 similarity scan 与增量更新流程

许可：
- 代码与脚本：见 [LICENSE](LICENSE)
- 文档与知识包：见 [LICENSE-docs](LICENSE-docs)

作者：南洋理工DAN读博笔记（小红书）
