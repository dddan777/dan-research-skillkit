---
name: "dan-literature"
description: "Turn search, screening, note-taking, and synthesis into a reusable literature workflow. 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。"
---

# dan-literature

## Purpose / 用途
Turn search, screening, note-taking, and synthesis into a reusable literature workflow.

把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。

## When To Use / 触发场景
- How should I read papers efficiently
- Build me a literature workflow
- 我不会读文献
- 帮我搭文献池

## Typical Situations / 典型情境
- 刚开始做题，需要从 0 搭一个可持续的文献池
- 已经存了很多 PDF，但写综述或写引言时调不出来
- 读完文献有印象，却做不出可比较、可复用的笔记

## Core Concepts / 核心概念
- 文献池 / evidence pool
- 精读 / deep reading
- 文献整理表 / literature matrix
- 文献金字塔 / literature pyramid

## Main Frameworks / 主方法框架
1. **Four-Step Literature Chain**: Search, read, note, and organize. Each step narrows the pool and increases reuse value.
1. **Layered Screening**: Separate background, related, directly relevant, and method-support papers before reading intensively.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 围绕研究对象、关系、情境和方法线索拆关键词组。
1. 做第一轮检索并按全景、相关、直接相关、补充四层分流。
1. 只对高价值文献做精读，并统一笔记字段。
1. 把新笔记放回同一张 literature matrix，而不是分散在零碎文档里。
1. 定期重画文献金字塔，判断核心层是否真的服务当前问题。

## Decision Rules / 判断规则
- 问题还很散时，先扩广度，不要一上来精读太深。
- 理论尚未稳定时，优先保留概念和机制型文献，而不是只看结论型文献。
- 写作卡住时，按章节用途回调文献，而不是继续盲目扩库。

## Default Deliverables / 默认产出
- 关键词网格
- 文献筛选记录
- 统一字段笔记
- 文献整理表
- 文献金字塔

## Templates And Checklists / 模板与清单
- `literature-matrix`
- `deep-reading note`
- `paper-retention checklist`
- `Why is this paper worth keeping?`
- `Which field in the note makes it reusable later?`
- `Does my current pool answer the present research question?`

## Example Prompts / 调用示例
- 请把我的研究方向拆成一组可检索关键词。
- 请给我一个围绕研究问题的文献整理表字段设计。
- 请帮我判断哪些文献应该进入精读层。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 133
- 检索与入口设计: 42
- 阅读步骤与笔记: 35
- 整理表与分类结构: 14
- 全局观与综述过渡: 42

## Scope In / 负责范围
- keyword planning
- screening layers
- reading depth decisions
- literature matrix design

## Scope Out / 不负责范围
- full systematic-review protocol
- journal submission strategy
- field-specific bibliometrics

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: keyword planning, screening layers, reading depth decisions, literature matrix design.
- Use this skill when the main task is about scope out: full systematic-review protocol, journal submission strategy, field-specific bibliometrics.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/literature/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-question-gap`: Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. / 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。
- `dan-academic-tools`: Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning. / 整理文献、写作、投稿、汇报和规划中的工具流与模板流。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
