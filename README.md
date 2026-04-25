# ai-recruiter-agent
AI agent for candidate matching and ranking

# 🤖 AI Recruitment Agent

## 🚀 Overview
This AI agent automates candidate sourcing, engagement, and ranking.

## 🔥 Features
- Job Description Parsing
- Candidate Matching with Explainability
- Simulated Candidate Engagement
- Final Ranking (Match Score + Interest Score)

## 🛠️ Tech Stack
- Python
- Streamlit
- Pandas

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py

📊 Sample Input
Looking for Data Engineer with Python, SQL, Snowflake, AWS

📤 Sample Output
Ranked candidates with scores

🧠 Scoring Logic

Final Score = 0.7 * Match Score + 0.3 * Interest Score

🏗️ Architecture

JD → Parser → Matcher → Conversation → Scoring → Output

🎥 Demo

(Add your Loom or screen recording link here)
