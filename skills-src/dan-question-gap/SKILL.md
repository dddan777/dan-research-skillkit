---
name: "dan-question-gap"
description: "Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。"
---

# dan-question-gap

## Purpose / 用途
Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution.

帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。

## When To Use / 触发场景
- How do I find a research gap
- Turn this topic into a research question
- 帮我找 research gap
- 把方向变成问题

## Typical Situations / 典型情境
- 方向很多，但总写不出一句可研究的问题
- 感觉主题有价值，却说不清 gap 在哪里
- 知道想做创新，但贡献表述总是空泛

## Core Concepts / 核心概念
- 研究问题 / research question
- 研究空缺 / research gap
- 创新点 / novelty
- 研究边界 / scope boundary

## Main Frameworks / 主方法框架
1. **Topic-to-Question Compression**: Move from broad direction to object, relationship, and boundary in one sentence.
1. **Gap-to-Contribution Ladder**: A gap matters only when you can explain why filling it changes explanation, evidence, comparison, or boundary conditions.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先把方向压成对象、关系和边界三要素。
1. 判断你缺的是现象理解、理论解释、方法设计还是情境比较。
1. 把 gap 写成一句‘已有研究做了什么，还缺什么，为何值得补’。
1. 把 gap 再推进成具体创新点和预期贡献。
1. 最后反查：这个问题是否真的能被现有证据支持。

## Decision Rules / 判断规则
- 如果问题一句话里没有对象、关系和边界，就还不是研究问题。
- 如果 gap 只能说‘很少有人研究’，那还不够。
- 如果贡献不能回到理论、方法、证据或边界，说明创新点还太虚。

## Default Deliverables / 默认产出
- 一句话研究问题
- gap 说明
- 创新点说明
- 研究边界说明

## Templates And Checklists / 模板与清单
- `one-sentence research question`
- `gap statement`
- `contribution note`
- `Is the question researchable with available evidence?`
- `What kind of gap am I claiming?`
- `Why would the answer matter beyond curiosity?`

## Example Prompts / 调用示例
- 请把这个研究方向压成一个有边界的问题。
- 请帮我把现有文献里的缺口转成可写的 gap。
- 请检查这个贡献说法是不是仍然太空。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 33
- 研究问题形成: 14
- gap 与创新点: 16
- 研究价值与边界: 3

## Scope In / 负责范围
- question formation
- gap typology
- value justification
- problem boundaries

## Scope Out / 不负责范围
- full theory writing
- full literature-search execution
- statistical model choice

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: question formation, gap typology, value justification, problem boundaries.
- Use this skill when the main task is about scope out: full theory writing, full literature-search execution, statistical model choice.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/question-gap/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-theory`: Build conceptual frameworks, theoretical logic, and contribution claims from the literature base. / 帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。
- `dan-design`: Use a four-layer alignment model to connect question, explanation, evidence, and analysis. / 用问题、解释、证据、分析四重对齐来设计研究方案。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
