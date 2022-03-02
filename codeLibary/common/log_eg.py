"""
CodeLibrary.log_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function: 

Crater: lin
CreateDate: 2022-01-11
"""
from codeLibary.common.log import compute_logger
from codeLibary.common.log import core_logger
from codeLibary.common.log import drivers_logger


compute_logger.info(f'compute_logger.info')
core_logger.info(f'core_logger.info')
drivers_logger.info(f'drivers_logger.info')