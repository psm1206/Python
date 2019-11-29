#11module_pandas.py

import sqlite3
import os

def common_dbconn() :
    # DB 목록가져오기
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # C:\kosa\workspace_python\venv\mysite
    db_path = os.path.join(BASE_DIR, 'db.sqlite3')
    BASE_DIR + "\db.sqlite3"
    print(db_path, "===============================")
    conn = sqlite3.connect(db_path)
    return conn

import pandas
mon = [3, 7, 9]
data = {"kor":[100, 90, 80], "math":[44 , 33, 55]}
df = pandas.DataFrame(data, index=mon) #index=None, columns=None
print(df)

conn = common_dbconn()
df.to_sql("pandas_score", conn, if_exists="replace") # sql로 보내기
# if_exist 이미 같은 table이 있으면 이미 존재한다고 error
# replace를 적으면 덮어씀

print(df.dtypes)

rows = pandas.read_sql("select * from pandas_score", conn)
print(rows)

#---------------matplotlib----------------
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (6, 4)
plt.rcParams["axes.grid"] = True
df.plot()
plt.show()
# plt.imsave("aa.png")