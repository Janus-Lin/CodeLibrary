"""
CodeLibrary.skills_logic
~~~~~~~~~~~~~~~~~~~~~~~

Function: 逻辑性技巧

Crater: lin
CreateDate: 2022-01-11
"""

# any、all
x = [True, True, False]

if any(x):
    print("至少有一个True")

if all(x):
    print("全是True")

if any(x) and not all(x):
    print("至少一个True和一个False")


from collections import OrderedDict, Counter
#  collections 模块[1]。这个方便的附加组件为你提供了更多的数据类型。
# 记住键的添加顺序！
x = OrderedDict(a=1, b=2, c=3)
print(x)

# 统计每个字符出现的频率
y = Counter("Hello World!")
print(y)


dir()
a = dir("Hello World")
print(a)
b = dir(dir)
print(b)

# 做个尝试
# emoji[3] 是日本在无线通信中所使用的视觉情感符号，绘指图画，文字指的则是字符，可用来代表多种表情，如笑脸表示笑、蛋糕表示食物等。
# 在中国大陆，emoji通常叫做“小黄脸”，或者直称emoji。
from emoji import emojize
print(emojize(":thumbs_up:"))


'''
Python 的inspect模块[7]非常适合了解幕后发生的事情。你甚至可以调用它自己的方法！下面的代码示例inspect.getsource() 
用于打印自己的源代码。inspect.getmodule() 还用于打印定义它的模块。
最后一行代码打印出它自己的行号。
'''
import inspect
print(inspect.getsource(inspect.getsource))
print(inspect.getmodule(inspect.getmodule))
print(inspect.currentframe().f_lineno)

'''
kwargs

在学习任何语言时，都会有许多里程碑。使用 Python 并理解神秘的**kwargs语法可能算作一个重要的里程碑。

字典对象前面的双星号**kwargs[9]允许你将该字典的内容作为命名参数传递给函数。

字典的键是参数名称，值是传递给函数的值。你甚至不需要调用它kwargs！
'''
dictionary = {"a": 1, "b": 2}
def someFunction(a, b):
    print(a + b)
    return
# 这些做同样的事情:
someFunction(**dictionary)
someFunction(a=1, b=2)

'''
pprint: 结构化输出

Python 的默认print函数完成了它的工作。但是如果尝试使用print函数打印出任何大的嵌套对象，其结果相当难看。
这个标准库的漂亮打印模块pprint[15]可以以易于阅读的格式打印出复杂的结构化对象。
'''
import requests
import pprint
url = 'https://randomuser.me/api/?results=1'
users = requests.get(url).json()
print(users)
pprint.pprint(users)

'''
该zip()内置函数需要一系列可迭代的对象，并返回一个元组列表中。每个元组按位置索引对输入对象的元素进行分组。
'''
keys = ['a', 'b', 'c']
vals = [1, 2, 3]
zipped = dict(zip(keys, vals))
print(zipped)