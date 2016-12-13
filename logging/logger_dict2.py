#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
import logging.config

config = {
    'version': 1,
    'root': {
        'level': 'NOTSET',
        'handlers': ['console', 'file', 'mongodb'],
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'stream': 'ext://sys.stdout',
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'detailed',
            'filename': 'info.log',
            'mode': 'a',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'smtp': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'alerts@calazan.com',
            'toaddrs': ['admin@calazan.com', 'support@calazan.com'],
            'subject': '[My Project] Error encountered.',
        },
        'mongodb': {
            'class': 'log4mongo.handlers.MongoHandler',
            'level': 'DEBUG',
            'host': 'localhost',
            'port': 27017,
            'database_name': 'myproject',
            'collection': 'logs',
            # 'username': 'logger',
            # 'password': 'password',
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(module)-17s line:%(lineno)-4d ' \
            '%(levelname)-8s %(message)s',
        },
        'email': {
            'format': 'Timestamp: %(asctime)s\nModule: %(module)s\n' \
            'Line: %(lineno)d\nMessage: %(message)s',
        },
    },
}

logging.config.dictConfig(config)


print 'logger:'
logger = logging.getLogger('root')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

