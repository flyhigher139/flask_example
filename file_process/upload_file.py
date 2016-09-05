#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask, request, redirect, url_for, jsonify
from flask.views import MethodView
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_TXT_EXTENSIONS = ('txt', 'py')

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads').replace('\\', '/')

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename, file_filter=ALLOWED_EXTENSIONS):
    return '.' in filename and filename.rsplit('.', 1)[1] in file_filter

@app.route('/')
def hello():
    data = {
        '/upload/': "upload files with extension ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']",
        '/upload-api/': "upload files api, support files are with  extension ['txt', 'py']"
    }
    return jsonify(data)
    

@app.route('/response/')
def response_page():
    if request.args.get('res') == 'succeeded':
        return 'Succeed'
    elif request.args.get('res') == 'failed':
        return "File type not in ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif']"
    elif request.args.get('res') == 'failed2':
        return "File type not in ['txt', 'py']"
    elif request.args.get('res') == 'no_file':
        return 'No uploaded files'
    else:
        return 'Nothing to response'

@app.route('/upload/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        
        if not file or file.filename == '':
            # return 'No file uploaded'
            return redirect(url_for('response_page')+'?res=no_file')

        if allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('response_page')+'?res=succeeded')

        return redirect(url_for('response_page')+'?res=failed')

    return '''
                <!doctype html>
                <title>Upload new File</title>
                <h1>Upload new File</h1>
                <form action="" method=post enctype=multipart/form-data>
                  <p><input type=file name=file>
                     <input type=submit value=Upload>
                </form>
            '''

class FileView(MethodView):
    def get(self):
        return 'Upload file in Postman with POST method'

    def post(self):
        file = request.files.get('file')
        
        if not file or file.filename == '':
            return 'No file uploaded', 400
            

        if allowed_file(file.filename, file_filter=ALLOWED_TXT_EXTENSIONS):
            data = {'content':file.read()}
            return jsonify(data)

        return "File type not in ['txt', 'py']", 400


app.add_url_rule('/upload-api/', view_func=FileView.as_view('upload_view'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)