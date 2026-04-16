from langchain_core.prompts import PromptTemplate

explain_prompt = PromptTemplate(
    input_variables=["match_data", "score_data"],
    template="""
You are an explainable AI assistant.

Explain why the candidate received this score.

Rules:
- Be clear and simple.
- Mention strengths.
- Mention missing areas.
- Do NOT assume anything not given.

Match Analysis:
{match_data}

Score Result:
{score_data}

Return in this format exactly:

Explanation:
[Write 4 to 6 clear lines]
"""
)