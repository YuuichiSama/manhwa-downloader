import requests

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin, quote, quote_plus


page = requests.get(
    url='https://toonily.com/webtoon/forest-of-the-fireflies/chapter-58/'
)

bs = BeautifulSoup(page.content, "html.parser")

container = bs.find("div", {"class": "reading-content"})
images = container.find_all("img")
images_url = [quote(img.get('data-src').strip(), safe=':/%') for img in images]

print(images_url)