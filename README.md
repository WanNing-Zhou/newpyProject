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


### 7 数据类型高级

#### 7.1 字符串高级

字符串的常见操作包括:
- 获取长度: len  len函数可以获取字符串的长度
- 查找内容: find 查找指定内容再字符串中是否存在,如果存在就返回该内容在字符串第一次出现的开始位置索引值,如果不存在,则返回-1
- 判断: startswith,endswith  判断字符串是不是以某某开头/几位
- 计算出现的次数: count 返回 某字符串 在start和end之间 在 字符串 里面出现的次数
- 替换内容: replace  替换字符串中指定的内容,如果指定次数count,则替换不会超过count次
- 切割字符串: split 同故宫参数的内容切割字符串
- 修改大小写: upper,lower 将字符串中的大小写字母转换
- 空格处理: strip 去空格
- 字符串拼接: join 字符串拼接

#### 7.2 列表高级

列表的增删改查  
**添加元素**  

添加元素右以下几个方法:  
- append 在末尾添加元素
- insert 在指定位置插入元素
- extend 合并两个列表

**append**

append 会把新元素添加到列表末尾

```python

names = ['勋悟空', '猪八戒', '沙和尚']
print("添加前的数据", names)  # 添加前的数据 ['勋悟空', '猪八戒', '沙和尚']
# 添加数据
names.append('唐僧')
print('添加后的数据', names)  # 添加后的数据 ['勋悟空', '猪八戒', '沙和尚', '唐僧']
```

##### **insert**

在指定位置添加元素

```python
names = ['勋悟空', '猪八戒', '沙和尚']
names.insert(1, 'IKun')
print('添加后的数据', names)  # 添加后的数据 ['勋悟空', 'IKun', '猪八戒', '沙和尚']
```


**extend**

合并两个列表
```python
names = ['勋悟空', '猪八戒', '沙和尚']
names1 = ['IKun', '唐僧']
names.extend(names1)
print('合并后的数据', names)  # 合并后的数据 ['勋悟空', '猪八戒', '沙和尚', 'IKun', '唐僧']
```

##### **修改元素**

我们是通过指定下标来访问列表元素,因此修改元素的时候,为指定的列表下标赋值即可
```python
names = ['勋悟空', '猪八戒', '沙和尚']
names[1] = 'KunKun'
print('修改后的数据', names)  # 修改后的数据 ['勋悟空', 'KunKun', '沙和尚']
```

##### **查找元素**

所谓的查找,就是判断指定的元素是否存在,以及查看元素的所在的位置,主要包含以下几个方法:  
- in 和 not in
- index 和 count

**in,not in**  
python中查找的查用方法为:  
- in(存在),如果存在那么结果为true,否则为false
- not in(不存在),如果不存在那么为true,否则为false

```python
names = ['勋悟空', '猪八戒', '沙和尚']
findName = input('请输入你要查找的姓名:\n')
print('查找的名字是否存在', findName in names)  # 返回值为True 或 False
```

**index**

返回指定元素的索引位置
```python
names = ['勋悟空', '猪八戒', '沙和尚']
print('勋悟空的位置', names.index('勋悟空'))  # 勋悟空的位置 0
```

**count**

指定元素在List中的个数
```python
names = ['勋悟空', '猪八戒', '沙和尚']
print('names中勋悟空有几个', names.count('勋悟空'))  # names中勋悟空有几个 1
```

##### **删除元素**

列表常用的删除方法有:  
- del: 根据下标进行删除
- pop: 删除最后一个元素
- remove: 根据元素的值进行删除

**del**  
```python
names = ['勋悟空', '猪八戒', '沙和尚']
del names[2]
print('删除后的列表', names)  # 删除后的列表 ['勋悟空', '猪八戒']
```

**pop**
```python
names = ['勋悟空', '猪八戒', '沙和尚']
names.pop()
print('删除后的列表', names)  # 删除后的列表 ['勋悟空', '猪八戒']
names.pop(1) 
print('删除后的列表', names)  # 删除后的列表 ['勋悟空']
```
> pop不接受参数默认删除最后一个元素, pop可以接受一个int类型的参数,可以删除指定索引位置的元素

**remove**  
```python
names = ['勋悟空', '猪八戒', '沙和尚']
names.remove('勋悟空')
print('删除后的列表', names)  # 删除后的列表 ['猪八戒', '沙和尚']
```

#### 7.3 **元组高级**  

python的元组与列表类似,不同之处在于**元组的元素不能修改**,元组使用小括号,列表使用方括号
`names = ('勋悟空', 77, 99.99)`
      
**访问元组**
```python
names = ('勋悟空', 77, 99.99)
print(names[0])
```

**修改元组**  
python中不允许修改元组的数据,包括不能删除其中的元素  
**定义只有一个数据的元组**  
定义一个只有一个元素的元组,需要**在唯一的元素后写一个逗号**  
`oneTuple = ('卡卡西',)
`

#### 8.4 切片

切片是指操作的对象截取其中的一部分的操作,**字符串,列表,元组**都支持切片操作  
切片的语法:`[起始:结束:步长]`, `也可以简化使用[起始:结束]`  
注意: 选育器地区间从'起始'位开始,到'结束'位的前一位结束(不包含结束位本身),步长表示选取间隔

```python
s = '01234567'
print(s[4])  # 4   字符串中的第四个元素
print(s[1:7])  # 123456 包含下标1,不包含下标7
print(s[1:])  # 1234567 从下标1开始,取出 后面所有的元素(没有结束位置)
print(s[:4])  # 0123  从开始到 下标为4的前一个元素(没有开始位置)
print(s[1:5:2])  # 13 从下标为1开始,取到下标为5的前一个元素, 步长为2 (不包含结束位置本身)
```
#### 8.5 字典高级

##### **查看元素**  

除了使用key查找数据,还可以使用get来获取数据 

```python
info = {'name': '勋悟空', 'age': 3200}
print(info['name'])  # 勋悟空
# print(info['sex'])  # 如果key不存在,就会发生异常

print(info.get('sex'))   # None # 获取不存在的key, 获取到空的内容, 不会出现异常
print(info.get('sex', '男'))   # 男 # 获取不存在的key, 可以提供一个默认值

```

##### **修改元素**  

字典的每个元素中的数据是可以修改的, 只要通过key找到, 即可修改  
  
```python
info = {'name': '勋悟空', 'age': 3200}
print('修改前的字典为 %s:' % info)
info['age'] = 2000  # 为已存在的键赋值就是修改
```

#####  **添加元素**

字典的元素是可以添加, 通过key进行添加
```python
info = {'name': '勋悟空', 'age': 3200}
print('修改前的字典为 %s:' % info)
info['id'] = 10086  # 为不存在的键赋值就是添加
print('修改后的字典为 %s:' % info)  # 修改后的字典为 {'name': '勋悟空', 'age': 2000, 'id': 10086}:
```

##### **删除元素**  
- del
1. 删除字典中指定的一个元素
```python
info = {'name': '勋悟空', 'age': 3200}
del info['age']
print('删除age后的字典为 %s:' % info)  # 删除age后的字典为 {'name': '勋悟空'}:
```
2. 删除整个字典
```python
info = {'name': '勋悟空', 'age': 3200}
del info
print('删除info字典%s' % info)  # 报错: NameError: name 'info' is not defined
```
- clear
  - 清空字典,但是保留字典对象
```python
# 删除
info = {'name': '勋悟空', 'age': 3200}
info.clear()
print('清空info字典后为%s' % info)  # 清空info字典后为{}
```

##### **字典的遍历**  

1. 遍历字典的key
- 字典`.keys()`方法可以获取字典中所有key的值, key是一个变量的名字
```python
info = {'name': '勋悟空', 'age': 3200}
for key in info.keys():
    print(key)

# 输出结果
# name
# age
```
2. 遍历字典的value
- 字典`.values()`方法可以获取字典中所有的value值
````python
info = {'name': '勋悟空', 'age': 3200}
for value in info.values():
    print(value)

# 输出结果
# 勋悟空
# 3200
````
3. 遍历字典的key和value  
```python
info = {'name': '勋悟空', 'age': 3200}
for key, value in info.items():
    print(key, value)
# 输出结果
# name 勋悟空
# age 3200
```
4. 遍历字典的项/元素  
```python
info = {'name': '勋悟空', 'age': 3200}
for item in info.items():
    print(item)
# 输出结果
# ('name', '勋悟空')
# ('age', 3200)
```

### 9 函数  

#### 9.1 定义函数  

定义函数的格式如下:  
```
def 函数名():
    代码
```
示例:  
```python
# 定义函数,能够完场打印信息功能
def fun():
    print('欢迎来到红浪漫')
```
#### 9.2 调用函数

定义了函数之后, 就相当于有了一个具有某些功能的代码,想让这些代码能够执行, 需要调用它, 通过 **函数名()** 即可完成调用
```python
# 定义函数,能够完场打印信息功能
def fun():
    print('欢迎来到红浪漫')
    
    
# 定义完函数后, 函数不是自动执行的, 需要调用它才可以
fun()  # 欢迎来到红浪漫
```

#### 9.3 函数参数
```python
# 定义一个函数,进行两个数的加法运算
def add(a, b):
    c = a + b
    print(c)


# 调用函数 
# 位置传参
add(1, 2)

# 关键字传参(不推荐使用)
add(b = 200, a = 100)
```
注意点:  
- 在定义的函数的时候, 小括号里写等待赋值的变量
- 在调用函数的时候, 小括号里写真正要进行的运算的数据  
> 定义时小括号中的实参, 用来接收参数用的称为'形参'  
> 调用时小括号中的参数, 用来传递给函数调用的,称为'实参'

#### 9.4 函数返回值  

**返回值介绍**  
- 所谓的'返回值',就是程序中完成一件事情后,最后给调用者的结果
- 使用返回值的前提需求就是函数调用者想要在函数外使用计算结果

**带有返回值的函数**  
想要在函数中把结果返回给调用者,需要在函数中使用return  
示例:
```python
# 定义一个函数计算两个数的加法
def add(a, b):
    c = a + b
    return c


print(add(1, 2))  # 3
```

#### 9.5 局部变量

**什么时局部变量**  
> 局部变量, 就是在函数内部定义的变量  
> 其作用范围时这个函数内部, 即只能在这个函数中使用, 在函数的外部时不能使用的

#### 9.6 全局变量

如果一个变量,既能在一个函数中使用, 也能在其他函数中使用,这样的变量就是全局变量


### 10 文件

### 10.1 文件的打开于关闭

**打开文件/创建文件**  
在python中, 使用open函数,可以打开一个已经存在的文件, 或者创建一个新文件  
`open(文件路径, 访问模式)`  
示例:
```python
# 打开文件
f = open('test.txt', 'w')
```
说明:  
**文件路径**  
- 绝对路径: 指的时绝对位置, 完整的描述了目标的所在地, 所有目录层级关系是一目了然的
  - 例如: `E:\python`, 从电脑的盘符开始, 表示的就是一个绝对路径
- 相对路径: 是从当前文件所在的文件夹开始的路径
  - `test.txt`, 是当前问价夹查找`test.txt`文件
  - `./test.txt`, 也是在当前文件夹里查找`test.text`文件, `./`表示的是当前文件夹
  - `../test.txt`, 从当前文件夹的上一级问价里查找`test.txt`文件, `../`表示的是上一级问价夹  
  - `demo/test.txt`, 当前文件夹里查找`demo`这个文件夹,并在这个文件夹里查找`test.txt`文件

**访问模式**  

|访问模式|说明|
|:---|:---|
|r | 以只读的方式打开文件,文件的指针将会放在文件的开头,如果文件不存在,则报错,**这是默认模式**|
|w | 打开一个文件只用于吸入, 如果该文件已经存在则将其覆盖, 如果该文件不存在, 创建新文件|
|a | 打开一个文件用于追加,如果该文件已存在, 文件指针将会放在文件的结尾; 也就是说, 新的内容将会被写入到已有内容之后, 如果该文件不存在, 创建新文件进行写入| 
| r+ |打开一个文件用于读写, 文件指针将会放在文件的开头 |
| w+  | 打开一个文件用于读写,如果该文件已存在则将其覆盖,如果该文件不存在,创建新文件 |
| a+ | 打开一个文件用于读写,如果文件已经存在,文件指针将会放在文件的结尾,文件打开时会是追加模式; 如果该文件不存在, 创建新文件用于读写 |
| rb | 以二进制的格式打开一个文件用于只读,文件指针将会放在文件的开头 |
| wb | 以二进制的格式打开一个文件只用于写入,如果该文件已经存在则将其覆盖,如果该文件不存在,创建新文件 |
| ab | 以二进制格式打开一个文件用于追加, 如果该文件已存在, 文件指针将会放在文件的结尾, 也就是说, 新的内容将会写入到已有的内容之后, 如果该文件不存在, 创建新文件进行写入 |
| rb+ | 以二进制打开一个文件用于读写,文件指针将会放在文件的开头 |
| wb+ | 以二进制格式打开一个文件用于读写,如果该文件已存在则将其覆盖,如果该文件不存在,创建新文件|
| ab+ | 以二进制格式打开一个文件用于读写, 如果该文件已存在, 文件指针将会放在文件的结尾, 如果该文件不存在, 创建新文件用于读写 |

**文件的关闭**  
可以使用close函数对文件进行关闭
```python
fp = open('test.txt', 'w')

fp.close()
```

#### 10.2 文件的读写

**写数据(write)**  
使用write()可以完成向文件写入数据
```python
# 文件的读写
# 打开一个文件
f = open('test.txt', 'w')
# 向文件中写入数据
f.write('hello world')
# 关闭文件
f.close()
```
**读数据**
- read  
使用read()可以完成对文件数据的读取
```python
fp = open('test.txt', 'r')
# 默认情况下 read是一字节一字节的读效率比较低
content = fp.read()
print(content)
```
> 默认情况下 read是一字节一字节的读效率比较低
- readline  
使用readline()可以完成对文件的整行读取
```python
fp = open('test.txt', 'a')
# readline只能读取一行
content = fp.readline()
print(content)
```
> 默认秦凯给你下,readline只能读取一行

- readlines  
读取多行数据
```python
fp = open('test.txt', 'a')
content = fp.readlines()
print(content)
```
> `readlines`可以按照行来读取, 会将所有的数据都读取到, 并且以一个列表的形式返回  
> 列表的元素, 是一行一行的数据


#### 10.3 序列化和反序列化

通过文件操作, 我们可以将字符串写入到一个本地文件, 但是, 如果一个对象(例如列表, 字典, 元组等), 就无法直接写入到
一个文件里,需要对这歌对象进行序列化, 然后才能写入到文件里

设计一套协议, 按照某周规则, 将内存中的数据转换为字节序列保存到文, 这就是序列化, 反之, 从文件的字节序列恢复到内存中, 就是反序列化

> 对象 => 字节序列  === 序列化  
> 字节序列 => 对象 === 反序列化  

python提供了JSON这个模块用来实现数据的序列化和反序列化

**JSON模块**

JSON(JavaScriptObjectNotation, JS对象简谱)是一种轻量级的数据交互标准, JSON的本质是字符串  

**使用JSON实现序列化**  
JSON提供了dump和dumps方法,将一个对象进行序列化  
dumps方法的作用是把对象转换为字符串,它本身不具备将数据写入到文件的功能

```python
import json
file = open('names.txt', 'w')
names = ['勋悟空', '猪八戒', '沙和尚', '唐僧']

# file.write(names)  # 出错,不能直接将列表写入到文件里

# 可以调用 json 的 dupms 方法, 传入一个对象参数
result = json.dumps(names)

# dumps 方法得到的结果是一个字符串
print(type(result))  # <class 'str'>

# 可以将字符出啊写入到文件里
file.write(result)
```

- dump
在对象转换为字符串的同时,指定一个文件对象,然后把转换后的对象字符串写入到这文件中
```python
import json

file = open('names.txt', 'w')
names = ['勋悟空', '猪八戒', '沙和尚', '唐僧']
json.dump(names, file)

file.close()
```

**反序列化**  
JSON提供了load和loads方法,将一个对象进行序列化  
loads方法的作用是把字符串转换对象,它本身不具备将读取文件的功能
```python
import json
fp = open('names.txt', 'r')

content = fp.read()
print(content)
print(type(content))  # <class 'str'>
result = json.loads(content)
print(result)
print(type(result))  # <class 'list'>

```

- load
load 方法的作用是将文件对象的数据反序列化,返回一个反序列出来的对象
```python
import json
fp = open('names.txt', 'r')
result = json.load(fp)
print(result)
print(type(result))
fp.close()
```

### 11 异常

程序在运行过程中, 由于我们的编码不规范, 或者其他原因一些客观原因, 导致我们的程序无法继续运行, 此时, 程序就会出现异常, 如果我们不对异常进行处理, 程序可能会由于异常直接中断掉;
为了保证程序的健壮性,我们在程序设计里提出了异常处理这个概念

#### 11.1 读取异常异常

在读取一个文件是,如果这个文件不存在,则会爆出`FileNotFoundError`  
![文件不存在异常](./markimgs/img_2.png)

#### 11.2 异常的捕获

- 格式  
```
try:
    可能出现异常的代码
except 异常的类型: 
    友好的提示 
```
- 示例
```python
try:
    f = open('卡卡西.txt', 'r')
    print(f.read())
except FileNotFoundError:
    print('文件不存在')
```

















