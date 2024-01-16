import requests
from bs4 import BeautifulSoup
response = requests.get("https://en.wikipedia.org/wiki/Web_scraping", timeout=60)
bs = BeautifulSoup(response.text, "lxml")
print(bs.find("p").text)
