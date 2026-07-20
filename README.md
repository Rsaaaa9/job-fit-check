# 🎯 Pleadly — 聪明地求职 / Plead Smart

> AI招聘经理视角的全流程求职助手 — 从JD投递到入职，每一步都有你。
> AI-powered full-cycle career assistant — from job matching to day-1 survival guide.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging_Face_Spaces-orange.svg)](https://huggingface.co/spaces)
[![GitHub Stars](https://img.shields.io/github/stars/Rsaaaa9/Pleadly?style=social)](https://github.com/Rsaaaa9/Pleadly)

---

## 这是什么？

Pleadly = **Plead(求职) + ly(智能地)** —— "聪明地求职"。

面向应届生的**全流程 AI 求职助手**。输入你的简历和岗位JD，AI招聘经理帮你跑完十步完整分析——从ATS关键词检测到入职生存指南。

## 十步工作流

| Step | 模块 | 说明 |
|:---:|------|------|
| 1 | ATS关键词检测 | 提取JD关键词→检查简历命中率→避免机器筛选翻车 |
| 2 | 岗位匹配度评分 | 6维度百分制评分→🟢匹配/🟡冲击/🔴放弃 |
| 3 | JD全维度拆解 | 公司背景+岗位业务+硬性要求+隐形需求+面试追问预测 |
| 4 | 简历逐行诊断 | 匹配点+冗余点+缺失点+风险点(含修复方案) |
| 5 | 多JD优先级排序 | 6维度加权→精力分配策略 |
| 6 | 差距学习计划 | 按严重度+紧急度+周期排序→学什么、多久、产出什么 |
| 7 | 全流程面试准备 | HR初筛→笔试→技术面→行为面→终面→情景模拟 6阶段逐题话术 |
| 8 | Mock面试官模式 | 切换面试官角色→随机出题→追问→即时反馈 |
| 9 | Offer薪资谈判 | 市场对标+7维度谈判点+逐字话术脚本 |
| 10 | 公司文化入职指南 | 文化速写+第一周Checklist+首月关键动作+退出信号 |

---

## 快速开始

### 方式一: 浏览器直接使用(推荐)

访问 Hugging Face Spaces 部署地址(即将上线):
```
https://huggingface.co/spaces/Rsaaaa9/Pleadly
```

无需安装，打开即用。

### 方式二: 本地运行

```bash
# 1. Clone
git clone https://github.com/Rsaaaa9/Pleadly.git
cd Pleadly

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置 API Key
cp .env.example .env
# 编辑 .env，填入你的 DEEPSEEK_API_KEY

# 4. (可选) 初始化知识库
python rag/data/seed_data.py

# 5. 启动
python app/main.py

# 6. 打开浏览器
# http://localhost:7860
```

### 方式三: Claude Code 终端使用

```bash
git clone https://github.com/Rsaaaa9/Pleadly.git
cd Pleadly
claude  # CLAUDE.md 自动加载，直接对话
```

然后说: "这是我的简历[粘贴]，岗位JD[粘贴]，帮我分析。"

---

## 从零部署上线教程

### 方案A: Hugging Face Spaces (免费，推荐)

1. **注册 Hugging Face**
   - 打开 [huggingface.co](https://huggingface.co)
   - 点击右上角 Sign Up
   - 用邮箱或 GitHub 账号注册

2. **创建 Space**
   - 登录后点击右上角头像 → New Space
   - 填写:
     - Space Name: `Pleadly` (或你喜欢的名字)
     - License: `mit`
     - SDK: `Docker`
     - Docker template: `Blank`
     - Space hardware: `CPU basic` (免费)
   - 点击 Create Space

3. **上传代码**
   ```bash
   # 克隆你的 Space
   git clone https://huggingface.co/spaces/YOUR_USERNAME/Pleadly
   cd Pleadly

   # 复制 Pleadly 所有文件到这个目录
   cp -r /path/to/Pleadly/* .

   # 设置 API Key Secret
   # 在 Hugging Face Space 网页 → Settings → Secrets
   # Name: DEEPSEEK_API_KEY
   # Value: sk-xxxxxxxxx

   # 提交并推送
   git add -A
   git commit -m "Deploy Pleadly"
   git push
   ```

4. **等待构建完成**
   - Hugging Face 会自动构建 Docker 镜像
   - 约 3-5 分钟后，Space 状态变为 "Running"
   - 点击 "Open Space" 即可使用

### 方案B: 本地开发后用 Vercel(未来 React 版)

当项目迁移到 React/Next.js 后，前端部署到 Vercel(免费)，后端部署到 Railway(免费起步)。

---

## 项目架构

```
pleadly/
├── README.md              # 项目文档
├── requirements.txt       # Python依赖
├── .env.example          # 环境变量模板
│
├── app/                  # Gradio 前端
│   ├── main.py           # 应用入口(十步UI+事件绑定)
│   └── components/       # 可复用UI组件
│
├── core/                 # 核心业务逻辑
│   ├── engine.py         # Prompt Engine(十步工作流调度)
│   ├── agent.py          # Agent工具调用(WebSearch/文档解析)
│   └── prompts/          # Prompt模板文件(十步各有一个)
│
├── rag/                  # RAG知识库
│   ├── vector_store.py   # ChromaDB管理+检索管道
│   ├── data/
│   │   ├── seed_data.py  # 种子数据导入脚本
│   │   ├── interviews/   # 面试题库
│   │   ├── companies/    # 公司信息
│   │   ├── salaries/     # 薪资数据
│   │   └── templates/    # 简历模板
│
├── deploy/               # 部署配置
│   ├── Dockerfile        # Hugging Face Spaces Docker
│   └── README_HF.md     # HF Space 配置
│
└── tests/                # 测试
    └── test_engine.py
```

## 技术栈

| 层 | 技术 | 说明 |
|------|------|------|
| 前端 | Gradio 5.0 | Python Web UI，支持文件上传、Tab切换 |
| 后端 | FastAPI + Uvicorn | 异步API服务 |
| LLM | DeepSeek API | 中文能力强，成本低 |
| RAG | ChromaDB + text2vec-base-chinese | 本地向量数据库，免费中文Embedding |
| Agent Tools | DuckDuckGo Search + BeautifulSoup | 免费联网检索 |
| 部署 | Hugging Face Spaces + Docker | 免费CPU实例 |

---

## License

MIT — 自由使用、修改、分发。保留署名。

---

<p align="center">
  <sub>Built with ❤️ for job seekers everywhere. | 为每一个求职者而建。</sub>
</p>
