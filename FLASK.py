from loguru import logger as log
from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__, template_folder="templates", static_folder="static", static_url_path="/static")
app.debug = True
log.add('file_{time:YYYY-MM-DD}.log', format="{name} {level} {message}", level="TRACE", rotation='5 MB',
        encoding='utf-8')


@app.route('/api', methods=['GET', 'POST'])
def api():
    # url传参
    name = request.args.get('name', '')
    # json 传参
    data = request.get_data(as_text=True)
    # 转为json对象
    jsonObj = json.loads(data)
    # json转Response
    r = jsonify(jsonObj)
    return r


@app.route('/')
def index():
    return send_file("./static/index.html")


if __name__ == '__main__':
    app.run()
