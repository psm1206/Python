# 12module_pandas.py
import pandas as pd
import numpy as np
# --------------- series ---------------
# list = ["a","b",1,2,]
# s = pd.Series(list);
# print(s)
import time
startTime = time.perf_counter()
numOfRows = 50000
keys = ['empno','ename','sal','job']
dataList = []

# ------ dataframe : [data], [index], [column] 사용 -----
for i in range(1, numOfRows):
    list = [7788+i, 'SMITH', 1000, 'manager']
    dataList.append(dict(zip(keys, list)))

df = pd.DataFrame(data=dataList, columns=keys)
df = df.set_index("empno")
#---------프레임 + 프레임 추가인경우
newData = [99999, 'NEWMAN',500,'clerk']
# newdf = pd.DataFrame([newData],  columns=keys)
# newdf = newdf.set_index("empno")
# df = df.append(newdf, ignore_index=True)

#---------프레임 + 리스트 추가인경우
df.loc[newData[0]] = newData[1:]

print(df)
print('Elapsed time: {:6.3f} seconds for {:d} rows'.format(time.perf_counter() - startTime, numOfRows))
