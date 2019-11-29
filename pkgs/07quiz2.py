# 07module_def_quiz.py
# 수정중이라 조금 이상합니당

# ---------------------------------------
# 총합 계산
# 함수이름: num_sum
# 파라미터: *args
# 결과리턴: 합
# ---------------------------------------
def num_sum1(*args):
    return sum(args)


print(num_sum1(1, 2, 3, 4, 5, 6))


# ---------------------------------------
# 총합 계산
# 함수이름: num_sum
# 파라미터: start, end
# 결과리턴: 합
# ---------------------------------------
def num_sum2(start, end):
    return sum(range(start, end + 1))


print(num_sum2(1, 6))
# ---------------------------------------
# 업체정보 등록
# 함수이름: add_company
# 파라미터: **kwargs  (key는 com_seq,com_name)
# 결과리턴: True/False
# ---------------------------------------
com_list = []


def add_company(**kwargs):
    com_list.append(kwargs)
    return True


add_company(com_seq=1, com_name="sam")
add_company(com_seq=2, com_name="sung")
print(com_list)

# ---------------------------------------
# 업체별 상품정보 등록
# 함수이름: add_goods
# 파라미터: com_seq, **kwargs(key는 good_seq,good_name,good_price)
# 결과리턴: True/False
# ---------------------------------------
good_list = []


def add_goods(com_seq, **kwargs):
    seq = []
    cnt = 0
    for j in range(len(com_list)):
        for m in com_list[j]["com_seq"]:
            seq.append(m)
    for i in range(len(com_list)):
        if cnt == 1:
            print("숫자 %s은/는 없는 회사번호입니다."%com_seq)
            cnt = 0
            return False
        else:
            if com_seq in seq:
                good_list.append(kwargs)
                good_list[i]["com_seq"] = com_seq
                cnt = 0
                return True
            else:
                cnt = 1


add_goods(1, good_seq="1", good_name="spoon", good_price="2000")
add_goods(2, good_seq="2", good_name="fork", good_price="3000")
add_goods(3, good_seq="3", good_name="chopsticks", good_price="4000")
add_goods(4, good_seq="4", good_name="water", good_price="5000")
print(good_list)

# ---------------------------------------
# 업체별 상품정보 출력
# 함수이름: print_com_goods
# 파라미터:   com_seq  (-1=전체출력  / com_seq:해당업체)
# 파라미터:   업체명 (빈값=전체출력 / com_name:해당업체)
# 결과리턴: X
# ---------------------------------------

def print_co_goods1(com_seq):
    if com_seq == -1:
        for i in good_list:
            print(i)
    elif com_seq > 0 and com_seq <= len(com_list):
        print(good_list[com_seq - 1])
    else:
        print("올바른 값을 입력하여 주십시오.")



#print_co_goods1(-1)
#print_co_goods1(1)

def print_co_goods2(*com_name):
    if com_name == ():
        for j in good_list:
            print(j)
    else:
        for i in range(len(com_list)):
            if com_list[i]["com_name"] == com_name:
                tmp_seq = com_list[i]["com_seq"]

                print(good_list[i]["com_seq"])

#print_co_goods2()
print(good_list)

