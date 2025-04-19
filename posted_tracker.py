import os
import json

# 永続ストレージのパス
POSTED_URLS_PATH = "/mnt/data/posted_urls.json"

def load_posted_urls():
    if not os.path.exists(POSTED_URLS_PATH):
        return []

    with open(POSTED_URLS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_posted_url(url):
    urls = load_posted_urls()
    urls.append(url)

    with open(POSTED_URLS_PATH, "w", encoding="utf-8") as f:
        json.dump(urls, f, indent=2, ensure_ascii=False)
