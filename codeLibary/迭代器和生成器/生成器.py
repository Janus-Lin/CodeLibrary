"""
CodeLibrary.生成器
~~~~~~~~~~~~~~~~~~~~~~~

Function:

Crater: lin
CreateDate: 2022-01-07
"""


# 函数里只要有yield关键字，就是生成器函数
def func():
    return 1


def gen_func():
    yield 1
    yield 2
    yield 3


# 原始版
def fib(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a + b
        n += 1
    return re_list


#  假如当数据量非常大的时候，这样全部打印会消耗非常大的内存，下面使用yield，虽然同样是获取数据，但是它实际上是不消耗内存的
def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1
# 生成器表达式
a=[7,8,9]
ib=(i**2 for i in a)

if __name__ == '__main__':

    res = func()
    print(type(res))  # <class 'int'>    返回1

    gen = gen_func()
    print(type(gen))  # <class 'generator'>   返回的是一个生成器对象

    for value in gen:
        print(value)

    print(fib(4))

    for data in gen_fib(10):
        print(data)  # 1, 1

    for i in ib:
        print(i)
