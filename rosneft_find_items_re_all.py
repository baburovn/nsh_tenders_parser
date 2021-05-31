import re
import urllib.request
from urllib.parse import quote

#Вводим ссылки для парсинга. В строку после quote добавляем слово для поиска, пробелы заменяем +
url_link = urllib.request.urlopen('https://www.tektorg.ru/procedures?q=' +quote('сейсморазведка') + "&lang=ru&sort=date&order=desc'")
#Данная переменная требуется для поиска по строкам:
rosnefttkp = "https://www.tektorg.ru/rosnefttkp/procedures/"

for line in url_link:
    url_link = line.decode().strip()
    if rosnefttkp in url_link:
        #регулярное выражение для Названия тендера
        print(re.findall('data-title="(.*?)"', url_link))
        # регулярное выражение для ссылку на тендер и документацию
        print(re.findall('data-url="(.*?)"', url_link))
#далее сделаем запись в файл
