"""
CodeLibrary.log
~~~~~~~~~~~~~~~

Function: 多文件日志输出

Crater: lin
CreateDate: 2022-01-11
"""
import logging
import logging.config
from config import LOG_CONFIG

logging.config.dictConfig(LOG_CONFIG)


def get_logger(log_name):
    return logging.getLogger(log_name)


drivers_logger = get_logger('drivers')
compute_logger = get_logger('compute')
core_logger = get_logger('core')
