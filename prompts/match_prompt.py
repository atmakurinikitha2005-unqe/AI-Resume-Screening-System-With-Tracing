from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["job_description", "extracted_data"],
    template="""
You are an AI recruiter assistant.

Compare the extracted resume data with the given job description.

Rules:
- Match only based on the provided text.
- Do NOT assume missing skills.
- Clearly show what is matched and what is missing.

Job Description:
{job_description}

Extracted Resume Data:
{extracted_data}

Return in this format exactly:

Matched Skills: [comma-separated list]
Missing Skills: [comma-separated list]
Experience Match: [Strong / Partial / Weak]
Tools Match: [comma-separated list]
Overall Match Summary: [2-3 lines]
"""
)