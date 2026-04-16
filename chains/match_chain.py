from langchain_core.runnables import RunnableLambda

JOB_REQUIREMENTS = [
    "Python", "Machine Learning", "Deep Learning", "NLP",
    "TensorFlow", "PyTorch", "Scikit-learn", "SQL"
]

def match_resume(inputs):
    extracted_data = inputs["extracted_data"]

    skills = extracted_data.get("skills", [])
    experience_text = extracted_data.get("experience", "")
    tools = extracted_data.get("tools", [])

    matched = [req for req in JOB_REQUIREMENTS if req in skills]
    missing = [req for req in JOB_REQUIREMENTS if req not in skills]

    if "3 years" in experience_text.lower() or "4 years" in experience_text.lower() or "2 years" in experience_text.lower():
        experience_match = "Strong"
    elif "internship" in experience_text.lower() or "project" in experience_text.lower():
        experience_match = "Partial"
    else:
        experience_match = "Weak"

    tools_match = [tool for tool in ["Python", "SQL", "TensorFlow", "PyTorch", "Scikit-learn"] if tool in tools]

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "experience_match": experience_match,
        "tools_match": tools_match,
        "overall_match_summary": f"Matched {len(matched)} important requirements and missed {len(missing)}."
    }

match_chain = RunnableLambda(match_resume)