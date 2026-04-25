import streamlit as st
import pandas as pd
from jd_parser import parse_jd
from matcher import match_candidates
from conversation_agent import simulate_interest
from scoring import final_ranking

st.set_page_config(page_title="AI Recruiter Agent", layout="wide")

st.title("🤖 AI Recruitment Agent")

jd = st.text_area("📄 Enter Job Description")

if st.button("🔍 Find Candidates"):
    df = pd.read_csv("candidates.csv")

    parsed = parse_jd(jd)
    jd_skills = parsed["skills"]

    matches = match_candidates(jd_skills, df)

    interest_results = [simulate_interest(m['name']) for m in matches]

    final = final_ranking(matches, interest_results)

    st.subheader("📊 Final Ranked Candidates")
    st.dataframe(pd.DataFrame(final))

    st.subheader("💡 Match Explanation")
    for m in matches:
        st.write(f"{m['name']} matched on: {', '.join(m['matched_skills'])}")
