f = open('example.txt', 'r', encoding='utf-8')
s = f.read()
aCount = s.count('a')
bCount = s.count("b")
cCount = s.count('c')

print('a出现的次数:', aCount)
print('b出现的次数', bCount)
print('c出现的次数', cCount)
