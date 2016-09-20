#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import logging, json
import logging.config

with open('./logging_config.json') as f:
    s = f.read()
    logging_config = json.loads(s)

# logging_config = {}
try:
    logging.config.dictConfig(logging_config)

    logger = logging.getLogger('root')

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

except ValueError:
    print 'json config error'