#пример, без использования regular expressions. Находим нужную нам строку с названием закупки, слайсим по индексу. 
import urllib.request
from urllib.parse import quote


#Вводим URL для парсинга
rosnefttkp = "https://www.tektorg.ru/rosnefttkp/procedures/"
#Вводим ссылки для парсинга. В строку после quote добавляем слово для поиска, пробелы заменяем +
fhand = urllib.request.urlopen('https://www.tektorg.ru/procedures?q=' +quote('сейсморазведка') + "&lang=ru&sort=date&order=desc'")

print(fhand)
for line in fhand:
    m = line.decode().strip()
    if rosnefttkp in m:
        start_link = m.find("https:")
        end_link = m.find('?la', start_link)
        print(m[start_link:end_link])


        data_title_startpos = m.find('data-title=' + '\"' )
        data_title_endpos = m.find('"', data_title_startpos+12)
        print(data_title_endpos,data_title_endpos)
        print(m[data_title_startpos+12:data_title_endpos])
        #print(m)

