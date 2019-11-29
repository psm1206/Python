score = 97    #debug 빨간점 : breakpoint
gen = 'm'
if score >= 90 :
    print("A")
    print("eeee")
    if gen == 'm' :
        print("가산점2")
    else :
        print("가산점0")
elif score >= 80 :
    print("B")
    if gen == 'm' :
        print("가산점1")
    else :
        print("가산점0")
else :
    print("FFFF")

print("------------------Done------------------")

result = sum([x for x in range(1000) if x%3==0 or x%5==0])
print(result)

result = []
for x in range(1000):
    if x%3==0 or x%5==0:
        result.append(x)
print(sum(result))