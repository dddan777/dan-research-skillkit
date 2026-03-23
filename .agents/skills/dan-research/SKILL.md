---
name: "dan-research"
description: "Route researchers through the full lifecycle, stage diagnosis, and next-output planning. 用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。"
---

# dan-research

## Purpose / 用途
Route researchers through the full lifecycle, stage diagnosis, and next-output planning.

用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。

## When To Use / 触发场景
- I do not know where to start my research
- Help me locate my current PhD stage
- 我现在卡在哪个阶段
- 帮我梳理整体研究路径

## Typical Situations / 典型情境
- 刚入题，不知道先做文献、问题还是方法
- 做了很多任务，但说不清自己目前处于哪个阶段
- 已经有若干草稿或结果，却不会把它们放回长期研究路径

## Core Concepts / 核心概念
- 主线任务 / core research tracks
- 研究生命周期 / research lifecycle
- 产出层 / output layer
- 阶段诊断 / stage diagnosis

## Main Frameworks / 主方法框架
1. **Three-Layer Diagnosis**: Look at every bottleneck through task, stage, and output before deciding what to do next.
1. **Seven Core Tracks**: Problem formation, literature building, theory framing, design, paper production, feedback loops, and thesis organization.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先判断当前卡点属于任务层、阶段层还是产出层。
1. 把当前目标改写成一份看得见的阶段性产出，而不是抽象目标。
1. 确认该产出对应的是哪条主线任务，以及它会喂给下一个什么环节。
1. 为当前阶段选择一个主 skill，不在多个方法之间来回切换。
1. 每周用同一张阶段诊断表回顾是否真的向下一个阶段推进。
1. Treat this skill as a router and stage-diagnosis layer first, not a place to solve every downstream task in depth.
1. If the user's real bottleneck clearly belongs to literature, theory, design, writing, submission, or defense, route there after producing a short diagnosis note.

## Decision Rules / 判断规则
- 如果你无法判断要做什么，先做阶段诊断，而不是先找工具。
- 如果你做了很多零碎任务却没有稳定产出，说明当前问题在产出层。
- 如果你已经有材料但仍然推进混乱，优先检查长期主线是否清楚。

## Default Deliverables / 默认产出
- 阶段诊断表
- 下一产出清单
- 主线任务定位图
- 章节或研究单元路线图

## Templates And Checklists / 模板与清单
- `stage-diagnosis-note`
- `next-output table`
- `What stage am I in right now?`
- `What concrete output should this week produce?`
- `Which next skill should I route to after diagnosis?`

## Example Prompts / 调用示例
- 请帮我判断我现在卡在研究生命周期的哪一层。
- 请把我手头这些任务重写成阶段性产出。
- 请按读博主线帮我决定下一步应该先补哪一块。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 32
- 读博主线与阶段地图: 9
- 博士论文组织与整合: 10
- 阶段卡点与推进诊断: 13

## Scope In / 负责范围
- research stage diagnosis
- lifecycle planning
- output mapping
- chapter-to-stage navigation

## Scope Out / 不负责范围
- database-specific search strings
- statistical implementation details
- journal formatting minutiae

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: research stage diagnosis, lifecycle planning, output mapping, chapter-to-stage navigation.
- Use this skill when the main task is about scope out: database-specific search strings, statistical implementation details, journal formatting minutiae.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/research/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-question-gap`: Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. / 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。
- `dan-planning`: Turn long-horizon research into stages, rhythms, milestones, and review loops. / 帮助用户把长期研究拆成阶段、节奏、里程碑和复盘机制。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
