from langchain_core.runnables import RunnableLambda

KNOWN_SKILLS = [
    "Python", "Machine Learning", "Deep Learning", "NLP", "SQL",
    "TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy",
    "Matplotlib", "Excel", "Java", "HTML", "CSS", "Communication"
]

KNOWN_TOOLS = [
    "Python", "SQL", "TensorFlow", "PyTorch", "Scikit-learn",
    "Jupyter Notebook", "Git", "Excel", "VS Code", "MS Office",
    "Pandas", "NumPy", "Matplotlib"
]

def extract_resume_data(inputs):
    resume_text = inputs["resume_text"]

    found_skills = [skill for skill in KNOWN_SKILLS if skill.lower() in resume_text.lower()]
    found_tools = [tool for tool in KNOWN_TOOLS if tool.lower() in resume_text.lower()]

    name = "Unknown"
    for line in resume_text.splitlines():
        if line.lower().startswith("name:"):
            name = line.split(":", 1)[1].strip()
            break

    experience_lines = []
    capture = False
    for line in resume_text.splitlines():
        if line.strip().lower().startswith("experience"):
            capture = True
            continue
        if capture:
            if line.strip().lower().startswith("tools"):
                break
            if line.strip():
                experience_lines.append(line.strip())

    experience_summary = " ".join(experience_lines[:3]) if experience_lines else "No clear experience found"

    return {
        "name": name,
        "skills": found_skills,
        "experience": experience_summary,
        "tools": found_tools
    }

extract_chain = RunnableLambda(extract_resume_data)