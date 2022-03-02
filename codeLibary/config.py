"""
CodeLibrary.config
~~~~~~~~~~~~~~~~~~~~~~~

Function: 全局config

Crater: lin
CreateDate: 2022-01-11
"""
import os

# log文件输出位置
DRIVERS_LOG = os.getenv('DRIVERS_LOG', '/tmp/drivers.log')
CORE_LOG = os.getenv('CORE_LOG', '/tmp/core.log')
COMPUTE_LOG = os.getenv('COMPUTE_LOG', '/tmp/compute.log')