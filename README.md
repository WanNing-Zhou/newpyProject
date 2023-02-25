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
> bool 类型转换成整形, True ->1, False -> 0  


### 4 运算符

#### 4.1 算数运算符

|运算符|描述|
|:---|:---|
| + | 加|
|- | 减|
|*|乘|
|/| 除|
|//|取整除|
|%|取余|
|**|指数|
|()|小括号|

> 注意:混合运算是,优先级顺序为: `**` 高于 `* / % //`高于`+ -`,为了避免期以, 建议使用()来处理运算父优先级  
> 并且,不同的类型的数字在进行混合运算是,证数建辉转换成浮点数来进行运算

```python
a = 3
b = 2
# 加法运算
print('a+b=', a + b)  # 5
# 减法运算
print('a-b=', a - b)  # 1
# 乘法运算
print('a*b=', a * b)  # 6
# 除法运算,结果可以为浮点类型
print('a/b=', a / b)  # 1.5
# 取整除, 结果只会保留整数部分
print('a//b=', a // b)  # 1
# 指数运算
print('a**b=', a ** b)  # 9
# 括号运算: 会改变运算优先级
print('(a+b)*b=', (a + b) * b)  # 10
```

*算数运算符在字符串中使用*  
- 如果是两个字字符串做加法运算,会直接把这两个字符串拼成一个字符串

`print('Hello' + 'World')  # HelloWorld`

> 在python中,两端都是字符缓才可以进行拼串
- 错误写法  
`print('123' + 456)`

- 字符串的乘法, 是将字符串重复多少次  
`print('Hello' * 3)  # HelloHelloHello`

#### 4.2 赋值运算符

赋值运算符会将符号左边的值赋值给右边

```python
# 普通赋值
a = 10
# 连续赋值
b = c = 20
# 多个变量去赋值(使用逗号分隔)
d, e, f = 1, 2, 3
```

#### 4.3 复合赋值运算符  

| 运算符 | 描述|实例|  
|:--- |:--- |:---|
|+= |加法赋值运算符|c += a 等效于 c = c + a| 
| -= |减法赋值运算符 | c += a 等效于 c = c + a|
|*= | 乘法赋值运算符|c *= a 等效于 c = c * a |
|/= | 除法赋值运算符|c /= a 等效于 c = c / a |
|//= |取整除赋值运算符 |c //= a 等效于 c = c // a |
|%= | 取模赋值运算符|c %= a 等效于 c = c % a |
|**= |幂等赋值运算符 | c **= a 等效于 c = c ** a|


#### 4.4 比较运算符

| 符号 | 描述 | 作用 |
|:---|:---|:---|
|==|恒等|判断==两边是否相等|
|!=|不等|!=是否不相等|
|<>|不等|python2版本使用,python3遗弃|
| &gt; |大于|右是否大于左|
|<|小于|右是否小于左|
| &gt;= |大于等于|右是否大于等于左|
| <= |小于等于|右是否小于等于左|

> 返回的是一个bool值

#### 4.5 逻辑运算符

逻辑运算符返回bool类型

|符号|描述|作用|
|:---|:---|:---|
|and|与|`a and b` a和b都为true的时候为true|
| or |或| `a or b` a和b有一个为true的时候为true|
| not | 非 | `not a` 将a的真假取反,a为false的时候为true|

*性能提升*  

and 和 or 会有短路现象  (短路与,短路或)
and: `a and b=3` 当 and 前的值为 false 则 and 后的语句不会执行
or: `a or b=3` 当 and 前的值为 true 则 or 后的语句不会执行

> 利用 与 和 或 特性,对 and 和 or 做出优化,从而使性能得到优化

### 5 输入输出

#### 5.1 输入  

- 普通输出

`print('hello world')`

- 格式化输出
    - %s代表的是字符串
    - %d代表的是数值
  
```python
# %s 字符串
# %d 数字
name = '勋悟空'
age = 18
print('我是%s' % name)  # 我是勋悟空
print('我是%s,我今年%d岁了' % (name, age))  # 我是勋悟空,我今年18岁了
```

#### 5.2 输入

- input

```python
# name 赋值为输入的值
name = input('请输入你的姓名\n')
# 输出
print('我是%s' % name)   
```

### 6 流程控制语句

#### 6.1 if控制语句

- if语句是用来进行判断的,其格式如下

```
    if 要判断的条件:
        条件成立时,要执行的语句
```
> if 下面的代码 必须是一个 tab 键 或者是 四个空格
- 示例:

```python
age = input('请输入你的年龄:\n')
age = int(age)
if age >= 18:
    print('您的年龄是%d,您已经成年,可以进入网吧' % age)
```

#### 6.2 if-else语句

- if-else 的使用格式  
``` 
if 条件:
    满足条件的操作
else: 
    不满足条件的操作
```

- 示例

```python
age = input('请输入你的年龄:\n')
age = int(age)
if age >= 18:
    print('您的年龄是%d,您已经成年,可以进入网吧' % age)
else:
    print('未成年人不允许进入网吧')
```

#### 6.3 elif

- elif 的使用格式如下: 
```
if xxx1:
    事件1
elif xxx2:
    事件2
elif xxx3:
    事件3
```
说明:  
- 当xxx1满足时,执行事件1,然后整个if结束
- 当xxx1不满足, xxx2满足,执行事件2,然后整个if结束
- 当xxx1,xxx2都不满足 xxx3满足, 则执行事件3,然后整个if结束

- 示例:

```python
age = input('请输入你的年龄:\n')
age = int(age)
if age >= 18:
    print('您的年龄是%d,您已经成年,可以进入网吧' % age)
elif age >= 17:
    print('马上就快成年了,再等一等吧')
elif age >= 13:
    print('小朋友, 你的作业写完了吗')
else:
    print('未成年人不允许进入0网吧')

```

#### 6.4 for循环

**for循环格式**
```
for 临时变量 in 列表或者字符串等可迭代对象:
    循环满足条件时执行的代码
```

**for循环的使用**
- 遍历字字符串

```python
for s in 'hello':
    print('%s' % s)
    
# 输出:
# h
# e
# l
# l
# o
```

**range方法的使用**  
- range方法的结果是一个可以遍历的对象

- range(n) 0-n 左闭右开区间的可遍历对象
```python
# range(5) 0-4 左闭右开区间[0,5)
for i in range(5):
    print(i)

```

- range(a,b) a到b-1 左闭右开区间的可遍历对象
  - a 起始值
  - b 结束值

```python
# range(1, 6) 1-5 左闭右开区间[1,6)
for i in range(1, 6):
    print(i)
```

- range(a,b,c)  a到b-1左闭右开, 从a开始每次+c
  - a 起始值
  - b 结束值
  - c 步长

```python
for i in range(1, 10, 3):
    print(i)

# 结果
# 1
# 4
# 7
```

**循环一个列表**

```python
words = ['只', '因', '你', '太', '美']
for word in words:
    print(word)

# 结果
# 只
# 因
# 你
# 太
# 美
```























      


