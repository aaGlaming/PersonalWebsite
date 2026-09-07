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
        "category": "语言与工程",
        "icon": "code",
        "items": [
            {"name": "Python", "level": 90, "desc": "FastAPI、RAG 管线、评测脚本、数据处理"},
            {"name": "JavaScript / Vue 3", "level": 80, "desc": "单页应用、状态管理、SSE 流式界面"},
            {"name": "SQL", "level": 80, "desc": "SQLite / MySQL 业务数据与日志查询"},
        ],
    },
    {
        "category": "LLM 应用",
        "icon": "brain",
        "items": [
            {"name": "RAG", "level": 90, "desc": "切分、Embedding、混合检索、来源引用、拒答"},
            {"name": "Prompt / Agent", "level": 85, "desc": "系统提示、多轮改写、LangChain 工具调用"},
            {"name": "OpenAI 兼容 API", "level": 85, "desc": "DeepSeek / 千问等，流式 Chat Completions"},
        ],
    },
    {
        "category": "检索与后端",
        "icon": "database",
        "items": [
            {"name": "FastAPI", "level": 85, "desc": "REST、SSE、后台任务、配置与鉴权脱敏"},
            {"name": "向量库 / Embedding", "level": 80, "desc": "Chroma、BGE，知识库隔离与入库流水线"},
            {"name": "Hybrid Search", "level": 80, "desc": "BM25 + 向量 RRF 融合，阈值过滤与评测"},
        ],
    },
    {
        "category": "前端与交付",
        "icon": "chart",
        "items": [
            {"name": "Vue 3 / TypeScript", "level": 80, "desc": "对话、知识库、设置页与路由拆分"},
            {"name": "流式交互 / PWA", "level": 75, "desc": "SSE 逐字输出、Service Worker、静态托管"},
            {"name": "Git / 桌面包", "level": 75, "desc": "版本协作；Tauri + PyInstaller 本地交付"},
        ],
    },
]

PROJECTS = [
    {
        "id": "my-rag",
        "name": "个人知识库 RAG",
        "role": "负责人",
        "period": "2026.06 — 2026.09",
        "featured": True,
        "medium": "Vue 3 / FastAPI / Chroma",
        "url": "https://github.com/aaGlaming/My-Owned-RAG",
        "summary": "手写 RAG 管线的个人知识库：上传文档 → 解析切分 → 本地 BGE 向量化 → 混合检索 → OpenAI 兼容 LLM 流式生成，回答带来源。",
        "points": [
            "独立实现 Loader / Splitter / Embedding / Store / Fusion / Retrieve / Prompt / Generate，不套 LangChain",
            "默认向量 + BM25 经 RRF 融合；多轮追问先 Query Rewrite；低于阈值则拒答且不调用 LLM",
            "SSE 流式输出，来源含文件名、页码与片段；评测脚本与线上共用 retrieve()，对比 Hit@K / MRR",
            "小样本评测（2026-09-07，20 问）：hybrid Hit@3 85%、MRR 0.7625，优于纯向量；可打包为 Windows 桌面应用",
        ],
        "tags": ["RAG", "FastAPI", "Chroma", "BGE", "Hybrid Search"],
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
        "id": "ai-agent",
        "name": "数据分析智能体项目",
        "role": "负责人",
        "period": "2025.05 — 2025.06",
        "featured": False,
        "medium": "Python / Streamlit / LangChain",
        "url": "",
        "summary": "基于 Python、Streamlit、LangChain 开发集成多种 AI 能力的智能处理平台，涵盖文本分析与数据分析两大核心模块。",
        "points": [
            "文本分析模块支持摘要、翻译、情感分析、文本生成及基于文档/网页的智能问答",
            "数据分析模块实现数据上传、清洗、统计与多类型可视化",
            "集成 OpenAI 等大模型 API，实现多轮对话记忆、RAG 智能问答",
            "支持 CSV/Excel 上传，生成柱状图、热力图等图表，支持自然语言绘图",
        ],
        "tags": ["LangChain", "RAG", "Streamlit", "OpenAI API"],
    },
    {
        "id": "ad-warehouse",
        "name": "广告投放数仓与流量分析可视化平台",
        "role": "组员",
        "period": "2024.05 — 2024.06",
        "featured": False,
        "medium": "Hive / Kafka / ClickHouse",
        "url": "",
        "summary": "搭建广告投放全链路数仓，从日志采集到可视化看板，识别异常流量并支撑投放运营实时监控。",
        "points": [
            "搭建 Flume+Kafka 实时日志采集链路，DataX 全量同步 MySQL 业务库至 HDFS，Shell 调度自动化采集入 ODS 层",
            "基于 Hive 构建 ODS/DIM/DWD 三层广告数仓，自定义 UDF 解析 IP 归属地与 UserAgent，识别 GIVT/SIVT 异常流量",
            "基于 XGBoost 构建异常流量分类模型，Prophet 实现流量时序预测，独立完成模型构建、特征工程与落地入库",
            "Spark JDBC 将 Hive 明细写入 ClickHouse，FineBI 对接数据源制作交互图表与多维筛选仪表板",
            "实现省份下钻城市、多维统计曝光/点击/异常流量指标，支撑业务自助分析报表",
        ],
        "tags": ["Hive", "Kafka", "ClickHouse", "XGBoost", "FineBI"],
    },
    {
        "id": "teddy-cup",
        "name": "生产线故障自动识别与人员配置",
        "role": "负责人",
        "period": "2024.04 — 2024.05",
        "featured": False,
        "medium": "Python / Random Forest",
        "url": "",
        "summary": "第十五届泰迪杯数据挖掘挑战赛项目，建模解决生产线故障自动识别与人员配置问题。",
        "points": [
            "使用 Python 对 700 万条以上数据进行清洗，并处理数据失衡",
            "根据工业流程分析数据特征，筛选关键维度，通过定义新标签构建新特征",
            "构建随机森林模型进行故障诊断，采用准确率、召回率、精确率和 F1 值综合评估识别效果",
        ],
        "tags": ["Python", "随机森林", "特征工程", "数据清洗"],
    },
    {
        "id": "e-commerce",
        "name": "基于 SpringBoot 的电商管理系统",
        "role": "负责人",
        "period": "2024.05 — 2024.06",
        "featured": False,
        "medium": "SpringBoot / Vue / MySQL",
        "url": "",
        "summary": "SpringBoot + Vue 技术栈，构建涵盖商品、用户、订单、数据分析核心模块的电商管理平台。",
        "points": [
            "满足客户购物（浏览、下单支付、订单查询）与商户管理（上下架、库存监控、数据统计）需求",
            "划分超级管理员、商品管理员等不同权限角色，实现完整交易流程",
            "完成前端页面设计与后端功能开发，实现前后端高效交互",
            "实现商品多级分类、库存预警、订单状态追踪、销售数据分析等核心功能",
        ],
        "tags": ["SpringBoot", "Vue", "MySQL", "RBAC"],
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
