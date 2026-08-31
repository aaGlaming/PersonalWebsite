# 个人网站 · 陆杨磊（Flask + Vue3 手绘风格）

基于简历的单页个人网站，后端 Flask 提供 REST API，前端 Vue3 + Element Plus，
整体为 Hand-Drawn（手绘/涂鸦）设计风格：歪斜边框、硬偏移阴影、便签贴纸、纸张纹理。

线上版本部署在腾讯 EdgeOne Pages（纯静态模式）；本地开发使用 Flask，两者页面与数据完全一致。

## 目录结构

```
Personal_Website/
├── app.py                  # Flask 入口：注册 API、托管 frontend/dist
├── routes.py               # /api 路由 + /data/*.json 兼容路由（Blueprint）
├── data/resume_data.py     # 简历数据（改网站内容只需改这里）
├── export_data.py          # 把简历数据导出为静态 JSON（部署静态托管用）
├── requirements.txt
└── frontend/               # Vue3 + Vite + Element Plus
    ├── public/data/        # 导出的静态 JSON（构建时随 dist 一起发布）
    ├── src/
    │   ├── api.js          # axios 封装（统一走 data/*.json 相对路径）
    │   ├── styles/handdrawn.css   # 手绘设计系统 tokens
    │   └── components/     # 导航/Hero/关于/技能/项目/教育/联系/Footer
    └── dist/               # 构建产物（Flask 托管 / 静态托管均用这份）
```

## 数据接口（两种模式路径一致）

| 路径 | 说明 |
|------|------|
| `data/profile.json`    | 姓名、联系方式、个人优势 |
| `data/skills.json`     | 分类技能与熟练度 |
| `data/projects.json`   | 项目经历 |
| `data/education.json`  | 教育经历 + 荣誉奖项 |

本地 Flask 同时保留 `/api/profile` 等原 REST 接口。

## 本地启动

### 生产模式（推荐，构建后只需 Flask）

```bash
# 1. 修改内容后：导出静态数据并构建前端
.venv/Scripts/python.exe export_data.py
cd frontend && npm install && npm run build && cd ..

# 2. 启动
.venv/Scripts/python.exe app.py
```

访问 http://127.0.0.1:5000

### 开发模式（前端热更新）

```bash
# 终端 1：Flask
.venv/Scripts/python.exe app.py

# 终端 2：Vite dev server（/api 自动代理到 5000）
cd frontend && npm run dev
```

访问 http://localhost:5173

## 线上部署（腾讯 EdgeOne Pages，免费）

1. 推送本仓库到 GitHub
2. 打开 [EdgeOne Pages 控制台](https://console.cloud.tencent.com/edgeone/pages)，用 GitHub 账号登录并授权
3. 「创建项目」→ 选择 GitHub 导入 → 选中本仓库
4. 构建配置填写：
   - 构建命令：`cd frontend && npm install && npm run build`
   - 输出目录：`frontend/dist`
5. 部署完成后获得 `xxx.edgeone.app` 免费域名（国内可访问、不休眠）

## 修改内容

编辑 `data/resume_data.py` → 运行 `python export_data.py` → 提交推送后 EdgeOne 自动重新部署；
本地查看则重新 `npm run build`（或直接用 Flask 模式，无需构建）。
