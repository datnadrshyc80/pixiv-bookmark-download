import os
import feedparser
import requests
import time
from bs4 import BeautifulSoup

# RSS feed URL
RSS_URL = 'https://rsshub.app/pixiv/user/bookmarks/'

# Download directory
DOWNLOAD_DIR = 'downloaded_images'

# File for storing downloaded image URLs
DOWNLOADED_FILE = 'downloaded_images.txt'


def download_image(url):
    while True:
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()  # This will raise a HTTPError if the status is 4xx or 5xx
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {url}: {e}")
            print("Waiting 10 seconds before retrying...")
            time.sleep(10)
            continue

        if response.headers['Content-Type'].startswith('image/'):
            filename = os.path.join(DOWNLOAD_DIR, url.split("/")[-1])
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f'Downloaded {url}')
            break
        else:
            print(f"URL {url} does not appear to be an image. Skipping.")
            break


def main():
    # Ensure download directory exists
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    # Load already downloaded images
    if os.path.exists(DOWNLOADED_FILE):
        with open(DOWNLOADED_FILE, 'r') as f:
            downloaded_images = f.read().splitlines()
    else:
        downloaded_images = []

    # Parse the RSS feed
    feed = feedparser.parse(RSS_URL)

    # Loop over each entry in the feed
    for entry in feed.entries:
        # Use BeautifulSoup to find image URLs
        soup = BeautifulSoup(entry.description, 'html.parser')
        img_tags = soup.find_all('img')

        for img in img_tags:
            url = img.get('src')
            if url.endswith('.png') or url.endswith('.jpg'):
                if url not in downloaded_images:
                    download_image(url)
                    downloaded_images.append(url)
                    with open(DOWNLOADED_FILE, 'a') as f:
                        f.write(url + '\n')


if __name__ == "__main__":
    main()
