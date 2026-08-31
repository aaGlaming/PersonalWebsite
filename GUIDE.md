# 个人网站操作指南

> 线上地址：**https://aaglaming.github.io/Personal_Website/**
> 代码仓库：**https://github.com/aaGlaming/Personal_Website**

---

## 一、项目架构速览

```
访问者 ──► GitHub Pages（线上，纯静态）
              ▲
              │ git push 后 GitHub Actions 自动构建部署
本机 ──► Flask (localhost:5000)  ← 本地开发/预览用，功能与线上一致
```

网站采用**双模式**设计，页面完全相同，只是数据来源不同：

| 模式 | 数据来源 | 用途 |
|------|----------|------|
| 线上 | `frontend/public/data/*.json` 静态文件 | GitHub Pages 托管 |
| 本地 | Flask 动态接口 `data/*.json`（与静态路径一致） | 本地开发预览 |

### 目录结构与职责

```
Personal_Website/
├── data/resume_data.py        ★ 简历数据（改内容只动这里）
├── export_data.py             ★ 把简历数据导出为静态 JSON
├── app.py                     Flask 入口（API + 托管前端产物）
├── routes.py                  API 路由
├── requirements.txt           Python 依赖（只有 Flask）
├── .github/workflows/deploy.yml   线上自动部署工作流
├── edgeone.json               EdgeOne 备选部署配置
└── frontend/
    ├── public/data/           导出的 JSON（自动生成，勿手改）
    ├── src/components/        8 个页面板块组件（Vue）
    ├── src/styles/handdrawn.css   手绘风格设计系统
    ├── src/api.js             数据请求封装
    └── dist/                  构建产物（自动生成，勿手改）
```

---

## 二、日常修改：更新简历内容（最常用）

**场景**：改名字、电话、项目描述、新增项目、修改技能等。

```bash
# 第 1 步：编辑数据文件（用 PyCharm/VSCode 打开编辑）
data/resume_data.py

# 第 2 步：导出静态 JSON（在项目根目录执行）
.venv/Scripts/python.exe export_data.py

# 第 3 步：本地检查效果（可选）
.venv/Scripts/python.exe app.py
# 浏览器打开 http://127.0.0.1:5000 确认无误后 Ctrl+C 关闭

# 第 4 步：提交推送，线上约 1-2 分钟后自动更新
git add -A
git commit -m "更新简历内容"
git push
```

### 各数据字段位置对照

| 想改什么 | 改 `data/resume_data.py` 里的 |
|----------|------------------------------|
| 姓名/电话/邮箱/一句话介绍 | `PROFILE` |
| 「关于我」4 张便签 | `PROFILE["highlights"]` |
| 技能分类与熟练度 | `SKILLS` |
| 项目经历（增删项目/要点/标签） | `PROJECTS` |
| 学校专业 | `EDUCATION` |
| 荣誉奖项 | `HONORS` |

---

## 三、日常修改：调整页面样式/布局

**场景**：改颜色、字体、间距、板块结构等前端代码。

```bash
# 终端 1：启动 Flask
.venv/Scripts/python.exe app.py

# 终端 2：启动前端热更新开发服务器
cd frontend
npm run dev
```

浏览器打开 **http://localhost:5173**（改代码实时生效），改完满意后：

```bash
git add -A
git commit -m "调整 XX 样式"
git push        # 推送后线上自动重新构建
```

### 常改的文件

| 想改什么 | 文件 |
|----------|------|
| 颜色/阴影/圆角等设计变量 | `frontend/src/styles/handdrawn.css`（顶部 `:root`） |
| 某个板块的内容布局 | `frontend/src/components/` 对应组件 |
| 网站标题/SEO 描述/字体 | `frontend/index.html` |

---

## 四、线上部署体系说明

### 工作原理

推送代码到 `main` 分支后，GitHub Actions（`.github/workflows/deploy.yml`）自动执行：

1. 安装 frontend 依赖
2. 执行 `npm run build -- --base=/Personal_Website/`（子路径前缀是 GitHub Pages 必需的）
3. 把 `frontend/dist` 发布到 GitHub Pages

### 查看部署状态

打开 https://github.com/aaGlaming/Personal_Website/actions ，每次 push 都有一条记录：
- ✅ 绿色勾 = 部署成功
- ❌ 红色叉 = 失败，点进去看报错；修复后 push 会自动重试，或点「Re-run jobs」

### 手动触发部署（不改代码时）

仓库页面 → **Actions** → 选 "Deploy to GitHub Pages" → **Run workflow**

### 首次部署配置回顾（已配置好，仅备查）

仓库 **Settings → Pages → Source = GitHub Actions**。

### 备选方案：EdgeOne Pages（当前未启用）

EdgeOne 项目仍存在于腾讯云（Makers），但其**免费默认域名有登录鉴权，外人无法访问**。
若日后要启用：需要一个域名（海外节点免备案）绑定到 EdgeOne 项目，
配置已在仓库 `edgeone.json` 中写好（构建命令 `cd frontend && npm install && npm run build`，输出目录 `frontend/dist`）。

---

## 五、常见问题

**Q1：改了数据但线上没变化？**
按顺序检查：① 是否运行了 `export_data.py`；② `frontend/public/data/*.json` 是否已更新并随 push 提交；③ Actions 是否跑完（绿色勾）；④ 浏览器 Ctrl+F5 强制刷新。

**Q2：国内访问慢/偶尔打不开？**
GitHub Pages 服务器在境外，属正常现象。想要更快：买一个域名（约 ¥10/年）绑定 Cloudflare 或 EdgeOne（海外节点免备案），前端代码零改动。

**Q3：本地 `python app.py` 报 ModuleNotFoundError？**
确认用的是项目虚拟环境：`.venv/Scripts/python.exe app.py`，且 `requirements.txt` 已安装（`.venv/Scripts/pip install -r requirements.txt`）。

**Q4：npm 相关命令报权限错误？**
用完整路径或先确认 npm 可用（`node --version`）。本机 npm 位于 `D:\Configuration\learning_APPs\NodeOld\nodejs`。

**Q5：git push 提示 403 权限拒绝？**
本机存有多个 GitHub 账号凭证。本项目远程地址已锁定为 aaGlaming 账号（`git remote -v` 可查看）。若再遇 403：Windows「凭据管理器」删除 github.com 相关凭证后重新推送，按提示登录 aaGlaming。

**Q6：想换一张头像/照片？**
编辑 `frontend/src/components/HeroSection.vue` 中 `.avatar` 区块，把便签占位换成 `<img>` 标签即可。

---

## 六、速查命令卡片

```bash
# ── 更新内容（最常用三连）──────────────
.venv/Scripts/python.exe export_data.py
git add -A && git commit -m "更新内容" && git push

# ── 本地预览 ────────────────────────────
.venv/Scripts/python.exe app.py            # http://127.0.0.1:5000
cd frontend && npm run dev                 # http://localhost:5173（热更新）

# ── 重新构建前端（改了前端代码后本地验证）──
cd frontend && npm run build && cd ..
```
