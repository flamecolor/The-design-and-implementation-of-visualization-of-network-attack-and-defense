import pandas as pd
import random
import json

data = pd.read_csv("newdata.csv")
nodes = []  # 节点集
links = []  # 边集
nodes_=[]
xresult = []
yresult = []
xresult = random.sample(range(73, 136), 62)
yresult = random.sample(range(3, 54), 50)
ndata = {}
ldata = []
l=0
nv = []
for i in range(50):  # 遍历数据集
    for j in range(1, 3):
        nn = (data.iloc[i][j], data.iloc[i][3])
        if data.iloc[i][j] not in nodes_:
            nodes_.append(data.iloc[i][j])
            ndata[data.iloc[i][j]] = [xresult[l], yresult[l]]
            l+=1
            nv.append(nn)
        if j == 1:
            link_={}
            link_["source"] = data.iloc[i][1]
            link_["target"] = data.iloc[i][2]
            nlink = (data.iloc[i][1], data.iloc[i][2])
            if link_["source"] not in link_["target"]:
                ldata.append(nlink)
ndata=json.dumps(ndata, ensure_ascii=False)
f2 = open('new_json.json', 'w')
f2.write(ndata)
f2.close()
for i in range(500):
    for j in range(1, 3):
        node = {}  # 创建新节点
        node["name"] = data.iloc[i][j]   # loc["i"]表示取索引为“i” iloc[i][j]取第i行第j列
        node["symbolSize"] = 3
        if node not in nodes:
            nodes.append(node)  # 新节点如果不在节点集里，将其加入
        if j == 1:
            link = {}  # 创建新边
            link["source"] = data.iloc[i][1]
            link["target"] = data.iloc[i][2]
            links.append(link)  # 新边如果不在边集里，将其加入

