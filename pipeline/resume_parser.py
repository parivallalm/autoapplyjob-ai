import os
import pdfplumber
import sys
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
    if len(sys.argv) < 2:
        print("Usage: python resume_parser.py <resume_file_path>")
        sys.exit(1)

    resume_path = sys.argv[1]
    print(parse_resume(resume_path)[:1000])