"""
CodeLibrary.skills_perf
~~~~~~~~~~~~~~~~~~~~~~~

Function: 高性能技巧

Crater: lin
CreateDate: 2022-01-11
"""
# -------- 易混淆操作----------

# 有放回随机采样和无放回随机采样
import random
seq = [1,2,3,4,5,6,7,8]
print(random.choices(seq, k=8) ) # 长度为k的list，有放回采样
print(random.sample(seq, k=8))     # 长度为k的list，无放回采样


# lambda 函数的参数
x = 1
func = lambda y: x + y          # x的值在函数运行时被绑定
func = lambda y, x=x: x + y     # x的值在函数定义时被绑定
x = 2
print(func(2))
print(func(2))


import copy
x = [345,99]
print(id(x))
y = copy.copy(x)      # 只复制最顶层
print(id(y))
z = copy.deepcopy(x)  # 复制所有嵌套部分
print(id(z))

#  == 和 is
x == y  # 两引用对象是否有相同值
x is y  # 两引用是否指向同一对象

# 判断类型
a = 0
type(a) == int      # 忽略面向对象设计中的多态特征
isinstance(a, int)  # 考虑了面向对象设计中的多态特征

# List 后向索引: 前向索引时下标从0开始，如果反向索引也想从0开始可以使用~。
a = [1,2,3,4,5]
print(a[-1], a[-2], a[-3])
print(a[~0], a[~1], a[~2])

# ------- C/C++ 用户使用指南-----------
# C/C++ 的习惯是定义一个很大的数字，Python 中有 inf 和 -inf：
print(float('inf'))
print(float('-inf'))

import os
# Python 中的 os.path.join 会自动根据操作系统不同补充路径之间的 / 或 \ 分隔符：
a = os.path.join('usr', 'lib', 'local')
print(a)