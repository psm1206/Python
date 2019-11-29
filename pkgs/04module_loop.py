# module_loop.py
# for : 반복횟수가 명확할 때
# while : 특정 조건에 의해 반복문을 빠져나올 때
'''
for 담을변수 in 여러개값 :
    print(담을변수)
'''

score_list = ["a", "b", "b", "c"]
for score in score_list: #in 자리에 len 사용하지 말자.
    print(score, "점", end="\t")
    print("%s점" % score, end="\t")

for score in score_list:
    print("%s점" % score, end="\t") #왜 탭 간격이 다를까?

for num in range(1, 11, 2): # 1 <= num < 11
    print(num, end="\t")

for k in range(0, len(score_list)):
    print(score_list[k])


for k in range(2, 10):
    if k % 2 == 0:
        print("[%d단]" % k)
        for m in range(1, 10):
            if m % 2 == 0:
                print("%d X %d = %d" % (k, m, k*m))

score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
i = 0
for k in range(0, len(score)):
    i = score[k] + i
    if k == len(score) - 1:
        print(i)

result = [k - 30 for k in score]
print(result)

result = ["%d X %d = %d" % (k, m, k*m) for k in range(2, 10)
                                        for m in range(1, 10)]
print(result)

result = [n*2 for n in range(1, 6) if n%2 == 1]
print(result)

# for dictionary
dic = {"uid":"kim", "upw":"111", "name":"아무개"}
for k in dic.values():
    print(k)                                    # dictionary 그대로 print하면 key가 출력됨.

dic = {"uid":"kim", "upw":"111", "name":"아무개"}
for k in dic:
    print(k, ":", dic[k])
print(list(dic.keys()))

#-------------------while------------------
a = 5
while a > 3:
    print("big")
    a = a - 1
print("---while done---")

a = 5
while True:
    print("big")
    a = a - 1
    if a <= 3:
        break
a = 6
b = 5
while a <= 9:
    print(a)
    b = 5
    while b <= 6:
        print(b)
        b += 1
    a += 1

a = 2
while a <= 9:
    b = 1
    print("[%d단]" % a)
    while b <= 9:
        print("%d X %d = %d" % (a, b, a*b), end="\t")
        b = b + 1
    print("")
    a = a + 1

#별찍기
for k in range(1, 10):
    print("*"*k)

for k in range(9, 1, -1):
    print(" "*k, end="")
    print("*"*(10-k))

for n1 in range(1, 5):
    for n2 in range(1, 5-n1):
        print(" ", end="")
    for n2 in range(1, n1+1):
        print("*", end="")
    print("")

for k, v in dic.items():        # 파이썬만의 기능
    print(k, v, dic)

print(list(dic.items())[0][1])
















