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
search_quote = "petroleum"

#поиск по актуальным, завершенным и архивным:
#url_link = urllib.request.urlopen('https://www.tektorg.ru/procedures?lang=ru&q='+ quote(search_quote) + "&sort=datestart")
url_link_file = "url_link_file"

with open("tektorg.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, "html5lib")
    #print(soup)
#soup = BeautifulSoup(url_link, "html5lib")


def purchases_page_link():
    purchases_page_link_lst = []
    count = 0
    purchases_page = soup.find_all(class_="section-procurement__item-title")
    for a in purchases_page:
        purchases_page_link_lst.append("https://www.tektorg.ru/" + a.get("href"))
        count += 1
    #print("количество ссылок на тендера", count)
    return purchases_page_link_lst

def purchases_page_date():
    purchases_page_date_lst = []
    count = 0
    purchases_page = soup.find_all(class_="section-procurement__item-date")
    for a in purchases_page:
        purch_date = a.find_next()
        print(purch_date)
        count += 1
    print(count)
    #print("количество ссылок на тендера", count)
    #return purchases_page_link_lst

def purchases_page_date2():
    count = 0
    # в section-procurement__item находятся 4 одинаковых тега div с нужными нам параметрами: дата начала подачи, дата окончания подачи"
    purchases_page = soup.find_all(class_="section-procurement__item")
    for i in purchases_page:
        #находим div с датой начала приема предложений
        #purchases_date = i.find(class_="section-procurement__item-date").find_next().b.next_sibling.strip()
        #находим div с датой окончания приема предложений
        #purchases_date = i.find(class_="section-procurement__item-date").find_next().next_sibling.next_sibling.b.next_sibling.strip()
        print(purchases_date)
        count += 1


    print(count)

purchases_page_date2()


def purchases_page_name():
    purchases_page_name_lst = []
    count = 0
    purchases_page = soup.find_all(class_="section-procurement__item-title")
    for a in purchases_page:
        purchases_page_name_lst.append(a.text.strip())
        count += 1
    #print("количество названий тендеров", count)
    return purchases_page_name_lst
#print(len(purchases_page_name()))
#purchases_page_link()

today = datetime.today().strftime("%d_%m_%Y_%H_%M_%S")
# записывае вызовы функций в итоговый файл
with open(f"{search_quote} {today}.csv", "w", encoding='windows-1251', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(("Наименование закупки","Ссылка закупки"))
    writer.writerows(zip(purchases_page_name(), purchases_page_link()))
