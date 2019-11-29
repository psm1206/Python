# 1.
addr = []
addr = list()

# 2.
addr.append("서울시")

# 3.
for i in addr:
    print(i)

# 4.
dic = {"uid" : "kim"}

# 5.
for i in dic.items():
    print(i)

# 6.
dic["addr"] = "서울시"

# 7.
# 아래 조건을 만족하는 리스트 생성
# 1. 해당하는 리스트 안에 item은 4개
# 2. 4개 중에 하나는 리스트 안에 리스트
# 3. 4개 중에 dictionary item도 있어야 함.
# 출력

i_list = ["A", "B", "C", [{"D":"D1"}]]
for i in i_list:
    print(i)