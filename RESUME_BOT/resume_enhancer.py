import requests

GROQ_API_KEY = "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"
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"

def enhance_resume(resume_text, jd_text):
    prompt = f"""
You're an expert resume optimizer. Rewrite the resume below to align strongly with the job description.
Ensure it remains truthful but emphasizes relevant skills, experience, and keywords.

Job Description:
\"\"\"{jd_text}\"\"\"

Resume:
\"\"\"{resume_text}\"\"\"
"""

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(GROQ_CHAT_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠️ Enhancement Error: {response.status_code} - {response.text}"
