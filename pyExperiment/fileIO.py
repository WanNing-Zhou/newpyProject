
if __name__ == "__main__":
    run_code = 0

with open("example.txt", "w") as f:
    # 向文件中写入一行文本
    f.write("Hello world!")

with open("example.txt", 'r') as f:
    print(f.read())
