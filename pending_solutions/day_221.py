"""
Create URL downloader.
"""

import requests

def download_url(url, file_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
    else:
        print(f"Failed to download URL: {url}")

# Example usage
download_url('https://example.com', 'downloaded_example.html')