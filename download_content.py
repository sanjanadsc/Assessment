
import requests
from time import sleep

def download_content(urls):
    results = []
    for url in urls:
        success = False
        for attempt in range(3):
            try:
                response = requests.get(url)
                response.raise_for_status()
                results.append(response.content)
                success = True
                break
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt+1} failed for URL {url}: {e}")
                sleep(1)  # Wait before retrying
        if not success:
            results.append(None)
    return results
