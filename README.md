# 个人网站 · 陆杨磊（Flask + Vue3 · Artistic）

基于简历的单页个人网站，后端 Flask 提供 REST API，前端 Vue3，
整体为当代艺术指导 / 编辑排版风格：象牙纸底、炭黑、朱红点缀，巨型标题与展览目录式作品档案。

线上版本部署在 **GitHub Pages**（纯静态模式，每次 push 自动部署）；本地开发使用 Flask，两者页面与数据完全一致。

**线上地址**：https://aaglaming.github.io/Personal_Website/

## 目录结构

```
Personal_Website/
├── app.py                  # Flask 入口：注册 API、托管 frontend/dist
├── routes.py               # /api 路由 + /data/*.json 兼容路由（Blueprint）
├── data/resume_data.py     # 简历数据（改网站内容只需改这里）
├── export_data.py          # 把简历数据导出为静态 JSON（部署静态托管用）
├── requirements.txt
└── frontend/               # Vue3 + Vite
    ├── public/data/        # 导出的静态 JSON（构建时随 dist 一起发布）
    ├── src/
    │   ├── api.js          # axios 封装（统一走 data/*.json 相对路径）
    │   ├── styles/artistic.css    # Artistic 设计系统 tokens
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

## 线上部署（GitHub Pages，免费）

- 工作流：`.github/workflows/deploy.yml`，push 到 main 自动构建部署
- 构建命令：`npm run build -- --base=/Personal_Website/`（GitHub Pages 子路径）
- 仓库 Settings → Pages → Source 需设为 **GitHub Actions**

> 备选：EdgeOne Pages（构建命令 `cd frontend && npm install && npm run build`，输出目录 `frontend/dist`），
> 但其免费默认域名目前有登录鉴权，仅预览可用，公开访问需绑定自定义域名。

## 修改内容

编辑 `data/resume_data.py` → 运行 `python export_data.py` → 提交推送后 EdgeOne 自动重新部署；
本地查看则重新 `npm run build`（或直接用 Flask 模式，无需构建）。
