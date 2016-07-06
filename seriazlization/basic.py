from flask import Flask, jsonify, request
from flask.views import MethodView

app = Flask(__name__)

@app.route('/list/')
def test_list():
    data = [{'a':1, 'b':2}, {'c':3, 'd':4}]
    return jsonify(result=data)

@app.route('/dict1/')
def test_dict1():
    data = {'a':1, 'b':2, 'c':3}
    return jsonify(data)

@app.route('/dict2/')
def test_dict2():
    data = {'a':1, 'b':2, 'c':3}
    return jsonify(**data)

@app.route('/dict3/')
def test_dict3():
    data = {'a':1, 'b':2, 'c':3}
    return jsonify(result=data)

class TestAPIView(MethodView):
    def get(self):
        data = {'a':1, 'b':2, 'c':3}
        return jsonify(data)

    def post(self):
        data = request.get_json()
        return jsonify(data)

    def put(self):
        data = request.get_json()
        return jsonify(data)

    def patch(self):
        data = request.get_json()
        return jsonify(data)

app.add_url_rule('/method-view/', view_func=TestAPIView.as_view('test_api_view'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)