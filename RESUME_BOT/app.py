import streamlit as st
from resume_parser import extract_text, parse_resume
from critique_llm import get_resume_feedback
from jd_matcher import match_resume_to_jd
from resume_enhancer import enhance_resume

st.set_page_config(page_title="GenAI Resume Critique Bot", layout="centered")

st.title("🧠 GenAI Resume Critique Bot")
st.markdown("Upload your resume to get LLM-powered feedback and optional JD match.")

uploaded_resume = st.file_uploader("📤 Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_text = st.text_area("📌 Paste Job Description (Optional)", height=200)

if uploaded_resume:
    with st.spinner("📄 Extracting and analyzing resume..."):
        resume_text = extract_text(uploaded_resume)
        parsed_data = parse_resume(resume_text)

    st.subheader("🗂️ Parsed Resume Info")
    st.json(parsed_data)

    with st.spinner("🧠 Getting LLM feedback..."):
        feedback = get_resume_feedback(resume_text)

    st.subheader("🧠 LLM Feedback")
    st.markdown(feedback)

    if jd_text.strip():
        with st.spinner("🔎 Matching resume to job description..."):
            match_score = match_resume_to_jd(resume_text, jd_text)

        st.subheader("📊 Resume–JD Match Score")
        st.success(f"✅ Similarity: **{match_score}%**")

        with st.spinner("🛠 Enhancing resume..."):
            enhanced_resume = enhance_resume(resume_text, jd_text)

        st.subheader("📄 Enhanced Resume Based on JD")
        st.markdown(enhanced_resume)

        st.download_button(
            label="📥 Download Enhanced Resume",
            data=enhanced_resume,
            file_name="enhanced_resume.txt",
            mime="text/plain"
        )
else:
    st.info("👆 Upload a resume file to get started.")
