from flask import Flask, request, jsonify
import json

# 将当前程序作为web app应用
# 配置static模式
# static_folder静态文件的路径
app = Flask(__name__,static_folder='static',static_url_path='/')

@app.route(rule='/login', methods=['POST'])
def post_test():
    jsonStr = request.get_data(as_text=True)
    jsonObj = json.loads(jsonStr)
    username = jsonObj['username']
    password = jsonObj['password']
    login_flag = False
    if username == '蔡徐坤' and password == 'ctrl':
        login_flag = True
    r = jsonify({"success": login_flag})
    return r


if __name__ == '__main__':
    app.run(port=80, debug=True)
