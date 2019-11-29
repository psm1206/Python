#module_shop_flask.py
from flask import Flask, render_template
import shop.wemep as wm
import shop.elevenst as st11
# from shop import wemep #wemep()
app = Flask(__name__) #Flask가 실행하도록 이 파일을 넘겨라. 객체를 app에 할당

@app.route("/<search_str>")
def index(search_str):
    # URL = 'https://front.wemakeprice.com/category/division/2100132'
    wm_data_list = wm.wemep(search_str)
    st_data_list = st11.elevenst()
    return render_template('index.html', WEMAKE_LIST_KEY = wm_data_list, ST_LIST_KEY = st_data_list)

# @app.route("/st_app_route_url")
# def index():
#     data_list = st11.elevenst()
#     return render_template('index.html', ST11_LIST_KEY = data_list)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8899")
