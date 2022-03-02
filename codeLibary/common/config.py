"""
CodeLibrary.config
~~~~~~~~~~~~~~~~~~

Function: 日志配置文件

Crater: lin
CreateDate: 2022-01-11
"""
from codeLibary.config import CORE_LOG, COMPUTE_LOG, DRIVERS_LOG

LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        },
        'common': {
            'format': '%(asctime)s - %(name)s - %(filename)s - %(funcName)s - %(lineno)s - %(levelname)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'common',
            'stream': 'ext://sys.stdout',
        },
        'drivers_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 10000000,
            'backupCount': 5,
            'formatter': 'common',
            'filename': DRIVERS_LOG,
            'encoding': 'utf-8',
            # 'when': 'W0',   # 每周一切割日志

        },
        'core_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 10000000,
            'backupCount': 5,
            'formatter': 'common',
            'filename': CORE_LOG,
            'encoding': 'utf-8',
            # 'when': 'W0',  # 每周一切割日志
        },
        'compute_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 10000000,
            'backupCount': 5,
            'formatter': 'common',
            'filename': COMPUTE_LOG,
            'encoding': 'utf-8',
            # 'when': 'W0',  # 每周一切割日志
        },
    },
    'loggers': {
        'console': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': 0
        },
        'drivers': {
            'level': 'INFO',
            'handlers': ['drivers_handler', 'console'],
            'propagate': 0
        },
        'core': {
            'level': 'INFO',
            'handlers': ['core_handler', 'console'],
            'propagate': 0
        },
        'compute': {
            'level': 'INFO',
            'handlers': ['compute_handler', 'console'],
            'propagate': 0
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['console']
    }
}
