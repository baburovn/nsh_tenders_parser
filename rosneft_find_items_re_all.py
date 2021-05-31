import re
import urllib.request

rosnefttkp = "https://www.tektorg.ru/rosnefttkp/procedures/"
url_link = urllib.request.urlopen('https://www.tektorg.ru/procedures?q=petroleum+experts&lang=ru&sort=date&order=desc')
for line in url_link:
    url_link = line.decode().strip()
    if rosnefttkp in url_link:
        #index print(data_title_endpos,data_title_endpos)
        print(re.findall('data-title="(.*?)"', url_link))
        #print(url_link)

        #start_link = url_link.find("https:")
        #end_link = url_link.find('?la', start_link)
        print(re.findall('data-title="(.*?)"', url_link))
        print(url_link[start_link:end_link])
