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
