#09module_craw_call.py

import pkgs.gu_module_craw_ytn as ytn
import pprint as p

# news_list = pkgs.gu_module_craw_ytn.ytn_craw()

url_list = ["https://www.ytn.co.kr/photo/photo_list_011703.html",
"https://www.ytn.co.kr/photo/photo_list_011704.html",
"https://www.ytn.co.kr/photo/photo_list_011705.html"
]
cnt = 0
for url in url_list:
    news_list = ytn.ytn_craw(url)
    for news_dic in news_list:
        print(news_dic['title'])
        cnt = cnt + 1
print(cnt)

# 유명한 탬플릿: 타임리프, 부트스트랩
# p.pprint(news_list)

#html은 templates폴더
#image나 css나 script는 static폴더
