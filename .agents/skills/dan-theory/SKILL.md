---
name: "dan-theory"
description: "Build conceptual frameworks, theoretical logic, and contribution claims from the literature base. 帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。"
---

# dan-theory

## Purpose / 用途
Build conceptual frameworks, theoretical logic, and contribution claims from the literature base.

帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。

## When To Use / 触发场景
- How do I build a conceptual framework
- What counts as theoretical contribution
- 帮我搭理论框架
- 理论贡献怎么写

## Typical Situations / 典型情境
- 文献读了很多，但理论部分始终像资料堆砌
- 知道几个变量，却说不清概念之间的机制关系
- 写贡献时只会说‘丰富了现有研究’

## Core Concepts / 核心概念
- 理论基础 / theoretical base
- 概念框架 / conceptual framework
- 机制链 / mechanism chain
- 理论贡献 / theoretical contribution

## Main Frameworks / 主方法框架
1. **Concept-Relation-Mechanism**: Clarify the concepts, their relationships, and the mechanism that makes the relationship meaningful.
1. **Five Contribution Moves**: Extend, refine, integrate, bound, or re-specify an existing explanation instead of making vague novelty claims.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先明确这项研究到底要解释什么现象。
1. 从文献中筛出最能承担解释任务的概念，而不是把所有理论都列上。
1. 把概念关系、机制链和边界条件画成框架。
1. 把理论任务写成一条可被检验或解释的逻辑链。
1. 最后把贡献归位到扩展、修正、整合、限定或重述之一。

## Decision Rules / 判断规则
- 理论不是背景知识，而是解释结构。
- 如果变量之间只有箭头没有机制，框架还不够。
- 如果贡献不改变现有解释的任何部分，它就不是理论贡献。

## Default Deliverables / 默认产出
- 概念框架图
- 机制链说明
- 理论选择理由
- 理论贡献段落

## Templates And Checklists / 模板与清单
- `conceptual framework note`
- `mechanism statement`
- `theoretical contribution paragraph`
- `Why this theory and not another nearby explanation?`
- `What mechanism am I truly claiming?`
- `Would the contribution still hold without my core argument?`

## Example Prompts / 调用示例
- 请帮我把这些概念整理成一个机制链。
- 请判断这段理论部分是在解释现象还是只是在堆文献。
- 请把我的贡献压到五种理论动作里。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 71
- 常见理论与经典文献: 53
- 概念框架与模型: 12
- 理论贡献写法: 6

## Scope In / 负责范围
- theory selection
- conceptual framework building
- mechanism logic
- theory contribution statements

## Scope Out / 不负责范围
- full empirical design
- journal fit decisions
- line-by-line copyediting

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: theory selection, conceptual framework building, mechanism logic, theory contribution statements.
- Use this skill when the main task is about scope out: full empirical design, journal fit decisions, line-by-line copyediting.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/theory/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-question-gap`: Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. / 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。
- `dan-design`: Use a four-layer alignment model to connect question, explanation, evidence, and analysis. / 用问题、解释、证据、分析四重对齐来设计研究方案。
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
