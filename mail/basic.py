#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask, request, redirect, url_for, current_app
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail()

class Config(object):
    # email server
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')


app.config.from_object(Config)
mail.init_app(app)


def send_mails(recipients, cc, mail_title, mail_body):
    msg = Message(mail_title)
    msg.body = mail_body

    msg.sender = current_app._get_current_object().config['MAIL_USERNAME']
    msg.recipients = recipients
    msg.cc = cc

    mail.send(msg)


@app.route('/')
def index():
    return 'This is a mail server'

@app.route('/mail/', methods=['GET', 'POST'])
def mail_view():
    if request.method == 'POST':
        recipients = request.form.get('recipients')
        recipients = [recipient.strip() for recipient in recipients.split(',')]

        cc = request.form.get('cc')
        cc = [cc.strip() for cc in cc.split(',')]

        title = request.form.get('title')
        body = request.form.get('body')

        send_mails(recipients, cc, title, body)
        return redirect(url_for('mail_view'))
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>Mail</title>
            <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
            <div class="container">
                <div class="col-md-10 col-md-offset-1">
                <h3>Send Mails</h3><hr/>
                <form method="POST">
                    <div class="form-group">
                        <label>Receivers:</label><input type="text", name="recipients" class="form-control" >
                    </div>
                    <div class="form-group">
                        <label>Cc:</label><input type="text", name="cc" class="form-control" >
                    </div>
                    <div class="form-group">
                        <label>Title:</label>
                        <input type="text", name="title" class="form-control" >
                    </div>
                    <div class="form-group">
                        <label>Body:</label>
                        <textarea class="form-control" rows="6" name="body"></textarea>
                    </div>
                    <div class="form-group">
                        <button type="submit" value="Submit" class="btn btn-primary">Submit</button>
                    </div>
                </form>
                </div>
            </div>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
