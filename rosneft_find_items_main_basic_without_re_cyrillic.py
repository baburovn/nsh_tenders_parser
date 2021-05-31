
import urllib.request
from urllib.parse import quote


#Вводим URL для парсинга
rosnefttkp = "https://www.tektorg.ru/rosnefttkp/procedures/"
#Вводим ссылки для парсинга.
#fhand = urllib.request.urlopen('https://www.tektorg.ru/procedures?q=petroleum+experts&lang=ru&sort=date&order=desc')
#fhand_start = ('https://www.tektorg.ru/procedures?q=')
#вводим наш запрос на поиск, вместо пробелов ставим +:
#fhand_middle = ("сейсморазведка")
#fhand_end = ('&lang=ru&sort=date&order=desc')
#fhand = fhand_start + fhand_middle + fhand_end
fhand = urllib.request.urlopen('https://www.tektorg.ru/procedures?q=' +quote('сейсморазведка') + "&lang=ru&sort=date&order=desc'")

print(fhand)
for line in fhand:
    m = line.decode().strip()
    if rosnefttkp in m:
        #print(line.strip())
        start_link = m.find("https:")
        #end_link = m.find("?lang=ru")
        #end_link = m.find('"', start_link)
        end_link = m.find('?la', start_link)
        print(m[start_link:end_link])


        data_title_startpos = m.find('data-title=' + '\"' )
        data_title_endpos = m.find('"', data_title_startpos+12)
        print(data_title_endpos,data_title_endpos)
        print(m[data_title_startpos+12:data_title_endpos])
        #print(m)

