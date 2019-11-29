#dataframe_sample.py

import numpy as np
import pandas as pd
import bigdata.common as comm

a = np.array(0)
print(a)

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[1][1])

a = np.arange(12)
print(a)

#a.shape = -1, 1
print(a[1:-1])

a = np.random.randint(-10, 10, size=(10, 10))
print(a)
b= np.median(a)
print(b)

#c = np.random.randint(1, 100, size=(3, 5))
arr = [[6, 14, 6, 18, 25],
        [18, 24, 27, 20, 28],
        [4, 5, 21, 28, 10]]

# if i in arr:
#     i%2==0
col = [ "col1", "col2", "col3", "col4", "col5" ]
df = pd.DataFrame(arr, columns=col)

print(df.col2)
print("============================")
print(df[["col3", "col4"]])
print("============================")
print(df.iloc[1:1])
print("============================")
print(df.loc[1:1])

# 컬럼 3으로 grouping해서 전체 평균

print("============================")
# column addr 추가
ndf = pd.DataFrame({"addr" : ["서울", "대전", "대구"]})
print(ndf)

df["addr"] = ["서울", "대전", "대구"]
print(df)
print("============123================")
df[df[["col1", "col2", "col3", "col4", "col5"]]<10] = np.nan

print(df)

print("==============123==============")

print(df.groupby('addr').mean())
print("============================")
print(df.sum(axis=0))
print(df.sum(axis=1))

ndf = pd.DataFrame([[3, 9, 26, 43, 5, "서울"]], columns=df.columns)
df = df.append(ndf, ignore_index=True)
print(df)
print("============================")

print(df.iloc[0][1])

#print(df.groupby('addr').mean())

# df.loc[df<10,:] = None
# ddf = df[["col1", "col2", "col3", "col4", "col5"]]
# print(df[(df.col1 < 10) | (df.col2 < 10) ])
# print(df.loc[["col1", "col2", "col3", "col4", "col5"]])
# df.loc[df.column<10, "col1"] = None

# print(df[["col1", "col2", "col3", "col4", "col5"]])
# print(df.columns)
#
# select = [x for x in df.columns if x != "addr"]
# df.loc[:, select]
# print(df.loc[:, select])

df = df.groupby('addr').mean()
#
# # df["col1":].astype(int)
# print("============================")
# #
# df[df<10] = None
# print(df)
# print(df.index)
# res = [x for x in df.index]
# print(res)
# for y in res:
#         print(y)
#
# print("============================")
# nres = [ i for i in range(0, 100, 3)]
# print(len(nres))
# print(nres)
# arr = np.array(nres)
#
# print(nres.__sizeof__())
# print(arr.__sizeof__())
# print("============================")
# print(df)
#
# print("============================")
# df.loc[(df.addr=="서울") | (df.addr=="대전"), "col5"] = 250
# print(df)
#
# print(df[["col1", "col2"]])
#
# print("============================")
#
# print(df.count(1))
#
#
#
# # print(df.iloc[2:3, 2:3, 1])
#
# # print(df.dropna(axis=1))
# print("============================")
# add_df = pd.read_csv("dataframe-value-add.csv")
# print(add_df)
# print("===========123123==============2312312===")
# # add_df = add_df.set_index("addr")
# # print(add_df)
# #
# # print("============================")
# #
# add_df = df.append(add_df, ignore_index=True)
# print(add_df)
#
# df = df.fillna(0)
# df.astype("int64")
# print("============================")
# nparr = df.to_numpy()
# print(nparr)
print(df.stack().describe())
print(df.stack().describe()["25%"])
head = df.head(2)
topdf = df[1:3]
print(head)
print(topdf)


# # print("============================")
# # print(add_df.stack())
# #
# print("mean : ", add_df.stack().mean())
#
# print("median : ", add_df.stack().median())
#
# print("var : ", add_df.stack().var())
#
# print("std : ", add_df.stack().std())
#
# print("range : ", add_df.stack().min(), "~", add_df.stack().max())
#
# print(add_df.stack())
