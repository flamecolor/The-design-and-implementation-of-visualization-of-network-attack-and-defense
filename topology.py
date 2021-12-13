import pandas as pd

data = pd.read_csv("newdata.csv")
nodes = []  # 节点集
links = []  # 边集
for i in range(500):  # 遍历数据集
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
