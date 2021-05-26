import requests
from bs4 import BeautifulSoup

WEBSITE = "http://www.srikanthtechnologies.com"
resp = requests.get(WEBSITE)
bs = BeautifulSoup(resp.text, "html.parser")
table = bs.find(id="ctl00_ContentPlaceHolder1_GridView2")
rows = table.find_all("tr")

for row in rows[1:]:  # Second row onwards
    cols = row.find_all("td")
    link = WEBSITE + "/" + cols[0].find("a")['href']
    print(cols[0].text)
    print(link)
    print(cols[2].text)
    print(cols[1].text)
    print("-" * 80)
