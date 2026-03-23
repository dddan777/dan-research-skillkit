---
name: "dan-review-paper"
description: "Differentiate review articles from regular literature reviews and organize screening, synthesis, and contribution writing. 帮助用户区分综述论文与文献综述，并组织综述的筛选、分类和贡献表达。"
---

# dan-review-paper

## Purpose / 用途
Differentiate review articles from regular literature reviews and organize screening, synthesis, and contribution writing.

帮助用户区分综述论文与文献综述，并组织综述的筛选、分类和贡献表达。

## When To Use / 触发场景
- How do I write a review paper
- Should this be a systematic review or not
- 综述论文怎么写
- PRISMA 应该怎么用

## Typical Situations / 典型情境
- 想写综述论文，但不知道该做 narrative 还是 systematic
- 已经收集了一批文献，却不会组织 review findings
- 知道要做筛选，但 PRISMA 和纳入标准总写得很虚

## Core Concepts / 核心概念
- 综述论文 / review article
- 文献综述 / literature review section
- 纳入标准 / inclusion criteria
- PRISMA-ready process

## Main Frameworks / 主方法框架
1. **Review-Type Decision**: Choose among narrative, systematic, scoping, or theory-building review according to the problem and evidence base.
1. **Screen-Sort-Synthesize**: Move from corpus building to coding, then from coding to analytical contribution.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先判断综述目标：盘点、分类、解释还是建模。
1. 为此选择 review 类型和材料边界。
1. 建立纳入标准、排除标准和筛选记录。
1. 把文献编码成主题、机制、方法或情境维度。
1. 把编码结果改写成发现结构，而不是逐篇摘要。

## Decision Rules / 判断规则
- 综述论文不是普通 literature review 的拉长版。
- 没有清晰筛选规则，就很难建立 review 的可信度。
- review findings 必须回答领域图景发生了什么变化。

## Default Deliverables / 默认产出
- review 类型说明
- 筛选协议与记录
- 编码表
- review findings 结构图

## Templates And Checklists / 模板与清单
- `review protocol note`
- `inclusion criteria sheet`
- `review findings matrix`
- `What kind of review am I truly writing?`
- `Would another researcher understand my inclusion logic?`
- `Are my findings organized as an argument rather than a stack of summaries?`

## Example Prompts / 调用示例
- 请判断这个题目更适合哪一种 review。
- 请帮我把筛选后的材料组织成 review findings。
- 请检查这套纳入标准是否足够清楚。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 52
- 综述类型与对比: 42
- PRISMA 与筛选规范: 6
- 经典 review 文献: 4

## Scope In / 负责范围
- review type selection
- screening criteria
- PRISMA-ready workflows
- review findings structure

## Scope Out / 不负责范围
- single-study empirical writing
- response letter drafting
- general planning coaching

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: review type selection, screening criteria, PRISMA-ready workflows, review findings structure.
- Use this skill when the main task is about scope out: single-study empirical writing, response letter drafting, general planning coaching.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/review-paper/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-question-gap`: Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution. / 帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。
- `dan-paper-writing`: Break paper writing into structure, section interfaces, and expression boundaries. / 把论文写作拆成结构设计、章节接口和表达策略三层。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
