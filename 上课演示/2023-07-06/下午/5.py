import json
import pymysql
from flask import Flask, request, jsonify
import pandas as pd

# 指定静态页面地址
# static_folder表示静态目录
app = Flask(__name__, static_folder="static", static_url_path='/')


@app.route(rule='/sales', methods=['GET'])
def sales():
    # 1. 创建数据库连接          2. 使用pandas从数据库中获取数据       3. 整理数据     4. 返回给前端
    connect = pymysql.Connect(host='127.0.0.1', port=3306, user='root', password='root', database='demo')
    sql = 'select value from sale order by id'
    df = pd.read_sql(sql, connect)
    value_list = df['value'].tolist()
    r = jsonify(value_list)
    connect.close()
    return r


if __name__ == '__main__':
    app.run(port=50090, debug=True)
