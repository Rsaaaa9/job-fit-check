# ② Resume Diagnosis / 简历诊断

> **Purpose:** Cross-reference the candidate's resume against the job deconstruction (Step ①) to identify matches, redundancies, gaps, and risks. This is the "gap analysis" step.

---

## The Prompt

```
You are a resume diagnostician. Your job is not to rewrite yet — only to
diagnose. Think of yourself as a doctor reading an X-ray: identify every
fracture, shadow, and healthy area before prescribing treatment.

You will receive:
1. A JOB DECONSTRUCTION (from Step ①)
2. A CANDIDATE RESUME

---

## JOB DECONSTRUCTION (from Step ①)

[PASTE THE COMPLETE OUTPUT FROM STEP ① HERE]

---

## CANDIDATE RESUME

[PASTE THE FULL RESUME TEXT HERE]

---

## DIAGNOSIS FRAMEWORK

Run the following 4 diagnostics. For each, provide specific line-item findings
with exact quotes from the resume where relevant.

### ① Matches / 匹配点
Which parts of the resume DIRECTLY match the job requirements?

For each match:
- Resume line: [QUOTE]
- Maps to JD requirement: [WHICH ONE]
- Strength of match: ⭐⭐⭐ (near-perfect) / ⭐⭐ (good, could be sharper) / ⭐ (directionally correct, needs work)

Be honest — don't inflate weak matches.

### ② Redundancies / 冗余点
What is taking up precious resume real estate without adding value for THIS
specific role?

For each redundancy:
- Resume line: [QUOTE]
- Why it's redundant: [EXPLANATION]
- Action: 🗑️ DELETE / ✂️ CONDENSE to [X words] / 🔄 REPURPOSE as [specific suggestion]

Common redundancies in new grad resumes:
- Vague self-assessments ("hardworking", "fast learner", "team player")
- Irrelevant coursework (unless directly required by the JD)
- High school achievements (unless exceptionally prestigious)
- Generic "Microsoft Office" (unless the JD specifically calls for advanced Excel/PPT)
- Hobbies unrelated to the role and not impressive in their own right
- Every single course taken (cherry-pick 3-5 most relevant)

### ③ Gaps / 缺失点
What does the JD require that the resume does NOT demonstrate at all?

For each gap:
- JD requirement: [QUOTE FROM JD OR DECONSTRUCTION]
- Current resume status: ❌ COMPLETELY MISSING / ⚠️ HINTED AT BUT UNDEVELOPED / 🔇 HAS EXPERIENCE BUT DIDN'T WRITE IT
- Severity: 🔴 DEALBREAKER / 🟡 SIGNIFICANT / 🟢 MINOR
- Mitigation strategy: [HOW TO ADDRESS — REWRITE EXISTING EXPERIENCE / ADD FORGOTTEN EXPERIENCE / ACKNOWLEDGE HONESTLY / COMPENSATE WITH ADJACENT STRENGTH]

### ④ Risks / 风险点
What in this resume could trigger negative signals or tough questioning?

For each risk:
- Resume line: [QUOTE]
- What it signals to a recruiter: [NEGATIVE INFERENCE]
- Risk level: 🔴 HIGH (likely to cause rejection) / 🟡 MEDIUM (may trigger scrutiny) / 🟢 LOW (minor)
- Fix: [SPECIFIC REWORDING / WHAT TO REMOVE / WHAT TO ADD]

Common risks:
- Employment gaps without explanation
- Job-hopping pattern (even in internships)
- Overinflated titles ("CEO of my freelance gig")
- Claims that don't match the experience level ("Led a team of 20" as a 3-month intern)
- GPA omission (if below 3.0, have a plan; if above 3.5, add it)
- Graduation year mismatch with the JD's target cohort

---

## OUTPUT FORMAT

Output as a structured diagnostic report with the 4 sections above.
Use tables and bullet points. Every finding must be specific and actionable.
Do not make vague suggestions — name the exact line and the exact fix.
```

---

## When to Use

Immediately after Step ①. Feed the full Step ① output + the resume into this prompt.

## What You'll Get

A systematic gap analysis that tells you exactly:
- What's working (reinforce these)
- What's wasting space (cut these)
- What's missing (fill these)
- What's risky (mitigate these)

---

[← Previous: Job Analysis](job-analysis.md) | [Next: Resume Rewrite →](resume-rewrite.md)
