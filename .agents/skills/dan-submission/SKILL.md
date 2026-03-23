---
name: "dan-submission"
description: "Support pre-submission checks, submission packages, response letters, and reviewer negotiation. 帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。"
---

# dan-submission

## Purpose / 用途
Support pre-submission checks, submission packages, response letters, and reviewer negotiation.

帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。

## When To Use / 触发场景
- How do I reply to reviewers
- Help me prepare my submission package
- 返修怎么写 response letter
- 投稿前要准备什么

## Typical Situations / 典型情境
- 准备投稿，但不确定材料是否齐全
- 收到审稿意见后，不知道怎么分类处理
- 想表达分歧，但担心回应太硬或太弱

## Core Concepts / 核心概念
- 投稿包 / submission package
- 返修逻辑 / revision logic
- 回应矩阵 / response matrix
- 分歧沟通 / disagreement management

## Main Frameworks / 主方法框架
1. **Submit-Respond-Revise Loop**: A manuscript improves through staged communication rather than one final upload.
1. **Comment-Type Triage**: Separate mandatory corrections, clarifications, defensible disagreements, and future-work notes before replying.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先做投稿前 readiness 检查。
1. 列出所有附件和期刊要求，不把问题留到提交窗口。
1. 把审稿意见拆成纠错、澄清、可辩护分歧和未来工作四类。
1. 先决定修改动作，再写回应理由。
1. 返修后再做一次全文一致性检查，避免局部改完整体失衡。

## Decision Rules / 判断规则
- response letter 先解释你做了什么，再解释为什么。
- 能承认的问题就直接承认，不要绕。
- 有分歧时，回应的是判断依据，而不是情绪立场。

## Default Deliverables / 默认产出
- 投稿材料清单
- response letter
- 审稿意见矩阵
- 返修一致性检查表

## Templates And Checklists / 模板与清单
- `submission package checklist`
- `response letter skeleton`
- `reviewer comment matrix`
- `Is the manuscript actually submission-ready?`
- `What category does each reviewer comment belong to?`
- `Does my reply explain both action and rationale?`

## Example Prompts / 调用示例
- 请帮我把这些 reviewer comments 分类。
- 请把这条回应改成先动作后理由的结构。
- 请检查我的 submission package 还缺什么。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 7
- 投稿流程与期刊判断: 6
- 返修与审稿回应: 1
- 投稿附件与模板: 0

## Scope In / 负责范围
- submission package planning
- reviewer response logic
- revision strategy
- disagreement framing

## Scope Out / 不负责范围
- full paper drafting
- detailed stats debugging
- research question formation

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: submission package planning, reviewer response logic, revision strategy, disagreement framing.
- Use this skill when the main task is about scope out: full paper drafting, detailed stats debugging, research question formation.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/submission/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。
- `dan-defense`: Prepare literature talks, proposal defenses, mid-term reviews, and final defenses by communication scenario. / 帮助用户按场景准备文献汇报、proposal defense、mid-term review 和 final defense。
- `dan-academic-tools`: Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning. / 整理文献、写作、投稿、汇报和规划中的工具流与模板流。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
