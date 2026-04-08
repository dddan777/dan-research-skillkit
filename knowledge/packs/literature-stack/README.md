# 文献采集、Zotero 项目管理与综述工作流 / Literature Acquisition, Zotero Project Management, and Review Workflows

## Summary / 简介
This pack turns Google Scholar/CNKI collection, Zotero-based project organization, and review preparation into one connected literature operations stack.

这个知识包把 Google Scholar/CNKI 检索、Zotero 入库与项目管理、以及后续文献综述准备串成一条可执行工作流，重点是让采集、整理和综述生成在同一个研究栈里衔接起来。

## When To Use / 何时调用
- Set up a literature stack with Zotero and Scholar
- Help me batch collect papers into Zotero and organize a review project
- 帮我配置 Google Scholar/CNKI + Zotero 的文献工作流
- 批量下载文献、管理项目库并生成综述任务

## Research Situations / 适用情境
- 想把 Google Scholar、CNKI、Zotero 和 AI 综述写作串成一条稳定工作流
- 需要批量采集文献，但不想让下载、入库、整理和综述彼此割裂
- 已经有 Zotero 库，但还没有项目级 collection、tag 和 note 规范

## Core Concepts / 核心概念
- 文献采集栈 / literature acquisition stack
- 项目文献库 / project-level Zotero library
- 批量入库 / batch ingest
- 综述就绪语料 / review-ready corpus

## Frameworks / 方法框架
1. **Acquire-Sync-Organize-Synthesize**: Collect references from browser-based discovery tools, sync them into Zotero, organize them by project logic, then hand off to review workflows.
1. **Zotero-As-Source-of-Truth**: Treat Zotero as the canonical library layer; browser skills gather and export, while Zotero MCP powers management, annotation, and synthesis.

## Expanded Workflow / 扩展工作流
1. 先判断当前宿主是 Claude Code、Codex，还是两者协同使用。
2. 安装 Zotero MCP，并确认 Zotero 桌面端和本地 API 可用。
3. 在 Claude Code 侧接入 Chrome DevTools MCP，再安装 `cnki-skills` 和 `gs-skills`。
4. 把检索、全文链接、导出和入库统一收束到 Zotero 这一层，而不是让浏览器工具长期承担读写真源。
5. 为项目建立 collection、tag、note 和 duplicate 处理规则。
6. 在 Zotero collection 清理完成后，再交给 `dan-literature` 或 `dan-review-paper` 生成综述产出。

## Decision Rules / 判断规则
- 浏览器采集负责发现与导出，Zotero 才是项目库真源。
- 批量下载只能在你有权访问的前提下进行，验证码和登录必须人工完成。
- 没有 collection 和标签规范时，不要急着让 AI 直接写综述。

## Checklists / 检查清单
- Does this workflow respect access permissions and site rules?
- Which collection, tag, or note schema will keep the project reusable later?
- Is the corpus ready for review writing, or is it still only a download pile?

## Templates / 模板与清单框
- `stack install report`
- `collection-tag schema`
- `review-ready corpus checklist`

## Suggested Deliverables / 建议产出
- 文献栈安装结果
- 项目 collection / tag 方案
- 批量采集与入库计划
- 综述就绪语料清单

## Common Pitfalls / 常见误区
- 把采集当成研究推进，库里越来越多但项目越来越乱
- 让多个工具同时写入真源，最后元数据和附件失同步
- 忽视授权边界、登录状态和验证码，误以为可以全自动抓取
- 没做去重和标签治理就直接生成综述

## Local Corpus Signals / 本地语料覆盖信号
- matched unique extracts: 205
- 文献采集与检索: 138
- 整理表与项目管理: 20
- 综述准备与综合: 42
- 工具与辅助流程: 5

## Example Prompts / 调用示例
- 请帮我安装并配置 Google Scholar/CNKI + Zotero 的文献工作流。
- 请把这批检索结果设计成 Zotero 的项目 collection 和标签结构。
- 请基于我的 Zotero collection 生成一套文献综述准备流程。

## Related Skills / 关联技能
- `dan-literature`
- `dan-review-paper`
- `dan-academic-tools`

## Pack Coverage / Pack 覆盖
- `S0201`
- `S0202`
- `S0203`
- `S0204`
- `S0205`
- `S0206`
- `S0207`
- `T0101`
- `T0102`
- `T0103`
- `T0104`
