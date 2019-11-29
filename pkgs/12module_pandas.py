# 12module_pandas.py

import pandas as pd
import numpy as np

# list = ["a", "b", 1, 2, ]
# s = pd.Series(list)
#
# print(s)

dates = pd.date_range('20190101', periods=4)

df = pd.DataFrame({'empno' : [7788, 7733, 7799, 7798],
                   'ename' : ['SMITH', 'ALLEN', 'MARK', 'KING'],
                   'sal' : [500, 300, 1000, 5555],
                   'job' : ['manager', 'manager', 'manager', 'clerk']},
                    index=dates)
# print(df)
# print(df.head(2))
# print(df.tail(1))
# print(df.to_numpy())


# print(df.T)
# print(df.describe())
# print(df['sal'], df['ename'])
# print(df[0:3])

# print(df.loc['20190103':'20190104', ['empno', 'ename']])
# print(df.loc[dates[2:4], ['empno', 'ename']])
#
# print("============================================")
# # print(df[df.sal >= 1000])
# print(df[(df.sal >= 1000) & (df.job == 'manager')])
#
# print("============================================")
# aa = ['MARK', 'KING']
# for i in aa :
#     print(df[df.ename == i])
#
# aa = ['MARK', 'KING']
# print("============================================")
# print(df[(df.ename == 'MARK') | (df.ename == 'KING') ])
# print("============================================")
#
# print(df.iloc[:,2])
# print(df.iloc[:,2:3])
print(df.empno)
print("============================================")

df2 = df.copy()

print(df2[df2['job'].isin(['manager', ])])

print(df2[df2.job.isin(['manager', 'clerk'])])

df.iloc[:, 2] = 2000
print(df)
print("============================================")

df.loc[df.job == 'manager', 'sal'] = 3333
print(df[df.job == 'manager'].sal)
# print(df[df.ename == 'ALLEN'].sal)
print(df)

cols = df.columns.tolist()
print("============================================")

print(cols[-1] + '111')
print("============================================")

print(cols[-1:])
print("============================================")

cols = cols[-1:] + cols[:-1]
print(cols)
print(df)

# df = pd.DataFrame({'empno' : [7788, 7733, 7799, 7798],
#                    'ename' : ['SMITH', 'ALLEN', 'MARK', 'KING'],
#                    'sal' : [500, 300, 1000, 5555],
#                    'job' : ['manager', 'manager', 'manager', 'clerk']},
#                     index=dates,
#                   columns=cols)
# df.loc[df.job.isin(['manager','clerk']), 'sal'] = 3333

dates = pd.date_range('20190101', periods=6)

columns = ['empno', 'ename', 'sal', 'job']
df3 = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=columns)
print("============================================")

print(df3)
df3[df3 > 0] = -df3
print(df3)
print("============================================")
df["deptno"] = [20, 30, 10, 20]
print(df)
print("============================================")

col = ['empno', 'ename', 'sal', 'deptno', 'job']

# insertRow = [9999, 'NEEWW', 9999,  30, 'clerk']
# insertDic = {'empno' : [7788, 4345, 5699],
#             'ename' : ['PARK', 'KANG', 'KIM'],
#             'sal' : [543, 3040, 1100],
#             'job' : ['manager', 'clerk', 'here'],
#              'deptno' : [40, 20, 10]}
#
# newRow = pd.DataFrame([insertRow], index=pd.date_range('20190105', periods=1), columns=col)
# newRow2 = pd.DataFrame(insertDic, index=pd.date_range('20190106', periods=3), columns=col)
# print(newRow)
# print(newRow2)
# print("============================================")
# ndf = df.append(newRow, sort=False)
# print(ndf)
# print("============================================")
# ndf2 = df.append(newRow2, sort=False)
# print(ndf2)
# print("============================================")
#
# df4 = pd.Series(insertRow, index= col)
# print(df4)
# print("============================================")
#
# df = df.append(df4, ignore_index=True)
# print(df)


#============================Dictionary형태로 합치기================================


keys = ['empno', 'ename', 'sal', 'job']
newData = [9999, 'NEEWW', 9999, 'clerk']
# 리스트형태를 딕셔너리로 바꿔주는 법
insertRow = dict(zip(keys, newData))



data = [
    [7788,'SMITH',1000,'manager'],
    [7733,'ALLEN',1000,'manager'],
    [7799,'MARK',1000,'manager'],
    [7798,'KING',1000,'clerk']
]
keys = ['empno', 'ename', 'sal', 'job']
dataList = []
for values in data :
    dataList.append(dict(zip(keys, values)))
print(dataList)

newData = [9999,'NEWMAN',500,'clerk']
dataList.append(dict(zip(keys, newData)))
print(dataList)
df = pd.DataFrame(data=dataList, columns=keys)
df = df.set_index("empno")

print(df)

print(df.groupby("job").size())


newData = [9998, 'NEEWW', 7777, 'clerk']

df.loc[newData[0]] = newData[1:]
print(df)

