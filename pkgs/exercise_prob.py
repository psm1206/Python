def solution(priorities, location):
    answer = []
    stno = 0
    while answer != []:


    for k in range(len(priorities)):
        for m in range(1, len(priorities)): # index 0을 제외한 나머지 수들
            stno = 0
            if priorities[0] >= priorities[m]:
                stno = stno + 1
                if stno == len(priorities) - 1:
                    answer.append(k)
                    del priorities[0]
                    priorities.append(priorities[-1])
                    del priorities[-1]
        priorities.append(priorities[0])
        del priorities[0]
    for i in answer:
        if i == location:
            return answer[location]


a=solution([2, 1, 3, 2], 2)
print(a)