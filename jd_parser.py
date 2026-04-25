def parse_jd(jd_text):
    # Simple parser (can upgrade with OpenAI later)
    words = jd_text.replace(",", "").split()

    skills = []
    known_skills = ["Python", "SQL", "Snowflake", "AWS", "Airflow", "TensorFlow", "PowerBI"]

    for skill in known_skills:
        if skill.lower() in [w.lower() for w in words]:
            skills.append(skill)

    return {
        "skills": skills,
        "experience": None,
        "role": None
    }