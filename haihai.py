import requests
from bs4 import BeautifulSoup

list_news = []
r = requests.get("https://news.mail.ru/")
soup = BeautifulSoup(r.text, 'html.parser')
mydivs = soup.find_all("a", {"class": "newsitem__title link-holder"})
for news in mydivs:
    newdict = {}
    newdict["link"] = news.get("href")
    newdict["title"] = news.span.get("class")
    print(newdict["link"])