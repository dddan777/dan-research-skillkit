---
name: "dan-upgrade"
description: "Maintain incremental updates, source mapping, and dual-host skill distribution. 维护 skillkit 的增量更新、来源映射和双宿主分发。"
---

# dan-upgrade

## Purpose / 用途
Maintain incremental updates, source mapping, and dual-host skill distribution.

维护 skillkit 的增量更新、来源映射和双宿主分发。

## When To Use / 触发场景
- Update this research skillkit
- Refresh packs after new source material arrives
- 更新这个 skillkit
- 刷新来源映射和技能布局

## Typical Situations / 典型情境
- 新增一批来源后，需要刷新 packs 和双宿主布局
- 想知道哪些变化适合公开，哪些必须留在本地
- 需要让维护流程可重复，而不是靠手工记忆

## Core Concepts / 核心概念
- 增量更新 / incremental update
- 中性来源映射 / neutral source mapping
- 双宿主分发 / dual-host distribution
- 覆盖率审计 / coverage audit

## Main Frameworks / 主方法框架
1. **Ingest-Normalize-Build-Validate**: Every update passes through ingest, normalization, pack rebuild, and validation before release.
1. **Single-Source Skill Layout**: Keep `skills-src/` as the truth and regenerate both host layouts instead of editing them directly.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先跑本地提取和去重，不直接动公开层。
1. 基于提取结果刷新统计、pack 覆盖和状态页。
1. 只挑适合公开的结构化内容进入 repo。
1. 重新生成双宿主布局与 manifests。
1. 最后跑校验和相似度扫描，再 push。
1. Audit repository state, source freshness, generated artifacts, and host layouts before editing anything.
1. Prefer reproducible regeneration through scripts over one-off manual changes.

## Decision Rules / 判断规则
- 本地缓存先行，公开更新后行。
- 能抽象成方法论再公开，不能直接公开原始材料。
- 双宿主布局永远从真源生成，不手工改分发目录。

## Default Deliverables / 默认产出
- 更新记录
- 公开层 diff
- 状态页刷新
- 发布前校验结果

## Templates And Checklists / 模板与清单
- `update checklist`
- `source intake note`
- `release validation sheet`
- `Did new source material change any public pack?`
- `Did the rebuild regenerate both host layouts?`
- `Did validation catch forbidden strings or forbidden file types?`

## Example Prompts / 调用示例
- 请基于最新提取结果刷新公开层状态页。
- 请判断这次新增内容哪些适合公开更新。
- 请重新生成双宿主技能并做发布前校验。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 0
- 本地提取刷新: 0
- 公开层状态刷新: 0

## Scope In / 负责范围
- source refresh
- pack regeneration
- dual-host build
- coverage checks

## Scope Out / 不负责范围
- subject-matter answering for a specific research problem
- paper drafting
- private-source publication decisions

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: source refresh, pack regeneration, dual-host build, coverage checks.
- Use this skill when the main task is about scope out: subject-matter answering for a specific research problem, paper drafting, private-source publication decisions.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/upgrade/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-research`: Route researchers through the full lifecycle, stage diagnosis, and next-output planning. / 用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。
- `dan-method-atlas`: Offer cross-method navigation instead of a single-method tutorial. / 给研究者提供跨方法导航，而不是单一方法教程。
- `dan-academic-tools`: Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning. / 整理文献、写作、投稿、汇报和规划中的工具流与模板流。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
