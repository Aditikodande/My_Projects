import re
import fitz  # PyMuPDF
from docx import Document

def extract_text(file):
    if file.type == "application/pdf":
        return extract_pdf(file)
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_docx(file)
    return "Unsupported format."

def extract_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def extract_docx(uploaded_file):
    doc = Document(uploaded_file)
    return "\n".join([p.text for p in doc.paragraphs])

def parse_resume(text):
    email = re.findall(r"[a-zA-Z0-9.\-+_]+@[a-zA-Z0-9.\-+_]+\.[a-zA-Z]+", text)
    phone = re.findall(r"\+?\d[\d\-()\s]{8,}\d", text)
    
    common_skills = ['python', 'java', 'sql', 'excel', 'machine learning', 'data analysis', 'aws', 'tensorflow']
    skills = [skill for skill in common_skills if skill.lower() in text.lower()]
    
    education = re.findall(r"(Bachelor|Master|B\.Tech|M\.Tech|Ph\.D|BSc|MSc|B\.E|M\.E)[^\n]*", text, re.IGNORECASE)
    name = text.strip().split("\n")[0]

    return {
        "Name": name,
        "Email": email[0] if email else "Not found",
        "Phone": phone[0] if phone else "Not found",
        "Skills": skills,
        "Education": education
    }
