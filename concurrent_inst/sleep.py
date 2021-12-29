"""
CodeLibrary.sleep
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-24
"""
import time

def sleep(seconds):
    time.sleep(seconds)

if __name__ == '__main__':
    times = [1] * 10
    time0 = time.time()
    for t in times:
        sleep(t)
    time1 = time.time()
    print ('The time cost is: {}s'.format(time1 - time0))
