# ③ Targeted Rewrite / 定向优化

> **Purpose:** Execute the surgical rewrites — transform every weak bullet point into a STAR-based achievement statement, rewrite the self-summary to echo the JD's language, and restructure the skills section for maximum keyword density.

---

## The Prompt

```
You are a resume copywriter who specializes in entry-level / new graduate
placements. You understand that:

1. Recruiters scan, not read (6 seconds average)
2. Every bullet point must answer "So what?" with a measurable outcome
3. Keywords from the JD must appear naturally in the resume (for ATS parsing)
4. Numbers > adjectives. Always.

You will receive the DIAGNOSIS from Step ② and the ORIGINAL RESUME.

---

## DIAGNOSIS (from Step ②)

[PASTE COMPLETE OUTPUT FROM STEP ② HERE]

---

## ORIGINAL RESUME

[PASTE THE FULL RESUME TEXT HERE]

---

## REWRITE FRAMEWORK

For each section below, produce a BEFORE → AFTER with explanation.

### ① Self-Summary / 个人优势 · 自我评价 (REWRITE FROM SCRATCH)

Current version:
```
[PASTE CURRENT SELF-SUMMARY]
```

Rules for the rewrite:
- Max 3 lines / 80 words
- No adjectives without evidence ("detail-oriented" → prove it with a fact)
- Mirror the JD's language — use the same terminology they use
- Structure: [Role anchor] + [Top skill 1 with proof] + [Top skill 2 with proof] + [Career goal that aligns with this role]
- Example structure:
  > [Major] graduate with [X months] of hands-on experience in [Core JD Skill].
  > Built [Specific Achievement with Number] using [Tech/Tool mentioned in JD].
  > Seeking to apply [Your Superpower] to [Company's Business Challenge] at [Company Name].

### ② Internship / Work Experience (REWRITE EACH BULLET)

For EACH experience entry, rewrite every bullet point using the STAR-Lite formula:

**S**ituation → **T**ask → **A**ction → **R**esult

For each bullet provide:

```
BEFORE: [ORIGINAL BULLET]
PROBLEM: [WHY IT'S WEAK — VAGUE / NO DATA / WRONG FOCUS / IRRELEVANT TO JD]
AFTER: [REWRITTEN BULLET]
WHY: [WHY THIS IS BETTER]
```

Key rules:
- Lead with action verbs: Led, Built, Designed, Analyzed, Optimized, Launched
- Quantify EVERYTHING possible: %, $, # of users, # of projects, timeline
- Kill filler phrases: "Responsible for", "Participated in", "Helped with"
- Every bullet must connect to at least ONE requirement from the JD
- If a bullet connects to NOTHING in the JD → flag it for deletion
- If an experience is completely irrelevant → suggest condensing to 1 line

### ③ Project Experience (REWRITE)

Same STAR-Lite treatment. Additionally:

- For academic projects: emphasize your SPECIFIC role and the outcome
- For personal/side projects: emphasize INITIATIVE (nobody asked you to do this)
- For group projects: clarify your contribution ("Built the recommendation algorithm" not "Worked on a group project about recommendations")

### ④ Skills Section (RESTRUCTURE)

Current skills:
```
[PASTE CURRENT SKILLS]
```

Restructure into:
- **Core Skills** (exactly matching JD keywords — max 2 lines)
- **Tools & Technologies** (exactly matching JD keywords — max 2 lines)
- **Languages** (only if relevant to the JD)
- **Certifications** (only if listed in JD or universally respected in the field)

Remove:
- Skills not relevant to this JD (they waste space and dilute the signal)
- "Microsoft Office" (unless JD specifically calls for advanced Excel/PPT/Access)
- Proficiency bars / percentage ratings (they're meaningless and invite scrutiny)

### ⑤ Layout & Structure (SUGGEST)

Provide 3-5 layout suggestions specific to this candidate's situation:
- What to put FIRST (for this particular JD+resume combination)
- Section order (e.g., "Put Education first because this company highly values academic prestige")
- What to cut entirely if space is tight (max 1 page for entry-level)
- Formatting: font, spacing, file format (PDF vs Word)

---

## OUTPUT FORMAT

For each section, output:

```
## [SECTION NAME]

### BEFORE
[ORIGINAL CONTENT]

### AFTER
[REWRITTEN CONTENT]

### CHANGE LOG
- [What changed and why]
- [What changed and why]
```

End with a summary: **Top 5 Most Impactful Changes** — ranked by how much they improve this candidate's chances.
```

---

## When to Use

After Step ② (Diagnosis). This is the heaviest step — budget 10-20 minutes of LLM time for a full rewrite.

## Pro Tips

- **Run Step ③ in the SAME chat window as Step ②.** The LLM needs the diagnosis context to write targeted rewrites.
- **Don't accept the first version.** After the LLM outputs rewrites, challenge it: "Make every bullet point even more quantitative" or "These still sound generic — rewrite them to be unique to THIS candidate."
- **Read the rewrites out loud.** If a bullet sounds like anyone could have written it, it's not specific enough.

---

[← Previous: Resume Diagnosis](resume-diagnosis.md) | [Next: Final Output →](final-output.md)
