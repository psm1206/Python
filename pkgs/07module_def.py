#07module_def.py

def login(id, pw):
    return "홍길동"

res = login("AA", 1111)
print(res)

#함수이름 : maxmin
#파라미터 : 리스트
#결과리턴 : max, min
# def maxmin(*number_list):
#     max_num = 0
#     max_num = 999999
#     for n in number_list:
#         if max_num < n:
#             max_num = n
#         if min_num > n:
#             min_num = n
#     return max_num, min_num
#
# (resmax, resmin) = maxmin(3, 4, 5, 1, 2, 7, 45, 3)
# print(resmax, resmin)


def maxmin(*number_list):
    res = []
    for n in number_list:
        res.extend(n)       #for문을 돌 때마다 메모리 공간을 새로 할당하기 때문에 많이 잡아먹을 수 있음. 되도록이면 지양하자.
    max_num = max(res)
    min_num = min(res)
    return max_num, min_num

(resmax, resmin) = maxmin([3, 4, 99], [9, 3], [6, 1, 4, 8])
print("Global Max = %d Global Min = %d" % (resmax, resmin))

def maxmin(*number_list):
    max_num = 0
    min_num = 999999
    for one_list in number_list:
        for num in one_list:
            if max_num < num:
                max_num = num
            if min_num > num:
                min_num = num
    return max_num, min_num
(resmax, resmin) = maxmin([3, 4, 99], [9, 3], [6, 1, 4, 8])
print("Global Max = %d Global Min = %d" % (resmax, resmin))
#함수이름 : bmi
#파라미터 : height, weight
#결과리턴 : bmi 수치

# def bmi(height, weight):
#     a = weight / ((height) / 100 * (height) / 100)
#     if height <= 0 or weight <= 0:
#         print("error")
#     elif a < 18.5:
#         print("BMI = %d    BMI < 18.5          마름"%a)
#     elif 18.5 <= a < 25.0:
#         print("BMI = %d    18.5 <= BMI < 25.0  보통"%a)
#     elif 25.0 <= a < 30.0:
#         print("BMI = %d    25.0 <= BMI < 30.0  비만"%a)
#     else:
#         print("BMI = %d    30.0 <= BMI         고도비만"%a)
# bmi(171, 90)

    # BMI < 18.5          마름
    # 18.5 <= BMI < 25.0  보통
    # 25.0 <= BMI < 30.0  비만
    # 30.0 <= BMI         고도비만

#함수이름 : circle
#파라미터 : r
#결과리턴 : area, circum
#파이썬에는 상수(constant)가 없음. 그래서 변수로 새로 만들어주는데 보통 대문자로 만듬.
# import math # 내장 패키지
#
# def circle(r):
#     return (math.pi)*(r**2), 2*(math.pi)*r
#     #2*2*2*2, 2**4, pow(2, 4): builtins 함수, math.pow(2, 4): 내장패키지 내장함수
#
# r = float(input("반지름(cm)을 입력하십시오: "))
#
# (area, circum) = circle(r)
#
# print("area = %.2fcm^2  circum = %.3fcm" % (area, circum))
# print("%.10f"%math.pi)



for a in [1, 2, 3]:
    print(round(a/3,1))

def sum(a, b):
    return a + b



