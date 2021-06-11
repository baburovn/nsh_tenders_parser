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
search_quote = "наклон"

#поиск по актуальным, завершенным и архивным:
url_link = urllib.request.urlopen('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote(search_quote) + "&FILTER[STATE]=ALL&LIMIT=20")

#поиск по актуальным:
#url_link = urllib.request.urlopen('https://zakupki.gazprom-neft.ru/tenderix/index.php?FILTER[SEARCH]=' +quote(search_quote) + "&LIMIT=20")



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
    purchases_link_list = []
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
    purchases_name_list = []
    #поиск названия закупки
    for i in purchases_page:
        purchases_desc = i.find("div", class_="purchase-desc").text.strip()
        if purchases_desc not in purchases_name_list:
            purchases_name_list.append(purchases_desc)
    return purchases_name_list

def purchases_time_start():

    #поиск даты начала закупки
    purchases_date_start = []

    for i in purchases_page:
        purchases_date = i.find("div", class_="date-title").find_next().text.strip()
        #регулярное выражение, которое выделяет дату
        purchases_date_start.extend(re.findall(r'\d{2}.\d{2}.\d{4}', purchases_date))
    return purchases_date_start

def purchases_time_end():

    #поиск даты начала закупки
    purchases_date_end = []

    for i in purchases_page:
        purchases_date = i.find("div", class_="purchase-end left_240").find_next().find_next().text.strip()
        purchases_date_end.append(purchases_date)
        #purchases_date_end = (re.findall(r'\d{2}.\d{2}.\d{4}', purchases_date))
    return purchases_date_end

# определяем сегодняшнюю дату и время:
today = datetime.today().strftime("%d_%m_%Y_%H_%M_%S")

# записывае вызовы функций в итоговый файл
with open(f"{search_quote} {today}.csv", "w", encoding='windows-1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(("Наименование закупки","Ссылка закупки","Начало приема предложений","Окончание приема предложений"))
    writer.writerows(zip(purchases_page_name(), purchases_number_foo(), purchases_time_start(), purchases_time_end()))
