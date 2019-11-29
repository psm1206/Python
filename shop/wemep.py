from bs4 import BeautifulSoup
import requests


def wemep(prm_search_str):
    print("###########", prm_search_str)
    # selenium...
    # driver.get("https://front.wemakeprice.com/category/division/2100132")
    # search_box = driver.find_element_by_id("_searchKeyword")
    # search_box.send_keys(prm_search_str)
    # # < button type = "button" id = "_searchKeywordBtn" > 검색 < / button >
    # search_button = driver.find_element_by_id("_searchKeywordBtn")
    # search_button.click()
    # search_box.submit()
    URL = 'https://front.wemakeprice.com/category/division/2100132'
    response = requests.get(URL)
    code = response.status_code
    html = response.text
    # print(code)
    soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
    wemep_list = soup.select("#list_lists > div > a") #이 있으면 위에서 순차적으로 접근하지 않아도 됨. #이 고유한 것이기 때문에.
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
    URL = 'https://front.wemakeprice.com/category/division/2100132'
    laptop_list = wemep(URL)
    import pprint as p
    p.pprint(laptop_list)