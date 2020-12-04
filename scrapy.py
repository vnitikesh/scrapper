import requests
import logging
from bs4 import BeautifulSoup

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

URL = "https://b2b.unitexint.com/COLLECTIONS/pl.php?resetbrand=1.php?resetbrand=1"
lst1 = []
lst2 = []
lst3 = []
r = requests.get(URL, headers)
soup = BeautifulSoup(r.content, 'html.parser')
#print(soup.prettify)
for link in soup.find_all('div', {'class':'col-lg-3 col-md-4 col-sm-4'}):
    lst1.append(link.get_text().strip("\n"))


print(lst1)
'''
for i in lst1:
    a = "https://b2b.unitextint.com/COLLECTIONS/" + i + "/pl.php"
    req = requests.get(a, headers)
    sop = BeautifulSoup(req.content, 'html.parser')
    for b in sop.find_all("div", {"class": "displaypadding col-md-8"}):
        lst2.append(b.get_text().strip("\n"))
print(lst2)
'''
