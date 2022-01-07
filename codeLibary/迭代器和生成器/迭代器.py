"""
CodeLibrary.迭代器
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2022-01-06
"""
# Python中 list，truple，str，dict这些都可以被迭代，但他们并不是迭代器。为什么？
#
# 因为和迭代器相比有一个很大的不同，list/truple/map/dict这些数据的大小是确定的，也就是说有多少事可知的。
# 但迭代器不是，迭代器不知道要执行多少次，所以可以理解为不知道有多少个元素，每调用一次next()，就会往下走一步，是惰性的。

from collections.abc import Iterable, Iterator

a = [1, 2, ]

print(isinstance(a, Iterable))  # True    list是可迭代的
print(isinstance(a, Iterator))  # False   list不是迭代器

a = [1, 2, ]

iter_rator = iter(a)
print(isinstance(a, Iterable))  # True         可迭代的
print(isinstance(iter_rator, Iterator))  # True        迭代器

print(isinstance((x for x in range(10)), Iterator))  # True


# 凡是可以for循环的，都是Iterable
# 凡是可以next()的，都是Iterator
# list，truple，dict，str，都是Itrable不是Iterator，但可以通过iter()函数获得一个Iterator对象

# 1、迭代器: 迭代器只不过是一个实现迭代器协议的容器对象。
# 特点：
# 访问者不需要关心迭代器内部的结构，仅需通过next()方法不断去取下一个内容
# 不能随机访问集合中的某个值 ，只能从头到尾依次访问
# 访问到一半时不能往回退
# 便于循环比较大的数据集合，节省内存


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


# 自定义迭代器
class MyIterator(Iterator):  # 如果不继承Iterator，则必须实现__iter__方法
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0  # 初始化索引位置

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["derek1", "derek2", "derek3"])
    my_itor = iter(company)

    print(next(my_itor))  # derek1
    print(next(my_itor))  # derek2
    print(next(my_itor))  # derek3

    for item in company:
        print(item)  # derek1  derek2  derek3
