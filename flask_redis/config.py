#!/usr/bin/env python
# -*- coding: utf-8 -*-
from celery import Celery

class Config(object):
    ########################
    # Celery Config
    ########################

    BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT=['json']
    CELERY_TIMEZONE = 'Asia/Shanghai'
    CELERY_ENABLE_UTC = True
    CELERY_IGNORE_RESULT = False


    @staticmethod
    def init_app(app):
        pass

def make_celery(app):
    celery = Celery(app.import_name, broker=app.config['BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery
