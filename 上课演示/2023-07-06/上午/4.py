from flask import Flask, request, jsonify
import json

# 将当前程序作为web app应用
# 配置static模式
# static_folder静态文件的路径
app = Flask(__name__,static_folder='static',static_url_path='/')

@app.route(rule='/sales', methods=['GET'])
def post_test():
    # 附加题: 从excel表中读取这些数据
    sales_data = [20, 20, 30, 10, 10, 15]
    r = jsonify(sales_data)
    return r


if __name__ == '__main__':
    app.run(port=80, debug=True)
