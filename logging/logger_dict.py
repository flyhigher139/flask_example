#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.config

config = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
        'file': {
            'class': 'logging.FileHandler',
            'filename': 'logging.log',
            'level': 'DEBUG',
            'formatter': 'simple'
        },
    },
    'loggers':{
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
            # 'propagate': True,
        },
        'simple': {
            'handlers': ['console', 'file'],
            'level': 'WARN',
        }
    }
}

logging.config.dictConfig(config)


print 'logger:'
logger = logging.getLogger('root')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')


print 'logger2:'
logger2 = logging.getLogger('simple')

logger2.debug('debug message')
logger2.info('info message')
logger2.warn('warn message')
logger2.error('error message')
logger2.critical('critical message')
