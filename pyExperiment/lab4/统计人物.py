import jieba
txt = open('红楼梦.txt', 'r', encoding='utf-8').read()
excludes = {'什么', '一个', '我们', '你们', '如今', '说道', '知道', '起来', '这里','姑娘',
            '出来','人','那里','自己','怎么','没有','两个','他们','众人','只见','一面',
            "众人","奶奶","姑娘","回来","大家","老爷","丫头","自己","一面","只见","怎么","两个",
            "没有","不是","不知","这个","听见","这样","进来","告诉","东西","卜咱们","就是","只是","只得","这些",
            "不敢","出去","所以","太太","咱们"
            }
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == '贾母' or word == '老太太':
        rword = '贾母'
    else:
        rword = word
    counts[rword] = counts.get(rword, 0) + 1
for word in excludes:
    if word in counts:
        del counts[word]
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
# 输出前十
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
