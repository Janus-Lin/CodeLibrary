"""
CodeLibrary.computer_cpu
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2021-12-24
"""
import psutil
a = psutil.cpu_count(logical=False)
b = psutil.cpu_count(logical=True)
print(f'物理核: {a}')
print(f'逻辑核: {b}')
