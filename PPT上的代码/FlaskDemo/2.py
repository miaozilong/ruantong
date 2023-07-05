from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route(rule='/get', methods=['GET'])
def get():
    method = request.method
    # get传参
    name = request.args.get('name')
    return name


@app.route(rule='/post', methods=['POST'])
def post():
    method = request.method
    # json 传参
    # If `as_text` is set to `True` the return value will be a decoded string.
    data = request.get_data(as_text=True)
    # 转为json对象
    jsonObj = json.loads(data)
    # json转Response
    r = jsonify(jsonObj)
    return r


if __name__ == '__main__':
    app.run(debug=True)
