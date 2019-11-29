# 12module_pandas_train_test.py

# 기본 문법 조금만 더 보고 가자~

import pandas as pd
import numpy as np

list = [1, 2, 3]
index = ["lee", "kim", "park"]
s = pd.Series(list, index=index, name='국어 성적')
print(s)
s = s * 2
print(s)

list = [['s0001', 50, 70, 60],
        ['s0002', 40, 80, 90],
        ['s0003', 50, 90, 30]]

columns = ['sno', 'kor', 'math', 'eng']

df = pd.DataFrame(list, columns=columns)
df = df.set_index('sno')

print(df['eng'])
print(df.loc[df.kor == 50, 'kor'])
print(df.loc['s0002'])

print(df['eng'][1])
df = df.drop('kor', axis=1)
print(df)

# print("==================================")
# lists = list * 3
# print(lists)
#
# arr = np.array(list)
# arrs = arr * 3
# print(arrs)

# data = [42500, 42550, 41800, 42550, 42650]
# index = ['2019-05-31', '2019-05-30', '2019-05-29', '2019-05-28', '2019-05-27']
# s = pd.Series(data=data, index=index)
# #cond = s > 42000
# print(s.index)
# print(s[s > 42000])
# print("=====================================")
# array1 = np.array(data)
# s = pd.Series(data=data, index=index)
#
# print(s[s > 42000])