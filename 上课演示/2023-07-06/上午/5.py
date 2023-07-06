from flask import Flask, request, jsonify
import json
import pymysql
import pandas as pd

# 将当前程序作为web app应用
# 配置static模式
# static_folder静态文件的路径
app = Flask(__name__, static_folder='static', static_url_path='/')


@app.route(rule='/sales', methods=['GET'])
def post_test():
    # 1. 连接数据库    2. 读取数据库的数据    3. 处理数据    4. 返回给前端
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='demo')
    df = pd.read_sql("select value from sale order by id", conn)
    sales_data = df['value'].tolist()
    r = jsonify(sales_data)
    conn.close()
    return r


if __name__ == '__main__':
    app.run(port=80, debug=True)
