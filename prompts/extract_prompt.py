from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
You are an AI resume analyzer.

Your task is to extract only the information explicitly present in the resume.

Rules:
- Do NOT assume any skill that is not written in the resume.
- Do NOT hallucinate.
- Extract only these fields:
  1. Skills
  2. Experience
  3. Tools

Resume:
{resume_text}

Return in this format exactly:

Skills: [comma-separated list]
Experience: [short summary]
Tools: [comma-separated list]
"""
)