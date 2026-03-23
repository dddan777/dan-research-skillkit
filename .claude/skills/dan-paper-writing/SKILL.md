---
name: "dan-paper-writing"
description: "Break paper writing into structure, section interfaces, and expression boundaries. 把论文写作拆成结构设计、章节接口和表达策略三层。"
---

# dan-paper-writing

## Purpose / 用途
Break paper writing into structure, section interfaces, and expression boundaries.

把论文写作拆成结构设计、章节接口和表达策略三层。

## When To Use / 触发场景
- How should I structure my paper
- Help me outline an introduction or discussion
- 论文结构怎么搭
- discussion 怎么写

## Typical Situations / 典型情境
- 材料已经不少，但论文总写不成完整故事
- 知道每一章大概要写什么，却不知道章节之间怎么接
- results 和 discussion 常常混在一起

## Core Concepts / 核心概念
- 八大模块 / eight core modules
- 章节接口 / section interfaces
- 结果与讨论边界 / results-discussion boundary
- 写作顺序 / drafting sequence

## Main Frameworks / 主方法框架
1. **Eight-Module Skeleton**: Use a stable paper skeleton so each section contributes to one argument rather than becoming a standalone memo.
1. **Section Handoffs**: Each section should answer what the next section now needs to justify.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先用八大模块搭一个整体骨架。
1. 给每一节定义唯一任务，而不是把所有内容都塞进来。
1. 检查上一节是否真的为下一节提供了写作前提。
1. 把方法、结果、讨论的边界提前写成规则。
1. 最后再做例句、润色和表达层面的优化。

## Decision Rules / 判断规则
- 先建结构，再修句子。
- 每节必须能回答‘这节为什么存在’。
- 如果结果段已经开始解释意义，说明 discussion 提前了。

## Default Deliverables / 默认产出
- 全篇提纲
- 章节接口说明
- 段落任务表
- results-discussion 边界表

## Templates And Checklists / 模板与清单
- `paper-outline sheet`
- `introduction scaffold`
- `results-discussion boundary checklist`
- `What job does this section do in the overall argument?`
- `Does the next section logically require what I have just written?`
- `Am I reporting results or interpreting them?`

## Example Prompts / 调用示例
- 请帮我把这篇论文整理成八大模块骨架。
- 请检查我的 introduction 和 literature review 是否职责混淆。
- 请重写这个 section handoff，让下一节接得更自然。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 41
- 结构骨架与模块: 25
- 章节写法与例句: 14
- 概念框架写作: 2

## Scope In / 负责范围
- paper outline
- section-by-section logic
- results vs discussion boundaries
- conceptual framework writing

## Scope Out / 不负责范围
- review-paper protocol
- journal cover letter drafting
- dataset construction

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: paper outline, section-by-section logic, results vs discussion boundaries, conceptual framework writing.
- Use this skill when the main task is about scope out: review-paper protocol, journal cover letter drafting, dataset construction.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/writing/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-theory`: Build conceptual frameworks, theoretical logic, and contribution claims from the literature base. / 帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。
- `dan-design`: Use a four-layer alignment model to connect question, explanation, evidence, and analysis. / 用问题、解释、证据、分析四重对齐来设计研究方案。
- `dan-submission`: Support pre-submission checks, submission packages, response letters, and reviewer negotiation. / 帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
