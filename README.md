# python 学习

## 一 python基础

### 1 python 环境的安装

[python-3.11下载(华为源镜像)](https://mirrors.huaweicloud.com/python/3.11.0/python-3.11.0-amd64.exe)

如果在安装的时候没有选中添加环境变量,可以在环境变量中添加环境变量如下图所示:

要将python添加到用户变量中的python中

![python环境变量](./markimgs/img.png)

### 2 pip的使用

#### 2.1 pip的安装与配置

1. pip的安装: 在安装python时会自动安装pip
2. pip -V: 查看当前pip版本
3. 如果控制台输入 `pip -V` 不是内部指令, 需要将python的scripts目录添加到环境变量中的path中


#### 2.2 使用pip管理python包

- `pip install<包名>` 安装指定的包
- `pip uninstall<包名>` 卸载指定的包
- `pip list` 显示已经安装的包
- `pip freeze` 显示已经安装的包,并且以指定的格式显示

#### 2.3 修改pip下载源

运行 `pip install` 命令会从网站上下载指定的python包, 默认是从默认提供的国外网站上下载,遇到网络状况不好的时候,可能会下载失败,我们可以通过指令,修改pip下载软件时的源

`pip install 包名 -i 国内源地址`


示例:`pip install ipython -i https://pypi.mirrors.ustc.edu.cn/simple/`

就是从中国科技大学(ustc)的服务器上下载requests(基于python的第三方web框架)

国内源配置  
常用的国内镜像  
阿里云 https://mirrors.aliyun.com/pypi/simple/  
豆瓣https://pypi.douban.com/simple/  
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/  
中国科学技术大学 https://pypi.mirrors.ustc.edu.cn/simple/  
华中科技大学https://pypi.hustunique.com/  
新版ubuntu要求使用https源，要注意
 

临时使用  
 在使用pip的时候，加上参数 -i 和镜像地址

可以使用pycharm集成开发环境进行python的开发  

可以在 pycharm 的 setting 中更改 python script 模板 


### 3 python基础

#### 3.1 注释

单行注释: `# 单行注释`  
多行注释:

```python
'''多行注释
    多行注释的范围
'''

```  

#### 3.2 变量的声明

变量声明的规则: `变量名 = 变量值`

#### 3.3 变量的类型

程序里: 在Python里为了应对不同的业务需求,也把数据分为不同的类型  
如下图所示  
![python变量的类型](./markimgs/img_1.png)

```python

money = 5000  # int类型
money1 = 2.33  # float类型

# boolean 布尔
# 流程控制语句

# 字符串: 使用的是单引号 或者 双引号
name = '勋悟空'
name1 = '猪八戒'

# list 列表
# tuple 元组
# dict 字典

# list 列表
# 应用场景: 当获取到了很多个数据的时候,那么我们可以将它们存储到列表中,然后直接使用列表访问
name_list = ['勋悟空', '猪八戒', '白骨精']
print('name', name_list[1])

# tuple 元组
age_tuple = (18, 20, 21)
print('age_tuple', age_tuple)

# dict 字典
# 应用场景: scrapy框架使用

# 格式: 变量的名字 = {key: value}
person = {
    'name': '勋悟空',
    'age': 20
}

print('person', person)

```

#### 3.4 查看数据类型

- 在python中,只要定义了一个变量,而且它有数据,那么它的类型就已经确定了,不需要咱们开发者主动的去说明他的类型,系统会自动识别,也就是说在使用的时候 *"变量没有类型, 数据才有类型"*
- 如果想要查看一个变量存储的数据类型,可以使用type(变量的名字),来查看变量存储的数据类型
```python
name = '勋悟空'
age = 12
salary = 1000.21
children = ['小红', '小白', '小红']
child1 = {
    'name': '小红',
    'age': 16
}

print(type(name))
```

#### 3.5 标识符和关键字

计算机编程语言中, 标识符是用户编程时使用的名字, 用于给变量,常量,函数,语句块等命名,以建立起名称与使用之间的关系

1. 标识符由字母,下划线和数字组成,且数字不能开头
2. 严格区分大小写
3. 不能使用关键字

*命名规范*  
- 标识符命名要做到见名知义
> 起一个有意义的名字,尽量做到一言就知道是什么意思(提高代码可读性=>方便维护)
- 遵守一定命名规范
  - 驼峰命名法分为 大驼峰 和 小驼峰
  - 
  
*关键字*  
- 关键字的概念
  - 一些具有特殊功能的标识符,这就是所谓的关键字
  - 关键字,已经被python使用了,所以不允许开发者自己定义和关键字相同名字的标识符

#### 3.6 类型转换  

| 函数 | 说明 |
|:--- |:---|
| int(x) | 将x转换为一个整数 |
|float(x)|将x转换为一个浮点数|
|str(x)|将对象x转换为字符串|
|bool(x)|将对象x转换成为布尔值|
```python
print('123.34转换成整型', int(123.34))  # 123
print('123.34转换成字符串', str(123.34))  # '123.34'
print('123.34转换bool值', bool(123.34))  # True
print('123转换成浮点型', float(123))  # 123.0

```



