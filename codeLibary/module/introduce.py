"""
CodeLibrary.introduce
~~~~~~~~~~~~~~~~~~~~~

Function: 模块介绍

Crater: lin
CreateDate: 2021-12-29
"""

# 概念
'''
Python Module(模块)，就是一个保存了Python代码的文件。模块能定义函数，类和变量。模块里也能包含可执行的代码。
文件名就是模块名加上后缀.py，在模块内部，模块名存储在全局变量__name__中，是一个string，可以直接在module中通过__name__引用到module name。

模块分为三种：自定义模块、内置标准模块（又称标准库）、开源模块
'''

# 导入模块
'''
import: 使客户端（导入者）以一个整体获取一个模块。
from:容许客户端从一个模块文件中获取特定的变量名。
reload:在不中止Python程序的情况下，提供了一个重新载入模块文件代码的方法。

import module
from module.xx.xx import xx
from module.xx.xx import xx as rename  # 推荐方便代码重构
from module.xx.xx import *
'''

# 获取路径
import sys

for i in sys.path:
    print(i)

# S:\Python 3.5.1\lib                  #存放标准库
# S:\Python 3.5.1\lib\site-packages    #存放第三方库，扩充库

# 添加路径
import sys
import os

pre_path = os.path.abspath('../')
sys.path.append(pre_path)
