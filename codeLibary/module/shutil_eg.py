"""
CodeLibrary.shutil_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function: 高级的 文件、文件夹、压缩包 处理模块

Crater: lin
CreateDate: 2022-01-06
"""

import shutil

# 将文件内容拷贝到另一个文件中
#shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))


import commands

result = commands.getoutput('cmd')