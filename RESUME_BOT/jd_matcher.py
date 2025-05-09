
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Load a light and effective local model
model = SentenceTransformer("all-MiniLM-L6-v2")

def truncate(text, max_chars=4000):
    return text[:max_chars]

def get_embedding(text):
    text = truncate(text)
    return model.encode(text)

def match_resume_to_jd(resume_text, jd_text):
    try:
        resume_emb = get_embedding(resume_text)
        jd_emb = get_embedding(jd_text)
        score = cosine_similarity([resume_emb], [jd_emb])[0][0]
        return round(score * 100, 2)
    except Exception as e:
        return f"⚠️ Matching Error: {e}"
