#naver.py

from bs4 import BeautifulSoup
import requests


def wemep(URL):
    # URL = 'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=50000151'
    response = requests.get(URL)
    code = response.status_code
    html = response.text
    print(code)
    soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
    wemep_list = soup.select("#_search_list > div.search_list.basis > ul > li") #이 있으면 위에서 순차적으로 접근하지 않아도 됨. #이 고유한 것이기 때문에.
    laptop_list = []
    # print(wemep_list)
    for wemep in wemep_list:
        # print(wemep.select_one("div > div.item_img > img"))
        img = wemep.select_one("div > div.item_img > img").get('data-lazy-src') #list_lists > div > a:nth-child(1) > div > div.item_img > img
        name = wemep.select_one("div > div.item_img > img").get('alt') #list_lists > div > a:nth-child(2) > div > div.item_img > img
        price = wemep.select_one("div > div.item_cont > div.option_txt > div > div.price_info > strong > em").text
        number = wemep.select_one("div > div.item_cont > div.option_txt > div > div.price_info > span > span.num").text
        href = wemep.get('href')
        dic = {}
        dic["img"] = img
        dic["name"] = name
        dic["price"] = price + "원"
        dic["number"] = number.strip() + "개"
        dic["href"] = "http://" + href
        laptop_list.append(dic)
    return laptop_list


if __name__ == "__main__":          #이 안에서 자체적으로 실행할 경우
    URL = 'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=50000151'
    laptop_list = wemep(URL)
    import pprint as p
    p.pprint(laptop_list)