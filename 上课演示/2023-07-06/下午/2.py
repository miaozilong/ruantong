from flask import Flask, request
import json

app = Flask(__name__)


# WEB请求方式:  最常见的为GET和POST
#   GET表示向服务端索取数据
#   POST表示将客户端数据发送给服务器
#   浏览器默认使用的是GET方式

@app.route(rule='/get_test', methods=['GET'])
def get_test():
    name = request.args.get('name')
    favorites = request.args.getlist('favorites')
    msg = '全民制作人们,大家好,我是' + name + "我喜欢" + favorites[0] + ',' + favorites[1] + ',' + favorites[2] + ',' + \
          favorites[3]
    return msg


# post请求中,一般使用post请求,传递数据
@app.route(rule='/post_test', methods=['POST'])
def post_test():
    # as_text为True表示需要编码
    jsonStr = request.get_data(as_text=True)
    jsonObj = json.loads(jsonStr)
    msg = 'POST请求'
    return msg


if __name__ == '__main__':
    app.run(port=50090, debug=True)
