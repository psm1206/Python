#melon_top50.py

from bs4 import BeautifulSoup
import requests
URL = 'https://www.melon.com/chart/'
response = requests.get(URL, headers={"User-Agent":"XY"})
code = response.status_code
html = response.text
print(code)

soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
melon_list = soup.select("tr#lst50") #이 있으면 위에서 순차적으로 접근하지 않아도 됨. #이 고유한 것이기 때문에.
song_list = []
for melon in melon_list:
    img = melon.select_one("div > a > img").get('src')
    title = melon.select_one("div > div > div.ellipsis.rank01 > span > a").text
    singer = melon.select_one("div > div > div.ellipsis.rank02 > a").text
    album = melon.select_one("td:nth-child(7) > div > div > div > a").text
    #div > a > img                                  .get('src')     사진
    #div > div > div.ellipsis.rank01 > span > a     .get('title')   제목
    #div > div > div.ellipsis.rank02 > a            .get('title')   가수
    #div > div > div > a                            .get('title)    앨범명
    dic = {}
    dic["img"] = img
    dic["title"] = title
    dic["singer"] = singer
    dic["album"] = album
    song_list.append(dic)

import pprint
pprint.pprint(song_list)
