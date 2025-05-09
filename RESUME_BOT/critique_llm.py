import requests

GROQ_API_KEY = "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"
GROQ_CHAT_URL = "https://api.groq.com/openai/v1/chat/completions"

def get_resume_feedback(resume_text):
    prompt = f"""
You're a resume critique expert. Analyze the following resume and give structured feedback in:
1. Grammar and clarity
2. Structure and formatting
3. Skill gaps and relevance
4. ATS compatibility
5. Suggested improvements

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
        return f"⚠️ LLM Error: {response.status_code} - {response.text}"
