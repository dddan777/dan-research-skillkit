---
name: "dan-design"
description: "Use a four-layer alignment model to connect question, explanation, evidence, and analysis. 用问题、解释、证据、分析四重对齐来设计研究方案。"
---

# dan-design

## Purpose / 用途
Use a four-layer alignment model to connect question, explanation, evidence, and analysis.

用问题、解释、证据、分析四重对齐来设计研究方案。

## When To Use / 触发场景
- Help me choose a method
- Does my design fit my research question
- 帮我选研究方法
- 我的设计和问题匹配吗

## Typical Situations / 典型情境
- 问题已经有了，但不知道该用什么数据和方法
- 方法会不少，但不知道哪种最适合当前问题
- 设计写出来像流程说明，缺少逻辑对齐

## Core Concepts / 核心概念
- 研究设计 / research design
- 证据策略 / evidence strategy
- 混合研究 / mixed methods
- 内容分析 / content analysis

## Main Frameworks / 主方法框架
1. **Four-Layer Alignment**: Question, explanation, evidence, and analysis should narrow together rather than drift apart.
1. **Method-by-Task Matching**: Choose methods by whether you need to describe, compare, explain, validate, or trace a process.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先判断问题要回答的是关系、机制、比较还是过程。
1. 明确理论层真正需要什么类型的证据。
1. 先定数据形态和获取路径，再定分析方法。
1. 如果考虑 mixed methods，明确每种证据分别承担什么任务。
1. 用一张对齐表复查问题、理论、数据和分析是否互相支持。

## Decision Rules / 判断规则
- 方法服从问题，不反过来。
- 数据类型先于具体分析软件或模型名。
- 混合研究必须有分工，不是多做一点就叫 mixed methods。

## Default Deliverables / 默认产出
- 设计对齐表
- 数据-证据说明
- 方法选择理由
- 开题设计核对表

## Templates And Checklists / 模板与清单
- `design alignment note`
- `method-fit checklist`
- `data-evidence table`
- `What kind of answer does the question require?`
- `Can the available evidence actually support that answer?`
- `Is mixed methods serving a real explanatory task?`

## Example Prompts / 调用示例
- 请判断这个问题需要什么类型的证据。
- 请帮我比较两种设计哪个更匹配当前问题。
- 请检查我的 mixed methods 是否真的有分工逻辑。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 60
- 数据类型与证据形式: 12
- mixed methods: 14
- 内容分析与编码: 2
- 方法选择与常见误区: 32

## Scope In / 负责范围
- research design alignment
- data-type selection
- mixed methods logic
- content analysis framing

## Scope Out / 不负责范围
- software-specific analysis code
- journal reviewer response wording
- full thesis structuring

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: research design alignment, data-type selection, mixed methods logic, content analysis framing.
- Use this skill when the main task is about scope out: software-specific analysis code, journal reviewer response wording, full thesis structuring.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/design/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-question-gap`: Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. / 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。
- `dan-theory`: Build conceptual frameworks, theoretical logic, and contribution claims from the literature base. / 帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。
- `dan-method-atlas`: Offer cross-method navigation instead of a single-method tutorial. / 给研究者提供跨方法导航，而不是单一方法教程。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
