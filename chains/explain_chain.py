from langchain_core.runnables import RunnableLambda

def explain_result(inputs):
    match_data = inputs["match_data"]
    score_data = inputs["score_data"]

    return {
        "explanation": (
            f"The candidate received a score of {score_data.get('score')} and falls under the "
            f"{score_data.get('category')} category. "
            f"Matched skills: {', '.join(match_data.get('matched_skills', [])) or 'None'}. "
            f"Missing skills: {', '.join(match_data.get('missing_skills', [])) or 'None'}. "
            f"Experience match level: {match_data.get('experience_match')}."
        )
    }

explain_chain = RunnableLambda(explain_result)