#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, redirect, url_for, jsonify
from config import Config, make_celery


app = Flask(__name__)
app.config.from_object(Config)

celery_app = make_celery(app)


@celery_app.task(name='app.test_celery')
def test_celery():
    print 'hello, world'

@celery_app.task(name='app.math_add')
def add_task(a, b):
    print a+b



@app.route('/')
def index():
    return 'hello, world'

@app.route('/tasks/test-celery/')
def test_celery_run():
    test_celery.delay()
    return 'checkout shell to get test result'

@app.route('/tasks/add/<int:a>/plus/<int:b>')
def add_number(a, b):
    add_task.delay(a, b)
     
    return 'checkout shell to get test result'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')