"""
CodeLibrary.tools
~~~~~~~~~~~~~~~~~~~~~~~

Function: 功能性技巧

Crater: lin
CreateDate: 2022-01-07
"""

# 一行代码定义List
x = [1,2,3,4]
out = [item**2 for item in x]
print(out)

# Lambda表达式用于在Python中创建小型，一次性和匿名函数对象。它能替你创建一个函数。
double = lambda x: x * 2
print(double(5))

# map通过对列表中每个元素执行某种操作并将其转换为新列表
seq = [1, 2, 3, 4, 5]
result = list(map(lambda var: var*2, seq))
print(result)

# Filter函数接受一个列表和一条规则，就像map一样，但它通过比较每个元素和布尔过滤规则来返回原始列表的一个子集。
seq = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x > 2, seq))
print(result)

print('-'*10)
import numpy as np
from numpy import array
# Arange返回给定步长的等差列表。它的三个参数start、stop、step分别表示起始值，结束值和步长，
# 请注意，stop点是一个“截止”值，因此它不会包含在数组输出中。
# np.arange(start, stop, step)
a = np.arange(3, 7, 2)
print(a)

b = array([3, 5])
print(b)

# Linspace和Arrange非常相似，但略有不同。
# Linspace以指定数目均匀分割区间。所以给定区间start和end，以及等分分割点数目num，linspace将返回一个NumPy数组。
# 这对绘图时数据可视化和声明坐标轴特别有用。
# np.linspace(start, stop, num)
a = np.linspace(2.0, 3.0, num=5)
b = array([ 2.0,  2.25,  2.5,  2.75, 3.0])
print(a, b)

# Axis代表什么？
# 在Pandas中，删除一列或在NumPy矩阵中求和值时，可能会遇到Axis
# 如果你想处理列，将Axis设置为1，如果你想要处理行，将其设置为0。
import pandas as pd
# Apply将一个函数应用于指定轴上的每一个元素。使用Apply，
# 可以将DataFrame列（是一个Series）的值进行格式设置和操作，不用循环，非常有用！
df = pd.DataFrame([[4, 9],] * 3, columns=[ 'A' ,  'B' ])
df1 = df.apply(np.sqrt)
df2 = df.apply(np.sum, axis=1)
print(df)
print(df1)
print(df2)

