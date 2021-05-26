import requests
from bs4 import BeautifulSoup

WEBSITE = "https://www.w3schools.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
links = bs.find_all("a")

for link in links:
    href = link['href']
    if not href.startswith("javascript"):
        if href.startswith("/"):
            print(WEBSITE + href)
        else:
            print(href)
