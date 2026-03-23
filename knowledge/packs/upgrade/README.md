# 知识包更新、来源刷新与双宿主发布 / Pack Refresh, Source Updates, and Dual-Host Publishing

## Summary / 简介
This pack is for maintainers. It defines how new source material enters the private extraction layer, how public packs are refreshed, and how Claude Code and Codex layouts stay in sync.

这个知识包面向维护者，规定新增来源如何进入私有提取层、如何更新公开 knowledge packs，以及如何同步 Claude Code 和 Codex 布局。

## When To Use / 何时调用
- Update this research skillkit
- Refresh packs after new source material arrives
- 更新这个 skillkit
- 刷新来源映射和技能布局

## Research Situations / 适用情境
- 新增一批来源后，需要刷新 packs 和双宿主布局
- 想知道哪些变化适合公开，哪些必须留在本地
- 需要让维护流程可重复，而不是靠手工记忆

## Core Concepts / 核心概念
- 增量更新 / incremental update
- 中性来源映射 / neutral source mapping
- 双宿主分发 / dual-host distribution
- 覆盖率审计 / coverage audit

## Frameworks / 方法框架
1. **Ingest-Normalize-Build-Validate**: Every update passes through ingest, normalization, pack rebuild, and validation before release.
1. **Single-Source Skill Layout**: Keep `skills-src/` as the truth and regenerate both host layouts instead of editing them directly.

## Expanded Workflow / 扩展工作流
1. 先跑本地提取和去重，不直接动公开层。
2. 基于提取结果刷新统计、pack 覆盖和状态页。
3. 只挑适合公开的结构化内容进入 repo。
4. 重新生成双宿主布局与 manifests。
5. 最后跑校验和相似度扫描，再 push。

## Decision Rules / 判断规则
- 本地缓存先行，公开更新后行。
- 能抽象成方法论再公开，不能直接公开原始材料。
- 双宿主布局永远从真源生成，不手工改分发目录。

## Checklists / 检查清单
- Did new source material change any public pack?
- Did the rebuild regenerate both host layouts?
- Did validation catch forbidden strings or forbidden file types?

## Templates / 模板与清单框
- `update checklist`
- `source intake note`
- `release validation sheet`

## Suggested Deliverables / 建议产出
- 更新记录
- 公开层 diff
- 状态页刷新
- 发布前校验结果

## Common Pitfalls / 常见误区
- 把本地缓存误提交到 GitHub
- 直接改分发目录导致双宿主失同步
- 只更新 pack，不更新 manifests 和状态页
- 没做校验就 push

## Local Corpus Signals / 本地语料覆盖信号
- matched unique extracts: 0
- 本地提取刷新: 0
- 公开层状态刷新: 0

## Example Prompts / 调用示例
- 请基于最新提取结果刷新公开层状态页。
- 请判断这次新增内容哪些适合公开更新。
- 请重新生成双宿主技能并做发布前校验。

## Related Skills / 关联技能
- `dan-research`
- `dan-method-atlas`
- `dan-academic-tools`

## Pack Coverage / Pack 覆盖
- `S0101`
- `S0102`
- `S0103`
- `S0104`
- `S0105`
- `S0106`
- `S0201`
- `S0202`
- `S0203`
- `S0204`
- `S0205`
- `S0206`
- `S0207`
- `S0301`
- `S0302`
- `S0303`
- `S0304`
- `S0305`
- `S0306`
- `S0307`
- `S0308`
- `S0401`
- `S0402`
- `S0403`
- `S0404`
- `S0405`
- `S0406`
- `S0407`
- `S0501`
- `S0502`
- `S0503`
- `S0504`
- `S0505`
- `S0506`
- `S0601`
- `S0602`
- `S0603`
- `S0604`
- `S0701`
- `S0702`
- `S0703`
- `S0704`
- `S0705`
- `S0706`
- `S0801`
- `S0802`
- `S0803`
- `S0804`
- `S0805`
- `S0806`
- `S0807`
- `S0901`
- `S0902`
- `S0903`
- `S0904`
- `S0905`
- `S0906`
- `S1001`
- `S1002`
- `S1003`
- `S1004`
- `S1005`
- `T0101`
- `T0102`
- `T0103`
- `T0104`
