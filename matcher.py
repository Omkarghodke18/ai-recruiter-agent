def match_candidates(jd_skills, candidates_df):
    results = []

    for _, row in candidates_df.iterrows():
        candidate_skills = set(row['skills'].split())
        jd_skill_set = set(jd_skills)

        matched = list(candidate_skills & jd_skill_set)

        match_score = len(matched) / len(jd_skill_set) if jd_skill_set else 0

        results.append({
            "name": row['name'],
            "match_score": round(match_score, 2),
            "matched_skills": matched,
            "skills": row['skills']
        })

    return sorted(results, key=lambda x: x['match_score'], reverse=True)