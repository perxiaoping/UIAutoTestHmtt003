import yaml
from config import BASE_PATH
import os
# 定义函数



def read_yaml(filename):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    # 定义空列表组装测试数据
    arr = []
    # 获取文件流
    with open(filepath, "r", encoding="utf-8") as f:
        # 遍历 调用yaml.safe_load（f）.values（）方法
        for datas in yaml.safe_load(f).values():
            print("datas是", datas)
            print(type(datas))
            arr.append(tuple(datas.values()))
    # 返回结果
    return arr


if __name__ == '__main__':
    print(read_yaml("mp_login.yaml"))
