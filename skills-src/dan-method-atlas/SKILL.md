---
name: "dan-method-atlas"
description: "Offer cross-method navigation instead of a single-method tutorial. 给研究者提供跨方法导航，而不是单一方法教程。"
---

# dan-method-atlas

## Purpose / 用途
Offer cross-method navigation instead of a single-method tutorial.

给研究者提供跨方法导航，而不是单一方法教程。

## When To Use / 触发场景
- Which methods are suitable for this type of question
- Give me a method atlas
- 给我一个方法图谱
- 什么问题适合什么方法

## Typical Situations / 典型情境
- 不确定自己的问题更适合哪一类方法家族
- 看了很多方法名，却不知道它们各自擅长回答什么
- 想做方法比较，但总停留在工具名层面

## Core Concepts / 核心概念
- 方法图谱 / method atlas
- 任务-方法映射 / task-method routing
- 证据形态 / evidence form
- 设计风险 / design risk

## Main Frameworks / 主方法框架
1. **Question-to-Method Matrix**: Compare method families by the kind of answer they can credibly support.
1. **Evidence-to-Analysis Matrix**: Map data forms to analysis strategies before choosing a named method.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先定义你要交付的是模式、关系、机制还是过程。
1. 再判断可用证据属于数值、文本、案例、实验还是混合形态。
1. 据此筛出 2 到 3 个候选方法家族，而不是从几十种方法里盲选。
1. 比较每种方法的前提、风险和证据要求。
1. 把最终方法写回设计对齐表，而不是独立看待。

## Decision Rules / 判断规则
- 方法图谱用于路由，不用于代替设计思考。
- 先定证据形态，再比较方法家族。
- 如果你说不清方法家族的局限，通常也没真正选定它。

## Default Deliverables / 默认产出
- 问题-方法矩阵
- 证据-分析矩阵
- 方法比较表
- 方法风险清单

## Templates And Checklists / 模板与清单
- `question-method matrix`
- `evidence-analysis matrix`
- `design risk table`
- `What answer format do I need: pattern, relationship, mechanism, or process?`
- `What evidence form do I have or can realistically get?`
- `What method family is being excluded, and why?`

## Example Prompts / 调用示例
- 请把我的研究问题路由到几个方法家族。
- 请比较这两类方法对我的证据要求有什么差别。
- 请帮我做一张问题-方法矩阵。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 51
- 常见方法图谱: 35
- 证据与数据形式: 2
- 混合与多方法设计: 14

## Scope In / 负责范围
- cross-method comparison
- task-to-method routing
- evidence-type overview
- method risk awareness

## Scope Out / 不负责范围
- software-specific execution
- complete study design writing
- submission or defense coaching

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: cross-method comparison, task-to-method routing, evidence-type overview, method risk awareness.
- Use this skill when the main task is about scope out: software-specific execution, complete study design writing, submission or defense coaching.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/methods/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-design`: Use a four-layer alignment model to connect question, explanation, evidence, and analysis. / 用问题、解释、证据、分析四重对齐来设计研究方案。
- `dan-theory`: Build conceptual frameworks, theoretical logic, and contribution claims from the literature base. / 帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。
- `dan-review-paper`: Differentiate review articles from regular literature reviews and organize screening, synthesis, and contribution writing. / 帮助用户区分综述论文与文献综述，并组织综述的筛选、分类和贡献表达。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
