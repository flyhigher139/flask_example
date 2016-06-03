#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, session, jsonify, current_app
from blinker import Namespace

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

my_signals = Namespace()
status_changed = my_signals.signal('model-saved')

ToDo = {
    'go_to_work': 'I will start my work',
    'go_home': 'I will have a rest and then write some flask app',
    'go_asleep': 'I will stop working and go to bed'
}

@status_changed.connect
def on_status_changed(sender, status, **extra):
    session['status'] = status
    session['to_do'] = ToDo.get(status, 'not assigned')

@app.route('/')
def home():
    return 'home'

@app.route('/work/')
def go_to_work():
    msg = 'I will go to work, and I just change my status to "go_to_work"'

    message, status = set_status(msg=msg, status='go_to_work')

    return jsonify(message=message, signal_callback=status)


def set_status(msg, status):
    message = {
        'msg': msg,
        'to_do': 'I do not know what to do, the signal will tell me'
    }

    status_changed.send(current_app._get_current_object(), status="go_to_work")

    status = get_status_callback()

    return message, status

def get_status_callback():
    status = session.get('status', 'unknown')
    to_do = session.get('to_do', 'unknown')
    current_state = {'status':status, 'to_do':to_do}

    return current_state



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)