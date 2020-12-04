import requests
import logging
from bs4 import BeautifulSoup
from scrapy import lst1
import xlwt
from xlwt import Workbook

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
lst2 = []
j = 0
k = 0
l = 0
for i in lst1[1:len(lst1)]:
    url = "https://b2b.unitexint.com/COLLECTIONS/"+ i +"/pl.php"
    req = requests.get(url, headers)
    k += 1
    soup = BeautifulSoup(req.content, 'html.parser')
    sheet1.write(k,1,i)
    for link in soup.find_all('h2', {'class':'productListTitle'}):
        j += 1
        sheet1.write(j,2, link.get_text().strip("\n"))
        lst2.append(link.get_text().strip("\n"))
    for link2 in soup.find_all('select', {'name':'productcode'}):
        l += 1
        sheet1.write(l,3,link2.get_text().strip("\n"))

wb.save('xlwt_example2.xls')
#print(lst2)
