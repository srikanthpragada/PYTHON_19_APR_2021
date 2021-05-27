import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "http://www.srikanthtechnologies.com/rss.xml"
resp = requests.get(URL)
bs = BeautifulSoup(resp.text, "xml")

items = bs.find_all("item")
today = datetime.now()
for item in items:
    pubdate = item.find("pubDate").text[5:16]
    if '2021' in pubdate:
        title = item.find("title").text.strip()
        link = item.find("link").text.strip()
        pdate = datetime.strptime(pubdate, '%d %b %Y')
        days = (today - pdate).days
        print(title)
        print(link)
        print(f'{pdate.strftime("%d-%m-%Y")}  {days} old')
        print('-' * 80)

