import sys
import requests
from bs4 import BeautifulSoup
import os

def extract_job_description(url: str) -> str:
    """
    Extract plain text job description from a given URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        return f"[ERROR] Could not fetch URL: {e}"

    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find('main') or soup
    paragraphs = main_content.find_all(['p', 'li'])

    text = "\n".join([p.get_text(strip=True) for p in paragraphs])
    return text.strip()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python jd_parser.py <job_description_url>")
        sys.exit(1)

    url = sys.argv[1]
    jd_text = extract_job_description(url)

    if jd_text.startswith("[ERROR]"):
        print(jd_text)
    else:
        os.makedirs("data/job_descriptions", exist_ok=True)
        with open("data/job_descriptions/sample_jd.txt", "w", encoding="utf-8") as f:
            f.write(jd_text)
        print("Job description saved to: data/job_descriptions/sample_jd.txt")
