#module_selenium_test.py
from selenium import webdriver
from bs4 import BeautifulSoup
#driver = webdriver.Chrome("c:\...chromedriver.exe") 하드코딩
#크롬 브라우저를 사용해 구글에 접속하고
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.google.com")
# <input class="gLFyf gsfi" maxlength="2048" name="q" type="text" jsaction="paste:puy29d" aria-autocomplete="both"
# aria-haspopup="false" autocapitalize="off" autocomplete="off" autocorrect="off" role="combobox" spellcheck="false"
# title="검색" value="아무개" aria-label="검색" data-ved="0ahUKEwi12sPJ0rHkAhWPv5QKHdFmCGYQ39UDCAk">
search_box = driver.find_element_by_name("q") #검색창이라 하겠다.
#//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[1]/input Xpath: 하드코딩이라는 단점이 있지만 최상위 디렉토리부터 최하위 디렉토리까지 보여줌.
search_box.send_keys("파이썬") #검색창에 파이썬을 검색하라
search_box.submit() #전송 날려라~

# <input type="text" id="_searchKeyword"
# name="search_keyword" autocomplete="off" class="ui_input_text"
# size="5" title="검색어 입력" maxlength="50" value="[위메프데이] 랩턴 오늘 하루만 30% 대박 쿠폰할인">
def wemake(prm_search_str):
    driver.get("https://front.wemakeprice.com/category/division/2100132")
    search_box = driver.find_element_by_name("search_keyword")
    search_box.send_keys(prm_search_str)
    # < button type = "button" id = "_searchKeywordBtn" > 검색 < / button >
    search_button = driver.find_element_by_id("_searchKeywordBtn")
    search_button.click()
    search_box.submit()

    # response = requests.get(URL)
    # html_text = response.text
    html_text = driver.page_source #위와 같은 결과 // 페이지 소스 보기 클릭하면 보이는 코드
if __name__ == "__main__":
    import pprint as p
    p.pprint(wemake("삼성"))
    # wemake("LG")


