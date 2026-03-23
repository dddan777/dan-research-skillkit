---
name: "dan-defense"
description: "Prepare literature talks, proposal defenses, mid-term reviews, and final defenses by communication scenario. 帮助用户按场景准备文献汇报、proposal defense、mid-term review 和 final defense。"
---

# dan-defense

## Purpose / 用途
Prepare literature talks, proposal defenses, mid-term reviews, and final defenses by communication scenario.

帮助用户按场景准备文献汇报、proposal defense、mid-term review 和 final defense。

## When To Use / 触发场景
- Help me prepare for my proposal defense
- How should I structure an academic presentation
- 开题答辩怎么准备
- 学术汇报怎么讲

## Typical Situations / 典型情境
- 即将做开题、中期或毕业答辩，但不知道重点怎么取舍
- 学术汇报材料很多，却不会讲成一个有逻辑的故事
- 担心答辩时讲太浅或讲太深

## Core Concepts / 核心概念
- 学术汇报 / academic presentation
- 开题答辩 / proposal defense
- 中期答辩 / mid-term review
- 毕业答辩 / final defense

## Main Frameworks / 主方法框架
1. **Audience-Question-Evidence**: Choose slides and speaking depth by what the audience needs to understand or challenge.
1. **Defense Scenario Routing**: Proposal, progress review, and final defense each require different levels of certainty and scope.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先定义这次汇报要达成的决策目标。
1. 按 audience-question-evidence 三元组安排材料。
1. 把讲稿分成‘必须放在 slides 上’和‘适合口头展开’两层。
1. 预设最容易被追问的几个环节，提前准备证据与解释。
1. 答辩前做一次时间版 rehearsal，保证主线不散。

## Decision Rules / 判断规则
- 不同答辩场景的目标不同，结构也不同。
- 讲稿要服务评审问题，而不是服务你想展示的一切努力。
- slides 负责结构和证据，口头负责转场和解释。

## Default Deliverables / 默认产出
- 汇报主线图
- slide 逻辑表
- 口头讲稿提纲
- 高频追问清单

## Templates And Checklists / 模板与清单
- `defense storyline sheet`
- `slide-logic checklist`
- `audience-question rehearsal sheet`
- `What is the core decision this defense is trying to secure?`
- `What evidence must the audience trust before moving on?`
- `What belongs in slides versus the spoken explanation?`

## Example Prompts / 调用示例
- 请按开题答辩逻辑重排我的 slides。
- 请帮我区分哪些内容放在 slide，哪些留到口头讲。
- 请预判这场答辩最可能被追问的 5 个问题。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 15
- 学术汇报与报告: 9
- 开题与中期答辩: 3
- 毕业答辩与 thesis 组织: 3

## Scope In / 负责范围
- presentation structure
- defense slide logic
- oral explanation boundaries
- thesis-organization communication

## Scope Out / 不负责范围
- full manuscript submission
- detailed qualitative coding
- database search strategies

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: presentation structure, defense slide logic, oral explanation boundaries, thesis-organization communication.
- Use this skill when the main task is about scope out: full manuscript submission, detailed qualitative coding, database search strategies.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/defense/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-research`: Route researchers through the full lifecycle, stage diagnosis, and next-output planning. / 用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。
- `dan-submission`: Support pre-submission checks, submission packages, response letters, and reviewer negotiation. / 帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
