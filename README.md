# 我求你了 / Pleadly

> AI招聘经理视角的全流程求职助手 — 从JD投递到入职，每一步都有你。
> AI-powered full-cycle career assistant — from job matching to day-1 survival guide.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)

---

## 这是什么

**我求你了**（英文名 **Pleadly** = Plead + ly，"聪明地求职"）是一套面向应届生的全流程 AI 求职系统。输入你的简历和岗位 JD，AI 招聘经理帮你跑完从投递到入职的完整分析。

## 十步工作流

| Step | 模块 | 说明 |
|:---:|------|------|
| 1 | ATS 关键词检测 | 提取 JD 关键词 → 检查简历命中率 → 避免机器筛选翻车 |
| 2 | 岗位匹配度评分 | 6 维度百分制加权评分 → 🟢匹配 / 🟡冲击 / 🔴放弃 |
| 3 | JD 全维度拆解 | 公司背景 + 岗位业务 + 硬性要求 + 隐形需求 + 面试追问预测 |
| 4 | 简历逐行诊断 | 匹配点 + 冗余点 + 缺失点 + 风险点（均含修复方案） |
| 5 | 多 JD 优先级排序 | 6 维度加权排序 → 精力分配策略 |
| 6 | 差距学习计划 | 按严重度 + 紧急度 + 学习周期综合排序 |
| 7 | 全流程面试准备 | HR 初筛 → 笔试 → 技术面 → 行为面 → 终面 → 情景模拟，6 阶段逐题话术 |
| 8 | Mock 面试官模式 | 切换面试官角色 → 随机出题 → 追问 → 即时反馈 |
| 9 | Offer 薪资谈判 | 市场薪资对标 + 7 维度谈判点拆解 + 逐字话术脚本 |
| 10 | 公司文化入职指南 | 文化速写 + 第一周 Checklist + 首月关键动作 + 退出信号识别 |

---

## 设计原则

- **所有分析基于真实数据**：公司信息、行业薪资、面试题库来自联网检索和持续积累，不做编造
- **AI 辅助但不替代判断**：每一步都有明确的人机边界——AI 提供推荐和分析，最终决策责任属于用户
- **开箱即用的 Prompt 体系**：每个模块既是可运行的代码，也是可复制粘贴到任何 AI 工具中的独立 Prompt
- **RAG 知识库持续积累**：面试题库、公司信息、简历模板、薪资数据通过向量数据库统一管理

---

## 项目结构

```
pleadly/
├── app/                  # 应用前端
│   ├── main.py           # 入口 + UI + 事件绑定
│   └── components/       # 可复用组件
├── core/                 # 核心引擎
│   ├── engine.py         # Prompt Engine（十步工作流调度）
│   ├── agent.py          # Agent 工具调用（WebSearch / 文档解析）
│   └── prompts/          # 各步骤 Prompt 模板
├── rag/                  # RAG 知识库
│   ├── vector_store.py   # ChromaDB 管理 + 检索管道
│   └── data/             # 种子数据（面试题 / 公司信息 / 薪资 / 模板）
├── deploy/               # 部署配置
├── tests/                # 测试
├── CLAUDE.md             # Claude Code 终端入口（进入目录自动加载）
└── README.md
```

---

## 技术栈

| 层 | 技术 |
|------|------|
| 前端 | Gradio 5.0 |
| 后端 | FastAPI + Uvicorn |
| LLM | DeepSeek API |
| RAG | ChromaDB + text2vec-base-chinese |
| Agent Tools | WebSearch + 文档解析 + 薪资检索 |

---

## License

MIT — 自由使用、修改、分发。保留署名。
