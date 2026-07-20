"""
Pleadly Gradio App — 全流程求职助手前端入口
启动命令: python app/main.py
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import gradio as gr
from dotenv import load_dotenv
load_dotenv()

from core.engine import (
    AnalysisInput, run_step, get_llm_client
)
from core.agent import AgentOrchestrator, search_company_info, search_interview_experience

# ── Theme ──
theme = gr.themes.Soft(
    primary_hue="blue",
    secondary_hue="gray",
    neutral_hue="slate",
).set(
    body_text_size="14px",
    button_primary_background_fill="*primary_500",
    button_primary_text_color="white",
)

# ── Agent State per session ──
agent = AgentOrchestrator()

# ── Step Functions ──

def step_ats_check(resume: str, jd: str):
    if not resume or not jd:
        return "请先输入简历和JD。"
    agent.set_input(resume, jd)
    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    result = run_step("ats_check", user_input)
    agent.state.step_results["ats_check"] = result.content
    return result.content

def step_match_score(resume: str, jd: str):
    if not resume or not jd:
        return "请先输入简历和JD。"
    agent.set_input(resume, jd)
    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    result = run_step("match_score", user_input)
    agent.state.step_results["match_score"] = result.content
    return result.content

def step_jd_analysis(resume: str, jd: str, company_hint: str):
    """Step 3: JD拆解 + 公司背景研究"""
    if not jd:
        return "请先输入JD。"

    agent.set_input(resume, jd)

    # 先做公司研究
    status = "正在联网搜索公司信息...\n"
    if company_hint:
        company_info = search_company_info(company_hint)
        agent.state.company_research = company_info
        status += f"✅ 已搜索公司: {company_hint}\n"

    # 进行JD拆解
    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    rag_ctx = agent.get_rag_context()
    result = run_step("jd_analysis", user_input, rag_context=rag_ctx)
    agent.state.step_results["jd_analysis"] = result.content

    return status + "\n" + result.content

def step_resume_diagnosis(resume: str, jd: str):
    if not resume or not jd:
        return "请先输入简历和JD。"
    if "jd_analysis" not in agent.state.step_results:
        # Run JD analysis first
        user_input = AnalysisInput(resume_text=resume, jd_text=jd)
        r = run_step("jd_analysis", user_input)
        agent.state.step_results["jd_analysis"] = r.content

    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    user_input.extra_instructions = agent.state.step_results.get("jd_analysis", "")
    result = run_step(
        "resume_diagnosis",
        user_input,
        previous_steps={"jd_analysis": agent.state.step_results.get("jd_analysis", "")}
    )
    agent.state.step_results["resume_diagnosis"] = result.content
    return result.content

def step_learning_plan(resume: str, jd: str):
    if not resume or not jd:
        return "请先输入简历和JD。"
    if "resume_diagnosis" not in agent.state.step_results:
        # Auto-run previous steps
        step_resume_diagnosis(resume, jd)

    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    result = run_step(
        "learning_plan",
        user_input,
        previous_steps={"diagnosis": agent.state.step_results.get("resume_diagnosis", "")}
    )
    agent.state.step_results["learning_plan"] = result.content
    return result.content

def step_interview_prep(resume: str, jd: str, company_hint: str):
    """Step 7: 全流程面试准备(含联网搜索面经)"""
    if not resume or not jd:
        return "请先输入简历和JD。"

    # 联网搜索面经
    status = ""
    if company_hint:
        status += "正在联网搜索真实面经...\n"
        role_hint = jd.strip().split('\n')[0][:30] if jd else "AI"
        experiences = search_interview_experience(company_hint, role_hint)
        agent.state.interview_experiences = experiences
        status += f"✅ 已搜索面经\n\n"

    # Auto-run required prior steps
    if "jd_analysis" not in agent.state.step_results:
        step_jd_analysis(resume, jd, company_hint)
    if "resume_diagnosis" not in agent.state.step_results:
        step_resume_diagnosis(resume, jd)

    user_input = AnalysisInput(resume_text=resume, jd_text=jd)
    rag_ctx = agent.get_rag_context()
    result = run_step(
        "interview_prep",
        user_input,
        rag_context=rag_ctx,
        previous_steps={
            "jd_analysis": agent.state.step_results.get("jd_analysis", ""),
            "diagnosis": agent.state.step_results.get("resume_diagnosis", ""),
        }
    )
    agent.state.step_results["interview_prep"] = result.content
    return status + result.content

def run_all_steps(resume: str, jd: str, company_hint: str):
    """一键运行全部步骤"""
    if not resume or not jd:
        return "请同时输入简历和岗位JD。"

    output = []
    # Step 1
    output.append("# ══════ 第一步: ATS关键词检测 ══════\n")
    output.append(step_ats_check(resume, jd))

    # Step 2
    output.append("\n\n# ══════ 第二步: 岗位匹配度评分 ══════\n")
    output.append(step_match_score(resume, jd))

    # Step 3
    output.append("\n\n# ══════ 第三步: JD全维度拆解 ══════\n")
    output.append(step_jd_analysis(resume, jd, company_hint))

    # Step 4
    output.append("\n\n# ══════ 第四步: 简历对照诊断 ══════\n")
    output.append(step_resume_diagnosis(resume, jd))

    # Step 6
    output.append("\n\n# ══════ 第六步: 差距分析与学习计划 ══════\n")
    output.append(step_learning_plan(resume, jd))

    # Step 7
    output.append("\n\n# ══════ 第七步: 全流程面试准备 ══════\n")
    output.append(step_interview_prep(resume, jd, company_hint))

    return "\n".join(output)

# ── Gradio UI ──

with gr.Blocks(theme=theme, title="Pleadly - 聪明地求职") as app:
    gr.Markdown("""
    # 🎯 Pleadly — 聪明地求职
    ### AI招聘经理视角的全流程求职助手

    粘贴你的**简历**和**岗位JD**，我帮你跑完整分析。
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 📄 你的简历")
            resume_input = gr.Textbox(
                label="在此粘贴简历内容(或上传文件)",
                placeholder="郑灿坤\n教育背景:\n中南林业科技大学...",
                lines=12,
                max_lines=20,
            )
            resume_file = gr.File(
                label="或上传简历文件(docx/pdf/txt)",
                file_types=[".docx", ".pdf", ".txt", ".md"],
            )

        with gr.Column(scale=1):
            gr.Markdown("### 📋 岗位JD")
            jd_input = gr.Textbox(
                label="在此粘贴岗位JD",
                placeholder="职位名称: AI产品经理\n公司: XX科技\n任职要求:\n1. ...",
                lines=12,
                max_lines=20,
            )

    company_hint = gr.Textbox(
        label="公司名称(可选，用于联网背景调查和面经搜索)",
        placeholder="例如: 进迭时空、健康元、字节跳动",
    )

    with gr.Row():
        run_btn = gr.Button("🚀 一键全流程分析", variant="primary", size="lg")
        clear_btn = gr.Button("🗑️ 清空", size="lg")

    output_box = gr.Markdown(
        value="👆 输入简历和JD后点击分析按钮。分析需要1-3分钟。",
        label="分析结果",
    )

    gr.Markdown("---")
    gr.Markdown("### 🔧 分步分析(可选)")

    with gr.Accordion("Step 1-2: ATS检测 + 匹配评分", open=False):
        with gr.Row():
            step1_btn = gr.Button("① ATS关键词检测")
            step2_btn = gr.Button("② 岗位匹配度评分")

    with gr.Accordion("Step 3-4: JD拆解 + 简历诊断", open=False):
        with gr.Row():
            step3_btn = gr.Button("③ JD全维度拆解(含公司背景)")
            step4_btn = gr.Button("④ 简历对照诊断")

    with gr.Accordion("Step 6-7: 学习计划 + 面试准备", open=False):
        with gr.Row():
            step6_btn = gr.Button("⑥ 差距学习计划")
            step7_btn = gr.Button("⑦ 全流程面试准备(含面经搜索)")

    gr.Markdown("""
    ---
    ### 📖 使用说明

    1. **粘贴简历** — 可以是纯文本，也可以上传 docx/pdf 文件
    2. **粘贴JD** — 从招聘网站直接复制
    3. **(可选)输入公司名** — 我会联网搜索公司背景和真实面经
    4. **点击分析** — 等待1-3分钟获取完整报告

    ### 🔒 隐私说明
    你输入的数据仅用于本次分析，不会存储。所有AI调用通过DeepSeek API。
    """)

    # ── Event Bindings ──

    # File upload: auto-parse
    def handle_file_upload(file):
        from core.agent import parse_resume_file
        if file is not None:
            return parse_resume_file(file.name)
        return ""

    resume_file.change(handle_file_upload, inputs=[resume_file], outputs=[resume_input])

    # Run all
    run_btn.click(
        run_all_steps,
        inputs=[resume_input, jd_input, company_hint],
        outputs=[output_box],
    )

    # Individual steps
    step1_btn.click(step_ats_check, inputs=[resume_input, jd_input], outputs=[output_box])
    step2_btn.click(step_match_score, inputs=[resume_input, jd_input], outputs=[output_box])
    step3_btn.click(step_jd_analysis, inputs=[resume_input, jd_input, company_hint], outputs=[output_box])
    step4_btn.click(step_resume_diagnosis, inputs=[resume_input, jd_input], outputs=[output_box])
    step6_btn.click(step_learning_plan, inputs=[resume_input, jd_input], outputs=[output_box])
    step7_btn.click(step_interview_prep, inputs=[resume_input, jd_input, company_hint], outputs=[output_box])

    # Clear
    clear_btn.click(
        lambda: ("", "", "", "👆 输入简历和JD后点击分析按钮。分析需要1-3分钟。"),
        outputs=[resume_input, jd_input, company_hint, output_box],
    )

# ── Launch ──
if __name__ == "__main__":
    print("🚀 Pleadly 启动中...")
    print(f"📡 本地访问: http://localhost:7860")
    app.launch(
        server_name="0.0.0.0",
        server_port=int(os.getenv("APP_PORT", 7860)),
        share=False,
    )
