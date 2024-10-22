"""
hcfund-package.多线程
~~~~~~~~~~~~~~~~~~~~~~~

Function:
Python 界有条不成文的准则： 计算密集型任务适合多进程，IO 密集型任务适合多线程。
通常来说多线程相对于多进程有优势，因为创建一个进程开销比较大，然而因为在 python 中有 GIL 这把大锁的存在，
导致执行计算密集型任务时多线程实际只能是单线程。而且由于线程之间切换的开销导致多线程往往比实际的单线程还要慢，
所以在 python 中计算密集型任务通常使用多进程，因为各个进程有各自独立的 GIL，互不干扰。

而在 IO 密集型任务中，CPU 时常处于等待状态，操作系统需要频繁与外界环境进行交互，
如读写文件，在网络间通信等。在这期间 GIL 会被释放，因而就可以使用真正的多线程。

Crater: lin
CreateDate: 2024-10-21
"""
import time

from queue import Queue
from threading import Thread

from concurrent.futures import ThreadPoolExecutor
from joblib import Parallel, delayed, parallel_backend

NUM_SUB = 40000
P_NUM = 10


def sub_f(x, queue=None):
    """计算函数"""
    # time.sleep(5)
    result = 0
    for i in range(x):
        result += i
    # print(f"计算函数: {x}")

    if queue is not None:
        queue.put(result)  # 将结果放入队列

    return result


def normal(sub_f):
    """普通计算"""
    res = []
    for j in range(NUM_SUB):
        a = sub_f(j)
        res.append(a)
    return sum(res)


def thread(sub_f):
    """Thread 多线程计算"""
    threads = []
    results_queue = Queue()  # 创建结果队列

    # 创建并启动线程
    for j in range(NUM_SUB):
        t = Thread(target=sub_f, args=(j, results_queue))
        threads.append(t)
        t.start()

    # 等待所有线程完成
    for t in threads:
        t.join()

    # 从队列中获取结果
    res = [results_queue.get() for _ in range(NUM_SUB)]
    return sum(res)


def thread_pool(sub_f):
    """concurrent.futures"""
    with ThreadPoolExecutor(max_workers=P_NUM) as executor:
        res = [executor.submit(sub_f, j) for j in range(NUM_SUB)]
    return sum([r.result() for r in res])


def joblib_thread(sub_f):
    """joblib多线程计算"""
    with parallel_backend('threading', n_jobs=P_NUM):
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
    showtime(thread, sub_f, "thread")
    showtime(thread_pool, sub_f, "concurrent.futures")
    showtime(joblib_thread, sub_f, "joblib thread")


if __name__ == '__main__':
    main(sub_f)
