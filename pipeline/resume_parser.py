import os
import pdfplumber
from docx import Document

def extract_text_from_pdf(filepath):
    text = ""
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text.strip()

def extract_text_from_docx(filepath):
    doc = Document(filepath)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text.strip()

def parse_resume(filepath):
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"{filepath} does not exist.")
    
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(filepath)
    elif ext == ".docx":
        return extract_text_from_docx(filepath)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")

# 🔍 Test
if __name__ == "__main__":
    test_file = "data/resumes/sample_resume.pdf"  # Change if needed
    print(parse_resume(test_file)[:1000])
