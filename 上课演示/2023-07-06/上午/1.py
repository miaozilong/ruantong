from flask import Flask

# 将当前程序作为web app应用
app = Flask(__name__)


# rule表示访问的路径
@app.route(rule='/')
def hello_world():
    msg = 'Hello World!  <br /> Again!'
    return msg


# 启动应用和之前一致,如果重启不了,则需要关闭所有的python.exe进程
if __name__ == '__main__':
    # host 表示监听的IP地址   默认是127.0.0.1或者localhost   如果指定为0.0.0.0,则表示所有的IP都能访问  也可以指定为某个网卡的网址
    # port http监听的端口  默认是5000
    # debug  是否开启flask的调试模式  开启调试模式后,会打印更多的日志
    app.run(port=5000, debug=True)
