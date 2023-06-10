def prime_factors_v2(n):
    factors = []  # 用 set 记录质因子，避免重复

    # 尝试 2~sqrt(n) 之间的所有可能的因子
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            # 如果找到一个因子 i，则将其加入因子集合
            factors.append(i)
            n //= i

    # 注意，如果在上述循环结束后 n 仍然大于 1，则它本身也是一个质因子
    if n > 1:
        factors.append(n)

    return list(factors)  # 转换成列表输出


# 示例：

s = int(input())
factors = (s, prime_factors_v2(s))
print("{}=".format(s), end="")
for i, f in enumerate(factors):
    if i < len(factors) - 1:
        print("{}*".format(f), end="")
    else:
        print(f)
