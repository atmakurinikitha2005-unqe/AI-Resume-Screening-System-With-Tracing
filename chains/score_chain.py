from langchain_core.runnables import RunnableLambda

def score_candidate(inputs):
    match_data = inputs["match_data"]

    matched_count = len(match_data.get("matched_skills", []))
    missing_count = len(match_data.get("missing_skills", []))
    experience_match = match_data.get("experience_match", "Weak")

    score = matched_count * 12

    if experience_match == "Strong":
        score += 25
    elif experience_match == "Partial":
        score += 15
    else:
        score += 5

    score = max(0, min(score, 100))

    if score >= 80:
        category = "Strong"
    elif score >= 50:
        category = "Average"
    else:
        category = "Weak"

    return {
        "score": score,
        "category": category,
        "reason": f"Calculated using matched skills ({matched_count}), missing skills ({missing_count}), and experience level."
    }

score_chain = RunnableLambda(score_candidate)