"""
CodeLibrary.concurrent_sleep
~~~~~~~~~~~~~~~~~~~~~~~

Function: 配置与耗时

Crater: lin
CreateDate: 2021-12-24
"""
import concurrent.futures
import time


# import sys

def sleep(seconds):
    time.sleep(seconds)
    return seconds


def con_sleep_01():
    times = [1] * 10
    time0 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sleep, times)
    time1 = time.time()
    print('The time cost is: {}s'.format(time1 - time0))


def con_sleep_02(sleep_count):
    # if sys.argv[1] == '-t':
    #     times = [1] * int(sys.argv[2]) # 获取命令行的时间输入参数
    times = [1] * sleep_count
    time0 = time.time()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sleep, times)
    time1 = time.time()
    print('The time cost is: {}s'.format(time1 - time0))


def con_sleep_03(sleep_count):
    times = [1] * sleep_count
    time0 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(sleep, times)
    time1 = time.time()
    print('The time cost is: {}s'.format(time1 - time0))


def con_sleep_04(sleep_count):
    times = [1] * sleep_count
    time0 = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = executor.map(sleep, times)
    print('The total sleep cpu time is: {}s'.format(sum(results)))
    time1 = time.time()
    print('The time cost is: {}s'.format(time1 - time0))


if __name__ == '__main__':
    # 12核
    con_sleep_04(17)
