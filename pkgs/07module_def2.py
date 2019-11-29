#07_module_def2.py

#함수이름 : add_hp
#파라미터 : name, tel
#결과리턴 : True / False

list_hp = []
sequence = 0

def add_hp(**user_info):
    global sequence         #전역변수설정: sequence가 def 안과 밖에서 따로 놈.
    sequence = sequence + 1 #sequence
    # print(user_info)
    user_info["seq"] = sequence
    list_hp.append(user_info)
    # print(len(list_hp))
    return True

#-------------------------------------------------

res = add_hp(name="홍길동", tel="111", office ="444")
# if res == True:
if res:
    print("저장되었습니다.")
else:
    print("다시 저장해주세요.")
print(list_hp)
print("--------------------------------------")
def print_hp():
    for dic_hp in list_hp:
        # print(list_hp[0].items()) # test = [{}, {}, {}, {}] 이런 형태에서 test[0]을 뽑아오면 dictionary!
        # print(hp["name"], hp["tel"])
        for k, v in dic_hp.items():
            print(dic_hp[k], end="\t")
        print()
res = add_hp(name="아무개", tel="222", office ="555")
print_hp()

list_hp[1]["tel"] = "5555"

#함수이름 : update_hp
#파라미터 : seq, key, value
#결과리턴 : True / False

def update_hp(seq, key, value):
    res = False
    if seq > len(list_hp):
        print("없는 번호입니당")
    else:
        list_hp[seq-1][key] = value
        res = True
    return True

update_hp(1, "name", "홍")
print_hp()

#어떤 회원의 이름은 뭐로 바꾸고 번호는 뭐로 바꿔줘.

def updateall_hp(seq, **all):       # **all <- (name="홍길동", tel="111", office="444", seq=1)
    for i in range(len(list_hp)):   # {"name":"홍길동", "tel":"111", "office":"444", "seq":1}
        if list_hp[i]["seq"] == seq:
            if "name" in list_hp[i].keys():
                list_hp[i]["name"] = all["name"]
            if "office" in list_hp[i].keys():
                list_hp[i]["office"] = all["office"]
            if "tel" in list_hp[i].keys():
                list_hp[i]["tel"] = all["tel"]


print(list_hp)
res = updateall_hp(2, office="1453", tel="0101", name="박")
print(list_hp)

def test(a, *b, **c):
    print(a)
    print(b)
    print(c)

test(1, 2, 3, 4, k1="v1", k2="v2") # 1 (2, 3, 4) {'k1': 'v1', 'k2': 'v2'}

def add_hp(a):
    return True

print(add_hp("name"))








