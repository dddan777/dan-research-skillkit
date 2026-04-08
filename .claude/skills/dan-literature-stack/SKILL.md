---
name: "dan-literature-stack"
description: "Connect Google Scholar, CNKI, Zotero MCP, and review generation into one executable literature operations workflow. 把 Google Scholar、CNKI、Zotero MCP 和综述产出串成一条可执行的文献采集与项目管理工作流。"
---

# dan-literature-stack

## Purpose / 用途
Connect Google Scholar, CNKI, Zotero MCP, and review generation into one executable literature operations workflow.

把 Google Scholar、CNKI、Zotero MCP 和综述产出串成一条可执行的文献采集与项目管理工作流。

## When To Use / 触发场景
- Set up a literature stack with Zotero and Scholar
- Help me batch collect papers into Zotero and organize a review project
- 帮我配置 Google Scholar/CNKI + Zotero 的文献工作流
- 批量下载文献、管理项目库并生成综述任务

## Typical Situations / 典型情境
- 想把 Google Scholar、CNKI、Zotero 和 AI 综述写作串成一条稳定工作流
- 需要批量采集文献，但不想让下载、入库、整理和综述彼此割裂
- 已经有 Zotero 库，但还没有项目级 collection、tag 和 note 规范

## Core Concepts / 核心概念
- 文献采集栈 / literature acquisition stack
- 项目文献库 / project-level Zotero library
- 批量入库 / batch ingest
- 综述就绪语料 / review-ready corpus

## Main Frameworks / 主方法框架
1. **Acquire-Sync-Organize-Synthesize**: Collect references from browser-based discovery tools, sync them into Zotero, organize them by project logic, then hand off to review workflows.
1. **Zotero-As-Source-of-Truth**: Treat Zotero as the canonical library layer; browser skills gather and export, while Zotero MCP powers management, annotation, and synthesis.

## First Response Pattern / 首轮回答模式
1. Diagnose the situation before offering tools or motivation.
1. Choose one main framework from this skill instead of mixing multiple frameworks at once.
1. Give 3-5 concrete steps that can be acted on immediately.
1. Produce one usable output: outline, checklist, table, matrix, script, or note.
1. Route to one adjacent `dan-*` skill only when the bottleneck has clearly moved.

## Operating Procedure / 执行流程
1. Start by restating the user's current stage, target output, and blocking point in one sentence.
1. 先判断当前宿主是 Claude Code、Codex，还是两者协同使用。
1. 安装 Zotero MCP，并确认 Zotero 桌面端和本地 API 可用。
1. 在 Claude Code 侧接入 Chrome DevTools MCP，再安装 `cnki-skills` 和 `gs-skills`。
1. 把检索、全文链接、导出和入库统一收束到 Zotero 这一层，而不是让浏览器工具长期承担读写真源。
1. 为项目建立 collection、tag、note 和 duplicate 处理规则。
1. 在 Zotero collection 清理完成后，再交给 `dan-literature` 或 `dan-review-paper` 生成综述产出。

## Decision Rules / 判断规则
- 浏览器采集负责发现与导出，Zotero 才是项目库真源。
- 批量下载只能在你有权访问的前提下进行，验证码和登录必须人工完成。
- 没有 collection 和标签规范时，不要急着让 AI 直接写综述。

## Default Deliverables / 默认产出
- 文献栈安装结果
- 项目 collection / tag 方案
- 批量采集与入库计划
- 综述就绪语料清单

## Templates And Checklists / 模板与清单
- `stack install report`
- `collection-tag schema`
- `review-ready corpus checklist`
- `Does this workflow respect access permissions and site rules?`
- `Which collection, tag, or note schema will keep the project reusable later?`
- `Is the corpus ready for review writing, or is it still only a download pile?`

## Example Prompts / 调用示例
- 请帮我安装并配置 Google Scholar/CNKI + Zotero 的文献工作流。
- 请把这批检索结果设计成 Zotero 的项目 collection 和标签结构。
- 请基于我的 Zotero collection 生成一套文献综述准备流程。

## Local Corpus Signals / 本地语料信号
- matched local extracts: 205
- 文献采集与检索: 138
- 整理表与项目管理: 20
- 综述准备与综合: 42
- 工具与辅助流程: 5

## Host Support / 宿主支持
- Claude Code: browser acquisition via Chrome DevTools MCP plus `cnki-skills` and `gs-skills`.
- Codex: Zotero MCP, project organization, and downstream review tasks once references are already in Zotero.
- Both hosts: use this skill as the orchestration layer; respect manual login, CAPTCHA, and authorized-access boundaries.

## Bundled References / 配套参考
- `references/stack-setup.md`: installation sequence, host matrix, and third-party component setup — read before configuring the stack or running the installer script
- `references/stack-playbooks.md`: batch collection, project tagging, and review-generation playbooks — read when moving from installation to actual literature operations

## Scope In / 负责范围
- literature stack installation planning
- Google Scholar and CNKI collection workflows
- Zotero project collections and batch organization
- review-ready library preparation

## Scope Out / 不负责范围
- bypassing paywalls or access controls
- solving captchas programmatically
- guaranteeing third-party CLI or browser compatibility
- final publication-ready review writing without source screening

## Routing Rules / 交接规则
- Use this skill when the main task is about scope in: literature stack installation planning, Google Scholar and CNKI collection workflows, Zotero project collections and batch organization, review-ready library preparation.
- Use this skill when the main task is about scope out: bypassing paywalls or access controls, solving captchas programmatically, guaranteeing third-party CLI or browser compatibility, final publication-ready review writing without source screening.
- When the request crosses into another bottleneck, route to the best adjacent skill instead of stretching this one too far.

## Knowledge Pack / 对应知识包
- Read `../../knowledge/packs/literature-stack/README.md` when you need the full pack summary, workflow details, pitfalls, and coverage signals.

## Related Skills / 关联技能
- `dan-literature`: Turn search, screening, note-taking, and synthesis into a reusable literature workflow. / 把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。
- `dan-review-paper`: Differentiate review articles from regular literature reviews and organize screening, synthesis, and contribution writing. / 帮助用户区分综述论文与文献综述，并组织综述的筛选、分类和贡献表达。
- `dan-academic-tools`: Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning. / 整理文献、写作、投稿、汇报和规划中的工具流与模板流。

## Output Contract / 输出要求
- Keep the answer concrete, stage-aware, and tied to a visible research deliverable.
- Prefer outlines, checklists, matrices, comparison tables, and draftable text over generic encouragement.
- If the user asks for a draft, give a working draft rather than only describing what to write.
- If the task is outside scope, state the boundary clearly and name the next `dan-*` skill to use.
