"""
CodeLibrary.pickle
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2022-01-11
"""
import pickle
'''
pickle 模块提供了以下 4 个函数供我们使用：
dumps()：将 Python 中的对象序列化成二进制对象，并返回；
loads()：读取给定的二进制对象数据，并将其转换为 Python 对象；
dump()：将 Python 中的对象序列化成二进制对象，并写入文件；
load()：读取指定的序列化数据文件，并返回对象。

以上这 4 个函数可以分成两类，其中 dumps 和 loads 实现基于内存的 Python 对象与二进制互转；dump 和 load 实现基于文件的 Python 对象与二进制互转。
'''
tup1 = ('I love Python', {1,2,3}, None)
p1 = pickle.dumps(tup1)
print(f'二进制对象: {p1}')

t2 = pickle.loads(p1)
print(f'Python对象: {t2}')

# 转换到指定的二进制文件中，要求该文件必须是以"wb"的打开方式进行操作。
import pickle
tup1 = ('I love Python', {1,2,3}, None)
#使用 dumps() 函数将 tup1 转成 p1
with open ("a.txt", 'wb') as f: #打开文件
    pickle.dump(tup1, f) #用 dump 函数将 Python 对象转成二进制对象文件
with open ("a.txt", 'rb') as f: #打开文件
    t3 = pickle.load(f) #将二进制文件对象转换成 Python 对象
    print(t3)

'''
看似强大的 pickle 模块，其实也有它的短板，即 pickle 不支持并发地访问持久性对象，在复杂的系统环境下，尤其是读取海量数据时，
使用 pickle 会使整个系统的I/O读取性能成为瓶颈。这种情况下，可以使用 ZODB。

ZODB 是一个健壮的、多用户的和面向对象的数据库系统，专门用于存储 Python 语言中的对象数据，它能够存储和管理任意复杂的 Python 对象，
并支持事务操作和并发控制。并且，ZODB 也是在 Python 的序列化操作基础之上实现的，因此要想有效地使用 ZODB，必须先学好 pickle。
'''