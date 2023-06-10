import re


def check_strength(s):
    # 定义正则表达式，用于匹配数字、小写字母、大写字母和特殊字符
    pattern = '[0-9a-z]+|[0-9A-Z]+|[.@!;?<>\',]+'
    # 使用正则表达式对字符串进行匹配，并判断是否包含数字、小写字母、大写字母和特殊字符
    if re.search('[0-9]', s) and re.search('[a-z]', s) and re.search('[A-Z]', s) and re.search(pattern, s):
        print("高强度字符串")
    else:
        print("error")


# 调用函数测试
check_strength("Abc123@.<>?")  # 高强度字符串
