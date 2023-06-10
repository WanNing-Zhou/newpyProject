# 用Pandas读取MySQL数据库中某只股票100天的日交易数据，将查询结果返回DataFrame里的数据，
# 直接保存到Excel文件，并绘制日收盘价格走势、5天移动平均线、10天移动平均线：
import numpy as np
import matplotlib.pyplot as plt
import openpyxl
# 绘制日收盘价格走势、5天移动平均线、10天移动平均线。
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import pandas as pd
import pymysql

connStr = "mysql+pymysql://root:123456@localhost:3306/stock1?"
engine = create_engine(connStr)
sql = "select cDay,mClose from trDay where cStockNo ='sz000561' and cDay>'20130101' and cDay<'20130411' order by cDay"
# 100天内的数据
trDay = pd.read_sql(sql, con=engine)  # 烽火电子日收盘价格
plt.figure(figsize=(8, 4), dpi=80)
trDay['mClose'].plot(title="sz000561", color='b')
trDay['mClose'].rolling(10).mean().plot(color='r')  # 10天移动平均
trDay['mClose'].rolling(5).mean().plot(color='r')                  # 5天移动平均
rows = trDay.shape[0]
d = trDay['cDay'][0:rows:10]  # 步长为10
plt.xticks(range(0, rows, 10), d, rotation=45, fontsize=12)  # 旋转45度
plt.legend(['mClose', 'MA(10)'])
# plt.legend(['mClose','MA(5)']) #5天平均用
plt.show()
cDay = {}
mClose = {}
for i in range(int(trDay.size / 2)):
    cDay[i] = trDay['cDay'][i]
    mClose[i] = trDay['mClose'][i]
wb = openpyxl.Workbook()
ws1 = wb.active
ws1.title = 'Sheet1'
ws1['A1'] = 'cDay'
ws1['B1'] = 'mClose'
for i in range(int(trDay.size / 2)):
    ws1.append([cDay[i], mClose[i]])
wb.save('lab8烽火电子日收盘价格.xlsx')
print(cDay)
print(mClose)
