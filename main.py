from dotenv import load_dotenv
load_dotenv()

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def process_resume(candidate_name, resume_text, job_description):
    print("=" * 80)
    print(f"PROCESSING: {candidate_name}")
    print("=" * 80)

    extracted_data = extract_chain.invoke({
        "resume_text": resume_text
    })


    print("\nSTEP 1: EXTRACTED DATA")
    print(f"Name: {extracted_data['name']}")
    print(f"Skills: {', '.join(extracted_data['skills'])}")
    print(f"Experience: {extracted_data['experience']}")
    print(f"Tools: {', '.join(extracted_data['tools'])}")

    match_data = match_chain.invoke({
        "job_description": job_description,
        "extracted_data": extracted_data
    })
    print("\nSTEP 2: MATCH RESULT")
    print(f"Matched Skills: {', '.join(match_data['matched_skills'])}")
    print(f"Missing Skills: {', '.join(match_data['missing_skills'])}")
    print(f"Experience Match: {match_data['experience_match']}")
    print(f"Tools Match: {', '.join(match_data['tools_match'])}")
    print(f"Overall Match Summary: {match_data['overall_match_summary']}")

    score_data = score_chain.invoke({
        "match_data": match_data
    })
    print("\nSTEP 3: SCORE RESULT")
    print(f"Score: {score_data['score']}")
    print(f"Category: {score_data['category']}")
    print(f"Reason: {score_data['reason']}")

    explanation = explain_chain.invoke({
        "match_data": match_data,
        "score_data": score_data
    })
    print("\nSTEP 4: EXPLANATION")
    print(explanation['explanation'])

    print("\n")


def main():
    job_description = read_file("data/job_description.txt")

    resumes = {
        "Strong Candidate": read_file("data/strong_resume.txt"),
        "Average Candidate": read_file("data/average_resume.txt"),
        "Weak Candidate": read_file("data/weak_resume.txt")
    }

    for candidate_name, resume_text in resumes.items():
        process_resume(candidate_name, resume_text, job_description)


if __name__ == "__main__":
    main()