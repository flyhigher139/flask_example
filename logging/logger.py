#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging

# create logger
logger = logging.getLogger('simple_example')

# Set default log level
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARN)

ch2 = logging.FileHandler('logging.log')
ch2.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)
ch2.setFormatter(formatter)

# add ch to logger
# The final log level is the higher one between the default and the one in handler
logger.addHandler(ch)
logger.addHandler(ch2)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')