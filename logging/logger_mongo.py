#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging
from log4mongo.handlers import MongoHandler

logger = logging.getLogger('mongo_example')

mon = MongoHandler(host='localhost', database_name='mongo_logs')
mon.setLevel(logging.WARNING)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

logger.addHandler(mon)
logger.addHandler(ch)


logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')