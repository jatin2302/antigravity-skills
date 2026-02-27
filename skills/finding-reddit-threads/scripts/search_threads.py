import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import time

# Minimal scraper for Reddit thread discovery
class RedditScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    def search_threads(self, keyword, limit=10):
        search_url = f"https://old.reddit.com/search/?q={keyword}&sort=relevance&t=all"
        threads = []
        try:
            resp = requests.get(search_url, headers=self.headers, timeout=10)
            if resp.status_code == 200:
                soup = BeautifulSoup(resp.text, 'html.parser')
                links = soup.find_all('a', {'class': 'search-title'})
                for link in links[:limit]:
                    url = link.get('href')
                    if url and "/comments/" in url:
                        if url.startswith('/'):
                            url = f"https://old.reddit.com{url}"
                        threads.append({
                            "title": link.text,
                            "url": url,
                            "id": url.split('/')[-3] if len(url.split('/')) > 3 else "unknown"
                        })
            else:
                print(f"Error: HTTP {resp.status_code}")
        except Exception as e:
            print(f"Exception: {e}")
        return threads

def main():
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    else:
        # Try to load from brand_profile.json if it exists in current dir
        if os.path.exists("brand_profile.json"):
            with open("brand_profile.json", "r") as f:
                profile = json.load(f)
                keyword = profile.get("keywords", ["marketing"])[0]
        else:
            print("Please provide a keyword or create brand_profile.json")
            sys.exit(1)

    scraper = RedditScraper()
    print(f"[*] Searching Reddit for: {keyword}")
    results = scraper.search_threads(keyword)
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    main()
