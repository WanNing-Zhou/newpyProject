


if __name__ == "__main__":
    run_code = 0

import pandas as pd

# 读取数据
data = pd.read_excel('股票日交易数据20120425.xls')

# 根据涨幅排序，并输出前100行
change_sorted = data.sort_values(by='Change1', ascending=False)
with open("股票日交易数据.txt", "a") as f:
    f.write(change_sorted.head(100).to_string())
    f.close()
print()

# 根据换手率排序，并输出前100行
turnover_sorted = data.sort_values(by='TurnoverRate', ascending=True)
# print(turnover_sorted.head(100))
with open("股票日交易数据.txt", "a") as f:
    f.write(change_sorted.head(100).to_string())
    f.close()
