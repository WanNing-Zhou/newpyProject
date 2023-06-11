# np.random.seed(0)作用: 使得随机数据可预测, 即只要seed的值一样,后续生成的随机数都一样,

# 当我们设置相同的seed, 每次生成的随机数相同, 如果不设置seed, 则每次回生成不同的随机数

import numpy as np
import numpy.random

np.random.seed(0)

A = np.random.rand(4)  # 生成区间[0,1]上的均匀分布的4个随机浮点数的一维数组

print(A)  # [0.5488135  0.71518937 0.60276338 0.54488318]

a = [i for i in range(10)]
b = [np.random.choice(a) for i in range(6)]  # 每次从a中随机返回一个元素, 共迭代6次
print(b)

# shuffle: 直接再原来的数组上进行操作
# permutation: 不知再原来的数组上操作, 回返回一个新的打乱顺序的数组

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.random.permutation(x)  # x的数据不动,把随机打乱后的数据返给y
print('x=', x)
print('y=', y)
numpy.random.shuffle(x)  # 直接随机打乱数组x的数据
print(x)

