---
name: "dan-academic-tools"
description: "Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning. 整理文献、写作、投稿、汇报和规划中的工具流与模板流。"
---

# dan-academic-tools

## Purpose / 用途
Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning.

整理文献、写作、投稿、汇报和规划中的工具流与模板流。

## When To Use / 触发场景
- What tools should I use for this research workflow
- Help me choose a template or toolchain
- 科研工具怎么搭
- 有哪些可复用模板

## Typical Situations / 典型情境
- 工具很多，但不知道如何组合成稳定工作流
- 手头有模板，却不知道什么时候该用、什么时候不该用
- 希望使用 AI 提升效率，但担心边界模糊

## Core Concepts / 核心概念
- 工具流 / toolflow
- 模板流 / template flow
- AI 辅助边界 / AI assistance boundary
- 研究支持系统 / research support system

## Main Frameworks / 主方法框架
1. **Tool-by-Task Routing**: Choose tools according to the research task they support rather than novelty or trend value.
1. **Template Reuse Ladder**: Start with a stable scaffold, then adapt it to the current stage, audience, and output requirement.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先按任务链划分工具，而不是按软件品牌堆清单。
1. 为每一类任务指定一个默认模板或默认工具。
1. 把 AI 放在整理、改写、核对和清单辅助的位置，而不是让它代替判断。
1. 每次替换工具前，先评估切换成本和长期维护成本。
1. 定期清理无效工具，保持工作流稳定。

## Decision Rules / 判断规则
- 工具应该减少摩擦，而不是制造切换负担。
- 模板优先解决起步成本，不能代替研究判断。
- AI 更适合加速结构化工作，不适合替代学术责任。

## Default Deliverables / 默认产出
- 工具链清单
- 模板使用说明
- AI 边界清单
- 工作流切换记录

## Templates And Checklists / 模板与清单
- `toolchain audit`
- `template selection sheet`
- `AI boundary checklist`
- `Does this tool reduce friction or create more switching cost?`
- `What part should remain human judgment?`
- `Which template can shorten setup without freezing thinking?`

## Example Prompts / 调用示例
- 请按任务链给我设计一个最小科研工具流。
- 请判断这个模板适合放在哪个阶段使用。
- 请帮我给这项工作划出 AI 可以帮忙和不该帮忙的边界。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 35
- 科研工具与网站: 16
- 模板与可编辑资产: 5
- 工作流辅助: 14

## Scope In / 负责范围
- toolchain selection
- template routing
- AI assistance boundaries
- workflow support assets

## Scope Out / 不负责范围
- proprietary software training
- sensitive data processing advice
- domain-specific programming frameworks

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: toolchain selection, template routing, AI assistance boundaries, workflow support assets.
- Use this skill when the main task is about scope out: proprietary software training, sensitive data processing advice, domain-specific programming frameworks.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/tools/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。
- `dan-submission`: Support pre-submission checks, submission packages, response letters, and reviewer negotiation. / 帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
