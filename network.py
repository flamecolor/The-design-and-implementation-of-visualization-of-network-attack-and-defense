import pandas as pd
import topology as tp

nlist = []
handers = ["nodes"]
for i in range(200):  # 遍历数据集
    for j in range(1, 3):
        if tp.data.iloc[i][j] not in nlist:
            nlist.append(tp.data.iloc[i][j])  # 节点数据
            handers.append(tp.data.iloc[i][j])
df = pd.DataFrame(columns=nlist)
df1 = pd.DataFrame(columns=nlist)
num = []
for i in range(len(nlist)):
    num.append(0)
df = df.reindex(nlist)
df1 = df1.reindex(nlist)
row = pd.Series(num, index=nlist)
for i in range(len(nlist)):
    df[nlist[i]] = row
    df1[nlist[i]] = row
j = 0
for item in tp.links:
    df.loc[item["source"], item["target"]] = 1
    df1.loc[item["source"], item["target"]] = tp.data.iloc[j, 3]
    j=j+1
rows = []
rrows = []
for i in range(len(nlist)):
    a = []
    a1 = []
    a.append(nlist[i])
    a1.append(nlist[i])
    for j in range(len(nlist)):
        a.append(df.iloc[i][j])
        a1.append(df1.iloc[i][j])
    rows.append(a)
    rrows.append(a1)
