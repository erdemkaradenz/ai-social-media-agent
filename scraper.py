import requests
from bs4 import BeautifulSoup

def scrape_url(url: str):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        

        if response.status_code != 200:
            return f"Error: Site {response.status_code} kodu döndürdü."

        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else ""

        text = " ".join([p.text for p in soup.find_all('p')])
        
        if not text:
            return "Error: Sayfadan metin çekilemedi."

        return f"Title: {title}\nContent: {text[:2500]}"
    except Exception as e:
        return f"Error scraping: {str(e)}"