import random

def simulate_interest(candidate_name):
    responses = [
        ("Yes, I am actively looking for opportunities.", 0.9),
        ("I might be interested, can you share more details?", 0.6),
        ("Not looking for a change right now.", 0.2)
    ]

    response, score = random.choice(responses)

    return {
        "candidate": candidate_name,
        "response": response,
        "interest_score": score
    }