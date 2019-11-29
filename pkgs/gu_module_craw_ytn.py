#09module_craw.py

#beautifulsoup은 html 태그 정보를 가져오는 패키지


from bs4 import BeautifulSoup
import requests

def ytn_craw(URL):
    # URL = 'https://www.ytn.co.kr/photo/photo_list_011705.html'
    response = requests.get(URL)
    code = response.status_code
    # 정상적으로 가져오면 200, 가져오려고 접속하다 문제 300, 접속했는데 안에 뭔가가 없으면 400, 뭔가가 있는데 내 쪽에 문제가 있으면 500번 대
    html = response.text
    # print(code, html)
    #-----response를 통해 html 갖고 옴-----
    #ytn_list_v2014
    # div#ytn_list_v2014 > dl.photo_list
    #id는 pk같은 것. class는 여러 개 나올 수 있음.
    #id는 #으로 접근하고 class는 .으로 접근함.
    #크롬에서 F12누르고 원하는 부분 copy selector함.
    soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
    dl_list = soup.select("div#ytn_list_v2014 > dl.photo_list")
    news_list = []
    for dl in dl_list:
        img = dl.select_one("dd.vertical > p > a > img").get('src')
        title = dl.select_one("dt > a").text
        href = dl.select_one("dt > a").get('href')
        content = dl.select_one("dd.text > a").text
        regdate = dl.select_one("dd.date").text
        #dd.vertical > p > a > img  .get('src')     사진
        #dt > a                     .text           제목
        #dt > a                     .get('href')    상세페이지주소
        #dd.text > a                .text           내용
        #dd.date                    .text           날짜
        dic = {}
        dic["img"] = img
        dic["title"] = title
        dic["href"] = "http://www.ytn.co.kr" + href
        dic["content"] = content
        dic["regdate"] = regdate
        news_list.append(dic)

# import pprint           #pretty print : print 와는 다르게 좀 더 예쁘게 출력해줌.
# pprint.pprint(news_list)
    return news_list

if __name__ == "__main__":          #이 안에서 자체적으로 실행할 경우
    URL = 'https://www.ytn.co.kr/photo/photo_list_011705.html'
    news_list = ytn_craw(URL)
    import pprint as p
    p.pprint(news_list)
