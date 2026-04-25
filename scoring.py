def final_ranking(matches, interest_results):
    final = []

    for m in matches:
        interest = next(i for i in interest_results if i['candidate'] == m['name'])

        final_score = (m['match_score'] * 0.7) + (interest['interest_score'] * 0.3)

        final.append({
            "name": m['name'],
            "match_score": m['match_score'],
            "interest_score": interest['interest_score'],
            "final_score": round(final_score, 2)
        })

    return sorted(final, key=lambda x: x['final_score'], reverse=True)