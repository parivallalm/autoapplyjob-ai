import requests
from bs4 import BeautifulSoup

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

# Test run
if __name__ == "__main__":
    test_url = "https://example.com/sample-job-description"
    jd_text = extract_job_description(test_url)
    print(jd_text[:1000])
