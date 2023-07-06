from flask import Flask, request
import json

# 将当前程序作为web app应用
app = Flask(__name__)


# rule表示访问的路径
# methods 表示接受的请求方式
#       GET POST    HEAD PUT PATCH   DELETE...
#       浏览器的支持情况:   新浏览器都支持,旧浏览器支持GET和POST 其他不支持
#       浏览器默认使用GET方式,如果直接使用URL方式,就是使用的GET方式
@app.route(rule='/')
def hello_world():
    msg = 'Hello World!  <br /> Again!'
    return msg


@app.route(rule='/get_test', methods=['GET'])
def get_test():
    name = request.args.get('name')
    favorites = request.args.getlist('favorites')
    # 附加题: 让蔡徐坤 ctrl
    msg = '这是GET请求,我的偶像是' + name
    return msg


@app.route(rule='/post_test', methods=['POST'])
def post_test():
    # 一般post请求使用请求体传递参数,一般使用json格式
    jsonStr = request.get_data(as_text=True)
    jsonObj = json.loads(jsonStr)
    msg = '这是POST请求'
    return msg


# 启动应用和之前一致,如果重启不了,则需要关闭所有的python.exe进程
if __name__ == '__main__':
    # host 表示监听的IP地址   默认是127.0.0.1或者localhost   如果指定为0.0.0.0,则表示所有的IP都能访问  也可以指定为某个网卡的网址
    # port http监听的端口  默认是5000
    # debug  是否开启flask的调试模式  开启调试模式后,会打印更多的日志
    app.run(port=5000, debug=True)
