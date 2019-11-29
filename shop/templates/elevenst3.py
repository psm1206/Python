from bs4 import BeautifulSoup
import requests
#thisClick_2442798175 > div > div.photo_wrap > a > img

def elevenst(URL):
    response = requests.get(URL)
    code = response.status_code
    html = response.text
    print(code)
    soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
    elevenst_list = soup.select("#hotItem > div.viewtype > ul > li") #이 있으면 위에서 순차적으로 접근하지 않아도 됨. #이 고유한 것이기 때문에.
    laptop_list = []

    for elevenst in elevenst_list:
        img = elevenst.select_one("div > a > img").get('src') #thisClick_2442798175 > div > div.photo_wrap > a > img
        name = elevenst.select_one("div > a ").get('data-long-body') #thisClick_2442798175 > div > div.list_info > p.info_tit > a
        price = elevenst.select_one("div > a > div > div > span > strong").text #thisClick_2442798175 > div > div.list_price > div.price_box > span.price_detail > strong .text


        dic = {}
        dic["img"] = img
        dic["name"] = name
        dic["price"] = price + "원"
        laptop_list.append(dic)
    return laptop_list

if __name__ == "__main__":          #이 안에서 자체적으로 실행할 경우
    URL = 'http://www.11st.co.kr/html/category/1001439.html'
    laptop_list = elevenst(URL)
    import pprint as p
    p.pprint(laptop_list)