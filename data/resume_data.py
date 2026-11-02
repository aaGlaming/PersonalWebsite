# -*- coding: utf-8 -*-
"""简历结构化数据 —— 修改网站内容只需改这个文件"""

PROFILE = {
    "name": "陆杨磊",
    "gender": "男",
    "phone": "13056991779",
    "email": "a3619413019@gmail.com",
    "title": "AI 应用开发工程师",
    "slogan": "把大模型接到可演示、可评测、可交付的产品里",
    "studio": "ATELIER L.Y.L.",
    "location": "Chongqing, CN",
    "intro": (
        "重庆理工大学数据科学与大数据技术专业 2026 届本科生，求职 AI 应用开发。"
        "能独立完成 RAG / Agent 管线、前后端联调与流式交互，"
        "并从数据清洗、特征工程做到检索评测与桌面/Web 交付。"
    ),
    "highlights": [
        {
            "title": "RAG 与检索工程",
            "body": "手写切分、向量 + BM25 混合检索、Query Rewrite、阈值拒答；评测与线上共用 retrieve()，用 Hit@K / MRR 对比策略。",
        },
        {
            "title": "LLM 应用落地",
            "body": "接入 OpenAI 兼容接口，SSE 流式生成，回答带来源；做过多轮对话、工具化问答与 LangChain 智能体。",
        },
        {
            "title": "全栈交付",
            "body": "Vue 3 + FastAPI 独立完成前后端；知识库可打包 Windows 桌面应用，互动站点支持 PWA 与静态部署。",
        },
        {
            "title": "数据与建模底子",
            "body": "Python / SQL 扎实，有海量清洗、特征工程、随机森林与 XGBoost 落地经验，能把业务数据接到模型与产品。",
        },
    ],
}

SKILLS = [
    {
        "category": "Python 后端与数据",
        "icon": "code",
        "items": [
            {"name": "Python / FastAPI", "level": 95, "desc": "RAG 服务、Agent API、SSE 流式问答与后台任务"},
            {"name": "SQL / 数据建模", "level": 85, "desc": "SQLite、MySQL、SQLAlchemy 与评审/工单业务数据"},
            {"name": "数据处理与评测", "level": 85, "desc": "文档解析、数据清洗、检索指标与端到端验收"},
        ],
    },
    {
        "category": "RAG 与检索工程",
        "icon": "brain",
        "items": [
            {"name": "Hybrid Retrieval", "level": 95, "desc": "向量 + BM25、RRF、父子块、过滤与可选重排"},
            {"name": "RAG 评测与证据", "level": 90, "desc": "Hit@K、MRR、引用连续性、Faithfulness 与 Relevancy"},
            {"name": "多模态 / 图谱增强", "level": 80, "desc": "Neo4j、Chinese-CLIP、VLM、Self-RAG 与 CRAG"},
        ],
    },
    {
        "category": "Agent 与工作流",
        "icon": "database",
        "items": [
            {"name": "LangGraph / LangChain", "level": 90, "desc": "Supervisor、专项 Agent、状态图与可恢复流程"},
            {"name": "工具调用与结构化输出", "level": 90, "desc": "Pydantic schema、工具白名单、预算与确定性校验"},
            {"name": "人工确认与审计", "level": 85, "desc": "高风险确认、轨迹记录、来源引用与结果回溯"},
        ],
    },
    {
        "category": "前端与工程交付",
        "icon": "chart",
        "items": [
            {"name": "Vue 3 / TypeScript", "level": 90, "desc": "知识库、评审、设施运维与互动站点单页应用"},
            {"name": "Vite / Element Plus / ECharts", "level": 85, "desc": "管理后台、可视化大屏、流式对话与交互组件"},
            {"name": "Docker / Nginx / PWA", "level": 80, "desc": "Compose 部署、GitHub Pages、静态托管与离线访问"},
        ],
    },
]

PROJECTS = [
    {
        "id": "my-rag",
        "name": "My RAG · 个人知识库问答与评测平台",
        "role": "负责人",
        "period": "2026.09",
        "featured": True,
        "medium": "FastAPI / Vue 3 / Chroma / LlamaIndex",
        "url": "https://github.com/aaGlaming/SelfRAG",
        "summary": "面向个人资料管理的本地 RAG 应用：支持多格式文档与图片入库、混合检索、引用式问答，以及可切换的 Self-RAG、CRAG 和模块化检索流程。",
        "points": [
            "支持 PDF、DOCX、Markdown、TXT 与常见图片的解析、索引、管理和来源回溯",
            "向量检索与 BM25 通过带权 RRF 融合，结合阈值过滤；无有效命中时直接拒答并跳过 LLM 调用",
            "统一 retrieve_multi() 服务线上问答、离线评测、Self-RAG、CRAG 和模块化模式，支持 Query Rewrite、HyDE、Step-Back 与多查询扩展",
            "可选接入 Neo4j 知识图谱、Chinese-CLIP 多模态检索、重排和联网兜底，并持久化检索日志与自动评估结果",
        ],
        "tags": ["RAG", "FastAPI", "Chroma", "Self-RAG", "Multimodal"],
    },
    {
        "id": "naiwa",
        "name": "NAIWADIY · 奶蛙世界",
        "role": "负责人",
        "period": "2026",
        "featured": True,
        "medium": "Vue 3 / FastAPI / PWA",
        "url": "https://aaglaming.github.io/NaiWa-Web/",
        "summary": "以独立视觉系统呈现的奶蛙主题站点：448+ 表情图库，抽卡、塔罗、梗图、心情测试、成就与桌宠，支持 PWA 离线访问。",
        "points": [
            "Vue 3 + Vite + Pinia + Vue Router，13 条懒加载路由；FastAPI 提供图库与联系接口，静态模式回退 images.json",
            "抽卡含四档稀有度、保底与十连；图鉴 / 收藏 / 成就经 localStorage 持久化",
            "Canvas 壁纸与梗图生成、塔罗牌阵、心情测试与可拖拽桌宠，组成完整互动档案",
            "Manifest + Service Worker 缓存，GitHub Pages 自动部署",
        ],
        "tags": ["Vue", "PWA", "Pinia", "Canvas", "FastAPI"],
    },
    {
        "id": "municipal-facility-ops",
        "name": "市政设施巡检与维修平台",
        "role": "负责人",
        "period": "2026.10",
        "featured": True,
        "medium": "FastAPI / Vue 3 / MySQL / LangGraph",
        "url": "https://github.com/aaGlaming/municipal-facility-ops",
        "summary": "面向道路、路灯、交通信号和公共设施的城市运行工作台，串联问题上报、设施识别、巡检、SLA 判断、工单调度、维修验收与知识问答。",
        "points": [
            "用 LangGraph 编排 Supervisor、分诊、设施识别、SLA、巡检、调度、安全和验收 Agent，形成可追踪的业务闭环",
            "实现设施台账、问题上报、巡检任务、工单状态机、逾期升级、维修证据和验收记录",
            "接入 Chroma 文档库、解析切分、Embedding、关键词检索、Rerank 和证据回溯，Agent 建议带来源",
            "Vue 3 + TypeScript 管理端覆盖值守总览、城市运行大屏、设施地图、工单中心、Agent 工作台和 RAG 工作台",
        ],
        "tags": ["LangGraph", "FastAPI", "Vue", "MySQL", "RAG"],
    },
    {
        "id": "paper-review",
        "name": "竞赛论文预审工作台",
        "role": "负责人",
        "period": "2026.10",
        "featured": True,
        "medium": "FastAPI / LangGraph / MySQL / Chroma",
        "url": "https://github.com/aaGlaming/paper-review",
        "summary": "面向竞赛论文预审的可恢复评审工作台，将论文解析、章节确认、按量规评分、一致性审查、修改建议和 AI 问询串成带证据的评审流程。",
        "points": [
            "用 LangGraph 编排 parse → confirm → retrieve → score 状态图，评分前通过 interrupt() 等待人工确认章节树",
            "设计 evidence、topic fit、coherence、review、verifier 五类 Agent，配合 16 个结构化工具契约和调用预算",
            "采用 Chroma child + MySQL parent 父子块、三路召回和连续原句校验，证据不足时不参与评分",
            "持久化评审结果、引用证据、Agent 轨迹和修改清单，支持权限控制、记录回溯、AI 问询与 Docker Compose 部署",
        ],
        "tags": ["LangGraph", "Agent", "Evidence RAG", "MySQL", "Vue"],
    },
]

EDUCATION = {
    "school": "重庆理工大学",
    "degree": "本科 · 数据科学与大数据技术",
    "period": "2022 — 2026",
    "note": "系统学习数据挖掘、机器学习、大数据组件与统计分析课程体系。",
}

HONORS = [
    {"name": "第十五届全国大学生数学竞赛三等奖", "time": "2024"},
    {"name": "丙等综合奖学金", "time": "在校期间"},
]
