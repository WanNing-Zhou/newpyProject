# 文件的读写
# 打开一个文件
f = open('test.txt', 'r+')
# 向文件中写入数据

for i in range(10):
    f.write('hello world!' + str(i)+'\n')
# 关闭文件
f.close()
