from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data"],
    template="""
You are an AI candidate scoring system.

Based on the match analysis, assign a fit score from 0 to 100.

Scoring guidance:
- 80 to 100 = Strong candidate
- 50 to 79 = Average candidate
- 0 to 49 = Weak candidate

Rules:
- Score only based on the provided match analysis.
- Do NOT give random scores.
- Consider matched skills, missing skills, tools, and experience.

Match Analysis:
{match_data}

Return in this format exactly:

Score: [number only]
Category: [Strong / Average / Weak]
Reason: [short reason]
"""
)