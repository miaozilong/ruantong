from flask import Flask, request, jsonify, send_file
import json
import pandas as pd
import pymysql

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/")


@app.route('/', methods=['GET'])
def index():
    return send_file("./static/index.html")


@app.route('/login', methods=['POST'])
def login():
    data = request.get_data(as_text=True)
    jsonObj = json.loads(data)
    success = False
    if jsonObj["username"] == 'abc' and jsonObj["password"] == '123':
        success = True
    r = jsonify({'success': success})
    return r

@app.route('/getSales', methods=['GET'])
def getSales():
    r = jsonify([5, 40, 36, 10, 10, 20])
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='root', db='demo')
    df = pd.read_sql("select value from sale", conn)
    data = df["value"].tolist()
    r = jsonify(data)
    return r


if __name__ == '__main__':
    app.run(debug=True)
