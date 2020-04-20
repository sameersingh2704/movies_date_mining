import requests
from bs4 import BeautifulSoup

raw=requests.get("https://en.wikipedia.org/wiki/Lists_of_films")
raw_data= raw.text
# print(raw_data)
soup=BeautifulSoup(raw_data,"html.parser")
ddt=soup.find_all('dd')
for dd in ddt:
    dlt=soup.find_all('dt')
    for dt in dlt:
        print(dt.string)
    