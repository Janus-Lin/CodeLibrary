"""
hcfund-package.eeeeeeeeeee
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2024-10-18
"""
import time
from multiprocessing import Pool
from concurrent.futures import ProcessPoolExecutor
from joblib import Parallel, delayed, parallel_backend


NUM_SUB = 40000
P_NUM = 10


def sub_f(x):
    """计算函数"""
    # time.sleep(5)
    result = 0
    for i in range(x):
        result += i
    # print(f"计算函数: {x}")
    return result


def normal(sub_f):
    """普通计算"""
    res = []
    for j in range(NUM_SUB):
        a = sub_f(j)
        res.append(a)
    return sum(res)


def asy(sub_f):
    """multiprocessing async 更加灵活，适合需要并行处理多个独立任务的场景，可以根据需要选择处理的顺序"""
    with Pool(processes=P_NUM) as p:
        result = []
        for j in range(NUM_SUB):
            a = p.apply_async(sub_f, args=(j,))
            result.append(a)
        res = [j.get() for j in result]
    return sum(res)


def mp(sub_f):
    """multiprocessing map 更加简洁，适合需要对多个输入进行相同处理的场景，使用更简单"""
    with Pool(processes=P_NUM) as p:
        res = p.map(sub_f, list(range(NUM_SUB)))
    return sum(res)


def concurrent_futures(sub_f):
    """concurrent.futures"""
    with ProcessPoolExecutor(max_workers=P_NUM) as executor:
        res = executor.map(sub_f, list(range(NUM_SUB)))

    return sum([r for r in res])


def joblib_process(sub_f):
    """joblib多进程计算"""
    with parallel_backend("multiprocessing", n_jobs=P_NUM):
        res = Parallel()(delayed(sub_f)(j) for j in range(NUM_SUB))
    return sum(res)


def showtime(f, sub_f, name):
    """计时函数"""
    start_time = time.time()
    res = f(sub_f)
    print("{} time: {:.4f}s".format(name, time.time() - start_time), f"res: {res}")


def main(sub_f):
    print("------ 单进程 ------")
    showtime(normal, sub_f, "normal")

    print("------ 多进程 ------")
    showtime(mp, sub_f, "pool")
    showtime(asy, sub_f, "async")
    showtime(concurrent_futures, sub_f, "concurrent_futures")
    showtime(joblib_process, sub_f, "joblib multiprocess")


if __name__ == '__main__':
    main(sub_f)
