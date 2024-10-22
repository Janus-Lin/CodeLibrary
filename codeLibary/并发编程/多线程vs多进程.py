"""
hcfund-package.sdasdasdas
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2024-10-18
"""
import time

from joblib import Parallel, delayed, parallel_backend, cpu_count





NUM_SUB = 40000
P_NUM = 10


def sub_f(x, queue=None):
    """计算函数"""
    result = 0
    for i in range(x):
        result += i
    # print(f"计算函数: {x}")

    if queue is not None:
        queue.put(result)  # 将结果放入队列

    return result


def normal(sub_f):
    """普通计算"""
    result = []
    for j in range(NUM_SUB):
        a = sub_f(j)
        result.append(a)
    return sum(result)


def joblib_thread(sub_f):
    """joblib多线程计算"""
    with parallel_backend('threading', n_jobs=P_NUM):
        res = Parallel()(delayed(sub_f)(j) for j in range(NUM_SUB))
    return sum(res)


def joblib_process(sub_f):
    """joblib多进程计算"""
    with parallel_backend("multiprocessing", n_jobs=P_NUM):
        res = Parallel()(delayed(sub_f)(j) for j in range(NUM_SUB))
    return sum(res)


def joblib_loky(sub_f):
    """joblib多进程计算"""
    with parallel_backend("loky", n_jobs=P_NUM):
        res = Parallel()(delayed(sub_f)(j) for j in range(NUM_SUB))
    return sum(res)


def showtime(f, sub_f, name):
    """计时函数"""
    start_time = time.time()
    res = f(sub_f)
    print("{} time: {:.4f}s".format(name, time.time() - start_time), f"res: {res}")


def main(sub_f):
    print("----- 单线程 ------")
    showtime(normal, sub_f, "normal")

    print("----- 多线程 -----")
    showtime(joblib_thread, sub_f, "joblib thread")

    print("----- 多进程 -----")
    showtime(joblib_process, sub_f, "joblib multiprocess")
    showtime(joblib_loky, sub_f, "joblib loky")


if __name__ == '__main__':
    # 获取当前系统的cpu核心数
    n_cores = cpu_count()
    print(f'系统的核心数是：{n_cores}')

    main(sub_f)
