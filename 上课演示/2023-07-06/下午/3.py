import json

from flask import Flask, request, jsonify

# 指定静态页面地址
# static_folder表示静态目录
app = Flask(__name__, static_folder="static", static_url_path='/')

# post请求中,一般使用post请求,传递数据
@app.route(rule='/login', methods=['POST'])
def post_test():
    # as_text为True表示需要编码
    jsonStr = request.get_data(as_text=True)
    jsonObj = json.loads(jsonStr)
    username = jsonObj["username"]
    password = jsonObj["password"]
    login_flag = False
    if username == '蔡徐坤' and password == '2.5':
        login_flag = True
    r = jsonify({'success': login_flag})
    return r


if __name__ == '__main__':
    app.run(port=50090, debug=True)
