"""
CodeLibrary.json_pickle
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-30
"""
"""
https://blog.csdn.net/whjkm/article/details/81159888

用于序列化的两个模块
- json，用于字符串 和 python数据类型间进行转换
- pickle，用于python特有的类型 和 python的数据类型间进行转换

Json模块提供了四个功能：dumps、dump、loads、load
pickle模块提供了四个功能：dumps、dump、loads、load

json.dumps 将 Python 对象编码成 JSON 字符串
json.loads 将已编码的 JSON 字符串解码为 Python 对象
json.dump和json.load,需要传入文件描述符，加上文件操作。
JSON内部的格式要注意，一个好的格式能够方便读取，可以用indent格式化。
"""
import pickle

data = {'k1': 123, 'k2': 'hello'}

p_str = pickle.dumps(data)
print(p_str)

with open('', 'w') as fp:
    pickle.dump(data, fp)

import json

j_str = json.dumps(data)
print(j_str)

with open('') as fp:
    json.dump(data, fp)
