

if __name__ == "__main__":
    run_code = 0

import numpy as np
import pandas as pd

# 读取xls文件
data_xls = pd.read_excel("人均国民收入.xls", header=1)

# 将读入的Excel数据保存为CSV文件
data_xls.to_csv("人均国民收入.csv", index=False, encoding="gbk")

# 使用loadtxt函数读取刚刚导出的CSV文件
data_csv = np.loadtxt("人均国民收入.csv", delimiter=",", skiprows=1)

print(data_csv)