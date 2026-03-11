import requests
from bs4 import BeautifulSoup
import os

def download_images_from_webpage(url):
    """ Download images from webpage. """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    
    if not os.path.exists('images'):
        os.makedirs('images')
    
    for img in img_tags:
        img_url = img.get('src')
        if not img_url:
            continue
        img_name = os.path.join('images', os.path.basename(img_url))
        if not img_name:
            continue
        img_data = requests.get(img_url).content
        with open(img_name, 'wb') as handler:
            handler.write(img_data)

download_images_from_webpage('https://example.com')