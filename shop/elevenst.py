from bs4 import BeautifulSoup
import requests
#thisClick_2442798175 > div > div.photo_wrap > a > img

def elevenst():
    URL = 'http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&dispCtgrNo=1001439'
    response = requests.get(URL)
    code = response.status_code
    html = response.text
    print(code)
    soup = BeautifulSoup(html, 'html.parser') #사용할 parser종류/ python 내장 parser인 html.parser
    elevenst_list = soup.select("#bestPrdList > ul > li > div.product_conts") #이 있으면 위에서 순차적으로 접근하지 않아도 됨. #이 고유한 것이기 때문에.
    laptop_list = []

    for elevenst in elevenst_list:
        img = elevenst.select_one("div.pub_photo > a > span > img").get('src')
        name = elevenst.select_one("div.pup_info > div.pup_title > a").text
        price = elevenst.select_one("div.pup_info > div.pub_priceW > s").text #thisClick_2442798175 > div > div.list_price > div.price_box > span.price_detail > strong .text
        company = elevenst.select_one("div.pup_info > div.seller_id > a").get('title') #thisClick_2442798175 > div > div.list_benefit > p.benefit_tit > a .text
        href = elevenst.select_one("div.pub_photo > a").get('href')

        dic = {}
        dic["img"] = img
        dic["name"] = name
        dic["price"] = price
        dic["company"] = company
        dic["href"] = href
        laptop_list.append(dic)
    return laptop_list

if __name__ == "__main__":          #이 안에서 자체적으로 실행할 경우
    URL = 'http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&dispCtgrNo=1001439'
    laptop_list = elevenst()
    import pprint as p
    p.pprint(laptop_list)