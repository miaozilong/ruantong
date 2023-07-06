import json
from flask import Flask, request, jsonify

# 指定静态页面地址
# static_folder表示静态目录
app = Flask(__name__, static_folder="static", static_url_path='/')


@app.route(rule='/sales', methods=['GET'])
def sales():
    # 附加题: 从excel表中读取数据
    r = jsonify([40, 20, 36, 10, 10, 15])
    return r


if __name__ == '__main__':
    app.run(port=50090, debug=True)
