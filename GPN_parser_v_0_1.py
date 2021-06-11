import re
import urllib.request
from datetime import datetime
from urllib.parse import quote
from bs4 import BeautifulSoup
import ssl
import requests as req
import lxml
import html5lib
import csv

#вводим запрос на поиск по ключевым словам
search_quote = "цифров"

#gazpromneft = "https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=petroleum&FILTER[STATE]=ALL&LIMIT=20"
url_link = urllib.request.urlopen('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote(search_quote) + "&FILTER[STATE]=ALL&LIMIT=20")
#url_link = "https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=petroleum&FILTER[STATE]=ALL&LIMIT=20"

purchases_name_list = []
purchases_link_list = []
purchases_date_start = []
purchases_date_end = []
soup = BeautifulSoup(url_link, "html5lib")

"""
#на случай, если мы хотим сначала записывать страницу в файл и считывать данные с него.
with open("index1.html", "w", encoding='utf-8') as file:
    file.write(str(soup))"""

def purchases_number_foo():

    #поиск ссылки на закупку
    head_div = soup.find_all(class_="purchase ~purchase-popup")
    #создаем список, в котором будут хранится ссылки на закупки:
    purchases_number_list =[]
    #парсим нужные ссылки:
    for i in head_div:
        purchases_number = i.find("div", class_="purchase-number").find("a").get("href")
        if purchases_number not in purchases_number_list:
            purchases_number_list.append(purchases_number)
    #print(purchases_name_list)
    #проверяем элементы, вошедшие в список:
    for k in purchases_number_list:
       purchases_link_list.append("https://zakupki.gazprom-neft.ru"+k)
    return purchases_link_list

purchases_page = soup.find_all(class_="purchase ~purchase-popup")

def purchases_page_name():

    #поиск названия закупки
    for i in purchases_page:
        purchases_desc = i.find("div", class_="purchase-desc").text.strip()
        if purchases_desc not in purchases_name_list:
            purchases_name_list.append(purchases_desc)
    return purchases_name_list

def purchases_time_start():

    #поиск даты начала закупки
    for i in purchases_page:
        purchases_date = i.find("div", class_="date-title").find_next().text.strip()
        # if i.find("div", class_="date-title").text ==  "Начало приёма":
        #регулярное выражение, которое выделяет вфа
        purchases_date_start.extend(re.findall(r'\d{2}.\d{2}.\d{4}', purchases_date))
    return purchases_date_start

def purchases_time_end():
    #поиск даты начала закупки
    for i in purchases_page:
        purchases_date = i.find("div", class_="purchase-end left_240").find_next().find_next().text.strip()
        purchases_date_end.append(purchases_date)
        #purchases_date_end = (re.findall(r'\d{2}.\d{2}.\d{4}', purchases_date))
    return purchases_date_end


purchase_n = "Наименование закупки"
purchase_l = "Ссылка закупки"
purchase_d_s = "Начало приема предложений"
purchase_d_e = "Окончание приема предложений"

purchase_name = purchases_page_name()
purchase_link = purchases_number_foo()
purchase_time_s = purchases_time_start()
purchase_time_e = purchases_time_end()

today = datetime.today().strftime("%d_%m_%Y_%H_%M_%S")

with open(f"{search_quote} {today}.csv", "w", encoding='windows-1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow((purchase_n,purchase_l,purchase_d_s,purchase_d_e))
    writer.writerows(zip(purchase_name, purchase_link, purchase_time_s, purchase_time_e))
