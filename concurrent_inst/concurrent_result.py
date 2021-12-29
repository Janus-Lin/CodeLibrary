"""
CodeLibrary.concurrent_result
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-24
"""
import time
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor, as_completed

from concurrent_inst.tools import clock


def sleep(num, list1):
    time.sleep(1)
    res = num * 10
    list1.append(res)


def sleep2(num):
    time.sleep(1)
    res = num * 10
    return res


# 推荐
@clock
def conn_res_01(cal_count):
    """Manager().list()接受返回值"""
    m_list = Manager().list()  # 这是数据接收容器
    num_list = [i for i in range(cal_count)]
    with ProcessPoolExecutor(max_workers=8) as executer:
        for num in num_list:
            executer.submit(sleep, num, m_list)  # 数据容器传参
    print(m_list)

@clock
def conn_res_02(cal_count):
    """future.result()接受返回值"""
    num_list = [i for i in range(cal_count)]
    print(f'count: {len(num_list)}')
    pool_lis = []

    with ProcessPoolExecutor(max_workers=8) as executer:
        for num in num_list:
            future = executer.submit(sleep2, num)
            pool_lis.append(future)  # 不能调用future.result()，会等待计算结果，多进程作用
        res = [future.result() for future in pool_lis]
        print(res)

@clock
def conn_res_03(cal_count):
    """as_completed接受返回值"""
    num_list = [i for i in range(cal_count)]
    print(f'count: {len(num_list)}')

    with ProcessPoolExecutor(max_workers=8) as executer:
        futures = {executer.submit(sleep2, num): num for num in num_list}
        for future in as_completed(futures):
            num = futures[future]
            try:
                data = future.result()
            except Exception as exc:
                print(f'num: {num}, exc: {exc}')
            else:
                print(f'num: {num}, data: {data}')


@clock
def conn_res_04(cal_count):
    """map接受返回值"""
    num_list = [i for i in range(cal_count)]
    print(f'count: {len(num_list)}')

    with ProcessPoolExecutor(max_workers=8) as executer:
        # 返回一个生成器，保存的是每个线程处理完返回的结果。其中range序列中0-4交给线程池并发调用，当其中一个线程完成后，将5交给线程池处理，以此类推
        res = executer.map(sleep2, num_list)
        print(res)
    print(list(res))

@clock
def conn_res_05(cal_count):
    """map接受返回值"""
    num_list = [i for i in range(cal_count)]
    print(f'count: {len(num_list)}')

    with ProcessPoolExecutor(max_workers=8) as executer:
        for number, prime in zip(num_list, executer.map(sleep2, num_list)):
            print('%d is res: %s' % (number, prime))


if __name__ == '__main__':
    conn_res_01(16)
    conn_res_02(16)
    conn_res_03(16)
    conn_res_04(16)
    conn_res_05(16)
