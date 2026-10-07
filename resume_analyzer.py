from pypdf import PdfReader


def extract_text(uploaded_file):
    """Extract text from uploaded PDF."""

    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


def analyze_resume(uploaded_file):
    """Analyze resume and find common technical skills."""

    resume_text = extract_text(uploaded_file)

    skills = [
        "python",
        "sql",
        "machine learning",
        "pandas",
        "numpy",
        "scikit-learn",
        "tensorflow",
        "pytorch",
        "fastapi",
        "docker",
        "git"
    ]

    found_skills = []

    for skill in skills:

        if skill.lower() in resume_text.lower():
            found_skills.append(skill)

    result = {
        "skills_found": found_skills,
        "total_skills": len(found_skills)
    }

    return result