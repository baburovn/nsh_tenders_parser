import re
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import ssl
import requests as req
import lxml
import html5lib

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#gazpromneft = "https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=petroleum&FILTER[STATE]=ALL&LIMIT=20"
url_link = urllib.request.urlopen('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote('сейсмораз') + "&FILTER[STATE]=ALL&LIMIT=20")

soup = BeautifulSoup(url_link, "html5lib")

#Получилось достать таки ссылки. прекрасно.
"""page_purchases_list_all = soup.find_all(class_="purchase-number")
list_link = []
for i in page_purchases_list_all:
    #print(i.find("a").get("href"))
    k = i.find("a").get("href")
    if k not in list_link:
        list_link.append(k)
print(list_link)
for i in list_link:
    pp = "https://zakupki.gazprom-neft.ru" + i
    print(pp)
print(len(list_link))

page_purchases_list_all2 = soup.find_all(class_="purchase-desc")
list_link = []
for i in page_purchases_list_all2:
    #print(i.find("a").get("href"))
    k = i.text
    k = k.strip()
    if k not in list_link:
        list_link.append(k)
print(list_link)
print(len(list_link))
"""
def purchases_number_foo():
    purchases_time = soup.find_all(class_="purchase ~purchase-popup")
    #print(purchases_time)
    purchases_time_number_list =[]
    for i in purchases_time:

        purchases_number = i.find("div", class_="purchase-number").find("a").get("href")
        #purchases_time_var = i.find("div", class_="date-value")
        #if purchases_time_var not in purchases_time_list:
        if purchases_number not in purchases_time_number_list:
            purchases_time_number_list.append(purchases_number)
    #проверяем элементы, вошедшие в список:
    #for k in purchases_time_number_list:
        #print("https://zakupki.gazprom-neft.ru"+k)
    return print(purchases_time_number_list)

purchases_number_foo()
