n = int(input())
s = n
factors = []

# 对偶数进行检查
while n > 1 and n % 2 == 0:
    factors.append(2)  # 能被2整除的时候,加入2
    n /= 2

# 对奇数进行检查
factor = 3
while factor <= n:
    # 如果n能被factor整除，则加入factors列表中
    while n % factor == 0:
        factors.append(factor)
        n /= factor
    factor += 2

print("{}=".format(s), end="")
for i, f in enumerate(factors):
    if i < len(factors) - 1:
        print("{}*".format(f), end="")
    else:
        print(f)
