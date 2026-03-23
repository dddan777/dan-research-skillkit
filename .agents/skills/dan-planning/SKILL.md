---
name: "dan-planning"
description: "Turn long-horizon research into stages, rhythms, milestones, and review loops. 帮助用户把长期研究拆成阶段、节奏、里程碑和复盘机制。"
---

# dan-planning

## Purpose / 用途
Turn long-horizon research into stages, rhythms, milestones, and review loops.

帮助用户把长期研究拆成阶段、节奏、里程碑和复盘机制。

## When To Use / 触发场景
- Help me plan my PhD workflow
- I am stuck and not making progress
- 科研时间安排怎么做
- 我总推进不下去

## Typical Situations / 典型情境
- 知道要做什么，但一周一周推进不稳
- 任务很多，却没有清晰阶段和里程碑
- 经常忙得很累，但回头看产出不成形

## Core Concepts / 核心概念
- 阶段治理 / stage governance
- 里程碑 / milestone
- 四周推进 / four-week rhythm
- 复盘 / review loop

## Main Frameworks / 主方法框架
1. **Stage-Rhythm-Output**: Every long task needs a stage definition, a short rhythm, and a concrete output.
1. **Bottleneck Review Loop**: Diagnose whether the slowdown comes from unclear direction, weak structure, missing data, or low execution bandwidth.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先确定当前阶段和这个阶段唯一最重要的产出。
1. 把阶段目标拆成四周节奏，再拆成本周推进点。
1. 为每一周指定一个必须完成的可见交付物。
1. 每周复盘一次：哪些工作推进了主线，哪些只是制造噪音。
1. 一旦卡住，优先诊断瓶颈类型，而不是盲目加班。

## Decision Rules / 判断规则
- 没有可见产出，就不算真正推进。
- 周计划必须服务阶段目标，而不是把任务塞满。
- 长期停滞通常不是不努力，而是瓶颈识别错误。

## Default Deliverables / 默认产出
- 阶段任务表
- 四周推进板
- 本周交付物清单
- 瓶颈复盘记录

## Templates And Checklists / 模板与清单
- `weekly planning sheet`
- `milestone tracker`
- `bottleneck review note`
- `What is the next visible deliverable?`
- `Does this week advance a stage or only create noise?`
- `What bottleneck needs diagnosis before more effort?`

## Example Prompts / 调用示例
- 请把我的任务整理成四周推进节奏。
- 请判断我现在的瓶颈是结构、资料还是执行带宽。
- 请帮我给本周定义一个最小可交付成果。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 20
- 阶段规划与节奏: 12
- 论文推进与里程碑: 8
- 卡点与效率误区: 0

## Scope In / 负责范围
- time planning
- weekly and monthly pacing
- milestone design
- execution diagnostics

## Scope Out / 不负责范围
- topic-specific theory building
- journal formatting
- coding or statistical estimation

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: time planning, weekly and monthly pacing, milestone design, execution diagnostics.
- Use this skill when the main task is about scope out: topic-specific theory building, journal formatting, coding or statistical estimation.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/planning/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-research`: Route researchers through the full lifecycle, stage diagnosis, and next-output planning. / 用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-defense`: Prepare literature talks, proposal defenses, mid-term reviews, and final defenses by communication scenario. / 帮助用户按场景准备文献汇报、proposal defense、mid-term review 和 final defense。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
