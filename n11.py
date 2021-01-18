import requests
from bs4 import BeautifulSoup


url = "https://www.n11.com/bilgisayar/dizustu-bilgisayar"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

productObject = {}
productList = soup.find_all("li", {"class": "column"}, limit=10)

for li in productList:
    name = li.h3.text.strip()
    link = li.div.a.get("href")
    price = li.find("div", {"class": "proDetail"}).find("ins").text.strip().strip('TL') 

    print('----------- PRODUCT -----------\n')
    print "NAME --> " + name
    print "URL --> " + link
    print "PRICE --> " + price
    print('---------------------------------\n')


