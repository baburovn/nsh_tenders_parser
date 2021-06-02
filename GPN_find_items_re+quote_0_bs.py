import re
import urllib.request
from urllib.parse import quote
from bs4 import BeautifulSoup
import ssl
import requests as req
import lxml


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#rosnefttkp = "https://www.tektorg.ru/rosnefttkp/procedures/"
#gazpromneft = "https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=petroleum&FILTER[STATE]=ALL&LIMIT=20"
url_link = urllib.request.urlopen('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote('моделирование') + "&FILTER[STATE]=ALL&LIMIT=20")
#url_link = req.get('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote('petroleum') + "&FILTER[STATE]=ALL&LIMIT=20")
soup = BeautifulSoup(url_link, "lxml")
print(soup)

#print(soup.find("div"))
#for i in soup:
#page_all_nazvanie = soup.find_all("div", class_="purchase-desc")
#page_all_nomer = soup.find_all("div", class_="purchase-number")
"""for i in page_all_nazvanie:
    print(i.text.strip())"""
#page_all_date_value = soup.find("div", class_="purchase-start").find("div", class_="date-value")
#print(page_all_date_value.text.strip())

#page_puchases_list = soup.find(class_ = "purchases-list").find(class_ = "purchase-desc").text.strip()
#print(page_puchases_list)
page_purchases_list_all = soup.find(class_ = "purchases-list").find_next().find_next().find_next().find_next().find_next().get("href")
print(page_purchases_list_all)
"""for items in page_purchases_list_all:
    item_url = items.get("href")
    print(item_url)"""
#print((page_puchases_list_all))
#for link in soup.find_all(class_ = "purchase-number"):




#page_all_date_title = soup.find_all("div", class_="date-title")
"""for i in page_all_date_title:
    print(i.text)"""
#print(soup.find("ul", id="mylist"))
# Retrieve all of the anchor tags

"""for line in url_link:
    url_link = line.decode().strip()
    print(url_link)
    #if ('<div class="purchase-desc">') in url_link:
        #print(re.findall('<div class="purchase-desc">', url_link))
        #print(re.findall(r'<div[^>]*>([^<]+)</div>', url_link))
        #print(url_link)"""
