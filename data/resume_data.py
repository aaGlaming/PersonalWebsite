# -*- coding: utf-8 -*-
"""简历结构化数据 —— 修改网站内容只需改这个文件"""

PROFILE = {
    "name": "陆杨磊",
    "gender": "男",
    "phone": "13056991779",
    "email": "3619413019@qq.com",
    "title": "数据分析 · 数据挖掘",
    "slogan": "把七百万行杂乱数据，变成一页看得懂的结论",
    "intro": (
        "重庆理工大学数据科学与大数据技术专业 2026 届本科生。"
        "从泰迪杯数据挖掘竞赛到广告投放数仓，多次担任项目负责人，"
        "能独立完成从数据清洗、特征工程、模型构建到可视化报表输出的全流程工作。"
    ),
    "highlights": [
        {
            "title": "数据技术扎实",
            "body": "掌握 Python、SQL，熟练运用 XGBoost、Prophet 完成分类建模与时序预测，独立完成海量数据清洗、特征工程与模型落地。",
        },
        {
            "title": "大数据与可视化",
            "body": "熟悉 Flume/Kafka/Hive/ClickHouse 数仓链路，会用 FineBI 搭建可下钻、多筛选的交互看板，具备前后端协同开发经验。",
        },
        {
            "title": "项目经验丰富",
            "body": "数据挖掘竞赛、AI 分析平台、广告数仓、电商系统多类实战项目，多次担任负责人，独立完成从数据处理到业务报表输出全流程。",
        },
        {
            "title": "综合素养良好",
            "body": "逻辑思维强，学习上手快，擅长跨团队协作，熟练使用 Office/WPS 撰写专业数据分析报告。",
        },
    ],
}

SKILLS = [
    {
        "category": "编程语言",
        "icon": "code",
        "items": [
            {"name": "Python", "level": 90, "desc": "pandas 清洗、特征工程、自动化脚本"},
            {"name": "SQL", "level": 85, "desc": "Hive SQL / ClickHouse / MySQL"},
            {"name": "Shell", "level": 70, "desc": "调度脚本、数据采集自动化"},
        ],
    },
    {
        "category": "机器学习",
        "icon": "brain",
        "items": [
            {"name": "XGBoost", "level": 85, "desc": "分类、预测模型全流程构建"},
            {"name": "Prophet", "level": 80, "desc": "业务流量时序预测"},
            {"name": "随机森林", "level": 85, "desc": "故障诊断、综合效果评估"},
        ],
    },
    {
        "category": "大数据与数仓",
        "icon": "database",
        "items": [
            {"name": "Hive 数仓建模", "level": 80, "desc": "ODS/DIM/DWD 分层、维度建模、UDF"},
            {"name": "Kafka / Flume", "level": 75, "desc": "实时日志采集链路搭建"},
            {"name": "ClickHouse", "level": 75, "desc": "低延迟分析引擎、Spark JDBC 入库"},
        ],
    },
    {
        "category": "可视化与工具",
        "icon": "chart",
        "items": [
            {"name": "FineBI", "level": 80, "desc": "可下钻、多筛选交互看板"},
            {"name": "Streamlit / Vue", "level": 70, "desc": "AI 应用与前端协同开发"},
            {"name": "Office / WPS", "level": 90, "desc": "数据报告、业务分析文档"},
        ],
    },
]

PROJECTS = [
    {
        "id": "teddy-cup",
        "name": "生产线故障自动识别与人员配置",
        "role": "负责人",
        "period": "2024.04 - 2024.05",
        "featured": True,
        "summary": "第十五届泰迪杯数据挖掘挑战赛项目，建模解决生产线故障自动识别与人员配置问题。",
        "points": [
            "使用 Python 对 700 万条以上数据进行清洗，并处理数据失衡",
            "根据工业流程分析数据特征，筛选关键维度，通过定义新标签构建新特征",
            "构建随机森林模型进行故障诊断，采用准确率、召回率、精确率和 F1 值综合评估识别效果",
        ],
        "tags": ["Python", "随机森林", "特征工程", "数据清洗"],
    },
    {
        "id": "ai-agent",
        "name": "数据分析智能体项目",
        "role": "负责人",
        "period": "2025.05 - 2025.06",
        "featured": True,
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
        "period": "2024.05 - 2024.06",
        "featured": False,
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
        "id": "e-commerce",
        "name": "基于 SpringBoot 的电商管理系统",
        "role": "负责人",
        "period": "2024.05 - 2024.06",
        "featured": False,
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
    "period": "2022 - 2026",
    "note": "系统学习数据挖掘、机器学习、大数据组件与统计分析课程体系。",
}

HONORS = [
    {"name": "第十五届全国大学生数学竞赛三等奖", "time": "2024"},
    {"name": "丙等综合奖学金", "time": "在校期间"},
]
