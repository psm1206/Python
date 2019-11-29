#10module_flask.py
from flask import Flask, render_template
import pkgs.gu_module_craw_ytn as ytn

app = Flask(__name__) #Flask가 실행하도록 이 파일을 넘겨라. 객체를 app에 할당

@app.route("/")
def index():
    # return "<h1>Hello World!</h1>"
    # return render_template('09html_test.html')
    # index.html 웹의 시작페이지
    url_list = [
        "https://www.ytn.co.kr/photo/photo_list_011703.html",
        "https://www.ytn.co.kr/photo/photo_list_011704.html",
        "https://www.ytn.co.kr/photo/photo_list_011705.html"
    ]
    for url in url_list:
        news_list = ytn.ytn_craw(url)
        # for news_dic in news_list:
        #     print(news_dic['title'])
    return render_template('index.html', NEW_LIST_KEY=news_list)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8888")
