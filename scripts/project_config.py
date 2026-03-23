from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = REPO_ROOT.parent
BOOK_PROJECT_ROOT = WORKSPACE_ROOT / "book_project"
BOOK_CHAPTERS_DIR = BOOK_PROJECT_ROOT / "manuscript" / "chapters"
BOOK_DATA_DIR = BOOK_PROJECT_ROOT / "data"
PRIVATE_CACHE_DIR = REPO_ROOT / "private_cache"

AUTHOR = "南洋理工DAN读博笔记（小红书）"
REPO_NAME = "dan-research-skillkit"
REPO_DESCRIPTION = (
    "A bilingual academic skill toolkit for Claude Code and Codex, "
    "built from an originally reconstructed research workflow library."
)

CODE_LICENSE = "MIT"
DOCS_LICENSE = "CC BY-NC 4.0"

TOP_LEVEL_PREFIX_HINTS = {
    "a": "literature",
    "b": "question-gap",
    "c": "writing",
    "d": "review-paper",
    "e": "planning",
    "f": "defense",
    "g": "tools",
    "h": "methods",
    "i": "planning",
    "j": "research",
    "z": "research",
    "0": "archive",
    "1": "research",
    "2": "audio",
}

SKILLS = [
    {
        "skill_id": "dan-research",
        "pack_id": "research",
        "dir_name": "research",
        "title_zh": "研究总览与主线导航",
        "title_en": "Research Map and Lifecycle Navigation",
        "description_zh": "用全局地图帮助研究者判断自己所处阶段、下一步产出与优先任务。",
        "description_en": "Route researchers through the full lifecycle, stage diagnosis, and next-output planning.",
        "triggers": [
            "I do not know where to start my research",
            "Help me locate my current PhD stage",
            "我现在卡在哪个阶段",
            "帮我梳理整体研究路径",
        ],
        "scope_in": [
            "research stage diagnosis",
            "lifecycle planning",
            "output mapping",
            "chapter-to-stage navigation",
        ],
        "scope_out": [
            "database-specific search strings",
            "statistical implementation details",
            "journal formatting minutiae",
        ],
        "related_skills": [
            "dan-literature",
            "dan-question-gap",
            "dan-planning",
        ],
        "chapter_file": "ch01_overall_map.md",
        "source_themes": ["overall_map", "appendix"],
        "pack_summary_zh": "把读博任务、论文生成路径、阶段性产出和学位论文组织方式放回同一张地图，帮助用户先判断自己身处何处，再判断下一步最值得交付什么。",
        "pack_summary_en": "This pack turns the research lifecycle into a usable map: stage, task, and output are aligned so a researcher can decide what comes next instead of staying lost in activity.",
        "concepts": [
            "主线任务 / core research tracks",
            "研究生命周期 / research lifecycle",
            "产出层 / output layer",
            "阶段诊断 / stage diagnosis",
        ],
        "frameworks": [
            {
                "title": "Three-Layer Diagnosis",
                "description": "Look at every bottleneck through task, stage, and output before deciding what to do next.",
            },
            {
                "title": "Seven Core Tracks",
                "description": "Problem formation, literature building, theory framing, design, paper production, feedback loops, and thesis organization.",
            },
        ],
        "checklists": [
            "What stage am I in right now?",
            "What concrete output should this week produce?",
            "Which next skill should I route to after diagnosis?",
        ],
        "templates": [
            "stage-diagnosis-note",
            "next-output table",
        ],
    },
    {
        "skill_id": "dan-literature",
        "pack_id": "literature",
        "dir_name": "literature",
        "title_zh": "文献检索、阅读与文献池搭建",
        "title_en": "Literature Search, Reading, and Evidence Pool Building",
        "description_zh": "把找文献、筛文献、做笔记和搭文献池连成一条可复用工作流。",
        "description_en": "Turn search, screening, note-taking, and synthesis into a reusable literature workflow.",
        "triggers": [
            "How should I read papers efficiently",
            "Build me a literature workflow",
            "我不会读文献",
            "帮我搭文献池",
        ],
        "scope_in": [
            "keyword planning",
            "screening layers",
            "reading depth decisions",
            "literature matrix design",
        ],
        "scope_out": [
            "full systematic-review protocol",
            "journal submission strategy",
            "field-specific bibliometrics",
        ],
        "related_skills": [
            "dan-question-gap",
            "dan-paper-writing",
            "dan-academic-tools",
        ],
        "chapter_file": "ch02_literature_workflow.md",
        "source_themes": ["literature"],
        "pack_summary_zh": "这个知识包把文献工作拆成可执行的四步链：关键词与入口、初始池与分层、精读与笔记、整理表与文献金字塔。",
        "pack_summary_en": "This pack reframes literature work as a four-step system: search, screen, read, and synthesize into a living evidence pool.",
        "concepts": [
            "文献池 / evidence pool",
            "精读 / deep reading",
            "文献整理表 / literature matrix",
            "文献金字塔 / literature pyramid",
        ],
        "frameworks": [
            {
                "title": "Four-Step Literature Chain",
                "description": "Search, read, note, and organize. Each step narrows the pool and increases reuse value.",
            },
            {
                "title": "Layered Screening",
                "description": "Separate background, related, directly relevant, and method-support papers before reading intensively.",
            },
        ],
        "checklists": [
            "Why is this paper worth keeping?",
            "Which field in the note makes it reusable later?",
            "Does my current pool answer the present research question?",
        ],
        "templates": [
            "literature-matrix",
            "deep-reading note",
            "paper-retention checklist",
        ],
    },
    {
        "skill_id": "dan-question-gap",
        "pack_id": "question-gap",
        "dir_name": "question-gap",
        "title_zh": "研究问题、research gap 与创新点形成",
        "title_en": "Research Questions, Gaps, and Contribution Formation",
        "description_zh": "帮助用户把方向压缩成值得研究的问题，并把 gap 转成创新点与贡献表述。",
        "description_en": "Help researchers compress a broad area into a study-worthy question, then turn the gap into a defensible contribution.",
        "triggers": [
            "How do I find a research gap",
            "Turn this topic into a research question",
            "帮我找 research gap",
            "把方向变成问题",
        ],
        "scope_in": [
            "question formation",
            "gap typology",
            "value justification",
            "problem boundaries",
        ],
        "scope_out": [
            "full theory writing",
            "full literature-search execution",
            "statistical model choice",
        ],
        "related_skills": [
            "dan-literature",
            "dan-theory",
            "dan-design",
        ],
        "chapter_file": "ch03_research_questions.md",
        "source_themes": ["research_question"],
        "pack_summary_zh": "这个知识包关注从方向到问题、从问题到 gap、从 gap 到创新点的三段压缩过程，强调边界、价值与可研究性。",
        "pack_summary_en": "This pack focuses on the compression chain from topic to question, from question to gap, and from gap to contribution.",
        "concepts": [
            "研究问题 / research question",
            "研究空缺 / research gap",
            "创新点 / novelty",
            "研究边界 / scope boundary",
        ],
        "frameworks": [
            {
                "title": "Topic-to-Question Compression",
                "description": "Move from broad direction to object, relationship, and boundary in one sentence.",
            },
            {
                "title": "Gap-to-Contribution Ladder",
                "description": "A gap matters only when you can explain why filling it changes explanation, evidence, comparison, or boundary conditions.",
            },
        ],
        "checklists": [
            "Is the question researchable with available evidence?",
            "What kind of gap am I claiming?",
            "Why would the answer matter beyond curiosity?",
        ],
        "templates": [
            "one-sentence research question",
            "gap statement",
            "contribution note",
        ],
    },
    {
        "skill_id": "dan-theory",
        "pack_id": "theory",
        "dir_name": "theory",
        "title_zh": "理论基础、概念框架与理论贡献",
        "title_en": "Theory Base, Conceptual Framework, and Theoretical Contribution",
        "description_zh": "帮助用户从文献中搭建概念框架、理论逻辑和理论贡献表达。",
        "description_en": "Build conceptual frameworks, theoretical logic, and contribution claims from the literature base.",
        "triggers": [
            "How do I build a conceptual framework",
            "What counts as theoretical contribution",
            "帮我搭理论框架",
            "理论贡献怎么写",
        ],
        "scope_in": [
            "theory selection",
            "conceptual framework building",
            "mechanism logic",
            "theory contribution statements",
        ],
        "scope_out": [
            "full empirical design",
            "journal fit decisions",
            "line-by-line copyediting",
        ],
        "related_skills": [
            "dan-question-gap",
            "dan-design",
            "dan-paper-writing",
        ],
        "chapter_file": "ch04_theory_and_contribution.md",
        "source_themes": ["theory_model"],
        "pack_summary_zh": "这个知识包把理论部分从“堆理论”改成“解释现象的结构”，重点是概念、关系、机制、边界和贡献写法。",
        "pack_summary_en": "This pack treats theory as an explanatory structure rather than a list of citations, with emphasis on concepts, mechanisms, boundaries, and contribution claims.",
        "concepts": [
            "理论基础 / theoretical base",
            "概念框架 / conceptual framework",
            "机制链 / mechanism chain",
            "理论贡献 / theoretical contribution",
        ],
        "frameworks": [
            {
                "title": "Concept-Relation-Mechanism",
                "description": "Clarify the concepts, their relationships, and the mechanism that makes the relationship meaningful.",
            },
            {
                "title": "Five Contribution Moves",
                "description": "Extend, refine, integrate, bound, or re-specify an existing explanation instead of making vague novelty claims.",
            },
        ],
        "checklists": [
            "Why this theory and not another nearby explanation?",
            "What mechanism am I truly claiming?",
            "Would the contribution still hold without my core argument?",
        ],
        "templates": [
            "conceptual framework note",
            "mechanism statement",
            "theoretical contribution paragraph",
        ],
    },
    {
        "skill_id": "dan-design",
        "pack_id": "design",
        "dir_name": "design",
        "title_zh": "研究设计、证据类型与方法匹配",
        "title_en": "Research Design, Evidence Types, and Method Fit",
        "description_zh": "用问题、解释、证据、分析四重对齐来设计研究方案。",
        "description_en": "Use a four-layer alignment model to connect question, explanation, evidence, and analysis.",
        "triggers": [
            "Help me choose a method",
            "Does my design fit my research question",
            "帮我选研究方法",
            "我的设计和问题匹配吗",
        ],
        "scope_in": [
            "research design alignment",
            "data-type selection",
            "mixed methods logic",
            "content analysis framing",
        ],
        "scope_out": [
            "software-specific analysis code",
            "journal reviewer response wording",
            "full thesis structuring",
        ],
        "related_skills": [
            "dan-question-gap",
            "dan-theory",
            "dan-method-atlas",
        ],
        "chapter_file": "ch05_research_design.md",
        "source_themes": ["methods"],
        "pack_summary_zh": "这个知识包把方法选择从‘熟悉什么做什么’改成‘问题、理论、数据、分析是否对齐’的判断过程。",
        "pack_summary_en": "This pack shifts method choice away from habit and toward alignment among the research question, theoretical task, evidence, and analysis.",
        "concepts": [
            "研究设计 / research design",
            "证据策略 / evidence strategy",
            "混合研究 / mixed methods",
            "内容分析 / content analysis",
        ],
        "frameworks": [
            {
                "title": "Four-Layer Alignment",
                "description": "Question, explanation, evidence, and analysis should narrow together rather than drift apart.",
            },
            {
                "title": "Method-by-Task Matching",
                "description": "Choose methods by whether you need to describe, compare, explain, validate, or trace a process.",
            },
        ],
        "checklists": [
            "What kind of answer does the question require?",
            "Can the available evidence actually support that answer?",
            "Is mixed methods serving a real explanatory task?",
        ],
        "templates": [
            "design alignment note",
            "method-fit checklist",
            "data-evidence table",
        ],
    },
    {
        "skill_id": "dan-paper-writing",
        "pack_id": "writing",
        "dir_name": "writing",
        "title_zh": "论文结构、章节呼应与表达边界",
        "title_en": "Paper Structure, Section Logic, and Writing Boundaries",
        "description_zh": "把论文写作拆成结构设计、章节接口和表达策略三层。",
        "description_en": "Break paper writing into structure, section interfaces, and expression boundaries.",
        "triggers": [
            "How should I structure my paper",
            "Help me outline an introduction or discussion",
            "论文结构怎么搭",
            "discussion 怎么写",
        ],
        "scope_in": [
            "paper outline",
            "section-by-section logic",
            "results vs discussion boundaries",
            "conceptual framework writing",
        ],
        "scope_out": [
            "review-paper protocol",
            "journal cover letter drafting",
            "dataset construction",
        ],
        "related_skills": [
            "dan-theory",
            "dan-design",
            "dan-submission",
        ],
        "chapter_file": "ch06_paper_structure.md",
        "source_themes": ["writing"],
        "pack_summary_zh": "这个知识包关注单篇论文的叙述闭环：问题怎样被引出、理论怎样被承接、方法怎样被解释、结果怎样被讨论。",
        "pack_summary_en": "This pack focuses on the narrative closure of a paper: how the question is introduced, theory is carried, methods are justified, and results are interpreted.",
        "concepts": [
            "八大模块 / eight core modules",
            "章节接口 / section interfaces",
            "结果与讨论边界 / results-discussion boundary",
            "写作顺序 / drafting sequence",
        ],
        "frameworks": [
            {
                "title": "Eight-Module Skeleton",
                "description": "Use a stable paper skeleton so each section contributes to one argument rather than becoming a standalone memo.",
            },
            {
                "title": "Section Handoffs",
                "description": "Each section should answer what the next section now needs to justify.",
            },
        ],
        "checklists": [
            "What job does this section do in the overall argument?",
            "Does the next section logically require what I have just written?",
            "Am I reporting results or interpreting them?",
        ],
        "templates": [
            "paper-outline sheet",
            "introduction scaffold",
            "results-discussion boundary checklist",
        ],
    },
    {
        "skill_id": "dan-review-paper",
        "pack_id": "review-paper",
        "dir_name": "review-paper",
        "title_zh": "综述论文类型、筛选规范与写作组织",
        "title_en": "Review Article Types, Screening Standards, and Writing Logic",
        "description_zh": "帮助用户区分综述论文与文献综述，并组织综述的筛选、分类和贡献表达。",
        "description_en": "Differentiate review articles from regular literature reviews and organize screening, synthesis, and contribution writing.",
        "triggers": [
            "How do I write a review paper",
            "Should this be a systematic review or not",
            "综述论文怎么写",
            "PRISMA 应该怎么用",
        ],
        "scope_in": [
            "review type selection",
            "screening criteria",
            "PRISMA-ready workflows",
            "review findings structure",
        ],
        "scope_out": [
            "single-study empirical writing",
            "response letter drafting",
            "general planning coaching",
        ],
        "related_skills": [
            "dan-literature",
            "dan-question-gap",
            "dan-paper-writing",
        ],
        "chapter_file": "ch07_review_writing.md",
        "source_themes": ["review", "appendix"],
        "pack_summary_zh": "这个知识包强调综述论文不是把文献堆在一起，而是通过筛选标准、组织逻辑和发现结构形成独立贡献。",
        "pack_summary_en": "This pack frames a review article as an argument built from explicit selection rules, synthesis logic, and an interpretable findings structure.",
        "concepts": [
            "综述论文 / review article",
            "文献综述 / literature review section",
            "纳入标准 / inclusion criteria",
            "PRISMA-ready process",
        ],
        "frameworks": [
            {
                "title": "Review-Type Decision",
                "description": "Choose among narrative, systematic, scoping, or theory-building review according to the problem and evidence base.",
            },
            {
                "title": "Screen-Sort-Synthesize",
                "description": "Move from corpus building to coding, then from coding to analytical contribution.",
            },
        ],
        "checklists": [
            "What kind of review am I truly writing?",
            "Would another researcher understand my inclusion logic?",
            "Are my findings organized as an argument rather than a stack of summaries?",
        ],
        "templates": [
            "review protocol note",
            "inclusion criteria sheet",
            "review findings matrix",
        ],
    },
    {
        "skill_id": "dan-submission",
        "pack_id": "submission",
        "dir_name": "submission",
        "title_zh": "投稿、返修与审稿沟通",
        "title_en": "Submission, Revision, and Reviewer Communication",
        "description_zh": "帮助用户处理投稿前判断、附件清单、返修结构和分歧沟通。",
        "description_en": "Support pre-submission checks, submission packages, response letters, and reviewer negotiation.",
        "triggers": [
            "How do I reply to reviewers",
            "Help me prepare my submission package",
            "返修怎么写 response letter",
            "投稿前要准备什么",
        ],
        "scope_in": [
            "submission package planning",
            "reviewer response logic",
            "revision strategy",
            "disagreement framing",
        ],
        "scope_out": [
            "full paper drafting",
            "detailed stats debugging",
            "research question formation",
        ],
        "related_skills": [
            "dan-paper-writing",
            "dan-defense",
            "dan-academic-tools",
        ],
        "chapter_file": "ch08_submission_and_revision.md",
        "source_themes": ["submission"],
        "pack_summary_zh": "这个知识包把投稿看成一个沟通过程，而不仅是上传文件。重点包括投稿前判断、材料完整性、意见分类与回应逻辑。",
        "pack_summary_en": "This pack treats submission as a communication workflow rather than a file-upload event, with emphasis on package readiness and reviewer response logic.",
        "concepts": [
            "投稿包 / submission package",
            "返修逻辑 / revision logic",
            "回应矩阵 / response matrix",
            "分歧沟通 / disagreement management",
        ],
        "frameworks": [
            {
                "title": "Submit-Respond-Revise Loop",
                "description": "A manuscript improves through staged communication rather than one final upload.",
            },
            {
                "title": "Comment-Type Triage",
                "description": "Separate mandatory corrections, clarifications, defensible disagreements, and future-work notes before replying.",
            },
        ],
        "checklists": [
            "Is the manuscript actually submission-ready?",
            "What category does each reviewer comment belong to?",
            "Does my reply explain both action and rationale?",
        ],
        "templates": [
            "submission package checklist",
            "response letter skeleton",
            "reviewer comment matrix",
        ],
    },
    {
        "skill_id": "dan-defense",
        "pack_id": "defense",
        "dir_name": "defense",
        "title_zh": "学术汇报、开题中期与毕业答辩",
        "title_en": "Academic Presentation, Proposal Defense, and Final Defense",
        "description_zh": "帮助用户按场景准备文献汇报、proposal defense、mid-term review 和 final defense。",
        "description_en": "Prepare literature talks, proposal defenses, mid-term reviews, and final defenses by communication scenario.",
        "triggers": [
            "Help me prepare for my proposal defense",
            "How should I structure an academic presentation",
            "开题答辩怎么准备",
            "学术汇报怎么讲",
        ],
        "scope_in": [
            "presentation structure",
            "defense slide logic",
            "oral explanation boundaries",
            "thesis-organization communication",
        ],
        "scope_out": [
            "full manuscript submission",
            "detailed qualitative coding",
            "database search strategies",
        ],
        "related_skills": [
            "dan-research",
            "dan-paper-writing",
            "dan-submission",
        ],
        "chapter_file": "ch09_presentation_and_defense.md",
        "source_themes": ["defense", "appendix"],
        "pack_summary_zh": "这个知识包按汇报场景而不是按幻灯片模板来组织，帮助用户识别‘要讲什么、给谁讲、讲到多深’。",
        "pack_summary_en": "This pack organizes presentation work by scenario rather than slide aesthetics, so the speaker can decide what to say, to whom, and at what depth.",
        "concepts": [
            "学术汇报 / academic presentation",
            "开题答辩 / proposal defense",
            "中期答辩 / mid-term review",
            "毕业答辩 / final defense",
        ],
        "frameworks": [
            {
                "title": "Audience-Question-Evidence",
                "description": "Choose slides and speaking depth by what the audience needs to understand or challenge.",
            },
            {
                "title": "Defense Scenario Routing",
                "description": "Proposal, progress review, and final defense each require different levels of certainty and scope.",
            },
        ],
        "checklists": [
            "What is the core decision this defense is trying to secure?",
            "What evidence must the audience trust before moving on?",
            "What belongs in slides versus the spoken explanation?",
        ],
        "templates": [
            "defense storyline sheet",
            "slide-logic checklist",
            "audience-question rehearsal sheet",
        ],
    },
    {
        "skill_id": "dan-planning",
        "pack_id": "planning",
        "dir_name": "planning",
        "title_zh": "科研规划、时间安排与长期推进",
        "title_en": "Research Planning, Time Allocation, and Long-Term Execution",
        "description_zh": "帮助用户把长期研究拆成阶段、节奏、里程碑和复盘机制。",
        "description_en": "Turn long-horizon research into stages, rhythms, milestones, and review loops.",
        "triggers": [
            "Help me plan my PhD workflow",
            "I am stuck and not making progress",
            "科研时间安排怎么做",
            "我总推进不下去",
        ],
        "scope_in": [
            "time planning",
            "weekly and monthly pacing",
            "milestone design",
            "execution diagnostics",
        ],
        "scope_out": [
            "topic-specific theory building",
            "journal formatting",
            "coding or statistical estimation",
        ],
        "related_skills": [
            "dan-research",
            "dan-literature",
            "dan-defense",
        ],
        "chapter_file": "ch10_planning_and_execution.md",
        "source_themes": ["planning", "overall_map"],
        "pack_summary_zh": "这个知识包关注长期推进而不是短期热情，强调阶段任务、每周节奏、里程碑产出和复盘修正。",
        "pack_summary_en": "This pack focuses on sustained progress instead of short bursts of effort, using stages, weekly rhythms, deliverables, and review loops.",
        "concepts": [
            "阶段治理 / stage governance",
            "里程碑 / milestone",
            "四周推进 / four-week rhythm",
            "复盘 / review loop",
        ],
        "frameworks": [
            {
                "title": "Stage-Rhythm-Output",
                "description": "Every long task needs a stage definition, a short rhythm, and a concrete output.",
            },
            {
                "title": "Bottleneck Review Loop",
                "description": "Diagnose whether the slowdown comes from unclear direction, weak structure, missing data, or low execution bandwidth.",
            },
        ],
        "checklists": [
            "What is the next visible deliverable?",
            "Does this week advance a stage or only create noise?",
            "What bottleneck needs diagnosis before more effort?",
        ],
        "templates": [
            "weekly planning sheet",
            "milestone tracker",
            "bottleneck review note",
        ],
    },
    {
        "skill_id": "dan-method-atlas",
        "pack_id": "methods",
        "dir_name": "methods",
        "title_zh": "方法图谱与任务-方法对照",
        "title_en": "Method Atlas and Task-to-Method Mapping",
        "description_zh": "给研究者提供跨方法导航，而不是单一方法教程。",
        "description_en": "Offer cross-method navigation instead of a single-method tutorial.",
        "triggers": [
            "Which methods are suitable for this type of question",
            "Give me a method atlas",
            "给我一个方法图谱",
            "什么问题适合什么方法",
        ],
        "scope_in": [
            "cross-method comparison",
            "task-to-method routing",
            "evidence-type overview",
            "method risk awareness",
        ],
        "scope_out": [
            "software-specific execution",
            "complete study design writing",
            "submission or defense coaching",
        ],
        "related_skills": [
            "dan-design",
            "dan-theory",
            "dan-review-paper",
        ],
        "chapter_file": "ch05_research_design.md",
        "source_themes": ["methods", "theory_model", "review"],
        "pack_summary_zh": "这个知识包不教某一个软件怎么点，而是帮助用户理解不同问题、不同证据和不同方法之间的映射关系。",
        "pack_summary_en": "This pack does not teach a single software workflow; it helps researchers understand how question types, evidence types, and methods map to one another.",
        "concepts": [
            "方法图谱 / method atlas",
            "任务-方法映射 / task-method routing",
            "证据形态 / evidence form",
            "设计风险 / design risk",
        ],
        "frameworks": [
            {
                "title": "Question-to-Method Matrix",
                "description": "Compare method families by the kind of answer they can credibly support.",
            },
            {
                "title": "Evidence-to-Analysis Matrix",
                "description": "Map data forms to analysis strategies before choosing a named method.",
            },
        ],
        "checklists": [
            "What answer format do I need: pattern, relationship, mechanism, or process?",
            "What evidence form do I have or can realistically get?",
            "What method family is being excluded, and why?",
        ],
        "templates": [
            "question-method matrix",
            "evidence-analysis matrix",
            "design risk table",
        ],
    },
    {
        "skill_id": "dan-academic-tools",
        "pack_id": "tools",
        "dir_name": "tools",
        "title_zh": "学术工具、模板与 AI 辅助边界",
        "title_en": "Academic Tools, Templates, and AI Usage Boundaries",
        "description_zh": "整理文献、写作、投稿、汇报和规划中的工具流与模板流。",
        "description_en": "Organize toolflows and reusable templates for literature work, writing, submission, presentation, and planning.",
        "triggers": [
            "What tools should I use for this research workflow",
            "Help me choose a template or toolchain",
            "科研工具怎么搭",
            "有哪些可复用模板",
        ],
        "scope_in": [
            "toolchain selection",
            "template routing",
            "AI assistance boundaries",
            "workflow support assets",
        ],
        "scope_out": [
            "proprietary software training",
            "sensitive data processing advice",
            "domain-specific programming frameworks",
        ],
        "related_skills": [
            "dan-literature",
            "dan-paper-writing",
            "dan-submission",
        ],
        "chapter_file": "ch10_planning_and_execution.md",
        "source_themes": ["tools", "literature", "writing", "submission", "defense", "planning"],
        "pack_summary_zh": "这个知识包把工具当成支持系统，而不是研究能力的替代品，重点是模板调用、信息组织和 AI 辅助边界。",
        "pack_summary_en": "This pack treats tools as support systems rather than substitutes for research thinking, with focus on templates, information organization, and AI boundaries.",
        "concepts": [
            "工具流 / toolflow",
            "模板流 / template flow",
            "AI 辅助边界 / AI assistance boundary",
            "研究支持系统 / research support system",
        ],
        "frameworks": [
            {
                "title": "Tool-by-Task Routing",
                "description": "Choose tools according to the research task they support rather than novelty or trend value.",
            },
            {
                "title": "Template Reuse Ladder",
                "description": "Start with a stable scaffold, then adapt it to the current stage, audience, and output requirement.",
            },
        ],
        "checklists": [
            "Does this tool reduce friction or create more switching cost?",
            "What part should remain human judgment?",
            "Which template can shorten setup without freezing thinking?",
        ],
        "templates": [
            "toolchain audit",
            "template selection sheet",
            "AI boundary checklist",
        ],
    },
    {
        "skill_id": "dan-upgrade",
        "pack_id": "upgrade",
        "dir_name": "upgrade",
        "title_zh": "知识包更新、来源刷新与双宿主发布",
        "title_en": "Pack Refresh, Source Updates, and Dual-Host Publishing",
        "description_zh": "维护 skillkit 的增量更新、来源映射和双宿主分发。",
        "description_en": "Maintain incremental updates, source mapping, and dual-host skill distribution.",
        "triggers": [
            "Update this research skillkit",
            "Refresh packs after new source material arrives",
            "更新这个 skillkit",
            "刷新来源映射和技能布局",
        ],
        "scope_in": [
            "source refresh",
            "pack regeneration",
            "dual-host build",
            "coverage checks",
        ],
        "scope_out": [
            "subject-matter answering for a specific research problem",
            "paper drafting",
            "private-source publication decisions",
        ],
        "related_skills": [
            "dan-research",
            "dan-method-atlas",
            "dan-academic-tools",
        ],
        "chapter_file": None,
        "source_themes": ["overall_map", "literature", "research_question", "theory_model", "methods", "writing", "review", "submission", "defense", "planning", "tools"],
        "pack_summary_zh": "这个知识包面向维护者，规定新增来源如何进入私有提取层、如何更新公开 knowledge packs，以及如何同步 Claude Code 和 Codex 布局。",
        "pack_summary_en": "This pack is for maintainers. It defines how new source material enters the private extraction layer, how public packs are refreshed, and how Claude Code and Codex layouts stay in sync.",
        "concepts": [
            "增量更新 / incremental update",
            "中性来源映射 / neutral source mapping",
            "双宿主分发 / dual-host distribution",
            "覆盖率审计 / coverage audit",
        ],
        "frameworks": [
            {
                "title": "Ingest-Normalize-Build-Validate",
                "description": "Every update passes through ingest, normalization, pack rebuild, and validation before release.",
            },
            {
                "title": "Single-Source Skill Layout",
                "description": "Keep `skills-src/` as the truth and regenerate both host layouts instead of editing them directly.",
            },
        ],
        "checklists": [
            "Did new source material change any public pack?",
            "Did the rebuild regenerate both host layouts?",
            "Did validation catch forbidden strings or forbidden file types?",
        ],
        "templates": [
            "update checklist",
            "source intake note",
            "release validation sheet",
        ],
    },
]

PACKS_BY_ID = {item["pack_id"]: item for item in SKILLS}
SKILLS_BY_ID = {item["skill_id"]: item for item in SKILLS}

PACK_DETAILS_BY_ID = {
    "research": {
        "situations": [
            "刚入题，不知道先做文献、问题还是方法",
            "做了很多任务，但说不清自己目前处于哪个阶段",
            "已经有若干草稿或结果，却不会把它们放回长期研究路径",
        ],
        "workflow_steps": [
            "先判断当前卡点属于任务层、阶段层还是产出层。",
            "把当前目标改写成一份看得见的阶段性产出，而不是抽象目标。",
            "确认该产出对应的是哪条主线任务，以及它会喂给下一个什么环节。",
            "为当前阶段选择一个主 skill，不在多个方法之间来回切换。",
            "每周用同一张阶段诊断表回顾是否真的向下一个阶段推进。",
        ],
        "decision_rules": [
            "如果你无法判断要做什么，先做阶段诊断，而不是先找工具。",
            "如果你做了很多零碎任务却没有稳定产出，说明当前问题在产出层。",
            "如果你已经有材料但仍然推进混乱，优先检查长期主线是否清楚。",
        ],
        "deliverables": [
            "阶段诊断表",
            "下一产出清单",
            "主线任务定位图",
            "章节或研究单元路线图",
        ],
        "pitfalls": [
            "把短期任务误当成长期目标",
            "把论文章节误当成研究阶段",
            "同时补太多环节，结果每个环节都推进很浅",
            "只盯眼前 deadline，不看长期研究主线",
        ],
        "example_prompts": [
            "请帮我判断我现在卡在研究生命周期的哪一层。",
            "请把我手头这些任务重写成阶段性产出。",
            "请按读博主线帮我决定下一步应该先补哪一块。",
        ],
        "corpus_buckets": [
            {"label": "读博主线与阶段地图", "keywords": ["读博", "阶段", "全流程", "路径", "生命周期"]},
            {"label": "博士论文组织与整合", "keywords": ["博士论文", "大论文", "thesis"]},
            {"label": "阶段卡点与推进诊断", "keywords": ["卡点", "定位", "问题", "任务"]},
        ],
    },
    "literature": {
        "situations": [
            "刚开始做题，需要从 0 搭一个可持续的文献池",
            "已经存了很多 PDF，但写综述或写引言时调不出来",
            "读完文献有印象，却做不出可比较、可复用的笔记",
        ],
        "workflow_steps": [
            "围绕研究对象、关系、情境和方法线索拆关键词组。",
            "做第一轮检索并按全景、相关、直接相关、补充四层分流。",
            "只对高价值文献做精读，并统一笔记字段。",
            "把新笔记放回同一张 literature matrix，而不是分散在零碎文档里。",
            "定期重画文献金字塔，判断核心层是否真的服务当前问题。",
        ],
        "decision_rules": [
            "问题还很散时，先扩广度，不要一上来精读太深。",
            "理论尚未稳定时，优先保留概念和机制型文献，而不是只看结论型文献。",
            "写作卡住时，按章节用途回调文献，而不是继续盲目扩库。",
        ],
        "deliverables": [
            "关键词网格",
            "文献筛选记录",
            "统一字段笔记",
            "文献整理表",
            "文献金字塔",
        ],
        "pitfalls": [
            "把下载等同于积累",
            "所有文献平均用力",
            "笔记只有摘抄，没有比较字段",
            "整理停留在文件夹管理层",
        ],
        "example_prompts": [
            "请把我的研究方向拆成一组可检索关键词。",
            "请给我一个围绕研究问题的文献整理表字段设计。",
            "请帮我判断哪些文献应该进入精读层。",
        ],
        "corpus_buckets": [
            {"label": "检索与入口设计", "keywords": ["检索", "关键词", "数据库", "参考文献"]},
            {"label": "阅读步骤与笔记", "keywords": ["文献阅读", "读文献", "笔记", "精读"]},
            {"label": "整理表与分类结构", "keywords": ["整理", "归纳", "表格", "金字塔"]},
            {"label": "全局观与综述过渡", "keywords": ["全局观", "综述", "脉络"]},
        ],
    },
    "question-gap": {
        "situations": [
            "方向很多，但总写不出一句可研究的问题",
            "感觉主题有价值，却说不清 gap 在哪里",
            "知道想做创新，但贡献表述总是空泛",
        ],
        "workflow_steps": [
            "先把方向压成对象、关系和边界三要素。",
            "判断你缺的是现象理解、理论解释、方法设计还是情境比较。",
            "把 gap 写成一句‘已有研究做了什么，还缺什么，为何值得补’。",
            "把 gap 再推进成具体创新点和预期贡献。",
            "最后反查：这个问题是否真的能被现有证据支持。",
        ],
        "decision_rules": [
            "如果问题一句话里没有对象、关系和边界，就还不是研究问题。",
            "如果 gap 只能说‘很少有人研究’，那还不够。",
            "如果贡献不能回到理论、方法、证据或边界，说明创新点还太虚。",
        ],
        "deliverables": [
            "一句话研究问题",
            "gap 说明",
            "创新点说明",
            "研究边界说明",
        ],
        "pitfalls": [
            "把热门主题直接当作研究问题",
            "把研究不足写成泛泛空白",
            "只会列创新点，不会说明为什么重要",
            "问题太大，证据能力太弱",
        ],
        "example_prompts": [
            "请把这个研究方向压成一个有边界的问题。",
            "请帮我把现有文献里的缺口转成可写的 gap。",
            "请检查这个贡献说法是不是仍然太空。",
        ],
        "corpus_buckets": [
            {"label": "研究问题形成", "keywords": ["研究问题", "问题", "选题", "a+b"]},
            {"label": "gap 与创新点", "keywords": ["gap", "创新", "创新点", "research gap"]},
            {"label": "研究价值与边界", "keywords": ["价值", "意义", "边界"]},
        ],
    },
    "theory": {
        "situations": [
            "文献读了很多，但理论部分始终像资料堆砌",
            "知道几个变量，却说不清概念之间的机制关系",
            "写贡献时只会说‘丰富了现有研究’",
        ],
        "workflow_steps": [
            "先明确这项研究到底要解释什么现象。",
            "从文献中筛出最能承担解释任务的概念，而不是把所有理论都列上。",
            "把概念关系、机制链和边界条件画成框架。",
            "把理论任务写成一条可被检验或解释的逻辑链。",
            "最后把贡献归位到扩展、修正、整合、限定或重述之一。",
        ],
        "decision_rules": [
            "理论不是背景知识，而是解释结构。",
            "如果变量之间只有箭头没有机制，框架还不够。",
            "如果贡献不改变现有解释的任何部分，它就不是理论贡献。",
        ],
        "deliverables": [
            "概念框架图",
            "机制链说明",
            "理论选择理由",
            "理论贡献段落",
        ],
        "pitfalls": [
            "把理论综述写成百科全书",
            "把概念框架当成变量罗列",
            "贡献只写抽象形容词",
            "忽略边界条件和适用场景",
        ],
        "example_prompts": [
            "请帮我把这些概念整理成一个机制链。",
            "请判断这段理论部分是在解释现象还是只是在堆文献。",
            "请把我的贡献压到五种理论动作里。",
        ],
        "corpus_buckets": [
            {"label": "常见理论与经典文献", "keywords": ["理论", "framework", "acceptance", "privacy", "trust"]},
            {"label": "概念框架与模型", "keywords": ["conceptual framework", "模型", "结构模型"]},
            {"label": "理论贡献写法", "keywords": ["贡献", "theoretical contribution", "理论贡献"]},
        ],
    },
    "design": {
        "situations": [
            "问题已经有了，但不知道该用什么数据和方法",
            "方法会不少，但不知道哪种最适合当前问题",
            "设计写出来像流程说明，缺少逻辑对齐",
        ],
        "workflow_steps": [
            "先判断问题要回答的是关系、机制、比较还是过程。",
            "明确理论层真正需要什么类型的证据。",
            "先定数据形态和获取路径，再定分析方法。",
            "如果考虑 mixed methods，明确每种证据分别承担什么任务。",
            "用一张对齐表复查问题、理论、数据和分析是否互相支持。",
        ],
        "decision_rules": [
            "方法服从问题，不反过来。",
            "数据类型先于具体分析软件或模型名。",
            "混合研究必须有分工，不是多做一点就叫 mixed methods。",
        ],
        "deliverables": [
            "设计对齐表",
            "数据-证据说明",
            "方法选择理由",
            "开题设计核对表",
        ],
        "pitfalls": [
            "先爱上一种方法再倒找问题",
            "想回答复杂机制却只有薄弱数据",
            "把定量和定性误当成研究逻辑本身",
            "设计写得很满，却没有说明为什么要这样设计",
        ],
        "example_prompts": [
            "请判断这个问题需要什么类型的证据。",
            "请帮我比较两种设计哪个更匹配当前问题。",
            "请检查我的 mixed methods 是否真的有分工逻辑。",
        ],
        "corpus_buckets": [
            {"label": "数据类型与证据形式", "keywords": ["数据类型", "数据收集", "样本", "访谈", "问卷"]},
            {"label": "mixed methods", "keywords": ["mixed methods", "mixed-method", "混合"]},
            {"label": "内容分析与编码", "keywords": ["内容分析", "编码", "文本"]},
            {"label": "方法选择与常见误区", "keywords": ["方法", "研究设计", "设计"]},
        ],
    },
    "writing": {
        "situations": [
            "材料已经不少，但论文总写不成完整故事",
            "知道每一章大概要写什么，却不知道章节之间怎么接",
            "results 和 discussion 常常混在一起",
        ],
        "workflow_steps": [
            "先用八大模块搭一个整体骨架。",
            "给每一节定义唯一任务，而不是把所有内容都塞进来。",
            "检查上一节是否真的为下一节提供了写作前提。",
            "把方法、结果、讨论的边界提前写成规则。",
            "最后再做例句、润色和表达层面的优化。",
        ],
        "decision_rules": [
            "先建结构，再修句子。",
            "每节必须能回答‘这节为什么存在’。",
            "如果结果段已经开始解释意义，说明 discussion 提前了。",
        ],
        "deliverables": [
            "全篇提纲",
            "章节接口说明",
            "段落任务表",
            "results-discussion 边界表",
        ],
        "pitfalls": [
            "一上来就追求漂亮表达",
            "每节都像独立笔记，缺少论文主线",
            "把理论、方法和结果写成并列堆叠",
            "discussion 只重复 results，不做解释推进",
        ],
        "example_prompts": [
            "请帮我把这篇论文整理成八大模块骨架。",
            "请检查我的 introduction 和 literature review 是否职责混淆。",
            "请重写这个 section handoff，让下一节接得更自然。",
        ],
        "corpus_buckets": [
            {"label": "结构骨架与模块", "keywords": ["模块", "结构", "章节", "introduction", "discussion"]},
            {"label": "章节写法与例句", "keywords": ["例句", "写法", "段落", "results", "discussion"]},
            {"label": "概念框架写作", "keywords": ["conceptual framework", "framework"]},
        ],
    },
    "review-paper": {
        "situations": [
            "想写综述论文，但不知道该做 narrative 还是 systematic",
            "已经收集了一批文献，却不会组织 review findings",
            "知道要做筛选，但 PRISMA 和纳入标准总写得很虚",
        ],
        "workflow_steps": [
            "先判断综述目标：盘点、分类、解释还是建模。",
            "为此选择 review 类型和材料边界。",
            "建立纳入标准、排除标准和筛选记录。",
            "把文献编码成主题、机制、方法或情境维度。",
            "把编码结果改写成发现结构，而不是逐篇摘要。",
        ],
        "decision_rules": [
            "综述论文不是普通 literature review 的拉长版。",
            "没有清晰筛选规则，就很难建立 review 的可信度。",
            "review findings 必须回答领域图景发生了什么变化。",
        ],
        "deliverables": [
            "review 类型说明",
            "筛选协议与记录",
            "编码表",
            "review findings 结构图",
        ],
        "pitfalls": [
            "把综述写成文献流水账",
            "只讲筛选流程，不讲分析逻辑",
            "类型选错，导致方法和贡献都不匹配",
            "future research 只写空泛建议",
        ],
        "example_prompts": [
            "请判断这个题目更适合哪一种 review。",
            "请帮我把筛选后的材料组织成 review findings。",
            "请检查这套纳入标准是否足够清楚。",
        ],
        "corpus_buckets": [
            {"label": "综述类型与对比", "keywords": ["综述", "review", "scoping", "systematic"]},
            {"label": "PRISMA 与筛选规范", "keywords": ["prisma", "筛选", "纳入"]},
            {"label": "经典 review 文献", "keywords": ["signaling", "framework", "theory review"]},
        ],
    },
    "submission": {
        "situations": [
            "准备投稿，但不确定材料是否齐全",
            "收到审稿意见后，不知道怎么分类处理",
            "想表达分歧，但担心回应太硬或太弱",
        ],
        "workflow_steps": [
            "先做投稿前 readiness 检查。",
            "列出所有附件和期刊要求，不把问题留到提交窗口。",
            "把审稿意见拆成纠错、澄清、可辩护分歧和未来工作四类。",
            "先决定修改动作，再写回应理由。",
            "返修后再做一次全文一致性检查，避免局部改完整体失衡。",
        ],
        "decision_rules": [
            "response letter 先解释你做了什么，再解释为什么。",
            "能承认的问题就直接承认，不要绕。",
            "有分歧时，回应的是判断依据，而不是情绪立场。",
        ],
        "deliverables": [
            "投稿材料清单",
            "response letter",
            "审稿意见矩阵",
            "返修一致性检查表",
        ],
        "pitfalls": [
            "把提交当成简单上传",
            "所有意见都用同一种语气回应",
            "只改局部，不检查全文联动",
            "把分歧回应写成防御姿态",
        ],
        "example_prompts": [
            "请帮我把这些 reviewer comments 分类。",
            "请把这条回应改成先动作后理由的结构。",
            "请检查我的 submission package 还缺什么。",
        ],
        "corpus_buckets": [
            {"label": "投稿流程与期刊判断", "keywords": ["投稿", "submit", "期刊"]},
            {"label": "返修与审稿回应", "keywords": ["返修", "reviewer", "response", "修改"]},
            {"label": "投稿附件与模板", "keywords": ["cover letter", "author statement", "highlights"]},
        ],
    },
    "defense": {
        "situations": [
            "即将做开题、中期或毕业答辩，但不知道重点怎么取舍",
            "学术汇报材料很多，却不会讲成一个有逻辑的故事",
            "担心答辩时讲太浅或讲太深",
        ],
        "workflow_steps": [
            "先定义这次汇报要达成的决策目标。",
            "按 audience-question-evidence 三元组安排材料。",
            "把讲稿分成‘必须放在 slides 上’和‘适合口头展开’两层。",
            "预设最容易被追问的几个环节，提前准备证据与解释。",
            "答辩前做一次时间版 rehearsal，保证主线不散。",
        ],
        "decision_rules": [
            "不同答辩场景的目标不同，结构也不同。",
            "讲稿要服务评审问题，而不是服务你想展示的一切努力。",
            "slides 负责结构和证据，口头负责转场和解释。",
        ],
        "deliverables": [
            "汇报主线图",
            "slide 逻辑表",
            "口头讲稿提纲",
            "高频追问清单",
        ],
        "pitfalls": [
            "把答辩做成材料堆砌",
            "每页都信息过满，导致主线不清",
            "只练表达，不练问题应对",
            "不同场景套用同一套 slides",
        ],
        "example_prompts": [
            "请按开题答辩逻辑重排我的 slides。",
            "请帮我区分哪些内容放在 slide，哪些留到口头讲。",
            "请预判这场答辩最可能被追问的 5 个问题。",
        ],
        "corpus_buckets": [
            {"label": "学术汇报与报告", "keywords": ["汇报", "报告", "presentation"]},
            {"label": "开题与中期答辩", "keywords": ["开题", "中期", "proposal"]},
            {"label": "毕业答辩与 thesis 组织", "keywords": ["毕业答辩", "thesis", "大论文"]},
        ],
    },
    "planning": {
        "situations": [
            "知道要做什么，但一周一周推进不稳",
            "任务很多，却没有清晰阶段和里程碑",
            "经常忙得很累，但回头看产出不成形",
        ],
        "workflow_steps": [
            "先确定当前阶段和这个阶段唯一最重要的产出。",
            "把阶段目标拆成四周节奏，再拆成本周推进点。",
            "为每一周指定一个必须完成的可见交付物。",
            "每周复盘一次：哪些工作推进了主线，哪些只是制造噪音。",
            "一旦卡住，优先诊断瓶颈类型，而不是盲目加班。",
        ],
        "decision_rules": [
            "没有可见产出，就不算真正推进。",
            "周计划必须服务阶段目标，而不是把任务塞满。",
            "长期停滞通常不是不努力，而是瓶颈识别错误。",
        ],
        "deliverables": [
            "阶段任务表",
            "四周推进板",
            "本周交付物清单",
            "瓶颈复盘记录",
        ],
        "pitfalls": [
            "只做任务列表，不定义阶段产出",
            "把日程填满却没有里程碑",
            "反复切换任务导致认知损耗",
            "卡住时继续机械堆时间",
        ],
        "example_prompts": [
            "请把我的任务整理成四周推进节奏。",
            "请判断我现在的瓶颈是结构、资料还是执行带宽。",
            "请帮我给本周定义一个最小可交付成果。",
        ],
        "corpus_buckets": [
            {"label": "阶段规划与节奏", "keywords": ["计划", "时间", "周历", "月历", "四周"]},
            {"label": "论文推进与里程碑", "keywords": ["推进", "一篇论文", "里程碑"]},
            {"label": "卡点与效率误区", "keywords": ["卡点", "低效", "假努力"]},
        ],
    },
    "methods": {
        "situations": [
            "不确定自己的问题更适合哪一类方法家族",
            "看了很多方法名，却不知道它们各自擅长回答什么",
            "想做方法比较，但总停留在工具名层面",
        ],
        "workflow_steps": [
            "先定义你要交付的是模式、关系、机制还是过程。",
            "再判断可用证据属于数值、文本、案例、实验还是混合形态。",
            "据此筛出 2 到 3 个候选方法家族，而不是从几十种方法里盲选。",
            "比较每种方法的前提、风险和证据要求。",
            "把最终方法写回设计对齐表，而不是独立看待。",
        ],
        "decision_rules": [
            "方法图谱用于路由，不用于代替设计思考。",
            "先定证据形态，再比较方法家族。",
            "如果你说不清方法家族的局限，通常也没真正选定它。",
        ],
        "deliverables": [
            "问题-方法矩阵",
            "证据-分析矩阵",
            "方法比较表",
            "方法风险清单",
        ],
        "pitfalls": [
            "把方法名当成答案",
            "只看自己熟悉的方法",
            "忽略方法的前提条件",
            "把方法图谱误当成具体软件教程",
        ],
        "example_prompts": [
            "请把我的研究问题路由到几个方法家族。",
            "请比较这两类方法对我的证据要求有什么差别。",
            "请帮我做一张问题-方法矩阵。",
        ],
        "corpus_buckets": [
            {"label": "常见方法图谱", "keywords": ["16种", "方法", "分析方法", "回归", "案例"]},
            {"label": "证据与数据形式", "keywords": ["数据类型", "样本", "文本", "问卷"]},
            {"label": "混合与多方法设计", "keywords": ["mixed methods", "混合", "多方法"]},
        ],
    },
    "tools": {
        "situations": [
            "工具很多，但不知道如何组合成稳定工作流",
            "手头有模板，却不知道什么时候该用、什么时候不该用",
            "希望使用 AI 提升效率，但担心边界模糊",
        ],
        "workflow_steps": [
            "先按任务链划分工具，而不是按软件品牌堆清单。",
            "为每一类任务指定一个默认模板或默认工具。",
            "把 AI 放在整理、改写、核对和清单辅助的位置，而不是让它代替判断。",
            "每次替换工具前，先评估切换成本和长期维护成本。",
            "定期清理无效工具，保持工作流稳定。",
        ],
        "decision_rules": [
            "工具应该减少摩擦，而不是制造切换负担。",
            "模板优先解决起步成本，不能代替研究判断。",
            "AI 更适合加速结构化工作，不适合替代学术责任。",
        ],
        "deliverables": [
            "工具链清单",
            "模板使用说明",
            "AI 边界清单",
            "工作流切换记录",
        ],
        "pitfalls": [
            "为了新工具频繁重构工作流",
            "把模板当成内容本身",
            "让 AI 越过本应由研究者承担的判断",
            "工具过多导致碎片化",
        ],
        "example_prompts": [
            "请按任务链给我设计一个最小科研工具流。",
            "请判断这个模板适合放在哪个阶段使用。",
            "请帮我给这项工作划出 AI 可以帮忙和不该帮忙的边界。",
        ],
        "corpus_buckets": [
            {"label": "科研工具与网站", "keywords": ["工具", "网站", "gpt", "ai"]},
            {"label": "模板与可编辑资产", "keywords": ["template", "模板", "slides", "cover letter"]},
            {"label": "工作流辅助", "keywords": ["清单", "表格", "整理"]},
        ],
    },
    "upgrade": {
        "situations": [
            "新增一批来源后，需要刷新 packs 和双宿主布局",
            "想知道哪些变化适合公开，哪些必须留在本地",
            "需要让维护流程可重复，而不是靠手工记忆",
        ],
        "workflow_steps": [
            "先跑本地提取和去重，不直接动公开层。",
            "基于提取结果刷新统计、pack 覆盖和状态页。",
            "只挑适合公开的结构化内容进入 repo。",
            "重新生成双宿主布局与 manifests。",
            "最后跑校验和相似度扫描，再 push。",
        ],
        "decision_rules": [
            "本地缓存先行，公开更新后行。",
            "能抽象成方法论再公开，不能直接公开原始材料。",
            "双宿主布局永远从真源生成，不手工改分发目录。",
        ],
        "deliverables": [
            "更新记录",
            "公开层 diff",
            "状态页刷新",
            "发布前校验结果",
        ],
        "pitfalls": [
            "把本地缓存误提交到 GitHub",
            "直接改分发目录导致双宿主失同步",
            "只更新 pack，不更新 manifests 和状态页",
            "没做校验就 push",
        ],
        "example_prompts": [
            "请基于最新提取结果刷新公开层状态页。",
            "请判断这次新增内容哪些适合公开更新。",
            "请重新生成双宿主技能并做发布前校验。",
        ],
        "corpus_buckets": [
            {"label": "本地提取刷新", "keywords": ["extract", "cache", "index"]},
            {"label": "公开层状态刷新", "keywords": ["collection status", "summary", "coverage"]},
        ],
    },
}

for item in SKILLS:
    details = PACK_DETAILS_BY_ID.get(item["pack_id"])
    if details:
        item.update(details)

PACKS_BY_ID = {item["pack_id"]: item for item in SKILLS}
SKILLS_BY_ID = {item["skill_id"]: item for item in SKILLS}
