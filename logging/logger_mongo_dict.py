#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.config
from log4mongo.handlers import MongoHandler

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
        'mongo': {
            'class': 'log4mongo.handlers.MongoHandler',
            'host': 'localhost', 
            # 'port': 27017,
            'database_name': 'mongo_logs2',
            # 'collection': 'logs',
            'level': 'DEBUG',
        },
        # 'mongo': {
        #     'class': 'log4mongo.handlers.MongoHandler',
        #     'level': 'DEBUG',
        #     'host': 'localhost',
        #     'port': 27017,
        #     'database_name': 'myproject',
        #     'collection': 'logs',
        #     # 'username': 'logger',
        #     # 'password': 'password',
        # },
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
        },
        'mongo': {
            'handlers': ['console', 'mongo'],
            'level': 'DEBUG',
        }
    }
}

logging.config.dictConfig(config)


# print 'logger:'
# logger = logging.getLogger('root')

# logger.debug('debug message')
# logger.info('info message')
# logger.warn('warn message')
# logger.error('error message')
# logger.critical('critical message')


# print 'logger2:'
# logger2 = logging.getLogger('simple')

# logger2.debug('debug message')
# logger2.info('info message')
# logger2.warn('warn message')
# logger2.error('error message')
# logger2.critical('critical message')

print 'logger3:'
logger2 = logging.getLogger('mongo')

logger2.debug('debug message')
logger2.info('info message')
logger2.warn('warn message')
logger2.error('error message')
logger2.critical('critical message')
