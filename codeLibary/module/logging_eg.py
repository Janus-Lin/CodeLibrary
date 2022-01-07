"""
CodeLibrary.logging_eg
~~~~~~~~~~~~~~~~~~~~~~~

Function:  用于便捷记录日志且线程安全的模块

Crater: lin
CreateDate: 2022-01-06
"""
import logging

logging.basicConfig(filename="model_data\log.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(module)s: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S %p",
                    level=logging.DEBUG)

logging.critical("critical")
logging.fatal("fatal")
logging.error("error")
logging.warning("warning")
logging.info("info")
logging.debug("debug")
logging.log(8,"log")
