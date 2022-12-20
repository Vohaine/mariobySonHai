import requests
from requests import Response

r: Response = requests.get("https://news.mail.ru/")
 print(r.text)