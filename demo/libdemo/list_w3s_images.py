
import requests
from bs4 import BeautifulSoup

resp = requests.get("https://www.w3schools.com")
bs = BeautifulSoup(resp.text, "html.parser")
images = bs.find_all("img")

for img in images:
    print(img['src'])