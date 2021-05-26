import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
links = bs.find_all("a")

for link in links:
    href = link['href']
    if not href.startswith("javascript"):
        if href.startswith("/"):
            print(WEBSITE + href)
        elif not href.startswith("http"):
            print(WEBSITE + "/" + href)
        else:
            print(href)
