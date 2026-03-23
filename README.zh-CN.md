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

## Skills 总览 / Skills Overview
| Skill | 作用 |
| --- | --- |
| `dan-research` | 研究阶段定位、主线导航与下一产出判断 |
| `dan-literature` | 文献检索、阅读、笔记与文献池搭建 |
| `dan-question-gap` | 研究问题、gap 与创新点形成 |
| `dan-theory` | 理论基础、概念框架与理论贡献 |
| `dan-design` | 问题、证据、数据与方法的对齐 |
| `dan-paper-writing` | 论文结构、章节呼应与表达边界 |
| `dan-review-paper` | 综述论文类型、筛选规范与组织逻辑 |
| `dan-submission` | 投稿材料、返修结构与审稿沟通 |
| `dan-defense` | 学术汇报、开题中期与毕业答辩 |
| `dan-planning` | 科研规划、节奏治理与长期推进 |
| `dan-method-atlas` | 方法图谱与任务-方法对照 |
| `dan-academic-tools` | 工具流、模板流与 AI 使用边界 |
| `dan-upgrade` | skillkit 更新、映射刷新与双宿主发布 |

## Knowledge Packs 总览 / Knowledge Packs Overview
知识包位于 [knowledge/packs](knowledge/packs)。每个 knowledge pack 都包含：
- 中英双语简介
- 核心概念
- 方法框架
- 检查清单
- 模板名称
- 关联 skill 与 pack 元数据

需要执行时调用 skill，需要深入理解时阅读 knowledge pack。

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

## 路线图、许可与作者 / Roadmap, License, and Author
路线图：
- 扩展图像型 PDF 的 OCR 能力
- 增加模板与案例深度
- 完善 similarity scan 与增量更新流程

许可：
- 代码与脚本：见 [LICENSE](LICENSE)
- 文档与知识包：见 [LICENSE-docs](LICENSE-docs)

作者：南洋理工DAN读博笔记（小红书）
