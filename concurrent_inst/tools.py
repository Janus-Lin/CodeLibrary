"""
CodeLibrary.tools
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-28
"""
import time
import functools
# https://zhuanlan.zhihu.com/p/110201563
def clock(func):
    """this is outer clock function"""
    @functools.wraps(func)  # --> 4
    def clocked(*args, **kwargs):  # -- 1
        """this is inner clocked function"""
        start_time = time.time()
        result = func(*args, **kwargs)  # --> 2
        time_cost = time.time() - start_time
        print(f'func: {func.__name__}, time_cost: {time_cost}')
        return result
    return clocked  # --> 3


if __name__ == '__main__':
    pass