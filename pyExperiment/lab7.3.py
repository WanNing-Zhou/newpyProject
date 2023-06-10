# 高数线代考试成绩频率直方图
import numpy as np
import xlrd
import matplotlib.pyplot as plt

wb = xlrd.open_workbook("高数线代考试成绩.xls")
sheet = wb.sheet_by_index(0)  # 通过索引获取sheet表格
col_2 = sheet.col_values(3)  # 获取第3列内容：考试成绩
x = np.array(col_2[1:], dtype=float)  # 考试成绩
f = plt.figure(figsize=(8, 4), dpi=80)  # 设置画布大小
f.set_facecolor((0.92, 0.92, 0.96))  # 设置坐标轴颜色
plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False
n, bins, patches = plt.hist(x, 10, density=1, facecolor='blue', edgecolor='white', lw=1, alpha=0.75)
mu = np.mean(x)  # 平均值
sigma = np.std(x)  # 标准差
y = np.exp(-0.5 * (bins - mu) * (bins - mu) / (sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)  # 密度值
plt.plot(bins, y, 'r-')  # 概率密度折线拟合图
plt.title('高等数学考试成绩频率直方图' + '，人数：' + str(len(x)))
plt.legend([r'正态分布: $\mu=%.2f$, $\sigma=%.2f$' % (mu, sigma)])
plt.show()
