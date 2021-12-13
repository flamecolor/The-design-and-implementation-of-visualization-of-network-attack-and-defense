import pandas as pd
import numpy as np

def check_source(ip):  # 判断源ip地址是否可用
    if "_" in ip:
        return None
    return ip


data = pd.read_csv("fridaydata.csv")  # 导入数据
data = data.loc[:, ["Time", "Source", "Destination", "Length"]]  # 筛选数据
data["Source"] = data["Source"].map(check_source)   # 映射
data = data.loc[data["Source"].notna()]   # 选取源ip可用的数据
data = data.drop_duplicates(["Source", "Destination"], keep='first')  # 删除重复数据
data = data.rename(columns={"Time": 0, 'Source': 1, "Destination": 2, "Length": 3})  # 重置列索引
data = data.reset_index(drop=True)  # 重置行索引
data.to_csv("newdata.csv", index=False, encoding='utf-8')  # 保存
