# Pleadly — 聪明地求职 / Plead Smart

> AI招聘经理视角的全流程求职助手——从JD投递到入职，每一步都有你。
> AI-powered full-cycle career assistant — from job matching to day-1 survival guide.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Workflow: 10 Steps](https://img.shields.io/badge/Workflow-10_Steps-purple.svg)](#)
[![Lang: ZH+EN](https://img.shields.io/badge/Lang-ZH%20%7C%20EN-orange.svg)](#)

---

## What is this?

A **full-cycle job application system** covering every stage of the job hunt — from initial JD matching to salary negotiation and onboarding. Born from real interviews with semiconductor, pharma, logistics, and AI SaaS companies in 2026.

一套**全流程求职系统**，覆盖找工作全链路。历经RISC-V芯片、医药集团、跨境物流、AI SaaS 等行业的真实面试实战迭代。

---

## Quick Start

### Easiest: Claude Code (1 command)

```bash
git clone https://github.com/Rsaaaa9/Pleadly.git
cd Pleadly
claude  # CLAUDE.md auto-loads the full 10-step workflow
```

Then say: "这是我的简历[粘贴]，这是岗位JD[粘贴]，帮我分析。"

### Copy-paste (any AI tool)

Open [`prompts/`](prompts/), copy any prompt, paste into ChatGPT / Claude / Kimi / DeepSeek.

### Slash command (for Claude Code users)

Copy `job-fit-check-agent.md` to `~/.claude/agents/pleadly.md`, then type `/pleadly`.

---

## The 10-Step Workflow

| Step | Module | Description |
|:---:|------|------|
| 1 | **ATS Keyword Detection** | Extract JD keywords → check resume hit rate → prevent machine-filtering failure |
| 2 | **Job Match Scoring** | 6-dimension weighted score → 🟢Match / 🟡Try / 🔴Give up |
| 3 | **JD Deconstruction** | Company background + role analysis + hard/soft requirements + hidden needs + predicted interview questions |
| 4 | **Resume Diagnosis** | Matches + redundancies + gaps + risks — line-by-line with fixes |
| 5 | **Multi-JD Priority Ranking** | 6-dimension weighted ranking → energy allocation strategy |
| 6 | **Gap Analysis & Learning Plan** | Ranked by severity+urgency+learning cycle → what to learn, how long, verifiable output |
| 7 | **Full Interview Prep** | HR screen → written test → technical → behavioral → final → scenario simulation (6 stages) |
| 8 | **Mock Interview Mode** | Switch to interviewer role → random Q&A → follow-up → instant feedback |
| 9 | **Offer & Salary Negotiation** | Market benchmark → negotiable points breakdown → script ready to send |
| 10 | **Culture & Survival Guide** | Culture snapshot → week-1 checklist → month-1 key moves → exit signals |

Plus: **Industry Salary & Market Trends** (on-demand module — web search for latest data)

---

## How It Works

This repo uses **CLAUDE.md** — a file that Claude Code automatically reads when you enter the directory. No installation, no plugins, no registration. Just `cd` in and go.

---

## Examples

See [`examples/`](examples/) for complete walkthroughs with real-world scenarios:

| Example | Scenario |
|---------|---------|
| [Product Manager (New Grad)](examples/product-manager.md) | CS major to PM role at a mid-size internet company |
| [Digital Marketing](examples/digital-marketing.md) | Marketing major with agency internship to brand-side role |

---

## Background

This methodology was born from real 2026 job hunting — facing interviews with a RISC-V chip unicorn (SpacemiT), a listed pharmaceutical group (Joincare), a cross-border logistics startup, and AI SaaS companies. Each version upgrade was driven by actual interview questions, HR screening logic, and hard-won lessons. V3 now covers the complete journey from application to onboarding.

> "Recruiters spend 6 seconds per resume. Every word on yours must answer: what problem can you solve for me?"

---

## License

MIT — take it, use it, remix it, teach with it. Just keep the attribution.

See [LICENSE](LICENSE).
