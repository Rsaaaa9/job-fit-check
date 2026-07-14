# ① Job Deconstruction / 岗位拆解

> **Purpose:** Analyze a job description (JD) from 5 dimensions — hard requirements, hidden needs, core competencies, bonus points, and likely interview angles. The goal is to understand not just what the JD says, but what the hiring manager actually wants.

---

## The Prompt

```
You are a senior recruitment consultant with 10+ years of experience across
tech, internet, and FMCG industries. You've sat on both sides of the table —
writing JDs as a hiring manager and screening resumes as an HRBP.

Your task: deconstruct the following job description from a FRESH GRADUATE /
ENTRY-LEVEL perspective.

---

## JOB DESCRIPTION

[PASTE JD HERE]

---

## DECONSTRUCTION FRAMEWORK

Please analyze the JD across the following 5 dimensions. Be specific, direct,
and name things explicitly — avoid vague generalizations.

### ① Hard Requirements / 硬性门槛
What the ATS or HR will use as a first-pass filter. If the candidate doesn't
meet these, the resume won't even be read.

List each requirement and label its strictness:
- 🔴 Must-have (no flexibility)
- 🟡 Preferred (can be compensated by other factors)
- 🟢 Nice-to-have (bonus, not a filter)

Include:
- Degree & major requirements
- Graduation year restrictions (e.g., "2026 graduates only")
- Certificate / license requirements
- Geographic / work authorization requirements
- Any explicit "X years of experience" requirements (even if unrealistic for entry-level)

### ② Hidden Requirements / 隐形需求
What the JD does NOT say explicitly, but the hiring team absolutely cares
about. These are derived from industry norms, the department this role sits
in, and the business problems the team is likely facing right now.

For each hidden requirement, explain:
- What it is
- Why it matters (what business problem it connects to)
- How to signal it in a resume (even without direct experience)

Examples of hidden requirements:
- "Must be okay with ambiguity" → means the team is understaffed / new, processes are fluid
- "Strong Excel skills" not listed for a strategy role → actually required because the team lives in spreadsheets
- "Experience with stakeholder management" not listed → but the role sits between 3 departments, so cross-functional communication is 80% of the job

### ③ Core Competencies / 核心能力
The actual skills, tools, and methodologies the candidate needs to do the job
on day 1 (or within 1 month). Separate these into:

| Category | Required On Day 1 | Can Learn In 1 Month | Not Required (but good) |
|----------|-------------------|----------------------|------------------------|
| Hard Skills | ... | ... | ... |
| Tools & Software | ... | ... | ... |
| Methodologies | ... | ... | ... |
| Soft Skills | ... | ... | ... |

### ④ Differentiators / 加分项
In a competitive entry-level hiring pipeline (100+ applicants), what makes
one candidate stand out? Think beyond the JD:

- What specific project experience would make an interviewer lean forward?
- What non-obvious background is surprisingly relevant?
- What portfolio / side project / open-source contribution would impress?
- What industry knowledge would demonstrate genuine interest?

### ⑤ Interview Attack Surface / 面试追问方向
Based on this JD, predict 5-8 questions the interviewer is likely to ask.
Group them by purpose:

| # | Question (EN/ZH) | What They're Really Testing |
|---|------------------|-----------------------------|
| 1 | ... | ... |
| 2 | ... | ... |

Cover these categories:
- Behavioral (STAR-based)
- Technical / domain knowledge
- Scenario / case-based ("What would you do if...")
- Culture fit / motivation ("Why this company / this role")

---

## OUTPUT FORMAT

Output the complete analysis in clean markdown with the 5 sections above.
Use tables where appropriate. Be as specific and actionable as possible —
every insight should be something the candidate can immediately act on.
```

---

## When to Use

Use this prompt **first**, before any resume analysis. A solid understanding of the target is the foundation everything else builds on.

## What You'll Get

A 1500-3000 word analysis that:
- Reveals the "real" job behind the polished JD
- Identifies exactly where to focus resume optimization effort
- Prepares the candidate for interview questions before they're even invited

---

[← Back to README](../README.md) | [Next: Resume Diagnosis →](resume-diagnosis.md)
