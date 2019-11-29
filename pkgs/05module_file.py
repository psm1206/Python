#05module_file.py
# open("test", "w")
# f = open("test", "r")
# line = f.readline() # 'a\n'
# line = f.readlines() # ['a\n', 'bb\n', 'ccc\n', 'dddd\n']
# line = f.read() # 우리 눈에 보이는 모양 그대로 갖고 옴.
# print(line)
#
# f = open("test", "a")
# f.write("\nzzzz11")
# f.write("\nzzzz22")
# f.close()

with open("test", "r") as f:

    print(type(f.readline()))

with open("test", "r", encoding="UTF-8") as f:
    for line in f.readlines():
        line = line.strip() # line의 앞뒤공백제거
        #line = line.replace(" ","") # 중간공백제거
        line = line.replace("\n", "") # 3번째 parameter는 앞에서부터 몇 개를 바꿀지라는 count!
        #print(line)
        if line == '"user": {':
            print("Find user!")
            #parsing(파싱) : 문장에서 필요한 값만 뽑아내는 것
#
# string --> dictionary
# package : json    dumps()/loads()

# for k in instagram_json["data"]:
#   print(k["user"]["username"])

# CRLF
# \r : 해당 문장의 끝을 나타냄.
# \n : 줄 바꿈.

a = {"uid":"kim"}

import json
with open("test", "r", encoding="UTF-8") as f:
    str = f.read()
    dic = json.loads(str)
    # str -> dict 타입 변환
    # 홑따옴표는 error! 습관적으로 JSON 표기 상의 key는 양따옴표 사용해서 묶자!
    # 다른 언어는 string일 때 양따옴표만 사용가능
    print(dic["data"][0]["user"]["username"])
    print(dic["meta"]["code"])

test_dic = {"location": "null",\
              "filter": "Normal",\
              "created_time": "1440501087"}
print(test_dic, type(test_dic))
test_str = json.dumps(test_dic)
# dict -> str 타입 변환
print(test_str, type(test_str))


